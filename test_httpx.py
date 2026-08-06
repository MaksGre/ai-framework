import httpx

response = httpx.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen3:8b",
        "prompt": "Привет",
        "stream": False,
    },
    timeout=60,
)

print(response.status_code)
print(response.json()["response"])
