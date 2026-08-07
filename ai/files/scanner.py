from pathlib import Path
from ai.models.file_info import FileInfo


class ProjectScanner:
    def scan(self, root: str) -> list[FileInfo]:
        files = []
        
        for path in Path(root).rglob("*"):
            if path.is_file():
                files.append(
                    FileInfo(
                        path = str(path)
                    )
                )
                
        return paths
