from ai.llm.client import LLMClient
from ai.llm.models import LLMRequest, LLMResponse
from ai.memory.base import Memory
from ai.context.builder import ContextBuilder
from ai.tools.base import Tool
from ai.tools.registry import ToolRegistry
from ai.memory.message import Message


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
            role="user",
            content=context,
        )

        messages = self._build_messages(
            self._memory.get()
        )

        return self._run_agent_loop(messages)

    def execute_tool(
        self,
        name: str,
        arguments: dict,
    ) -> str:
        tool = self._tool_registry.get(name)

        return tool.execute(**arguments)

    def _build_messages(
        self,
        history: list[Message],
    ) -> list[dict]:
        messages = [
            {
                "role": "system",
                "content": self._system_prompt,
            }
        ]

        messages.extend(
            self._message_to_dict(message)
            for message in history
        )

        return messages

    def _run_agent_loop(
        self,
        messages: list[dict],
    ) -> str:
        request = self._build_request(messages)

        while True:
            response = self._llm.generate(request)

            if not response.tool_calls:
                self._memory.add(
                    role="assistant",
                    content=response.text,
                )

                return response.text

            self._handle_tool_calls(
                response=response,
                messages=messages,
            )

            request = self._build_request(messages)
        
    def _handle_tool_calls(
        self,
        response: LLMResponse,
        messages: list[dict],
    ) -> None:
        assistant_tool_calls = [
            {
                "id": tool_call.id,
                "type": "function",
                "function": {
                    "name": tool_call.name,
                    "arguments": tool_call.arguments,
                },
            }
            for tool_call in response.tool_calls
        ]

        self._memory.add(
            role="assistant",
            content=response.text,
            tool_calls=assistant_tool_calls,
        )

        messages.append(
            {
                "role": "assistant",
                "content": response.text,
                "tool_calls": assistant_tool_calls,
            }
        )

        for tool_call in response.tool_calls:
            result = self.execute_tool(
                name=tool_call.name,
                arguments=tool_call.arguments,
            )

            self._memory.add(
                role="tool",
                content=result,
                tool_call_id=tool_call.id,
            )

            messages.append(
                {
                    "role": "tool",
                    "content": result,
                    "tool_call_id": tool_call.id,
                }
            )
            
    def _build_request(
        self,
        messages: list[dict],
    ) -> LLMRequest:
        return LLMRequest(
            messages=messages,
            tools=self._tool_registry.schemas(),
        )
            
    def _message_to_dict(
        self,
        message: Message,
    ) -> dict:
        data = {
            "role": message.role,
            "content": message.content,
        }

        if message.tool_calls is not None:
            data["tool_calls"] = message.tool_calls

        if message.tool_call_id is not None:
            data["tool_call_id"] = message.tool_call_id

        return data
