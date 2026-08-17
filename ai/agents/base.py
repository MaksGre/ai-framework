from ai.llm.client import LLMClient
from ai.llm.models import LLMRequest
from ai.memory.base import Memory
from ai.context.builder import ContextBuilder
from ai.tools.base import Tool
from ai.tools.registry import ToolRegistry


class Agent:

    def __init__(
        self,
        name: str,
        system_prompt: str,
        llm: LLMClient,
        builder: ContextBuilder,
        memory: Memory,
        tools: list[Tool],
    ):
        self._name = name
        self._system_prompt = system_prompt
        self._llm = llm
        self._builder = builder
        self._memory = memory
        self._tool_registry = ToolRegistry(tools)

    def ask(self, prompt: str) -> str:
        context = self._builder.build(prompt)
        
        self._memory.add(
            role = "user",
            content = context
        )
        
        history = self._memory.get()
        
        conversation = "\n\n".join(
            f"{message.role}: {message.content}"
            for message in history
        )
        
        request = LLMRequest(
            prompt = conversation,
        )
        
        response = self._llm.generate(request)
        
        self._memory.add(
            role = "assistant",
            content = response.text
         )
        
        return response.text
        
    def analyze_file(
        self,
        path: str,
        task: str
    ) -> str:
        prompt = self._builder.build(
            prompt = f"@{path}",
            task = task
        )
        
        request = LLMRequest(
            prompt = prompt
        )
        
        response = self._llm.generate(request)
        
        return response.text

    def analyze_files(
        self,
        paths: list[str],
        task: str
    ) -> str:
        prompt = self._builder.build_files(
            paths = paths,
            task = task
        )
        
        request = LLMRequest(
            prompt = prompt
        )
        
        response = self._llm.generate(request)
        
        return response.text

    def execute_tool(
        self,
        name: str,
        arguments: dict,
    ) -> str:
        tool = self._tool_registry.get(name)
        
        return tool.execute(**arguments)
