from dataclasses import dataclass, field


@dataclass
class ToolCall:
    id: str
    name: str
    arguments: dict


@dataclass
class LLMRequest:
    messages: list[dict]
    tools: list[dict] = field(default_factory=list)


@dataclass
class LLMResponse:
    text: str

    thinking: str | None = None

    model: str | None = None

    prompt_tokens: int | None = None

    completion_tokens: int | None = None

    total_duration: int | None = None

    tool_calls: list[ToolCall] = field(default_factory=list)
