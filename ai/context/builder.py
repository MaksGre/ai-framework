from ai.files.loader import FileLoader
from ai.prompts.builder import PromptBuilder
from ai.files.finder import ProjectFinder
from ai.models.file_content import FileContent

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
        
    def build(
        self,
        prompt: str,
    ) -> str:

        if not prompt.startswith("@"):
            return prompt

        lines = prompt.splitlines()

        file_name = lines[0][1:].strip()
        task = "\n".join(lines[1:]).strip()

        file = self._load_file(file_name)

        return self._prompt_builder.build_file_analysis_prompt(
            file,
            task,
        )

    def _load_file(self, name: str) -> FileContent:
        matches = self._finder.find(
            name = name,
            root = "."
        )
        
        if not matches:
            raise FileNotFoundError(name)
            
        if len(matches) > 1:
            raise ValueError(
                f"Found multiple files: {[file.path for file in matches]}"
            )

        return self._loader.load(matches[0].path)
