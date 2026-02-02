from typing import List
from covenant.models import BiasContract


class ContractValidationError(Exception):
    """Raised when a Bias Contract is structurally or semantically invalid."""
    pass


def validate_contract(contract: BiasContract) -> None:
    """
    Validate a Bias Contract before it can be used.

    This function enforces:
    - structural completeness
    - semantic consistency
    - Covenant invariants

    It raises ContractValidationError on failure.
    """

    _validate_status(contract)
    _validate_invariants(contract)
    _validate_constraints(contract)
    _validate_refusal_rules(contract)


def _validate_status(contract: BiasContract) -> None:
    if contract.header.status != "active":
        raise ContractValidationError(
            "Only contracts with status='active' may be enforced."
        )


def _validate_invariants(contract: BiasContract) -> None:
    inv = contract.invariants

    if not inv.refusal_allowed:
        raise ContractValidationError(
            "Covenant requires refusal to be an allowed outcome."
        )

    if not inv.no_silent_modification:
        raise ContractValidationError(
            "Silent modification of outputs is forbidden by Covenant invariants."
        )


def _validate_constraints(contract: BiasContract) -> None:
    hc = contract.hard_constraints
    ss = contract.soft_signals

    _ensure_disjoint(
        hc.forbidden_signals,
        ss.allowlist,
        "forbidden_signals",
        "soft_signals.allowlist",
    )

    _ensure_disjoint(
        hc.forbidden_signals,
        ss.denylist,
        "forbidden_signals",
        "soft_signals.denylist",
    )


def _validate_refusal_rules(contract: BiasContract) -> None:
    seen_conditions: List[str] = []

    for rule in contract.refusal_rules:
        if rule.condition in seen_conditions:
            raise ContractValidationError(
                f"Duplicate refusal rule condition: {rule.condition}"
            )
        seen_conditions.append(rule.condition)


def _ensure_disjoint(a: List[str], b: List[str], name_a: str, name_b: str) -> None:
    overlap = set(a).intersection(set(b))
    if overlap:
        raise ContractValidationError(
            f"Overlap detected between {name_a} and {name_b}: {overlap}"
        )
