from ai.files.finder import ProjectFinder
from ai.files.loader import FileLoader
from ai.tools.base import Tool


class FileTool(Tool):

    def __init__(
        self,
        loader: FileLoader,
        finder: ProjectFinder,
    ):
        self._loader = loader
        self._finder = finder

    @property
    def name(self) -> str:
        return "read_file"

    @property
    def description(self) -> str:
        return (
            "Reads the contents of a project file. "
            "Use this tool when you need to inspect or analyze "
            "a file from the project."
        )
        
    def execute(self, **kwargs) -> str:
        path = kwargs["path"]

        matches = self._finder.find(
            name=path,
            root=".",
        )

        if not matches:
            raise FileNotFoundError(path)

        if len(matches) > 1:
            raise ValueError(
                f"Found multiple files: {[file.path for file in matches]}"
            )

        file = self._loader.load(matches[0].path)

        return file.content

    def schema(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": (
                                "Path to the project file, for example "
                                "'ai/agents/base.py'."
                            ),
                        },
                    },
                    "required": ["path"],
                },
            },
        }
