from QuoteEngine import (
    CSVIngestor,
    DocxIngestor,
    IngestorInterface,
    PDFIngestor,
    TextIngestor,
)


class Ingestor(IngestorInterface):
    ingestors = [PDFIngestor, TextIngestor, CSVIngestor, DocxIngestor]
    allowed_extensions = [
        ext for ingestor in ingestors for ext in ingestor.allowed_extensions
    ]

    @classmethod
    def parse(cls, path: str):
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        raise Exception(f"Extension not valid. Must be one of {cls.allowed_extensions}")
