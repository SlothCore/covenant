# Vendor Questionnaire → Regulatory Mapping

## Section 1 — System Scope

**Q1–Q3 (What decisions does the system make?)**
**Mapped to:**

- EU AI Act — _Scope & classification of AI systems_ (risk categorization)
- GDPR Art. 22 — _Automated decision-making affecting individuals_

**Regulatory intent:**
Determine whether the system falls under **high-risk AI** or automated decision regimes.

---

## Section 2 — Governance Model

**Q4–Q6 (Explicit rules, enforceability, no-default operation)**
**Mapped to:**

- EU AI Act — _Risk management system (ex-ante)_
- EU AI Act — _Governance and organizational measures_
- GDPR Art. 5(2) — _Accountability principle_

**Regulatory intent:**
Ensure governance is **designed-in**, not implied or retrofitted.

---

## Section 3 — Bias Declaration

**Q7–Q10 (Explicit allowed/prohibited factors, no implicit defaults)**
**Mapped to:**

- EU AI Act — _Data governance & bias mitigation_
- GDPR Art. 5(1)(a) — _Lawfulness and fairness_
- Anti-discrimination frameworks (sectoral)

**Regulatory intent:**
Prevent **implicit discriminatory logic** and undocumented assumptions.

---

## Section 4 — Refusal Capability

**Q11–Q14 (Ability to refuse decisions)**
**Mapped to:**

- EU AI Act — _Risk mitigation measures_
- General safety engineering principle: _fail-safe behavior_
- GDPR Art. 22(3) — _Safeguards against automated decisions_

**Regulatory intent:**
Ensure systems can **prevent harm**, not just explain it later.

---

## Section 5 — Determinism and Predictability

**Q15–Q17 (Consistent, reproducible governance behavior)**
**Mapped to:**

- EU AI Act — _Technical robustness and reliability_
- Auditability expectations in financial and safety regulation

**Regulatory intent:**
Enable **repeatable audits** and legal review.

---

## Section 6 — Post-Decision Controls

**Q18–Q20 (Output checks, redaction, visible enforcement)**
**Mapped to:**

- EU AI Act — _Human oversight and output controls_
- GDPR Art. 5(1)(c) — _Data minimization_

**Regulatory intent:**
Ensure prohibited information is **actively controlled**, not silently used.

---

## Section 7 — Auditability

**Q21–Q24 (Structured audit records, immutability)**
**Mapped to:**

- EU AI Act — _Logging and record-keeping obligations_
- GDPR Art. 30 — _Records of processing activities_
- Financial and safety audit norms

**Regulatory intent:**
Allow **after-the-fact verification without reconstruction**.

---

## Section 8 — Rule Changes and Versioning

**Q25–Q28 (Versioned rules, no retroactive changes)**
**Mapped to:**

- EU AI Act — _Change management & lifecycle governance_
- General compliance doctrine: _non-retroactivity_

**Regulatory intent:**
Preserve **historical accountability** when policies evolve.

---

## Section 9 — Jurisdiction and Compliance

**Q29–Q31 (Jurisdictional scoping, regulatory adaptation)**
**Mapped to:**

- EU AI Act — _Territorial scope_
- GDPR Art. 3 — _Territorial applicability_

**Regulatory intent:**
Prevent **regulatory leakage** across regions.

---

## Section 10 — Failure Modes and Safeguards

**Q32–Q34 (Incomplete rules, safe failure)**
**Mapped to:**

- EU AI Act — _Risk management & robustness_
- Safety-critical system standards (fail-safe design)

**Regulatory intent:**
Ensure systems **default to safety**, not execution.

---

## Section 11 — Accountability

**Q35–Q37 (Who approved rules, who is responsible)**
**Mapped to:**

- GDPR Art. 5(2) — _Accountability_
- EU AI Act — _Allocation of responsibility_

**Regulatory intent:**
Identify **human responsibility**, not just system behavior.

---

## Final Declaration

**Q38 (Vendor attestation)**
**Mapped to:**

- Procurement law
- Regulatory enforcement practice

**Regulatory intent:**
Create **legal commitment**, not just technical description.

---

# Regulator-facing summary

> **Each question in this questionnaire maps to a concrete regulatory obligation around ex-ante risk control, auditability, and accountability.
> The goal is not to assess model quality, but to determine whether automated decisions are governed before they occur.**
