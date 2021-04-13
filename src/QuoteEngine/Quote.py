class QuoteModel:
    """ takes body and  author as an argument"""

    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """gives human readable name to return"""
        return f"QuoteModel({self.body}, {self.author})"
