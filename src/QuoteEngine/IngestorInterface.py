from abc import ABC, abstractmethod
from typing import List

from .Quote import QuoteModel


class IngestorInterface(ABC):
    """ Using Abstract Base Classess """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Takes path as a argument and use it to check if the
        path is on the extension list and returns Boolean value """
        ext = path.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Is defined so that other child classes using
         this function can overide the function as per requirement"""
        pass

