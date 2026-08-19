from ai.agents.base import Agent
from ai.context.builder import ContextBuilder
from ai.files.finder import ProjectFinder
from ai.files.loader import FileLoader
from ai.files.scanner import ProjectScanner
from ai.llm.ollama import OllamaClient
from ai.memory.base import Memory
from ai.prompts.builder import PromptBuilder
from ai.prompts.engineering_mentor import ENGINEERING_MENTOR_PROMPT
from ai.tools.calculator import CalculatorTool
from ai.tools.file import FileTool


def create_engineering_mentor() -> Agent:
    llm = OllamaClient(
        model="qwen3:8b",
    )

    loader = FileLoader()
    prompt_builder = PromptBuilder()
    scanner = ProjectScanner()

    finder = ProjectFinder(
        scanner=scanner,
    )

    builder = ContextBuilder(
        loader=loader,
        prompt_builder=prompt_builder,
        finder=finder,
    )

    memory = Memory()

    calculator = CalculatorTool()

    file_tool = FileTool(
        loader=loader,
        finder=finder,
    )

    return Agent(
        name="Engineering Mentor",
        system_prompt=ENGINEERING_MENTOR_PROMPT,
        llm=llm,
        builder=builder,
        memory=memory,
        tools=[
            calculator,
            file_tool,
        ],
    )
