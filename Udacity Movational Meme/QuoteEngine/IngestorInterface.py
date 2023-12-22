"""Abstract base class for parsing quotes."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract Ingestor classe."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Check for valid file extension."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return QuoteModels for each quote found in a parsed file."""
        pass
    