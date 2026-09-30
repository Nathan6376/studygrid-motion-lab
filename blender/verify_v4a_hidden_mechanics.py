"""Pure-Python analytic verifier for scene_v4a_2c_compare.py.
No Blender dependency. Samples candidate sweeps and performs 3D OBB SAT tests.
"""

import json
import math

L = 1.0
GAP = 0.10
HALF = 0.5
SAMPLES = 721
FLOOR_Z = -1.25


def vadd(a, b): return tuple(a[i] + b[i] for i in range(3))
def vsub(a, b): return tuple(a[i] - b[i] for i in range(3))
def vmul(a, s): return tuple(x * s for x in a)
def dot(a, b): return sum(a[i] * b[i] for i in range(3))
def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def norm(a): return math.sqrt(dot(a, a))
def unit(a):
    n = norm(a)
    return tuple(x / n for x in a) if n > 1e-12 else (0.0, 0.0, 0.0)


def mmul(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def mvec(A, v): return tuple(sum(A[i][k]*v[k] for k in range(3)) for i in range(3))


def rx(a):
    c,s=math.cos(a),math.sin(a)
    return ((1,0,0),(0,c,-s),(0,s,c))


def ry(a):
    c,s=math.cos(a),math.sin(a)
    return ((c,0,s),(0,1,0),(-s,0,c))


def rz(a):
    c,s=math.cos(a),math.sin(a)
    return ((c,-s,0),(s,c,0),(0,0,1))

I=((1,0,0),(0,1,0),(0,0,1))


CUBE_VERTS = tuple((x,y,z) for x in (-HALF,HALF) for y in (-HALF,HALF) for z in (-HALF,HALF))

def min_vertex_z(center, R):
    return min(vadd(center, mvec(R, v))[2] for v in CUBE_VERTS)

def axes_from_R(R):
    # columns are local axes in world space
    return tuple(tuple(R[r][c] for r in range(3)) for c in range(3))


def obb_intersects(ca, Ra, cb, Rb, ha=(HALF,HALF,HALF), hb=(HALF,HALF,HALF), eps=1e-9):
    # Generic SAT over face normals and edge cross-products.
    Aa=axes_from_R(Ra); Bb=axes_from_R(Rb)
    axes=list(Aa)+list(Bb)
    for a in Aa:
        for b in Bb:
            cp=cross(a,b)
            if norm(cp)>1e-10:
                axes.append(unit(cp))
    d=vsub(cb,ca)
    for axis in axes:
        ra=sum(ha[i]*abs(dot(axis,Aa[i])) for i in range(3))
        rb=sum(hb[i]*abs(dot(axis,Bb[i])) for i in range(3))
        sep=abs(dot(d,axis))-(ra+rb)
        if sep >= -eps:
            return False
    return True


def sat_max_separation(ca, Ra, cb, Rb):
    # Largest positive separating-axis gap. Positive proves disjointness.
    Aa=axes_from_R(Ra); Bb=axes_from_R(Rb)
    axes=list(Aa)+list(Bb)
    for a in Aa:
        for b in Bb:
            cp=cross(a,b)
            if norm(cp)>1e-10:
                axes.append(unit(cp))
    d=vsub(cb,ca)
    best=-1e9
    for axis in axes:
        ra=sum(HALF*abs(dot(axis,Aa[i])) for i in range(3))
        rb=sum(HALF*abs(dot(axis,Bb[i])) for i in range(3))
        best=max(best,abs(dot(d,axis))-(ra+rb))
    return best


def sample_range(a,b,n=SAMPLES):
    for i in range(n):
        t=i/(n-1)
        yield a+(b-a)*t


def candidate_a(angle):
    parent=(0.0,0.0,0.0)
    pivot=(0.5,0.0,0.5)
    local=(0.6,0.0,-0.5)
    R=ry(angle)
    child=vadd(pivot,mvec(R,local))
    return parent,I,child,R


def candidate_c(a1,a2):
    parent=(0.0,0.0,0.0)
    p1=(0.5,0.5,0.0)
    h2=(0.0,0.6,0.5)
    child_local=(-0.5,0.0,-0.5)
    R1=rz(a1)
    R2=ry(a2)
    child=vadd(p1,mvec(R1,vadd(h2,mvec(R2,child_local))))
    R=mmul(R1,R2)
    return parent,I,child,R


def run():
    report={"L":L,"rest_gap":GAP,"samples_per_stage":SAMPLES}

    # A: -90 -> 0 around world Y.
    coll=0; min_sep=1e9; worst=None; min_floor_a=1e9
    for a in sample_range(math.radians(-90),0):
        pa,Ra,cb,Rb=candidate_a(a)
        if obb_intersects(pa,Ra,cb,Rb): coll+=1
        sep=sat_max_separation(pa,Ra,cb,Rb)
        if sep<min_sep: min_sep=sep; worst=math.degrees(a)
        min_floor_a=min(min_floor_a, min_vertex_z(cb,Rb)-FLOOR_Z)
    a_start=candidate_a(math.radians(-90))[2]
    a_end=candidate_a(0)[2]
    report["A"]={
        "start_center":a_start,"end_center":a_end,
        "hinge":"world Y through parent face-edge x=+0.50L,z=+0.50L",
        "colliding_samples":coll,
        "minimum_positive_SAT_separation":min_sep,
        "worst_angle_deg":worst,
        "final_rest_gap":a_end[0]-HALF-HALF,
        "minimum_floor_clearance":min_floor_a,
    }

    # C stage1: H1 0 -> -90 Z, H2 0.
    coll1=0; min1=1e9; worst1=None; min_floor_c1=1e9
    for a1 in sample_range(0,math.radians(-90)):
        pa,Ra,cb,Rb=candidate_c(a1,0)
        if obb_intersects(pa,Ra,cb,Rb): coll1+=1
        sep=sat_max_separation(pa,Ra,cb,Rb)
        if sep<min1: min1=sep; worst1=math.degrees(a1)
        min_floor_c1=min(min_floor_c1, min_vertex_z(cb,Rb)-FLOOR_Z)

    # C stage2: H1 held -90 Z; H2 0 -> -90 local Y (= world X).
    coll2=0; min2=1e9; worst2=None; min_floor_c2=1e9
    for a2 in sample_range(0,math.radians(-90)):
        pa,Ra,cb,Rb=candidate_c(math.radians(-90),a2)
        if obb_intersects(pa,Ra,cb,Rb): coll2+=1
        sep=sat_max_separation(pa,Ra,cb,Rb)
        if sep<min2: min2=sep; worst2=math.degrees(a2)
        min_floor_c2=min(min_floor_c2, min_vertex_z(cb,Rb)-FLOOR_Z)

    c_start=candidate_c(0,0)[2]
    c_mid=candidate_c(math.radians(-90),0)[2]
    c_end=candidate_c(math.radians(-90),math.radians(-90))[2]

    # Exact-front pinhole containment proof, normalized focal factor omitted.
    # Camera is at y=-15, looking +Y. Use nearest parent/child faces.
    cam_y=-15.0
    parent_near_y=-0.5
    child_near_y=c_start[1]-0.5
    parent_half_projection=HALF/(parent_near_y-cam_y)
    child_half_projection=HALF/(child_near_y-cam_y)

    report["C"]={
        "start_center":c_start,"stage1_end_center":c_mid,"final_center":c_end,
        "hinge1":"world Z through parent back-right edge x=+0.50L,y=+0.50L",
        "hinge2":"local Y on H2; after H1=-90deg it is world X through y=+0.50L,z=+0.50L",
        "stage1_colliding_samples":coll1,
        "stage1_minimum_positive_SAT_separation":min1,
        "stage1_worst_angle_deg":worst1,
        "stage1_minimum_floor_clearance":min_floor_c1,
        "stage2_colliding_samples":coll2,
        "stage2_minimum_positive_SAT_separation":min2,
        "stage2_worst_angle_deg":worst2,
        "stage2_minimum_floor_clearance":min_floor_c2,
        "final_rest_gap":c_end[0]-HALF-HALF,
        "visibility_toggle":"none",
        "front_camera_start_fully_occluded":child_half_projection < parent_half_projection,
        "parent_projected_half_extent_normalized":parent_half_projection,
        "child_projected_half_extent_normalized":child_half_projection,
    }

    report["floor_z"]=FLOOR_Z
    report["pass"]=(coll==0 and coll1==0 and coll2==0 and min_floor_a>0 and min_floor_c1>0 and min_floor_c2>0 and abs(report["A"]["final_rest_gap"]-GAP)<1e-9 and abs(report["C"]["final_rest_gap"]-GAP)<1e-9 and report["C"]["front_camera_start_fully_occluded"])
    print(json.dumps(report,indent=2))
    if not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    run()
