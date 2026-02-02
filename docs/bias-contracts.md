# Bias Contracts

This document defines the canonical structure and enforcement semantics of **Bias Contracts** in Covenant.

A Bias Contract is a **first-class, ex-ante artifact** that declares under what constraints an automated system is allowed to make a decision.

Bias Contracts exist to eliminate ambiguity about intent, responsibility, and permissible bias _before_ execution.

---

## 1. Purpose of a Bias Contract

A Bias Contract answers one question:

> Under what declared constraints is this system allowed to produce a decision?

It does **not**:

- guarantee fairness
- optimize outcomes
- evaluate morality
- learn from behavior

It **does**:

- bind execution to declared intent
- make bias explicit and auditable
- enable deterministic refusal
- remove plausible deniability

Bias Contracts govern **systems**, not people.

---

## 2. Design Principles

All Bias Contracts must adhere to the following principles:

1. **Ex-ante declaration**  
   Contracts are evaluated before generation, not after outcomes.

2. **No defaults**  
   Undeclared signals, intents, or operations do not exist.

3. **Separation of validity and preference**  
   Some conditions invalidate decisions; others only shape them.

4. **Immutability once active**  
   Active contracts cannot be modified, only superseded.

5. **Human-legible first**  
   A contract must be understandable without reading code.

---

## 3. Contract Lifecycle

A Bias Contract has a simple lifecycle:

1. Created
2. Activated
3. Enforced
4. Superseded (optional)

Contracts are **versioned**.  
Changing intent requires issuing a new version with explicit lineage.

Silent edits are forbidden.

---

## 4. Canonical Contract Structure (v0)

Below is the minimal canonical schema for a Bias Contract in Covenant v0.

### 4.1 Contract Header

```json
{
  "contract_id": "hiring-eu-v1",
  "version": "1.0.0",
  "status": "active",
  "domain": "hiring",
  "jurisdiction": ["EU"],
  "owner": "talent-platform-risk",
  "created_at": "2026-02-01T00:00:00Z",
  "supersedes": null
}
```

### 4.2 Invariants

```json
"invariants": {
  "explainability_required": true,
  "refusal_allowed": true,
  "no_silent_modification": true
}
```

### 4.3 Hard Constraints

json```
"hard_constraints": {
"forbidden_signals": [
"race",
"religion",
"medical_conditions",
"sexual_orientation"
],
"forbidden_intents": [
"discrimination",
"legal_advice",
"medical_diagnosis"
],
"forbidden_operations": [
"ranking_by_cultural_fit"
]
}

````

### 4.4 Soft Signals

json```
"soft_signals": {
  "allowlist": [
    "skills",
    "experience",
    "education",
    "role_requirements"
  ],
  "denylist": [
    "age",
    "gender"
  ]
}
````

### 4.5 Bias Primitives

json```
"bias_primitives": {
"risk_aversion": "high",
"safety_over_efficiency": true,
"uncertainty_penalty": "medium"
}

````

### 4.6 Refusal Rules

json```
"refusal_rules": [
  {
    "condition": "forbidden_intent_detected",
    "action": "refuse",
    "explanation": "Intent violates hiring domain constraints."
  },
  {
    "condition": "insufficient_allowed_signals",
    "action": "refuse",
    "explanation": "Decision lacks admissible basis."
  }
]
````

# 5. Enforcement Order

1. Validate contract identity and version
2. Enforce invariants
3. Evaluate hard constraints
4. Filter signals
5. Apply bias primitives
6. Evaluate refusal rules
7. Emit decision and audit artifact

# 6. Audit Semantics

Each decision produces an audit record including:

- contract id and version
- constraints enforced
- signals considered and ignored
- actions taken
- timestamp

# 7. Scope and Limitations

Bias Contracts do not guarantee ethical outcomes.
They guarantee explicit, enforceable intent.

# 8. Summary

Bias Contracts make bias explicit, enforceable, and auditable.
