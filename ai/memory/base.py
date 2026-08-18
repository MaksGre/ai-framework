from ai.memory.message import Message

class Memory:
    
    def __init__(self, max_messages: int = 20):
        self._messages: list[Message] = []
        self._max_messages = max_messages
        
    def add(
        self,
        role: str,
        content: str | None = None,
        tool_calls: list[dict] | None = None,
        tool_call_id: str | None = None,
    ) -> None:
        self._messages.append(
            Message(
                role=role,
                content=content,
                tool_calls=tool_calls,
                tool_call_id=tool_call_id,
            )
        )
        
        if len(self._messages) > self._max_messages:
            self._messages.pop(0)
    
    def get(self) -> list[Message]:
        return self._messages.copy()
