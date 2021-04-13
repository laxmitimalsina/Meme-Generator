from typing import List

import docx

from .IngestorInterface import IngestorInterface
from .Quote import QuoteModel


class DocxIngestor(IngestorInterface):
    """Handels Docx file and extracts quotes from docx file """

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                body, author = para.text.split("-")
                body = body.replace('"', "").strip()
                author = author.strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)
        return quotes
