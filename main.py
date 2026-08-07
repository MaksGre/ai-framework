from ai.agents.base import Agent
from ai.llm.ollama import OllamaClient
from ai.prompts.engineering_mentor import ENGINEERING_MENTOR_PROMPT

llm = OllamaClient(
    model="qwen3:8b",
)

mentor = Agent(
    name="Engineering Mentor",
    system_prompt=ENGINEERING_MENTOR_PROMPT,
    llm=llm,
)

response = mentor.run("Привет!")

print(response)
