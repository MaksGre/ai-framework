from ai.files.loader import FileLoader

class ContextBuilder:
    def __init__(self, loader: FileLoader):
        self._loader = loader

    def build(self, prompt: str) -> str:
        if prompt.startswith("@"):
            file = self._loader.load(prompt[1:])
            
        return f"""
Проанализируй следующий файл.

Файл: {file.path}
Расширение: {file.extension}

Содержимое: 

{file.content}
""".strip()

        return prompt
