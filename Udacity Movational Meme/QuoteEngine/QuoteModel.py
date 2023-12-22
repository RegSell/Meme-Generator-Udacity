"""Encapsulate the body and author of the parsed quote."""


class QuoteModel:
    """Quote object."""

    def __init__(self, body, author):
        """Take a body and author string."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return a meme format."""
        return self.body + '-' + self.author
    