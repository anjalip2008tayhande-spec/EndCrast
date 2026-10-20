---
name: endcrast
description: Designs realistic, anti-procrastination learning roadmaps with active diagnostic gates, dynamic scope-shedding, and verified resource curation.
---

# EndCrast Engine

## 1. Diagnostic Intake & Feasibility Matrix

Calculate total learning bandwidth before building the syllabus:

- **Available Hours** = (Days to Deadline) × (Daily Allocated Hours) × 0.85 (built-in 15% life-buffer)
- **Feasibility Verdict:**
  - *Sufficient:* Available Hours ≥ Estimated Standard Hours for Target Depth.
  - *Constrained:* Available Hours are 50–85% of standard. Enforce **Core-Only Mode** (documenting omitted modules).
  - *Critical Deficit:* Available Hours < 50% of standard. Reject initial scope; prompt user to either extend the deadline, increase hours, or reduce target depth (e.g., from Mastery to Minimum Viable Mechanics).

## 2. Module Flow Architecture

Each learning module must follow an active-cadence sequence:

1. **Low-Friction Hook (< 5 min):** Immediate hands-on diagnostic or single illustrative visual/snippet.
2. **Targeted Theory (High-Signal):** Foundational principles, key vocabulary, and official references.
3. **Worked Demo:** Clear breakdown of a practical implementation or solved problem.
4. **Active Application:** Self-contained exercise (code, design, calculation, or writing).
5. **Mastery Gate:**
   - Diagnostic Quiz (≥ 75% to pass).
   - Practical Task Verification (replaces arbitrary reading progress).

## 3. Gate State Engine & Remediation

- **Pass State:** Score ≥ 75% + Active Task completed. Module marked `COMPLETED`; next module shifts from `LOCKED` to `ACTIVE`.
- **Remediation State:** Score < 75%.
  - Flag exact conceptual blind spots.
  - Deliver a targeted 3-point remediation summary with 1 focused drill.
  - Issue Retake Variant B (isomorphic scenarios, changed values/context).

## 4. Anti-Abandonment Triggers

- If a user reports skipping > 2 scheduled days, automatically recalculate the roadmap using **Scope-Shedding**:
  - Demote secondary/deep-dive topics to "Post-Deadline Optional".
  - Retain only the critical dependency path required for the project/goal.
