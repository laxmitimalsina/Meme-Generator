"""Model for extracting quotes."""


class QuoteModel:
    """Take body and  author as an argument."""

    def __init__(self, body: str, author: str):
        """Instanciate QuoteModel class."""
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """Give human readable name to return."""
        return f"QuoteModel({self.body}, {self.author})"
