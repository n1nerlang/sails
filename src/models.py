from pydantic import BaseModel, Field
from typing import Optional

class AIResponse(BaseModel):
    content: str = Field(..., description="The main output from the AI")
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    metadata: Optional[dict] = None

class ProcessingRequest(BaseModel):
    prompt: str
    max_tokens: int = 1024
