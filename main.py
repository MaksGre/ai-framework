from ai.agents.base import Agent
from ai.llm.ollama import OllamaClient
from ai.prompts.engineering_mentor import ENGINEERING_MENTOR_PROMPT
from ai.context.builder import ContextBuilder
from ai.files.loader import FileLoader

llm = OllamaClient(
    model="qwen3:8b",
)

loader = FileLoader()

builder = ContextBuilder(
    loader = loader
)

mentor = Agent(
    name="Engineering Mentor",
    system_prompt=ENGINEERING_MENTOR_PROMPT,
    llm=llm,
    builder=builder,
)

response = mentor.analyze_file("README.md")

print(response)
