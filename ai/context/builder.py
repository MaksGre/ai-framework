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
        task: str = ""
    ) -> str:
        if not prompt.startswith("@"):
            return prompt
            
        file = self._load_file(prompt[1:])
        
        return self._prompt_builder.build_file_analysis_prompt(
            file,
            task
        )
        
    def build_files(
        self,
        paths: list[str],
        task: str
    ) -> str:
        if not paths:
            raise ValueError("No files provided")

        files = []
        
        for path in paths:
            files.append(
                self._load_file(path)
            )

        return self._prompt_builder.build_files_analysis_prompt(
            files,
            task
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
