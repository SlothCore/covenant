from typing import Any, Dict, List, Optional, Literal
from pydantic import BaseModel, Field


# ---------- Core Contract Models ----------

class ContractHeader(BaseModel):
    contract_id: str
    version: str
    status: Literal["active", "inactive"]
    domain: str
    jurisdiction: List[str]
    owner: str
    created_at: str
    supersedes: Optional[str] = None


class Invariants(BaseModel):
    explainability_required: bool
    refusal_allowed: bool
    no_silent_modification: bool


class HardConstraints(BaseModel):
    forbidden_signals: List[str] = Field(default_factory=list)
    forbidden_intents: List[str] = Field(default_factory=list)
    forbidden_operations: List[str] = Field(default_factory=list)


class SoftSignals(BaseModel):
    allowlist: List[str] = Field(default_factory=list)
    denylist: List[str] = Field(default_factory=list)


class BiasPrimitives(BaseModel):
    risk_aversion: Optional[Literal["low", "medium", "high"]] = None
    safety_over_efficiency: Optional[bool] = None
    uncertainty_penalty: Optional[Literal["low", "medium", "high"]] = None


class RefusalRule(BaseModel):
    condition: str
    action: Literal["refuse"]
    explanation: str


class BiasContract(BaseModel):
    header: ContractHeader
    invariants: Invariants
    hard_constraints: HardConstraints
    soft_signals: SoftSignals
    bias_primitives: Optional[BiasPrimitives] = None
    refusal_rules: List[RefusalRule] = Field(default_factory=list)


# ---------- Decision Flow Models ----------

class DecisionContext(BaseModel):
    domain: str
    jurisdiction: str


class PrecheckRequest(BaseModel):
    contract: BiasContract
    prompt: str
    context: DecisionContext


class PrecheckResponse(BaseModel):
    decision: Literal["allow", "refuse"]
    reason: str
    decision_id: str


class PostcheckRequest(BaseModel):
    decision_id: str
    contract: BiasContract
    llm_output: str


class ActionTaken(BaseModel):
    type: Literal["redaction", "refusal"]
    signal: Optional[str] = None
    reason: str


class AuditRecord(BaseModel):
    decision_id: str
    contract_id: str
    version: str
    precheck_decision: Literal["allow", "refuse"]
    postcheck_decision: Literal["allow", "redact", "refuse"]
    signals_ignored: List[str]
    actions: List[ActionTaken]
    timestamp: str


class PostcheckResponse(BaseModel):
    decision: Literal["allow", "refuse"]
    output: Optional[str] = None
    actions: List[ActionTaken]
    audit: AuditRecord
