import threading
import time

from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings


class CLI:

    def __init__(self, agents):
        self._agents = agents

        bindings = KeyBindings()

        @bindings.add("escape", eager=True)
        def _(event):
            buffer = event.current_buffer
            buffer.text = ""
            buffer.cursor_position = 0

        self._session = PromptSession(
            key_bindings=bindings,
        )

    def run(self) -> None:
        agent = self._select_agent()

        while True:
            try:
                prompt = self._session.prompt("> ")

                if not prompt.strip():
                    continue

                if prompt.lower() in ("exit", "выход"):
                    break

                response = run_with_spinner(
                    lambda: agent.ask(prompt)
                )

                print(response)

            except KeyboardInterrupt:
                print("\nВыход.")
                break

    def _select_agent(self):
        print("Выберите агента:")

        agents = list(self._agents.items())

        for index, (name, _) in enumerate(agents, start=1):
            print(f"{index}. {name}")

        while True:
            choice = input("> ").strip()

            if choice.isdigit():
                index = int(choice) - 1

                if 0 <= index < len(agents):
                    name, agent = agents[index]
                    print(f"\nВыбран агент: {name}\n")
                    return agent

            print("Введите номер агента.")


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
        print(
            f"\rДумаю... {spinner[index % len(spinner)]}",
            end="",
            flush=True,
        )

        index += 1
        time.sleep(0.1)

    thread.join()

    print("\r" + " " * 20 + "\r", end="")

    if error:
        raise error

    return result
