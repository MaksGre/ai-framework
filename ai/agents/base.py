from ai.llm.client import LLMClient
from ai.llm.models import LLMRequest
from ai.context.builder import ContextBuilder

class Agent:

    def __init__(
        self,
        name: str,
        system_prompt: str,
        llm: LLMClient,
        builder: ContextBuilder,
    ):
        self._name = name
        self._system_prompt = system_prompt
        self._llm = llm
        self._builder = builder

    def run(self, prompt: str) -> str:
        context = self._builder.build(prompt)
        
        request = LLMRequest(
            prompt=context,
        )
        
        response = self._llm.generate(request)
        
        return response.text
