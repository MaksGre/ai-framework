import httpx
import time

from .client import LLMClient
from .models import LLMRequest, LLMResponse, ToolCall


class OllamaClient(LLMClient):
    def __init__(
        self,
        base_url: str = "http://localhost:11434",
        model: str = "qwen3:8b",
    ):
        self._model = model

        self._client = httpx.Client(
            base_url = base_url,
            timeout = 120,
        )

    def generate(self, request: LLMRequest) -> LLMResponse:
        start = time.perf_counter()
        
        payload = {
            "model": self._model,
            "messages": request.messages,
            "stream": False,
            "think": False,
            "options": {
                "num_predict": 3072,
            }
        }
        
        if request.tools:
            payload["tools"] = request.tools
        
        response = self._client.post(
            "/api/chat",
            json=payload
        )

        elapsed = time.perf_counter() - start
        
        print(f"Request completed in {elapsed:.2f} seconds")
        
        response.raise_for_status()

        data = response.json()
        
        prompt_tokens = data.get("prompt_eval_count")
        completion_tokens = data.get("eval_count")

        print(f"Tokens: {prompt_tokens} prompt + {completion_tokens} completion = {prompt_tokens + completion_tokens} total")
        
        print(f"Done reason: {data.get('done_reason')}")
        
        return LLMResponse(
            text = data["message"].get("content", ""),
            total_duration = data.get("total_duration"),
            thinking = data["message"].get("thinking"),
            model = data.get("model"),
            prompt_tokens = data.get("prompt_eval_count"),
            completion_tokens = data.get("eval_count"),
            done_reason = data.get("done_reason"),
            tool_calls = [
                ToolCall(
                    id = tool_call["id"],
                    name = tool_call["function"]["name"],
                    arguments = tool_call["function"]["arguments"],
                 )
                 for tool_call in data["message"].get("tool_calls", [])
            ]
        )
