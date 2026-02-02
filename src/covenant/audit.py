from datetime import datetime
from typing import List

from covenant.models import AuditRecord, ActionTaken


def build_audit_record(
    *,
    decision_id: str,
    contract_id: str,
    version: str,
    precheck_decision: str,
    postcheck_decision: str,
    signals_ignored: List[str],
    actions: List[ActionTaken],
) -> AuditRecord:
    """
    Build an immutable audit record for a decision.

    Audit records are first-class outputs of Covenant.
    """

    return AuditRecord(
        decision_id=decision_id,
        contract_id=contract_id,
        version=version,
        precheck_decision=precheck_decision,
        postcheck_decision=postcheck_decision,
        signals_ignored=signals_ignored,
        actions=actions,
        timestamp=_now(),
    )


def _now() -> str:
    return datetime.utcnow().isoformat()
