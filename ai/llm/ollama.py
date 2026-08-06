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
        print("Sending request to Ollama...")

        payload = {
            "model": self._model,
            "prompt": request.prompt,
            "stream": False,
        }

        print(payload)

        response = httpx.post(
            "http://localhost:11434/api/generate",
            json=payload,
            timeout=60,
        )

        print("Response received from Ollama.")

        response.raise_for_status()

        data = response.json()

        return LLMResponse(
            text=data["response"],
        )
