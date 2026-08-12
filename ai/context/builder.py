from ai.files.loader import FileLoader
from ai.prompts.builder import PromptBuilder
from ai.files.finder import ProjectFinder

class ContextBuilder:
    def __init__(
        self,
        loader: FileLoader,
        prompt_builder: PromptBuilder,
        finder: ProjectFinder,
    ):
        self._loader = loader
        self._prompt_builder = prompt_builder
        self._finder = finder

    def build(self, prompt: str) -> str:
        if not prompt.startswith("@"):
            return prompt
            
        files = self._finder.find(
                name = prompt[1:],
                root = "."
        )
            
        if not files:
            raise FileNotFoundError(prompt[1:])
            
        if len(files) > 1:
            raise ValueError(
                f"Found multiple files: {[file.path for file on files]}"
             )
            
        file = self._loader.load(files[0].path)
        
        return self._prompt_builder.build_file_analysis(file)
