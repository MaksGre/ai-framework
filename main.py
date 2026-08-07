from ai.agents.base import Agent
from ai.llm.ollama import OllamaClient
from ai.prompts.engineering_mentor import ENGINEERING_MENTOR_PROMPT
from ai.context.builder import ContextBuilder

llm = OllamaClient(
    model="qwen3:8b",
)

builder = ContextBuilder()

mentor = Agent(
    name="Engineering Mentor",
    system_prompt=ENGINEERING_MENTOR_PROMPT,
    llm=llm,
    builder=builder,
)

response = mentor.run("Привет!")

print(response)
