from ai.llm.client import LLMClient
from ai.llm.models import LLMRequest

class Agent:

    def __init__(self, llm: LLMClient):
        self._llm = llm

    def run(self, prompt: str) -> str:
        request = LLMRequest(prompt=prompt)
        response = self._llm.generate(request)
        return response.text
