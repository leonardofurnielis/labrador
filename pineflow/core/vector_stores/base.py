from abc import ABC, abstractmethod
from typing import List

from pineflow.core.document.schema import Document


class BaseVectorStore(ABC):
    """An interface for vector store."""

    @classmethod
    def class_name(cls) -> str:
        return "BaseVectorStore"

    @abstractmethod
    def add_documents(self, documents: List[Document]) -> List[str]:
        """Add documents to vector store."""

    @abstractmethod
    def query(self, query: str, top_k: int = 4) -> List[Document]:
        """Query vector store."""

    @abstractmethod
    def delete_documents(self, ids: List[str] = None) -> None:
        """Delete documents from vector store."""
        