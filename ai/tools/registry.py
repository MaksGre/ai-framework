from ai.tools.base import Tool


class ToolRegistry:

    def __init__(self, tools: list [Tool]):
        self._tools = tools
    
    def get(self, name: str) -> Tool:
        for tool in self._tools:
            if tool.name == name:
                return tool
                
        raise ValueError(f"Tool not found: {name}")

    def schemas(self) -> list[dict]:
        return [
            tool.schema()
            for tool in self._tools
        ]
