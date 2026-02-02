from fastapi import FastAPI

from covenant.models import (
    PrecheckRequest,
    PrecheckResponse,
    PostcheckRequest,
    PostcheckResponse,
)
from covenant.precheck import precheck_decision
from covenant.postcheck import postcheck_decision

app = FastAPI(
    title="Covenant MCP",
    description="Ex-ante bias governance layer for LLM decisions",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/decisions/precheck", response_model=PrecheckResponse)
def precheck(req: PrecheckRequest):
    """
    Perform ex-ante enforcement before any LLM call.
    """
    return precheck_decision(req)


@app.post("/decisions/postcheck", response_model=PostcheckResponse)
def postcheck(req: PostcheckRequest):
    """
    Perform post-generation enforcement and audit creation.
    """
    return postcheck_decision(req)
