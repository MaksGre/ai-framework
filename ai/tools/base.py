from abc import ABC, abstractmethod


class Tool(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def execute(self, **kwargs) -> str:
        pass

    @abstractmethod
    def schema(self) -> dict:
        pass
