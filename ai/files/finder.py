from ai.files.scanner import ProjectScanner


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
    ) -> List[FileInfo]:
        raise NotEmplementedError
