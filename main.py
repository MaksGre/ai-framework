from ai.agents.base import Agent
from ai.llm.ollama import OllamaClient
from ai.prompts.builder import PromptBuilder
from ai.prompts.engineering_mentor import ENGINEERING_MENTOR_PROMPT
from ai.context.builder import ContextBuilder
from ai.files.loader import FileLoader
from ai.files.scanner import ProjectScanner
from ai.files.finder import ProjectFinder
from ai.memory.base import Memory

llm = OllamaClient(
    model="qwen3:8b",
)

loader = FileLoader()

prompt_builder = PromptBuilder()

scanner = ProjectScanner()

finder = ProjectFinder(
    scanner = scanner
)

builder = ContextBuilder(
    loader = loader,
    prompt_builder = prompt_builder,
    finder = finder
)

memory = Memory()

mentor = Agent(
    name = "Engineering Mentor",
    system_prompt = ENGINEERING_MENTOR_PROMPT,
    llm = llm,
    builder = builder,
    memory = memory
)

#response = mentor.analyze_file(
#    "ai/context/builder.py",
#    task = "Объясни, зачем нужен ContextBuilder",
#)

mentor.ask("Меня зовут Максим")
mentor.ask("Как меня зовут?")
