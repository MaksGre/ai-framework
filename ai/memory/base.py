from ai.memory.message import Message

class Memory:
    
    def __init__(self):
        self._messages: list[Message] = []
        
    def add(
        self,
        role: str,
        content: str,
    ) -> None:
        self._messages.append(
        Message(
            role = role,
            content = content,
        )
    )
    
    def get(self) -> list[Message]:
        return self._messages 
