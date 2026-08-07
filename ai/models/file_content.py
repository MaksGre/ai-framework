from dataclasses import dataclass

@dataclass
class FileContent:
    path: str
    extension: str
    content: str
    
    language: str | None = None
    
    size: int | None = None
    
    encoding: str | None = None
