from logging import exception
from typing import List
from .Quote import QuoteModel
from .IngestorInterface import IngestorInterface


class TextIngestor(IngestorInterface):
    """ handels files with .txt extention and extracts quotes"""

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("not able to ingest file")

        quotes = []
        with open(path, encoding="utf-8-sig") as file:
            for line in file:
                body, author = line.split("-")
                body = body.strip().strip(".")
                author = author.strip("\n").strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

            return quotes

