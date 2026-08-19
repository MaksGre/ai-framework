import threading
import time
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings

class CLI:

    def __init__(self, mentor):
        self._mentor = mentor

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
        while True:
            try:
                prompt = self._session.prompt("> ")

                if not prompt.strip():
                    continue

                if prompt.lower() in ("exit", "выход"):
                    break

                response = run_with_spinner(
                    lambda: self._mentor.ask(prompt)
                )

                print(response)

            except KeyboardInterrupt:
                print("\nВыход.")
                break

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
