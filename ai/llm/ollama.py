import httpx

from .client import LLMClient
from .models import LLMRequest, LLMResponse


class OllamaClient(LLMClient):
    def __init__(
        self,
        base_url: str = "http://localhost:11434",
        model: str = "qwen3:8b",
    ):
        self._model = model

        self._client = httpx.Client(
            base_url=base_url,
            timeout=60,
        )

    def generate(self, request: LLMRequest) -> LLMResponse:
        response = self._client.post(
            "/api/generate",
            json={
                "model": self._model,
                "prompt": request.prompt,
                "stream": False,
            },
        )

        response.raise_for_status()

        data = response.json()

        return LLMResponse(
            text=data["response"],
        )
