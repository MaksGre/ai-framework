import httpx
import time

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
        
        start = time.perf_counter()

        response = httpx.post(
            "http://localhost:11434/api/generate",
            json=payload,
            timeout=300,
        )

        elapsed = time.perf_counter() - start
        
        print(f"Request completed in {elapsed:.2f} seconds")

        print("Response received from Ollama.")

        response.raise_for_status()

        data = response.json()

        return LLMResponse(
            text=data["response"],
            thinking=data.get("thinking"),
            model=data.get("model"),
            prompt_tokens=data.get("prompt_eval_count"),
            completion_tokens=data.get("eval_count"),
            total_duration=data.get("total_duration"),
        )
