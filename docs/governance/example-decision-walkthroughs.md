# Example Decision Walkthroughs

This document illustrates how automated decisions are governed under Bias Contracts, step by step.

The goal is to make enforcement, refusal, and accountability observable.

---

## Example 1 — Prohibited Hiring Decision (Refusal)

### Scenario

A user requests an automated ranking of job candidates based on “cultural fit”.

### Step-by-step

1. A Bias Contract is active for hiring decisions.
2. The contract explicitly forbids:
   - discrimination
   - ranking by subjective cultural criteria
3. The request is evaluated **before** any AI model runs.
4. The system detects a forbidden operation.
5. The request is **refused**.

### Outcome

- No model execution
- No output generated
- Refusal reason recorded
- Audit artifact created

### Regulatory significance

This demonstrates **ex-ante prevention** of illegitimate decisions.
The system does not attempt to “fix” or justify the request after execution.

---

## Example 2 — Allowed Decision with Postcheck Redaction

### Scenario

A system generates a candidate summary that inadvertently references age.

### Step-by-step

1. The request passes precheck.
2. The AI model produces an output.
3. Postcheck evaluates the output.
4. Age is detected as a denylisted signal.
5. The reference is explicitly removed.
6. Redaction is recorded in the audit artifact.

### Outcome

- Output is delivered with redaction
- Enforcement action is visible
- No silent filtering

### Regulatory significance

This shows how prohibited information is controlled without hiding enforcement actions.

---

## Example 3 — Incomplete Governance Rules (Safe Failure)

### Scenario

A system is invoked with missing or contradictory governance rules.

### Step-by-step

1. The system validates the Bias Contract.
2. The contract is found to be incomplete.
3. The system refuses to operate.

### Outcome

- No decision is produced
- No model execution occurs
- Failure is intentional and recorded

### Regulatory significance

This demonstrates **fail-safe behavior** when governance is insufficient.

---

## Key takeaway

In all cases:

- Decisions are governed before execution
- Refusal is an intentional outcome
- Accountability is preserved without reconstruction
