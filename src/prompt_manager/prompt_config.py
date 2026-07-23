from pydantic import BaseModel
from typing import Dict


class PromptConfig(BaseModel):
    version: str
    author: str
    created_at: str
    description: str

    provider: str
    model: str

    temperature: float
    max_tokens: int

    system_prompt: str

    expected_output: Dict[str, str]