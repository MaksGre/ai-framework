import threading
import time
from ai.llm.ollama import OllamaClient
from ai.assembly import create_engineering_mentor


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

llm = OllamaClient(
    model="qwen3:8b",
)

mentor = create_engineering_mentor()

while True:
    try:
        prompt = input("> ")
        
        if not prompt.strip():
            continue

        if prompt.lower() in ("exit", "выход"):
            break

        response = run_with_spinner(
            lambda: mentor.ask(prompt)
        )
        
        print(response)
        
    except KeyboardInterrupt:
        print("\nВыход.")
        break
