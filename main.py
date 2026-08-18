import threading
import time
from ai.agents.base import Agent
from ai.llm.ollama import OllamaClient
from ai.prompts.builder import PromptBuilder
from ai.prompts.engineering_mentor import ENGINEERING_MENTOR_PROMPT
from ai.context.builder import ContextBuilder
from ai.files.loader import FileLoader
from ai.files.scanner import ProjectScanner
from ai.files.finder import ProjectFinder
from ai.memory.base import Memory
from ai.tools.calculator import CalculatorTool


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

mentor = Agent(
    name = "Engineering Mentor",
    system_prompt = ENGINEERING_MENTOR_PROMPT,
    llm = llm,
    builder = builder,
    memory = memory,
    tools = [calculator],
)

def run_with_spinner(func):
    result = None
    error = None
    finished = threading.Event()

    def worker():
        nonlocal result, error

        try:
            result = func()
        except Exception as e:
            error = e
        finally:
            finished.set()

    thread = threading.Thread(target=worker)
    thread.start()

    spinner = ["|", "/", "-", "\\"]
    index = 0

    while not finished.is_set():
        print(f"\rДумаю... {spinner[index % len(spinner)]}", end="", flush=True)
        index += 1
        time.sleep(0.1)

    thread.join()

    print("\r" + " " * 20 + "\r", end="")

    if error:
        raise error

    return result

while True:
    try:
        prompt = input("> ")
        
        if not prompt.strip():
            continue

        if prompt.lower() in ("exit", "quit"):
            break

        response = run_with_spinner(
            lambda: mentor.ask(prompt)
        )
        
        print(response)
        
    except KeyboardInterrupt:
        print("\nВыход.")
        break
