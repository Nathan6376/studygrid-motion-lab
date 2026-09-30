# StudyGrid Stuart Q-S9 — Corrected R6 Focus + Compact Regression Reacceptance

Timestamp: 2026-09-30 17:01 ET  
Lifecycle: DONE  
Disposition: **PASS within tested scope**; existing real-device/hosted/full-accessibility items remain **HOLD**.

## Exact corrected candidate

- `StudyGrid-CF0042-QB13-r6-focusfix.html`
- Drive `10ISHnuiaZTIispYlRSkO81h__J63x-ND`
- Provider metadata size: **954307 bytes**
- Independently recomputed SHA-256: **9cd7b6dd37caac46dcab8f049bd4f0e218e0b027d60bd89cccbc9b547b43e8fe**
- `APP_VERSION`: **v7.16-cf0042-qb13-r6-focusfix**
- `SG_R6_BUILD`: **v7.16-cf0042-qb13-r6-focusfix**
- registry build: **v7.16-cf0042-qb13-r6-focusfix**

Exact origin R6 was fetched fresh from provider and independently reverified as 954208 bytes / SHA-256 `875a81262d80cf33ceb32545ff20c1cbc03ae91db34c66a3a8a679f93f0314ef`.

## Direct reproduction of Q-S8 defects

### QS8-F1 — Students sort/filter repaint focus
PASS.

- Sort: after repaint, `document.activeElement.id === r6StudentSort`; not BODY.
- Filter: after repaint, `document.activeElement.id === r6StudentFilter`; not BODY.
- Both use the replacement controls after repaint and preserve scroll in the bounded runtime check.

### QS8-F2 — assessment confirmation refresh focus
PASS.

- `#r6TaskCanvas` exists with `tabindex=-1` and is programmatically focusable.
- Confirmation activated from the keyboard leaves `document.activeElement.id === r6TaskCanvas`; not BODY.
- Strong nonzero-scroll replay: scrollY **1722 before / 1722 after**, active element `r6TaskCanvas`.

## Previously passing keyboard/focus behaviour

PASS.

- Roving instructor tabs: ArrowRight from Overview moved both selection and focus to Students.
- Source-policy dialog: opens with focus moved into the dialog; Escape closes it and returns focus to `#r6InspectPolicy`.

Focused runtime set: **17/17 PASS** with zero bounded page errors and zero console warnings/errors.

## Compact regression / responsive / registry smoke

PASS.

- Executable inline JavaScript syntax: **4/4 blocks PASS** under `node --check`.
- Registry: **rev 11 / 237 entries / 237 unique component IDs**.
- Deterministic built-in fixtures: **6/6 PASS**.
- Responsive runtime matrix: **18/18 PASS** = Paper + Dusk × desktop 1280 / tablet 820 / phone 390 × Overview / Students / Sources.
- Across that matrix: zero page-level horizontal-overflow failures, zero duplicate-ID failures, zero bounded page errors, zero console warnings/errors, zero external HTTP(S) requests.

Bob's provider verification JSON was integrity-checked separately: SHA-256 `68d9b989a298e7fa43aa210fc7bba8ee258e4044edc4c4e4831ff44f93415c1d`, 5792 bytes, and it binds to the same corrected candidate identity while reporting 45/45 PASS. It is corroborating evidence only; Stuart's acceptance above is independently reproduced.

## Independent exact diff conclusion

PASS — bounded to the requested repair.

Exact R6 → Q-B13 has **5 non-equal source-line hunks**:

1. `APP_VERSION` identity update.
2. `SG_R6_BUILD` identity update.
3. QS8-F2 confirmation focus target changes `r6AttentionTitle` → `r6TaskCanvas`.
4. QS8-F1 adds replacement-focus restoration for `r6StudentSort` and `r6StudentFilter` after repaint.
5. Component-registry top-level `build` identity update.

Independent reverse-normalisation is exact: replacing the three candidate identity occurrences with the R6 identity, removing the two Students focus-restoration calls, and restoring the original confirmation target produces bytes **exactly identical** to provider R6, including SHA-256 `875a81262d80cf33ceb32545ff20c1cbc03ae91db34c66a3a8a679f93f0314ef`. Candidate byte delta is +99 bytes.

No professor-scale/gateway/backend/auth/Supabase/deployment/Blender/motion/A-C/canonical-G/brand-portal addition is present in this corrected candidate.

## HOLDs preserved

No new evidence changes the existing holds for physical iPad/Safari/WebKit, VoiceOver, Apple Pencil/physical interaction, physical hardware keyboard, true 200% zoom, full WCAG, or hosted-origin storage/cross-tab behaviour.

Runtime evidence here used the exact provider-downloaded HTML bytes in bounded headless Chromium/in-memory loading. It is not promoted to hosted-origin, physical-device, or assistive-technology evidence.

## Result

**PASS** — exact Q-B13 corrected candidate is independently reaccepted within the Q-S9 tested scope. QS8-F1 and QS8-F2 are resolved in the tested runtime, prior positive keyboard behaviour remains intact, compact regression/responsive/registry checks pass, and the exact diff is limited to the focus repairs plus candidate identity fields.

No canonical promotion or product/backend/deployment/motion mutation was performed.
