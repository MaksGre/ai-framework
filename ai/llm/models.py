from dataclasses import dataclass


@dataclass
class LLMRequest:
    prompt: str


@dataclass
class LLMResponse:
    text: str
    
    thinking: str | None = None
    
    model: str | None = None
    
    prompt_tokens: int | None = None
    
    completion_tokens: int | None = None
    
    total_duration: int | None = None
