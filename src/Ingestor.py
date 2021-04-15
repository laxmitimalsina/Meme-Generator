"""Loops over different file with different format."""


from QuoteEngine import (
    CSVIngestor,
    DocxIngestor,
    IngestorInterface,
    PDFIngestor,
    TextIngestor,
)


class Ingestor(IngestorInterface):
    """Parses data from different data sources."""

    ingestors = [PDFIngestor, TextIngestor, CSVIngestor, DocxIngestor]
    allowed_extensions = [
        ext for ingestor in ingestors for ext in ingestor.allowed_extensions
    ]

    @classmethod
    def parse(cls, path: str):
        """Parse path if its on allowed_extensions or not and returns list."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        raise Exception(
            f"Extension not valid.\
            Must be one of {cls.allowed_extensions}"
        )
