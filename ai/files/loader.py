from pathlib import Path
from ai.models.file_content import FileContent

class FileLoader:
    def load(self, path: str) -> FileContent:
        file = Path(path)
        
        return FileContent(
            path=str(file),
            extension=file.suffix,
            content=file.read_text(
                encoding="utf-8",
            ),
        )
