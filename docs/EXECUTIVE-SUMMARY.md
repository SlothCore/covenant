# Covenant — Executive Summary

> **Status:** Reference implementation and governance framework (not a commercial product).

## What this is

Covenant is a governance system for automated decisions.

It ensures that AI-driven decisions only occur under **explicit, pre-approved rules**, with the ability to **refuse decisions**, **enforce constraints**, and **produce audit-ready records**.

Covenant does not promise perfect outcomes.
It guarantees **explicit accountability**.

---

## The problem it addresses

Most AI failures are not caused by models behaving unexpectedly.
They occur because organizations never made their decision rules explicit.

When something goes wrong:

- responsibility is unclear
- intent is reconstructed after the fact
- compliance relies on explanation, not control

This creates legal, regulatory, and reputational risk.

---

## The core idea

Covenant introduces **Bias Contracts**:
formal declarations of what an automated system is allowed or forbidden to do **before it runs**.

These contracts are:

- enforced ex-ante (before decisions exist)
- refusal-capable
- versioned and auditable

---

## How it works (high level)

1. Rules are declared explicitly (Bias Contract)
2. Requests are checked before execution (Precheck)
3. Illegitimate decisions are refused
4. Outputs are checked and corrected if needed (Postcheck)
5. Each decision produces an audit artifact

---

## What Covenant is not

- Not a fairness guarantee
- Not a model alignment technique
- Not a replacement for regulation
- Not an ethics framework

It is a **decision governance layer**.

---

## Why this matters to leadership

Covenant enables organizations to:

- demonstrate ex-ante risk control
- remove plausible deniability
- support audits without reconstruction
- adapt governance as regulations evolve

---

## Where to go next

- For concepts and background: `docs/concepts/`
- For regulatory and procurement materials: `docs/governance/`
- For the formal specification: `docs/specification/`
