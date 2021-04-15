"""Ingestor Interface for all the file format."""
from abc import ABC, abstractmethod
from typing import List

from .Quote import QuoteModel


class IngestorInterface(ABC):
    """Using Abstract Base Classess."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Check path is in allowed extensions."""
        ext = path.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Other child classes using function can overide."""
        pass
