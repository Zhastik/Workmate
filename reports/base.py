from abc import ABC, abstractmethod
from typing import Any


class BaseReport(ABC):
    name: str

    @abstractmethod
    def build(self, rows: list[dict[str, Any]]) -> tuple[list[str], list[list[Any]]]:
        raise NotImplementedError