"""Parsing the text file."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Ingest a text file."""
    
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return QuoteModels for each quote found in the txt parsed file."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        file = open(path, "r", encoding='utf-8-sig')
        lines = file.readlines()
        file.close()

        quotes = []

        for quote in lines:
            parsed = quote.rstrip("\n").split(" - ")
            if len(parsed) > 1:
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        return quotes
    