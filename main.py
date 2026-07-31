from ai.llm.models import LLMRequest
from ai.llm.ollama import OllamaClient

llm = OllamaClient()

response = llm.generate(
    LLMRequest(prompt="Привет! Кто ты?")
)

print(response.text)
