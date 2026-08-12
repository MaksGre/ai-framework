from ai.files.loader import FileLoader
from ai.prompts.builder import PromptBuilder

class ContextBuilder:
    def __init__(
        self,
        loader: FileLoader,
        prompt_builder: PromptBuilder,
    ):
        self._loader = loader
        self._prompt_builder = prompt_builder

    def build(self, prompt: str) -> str:
        if prompt.startswith("@"):
            file = self._loader.load(prompt[1:])
            
        return self._prompt_builder.build_file_analysis(file)
