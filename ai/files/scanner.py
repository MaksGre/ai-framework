from pathlib import Path
from ai.models.file_info import FileInfo

IGNORED_DIRS = {
    ".git",
    ".venv",
    "__pycache__"
}

class ProjectScanner:
    def scan(self, root: str) -> list[FileInfo]:
        files = []
        
        for path in Path(root).rglob("*"):
            if any(part in IGNORED_DIRS for part in path.parts):
                continue
                
            if path.is_file():
                files.append(
                    FileInfo(
                        path = str(path)
                    )
                )
                
        return files
