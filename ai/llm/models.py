from dataclasses import dataclass


@dataclass
class LLMRequest:
    prompt: str


@dataclass
class LLMResponse:
    text: str
