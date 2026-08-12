from ai.files.scanner import ProjectScanner
from ai.models.file_info import FileInfo


class ProjectFinder:
    def __init__(
        self,
        scanner: ProjectScanner
    ):
        self._scanner = scanner
        
    def find(
        self,
        name: str,
        root: str,
    ) -> list[FileInfo]:
        files = self._scanner.scan(root)
        
        return [
            file
            for file in files
            if file.path.endswith(name)
        ]
