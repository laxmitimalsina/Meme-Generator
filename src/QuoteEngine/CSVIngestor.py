"""Handels csv file format."""
from typing import List

import pandas

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.Quote import QuoteModel

from .IngestorInterface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """Handles csv file and extracts quotes."""

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse path if its on allowed_extensions or not and returns list."""
        if not cls.can_ingest(path):
            raise Exception("can't ingest excepction")

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quotes = QuoteModel(row["body"], row["author"])
            quotes.append(new_quotes)
        return quotes
