from typing import List
from abc import ABC, abstractmethod

class Embeddings(ABC):
    """Interface for embedding models."""

    @classmethod
    def class_name(cls) -> str:
        return "Embeddings"
    
    @abstractmethod
    def get_text_embedding(self, text: str) -> List[float]:
        """Embed query text."""
    
    @abstractmethod
    def get_text_embeddings(self, texts: List[str]) -> List[float]:
        """Embed list of texts."""

    @abstractmethod
    def get_documents_embedding(self, nodes: List[str]) -> List[List[float]]:
        """Embed search docs."""

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.get_text_embeddings(texts=texts)