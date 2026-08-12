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
                f"Found multiple files: {[file.path for file in files]}"
             )
            
        file = self._loader.load(files[0].path)
        
        return self._prompt_builder.build_file_analysis_prompt(file)
        
    def build_files(
        self,
        paths: list[str],
    ) -> str:
        if not paths:
            raise ValueError("No files provided")

        files = []        
        
        for path in paths:
            matches = self._finder.find(
                name = path,
                root = "."
            )
        
            if not matches:
                raise FileNotFoundError(path)
                
            if len(matches) > 1:
                raise ValueError(
                    f"Found multiple files: {[file.path for file in matches]}"
                )
                
            files.append(
                self._loader.load(matches[0].path)
            )

        return self._prompt_builder.build_files_analysis_prompt(files)
