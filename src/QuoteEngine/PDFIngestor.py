"""Handels Pdf files."""
import os
import random
import subprocess
from typing import List

from .IngestorInterface import IngestorInterface
from .Quote import QuoteModel

# from pdfminer.high_level import extract_text


class PDFIngestor(IngestorInterface):
    """Handles pdf files and extracts quotes from pdf file."""

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse path if its on allowed_extensions or not and returns list."""
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        tmp = f"./tmp/{random.randint(0,1000000)}.txt"
        call = subprocess.call(["pdftotext", path, tmp])
        file_ref = open(tmp, "r")
        quotes = []

        # text = extract_text(path)
        # lines = text.split("\n")

        for line in file_ref.readlines():
            line = line.strip()
            if line == "":
                continue
            body, author = line.split("-")
            body = body.replace('"', "").strip()
            author = author.strip()
            new_quote = QuoteModel(body, author)
            quotes.append(new_quote)
        file_ref.close()
        os.remove(tmp)

        return quotes
