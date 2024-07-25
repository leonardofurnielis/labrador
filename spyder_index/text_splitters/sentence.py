from typing import List, Dict, Tuple

from spyder_index.core.document import Document

from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from spyder_index.core.text_splitters.utils import (
    split_by_regex,
    split_by_sep,
    split_by_sentence_tokenizer,
    split_by_char,
    num_tokens
)


class SentenceSplitter():

    def __init__(self,
                 chunk_size: int = 512,
                 chunk_overlap: int = 256,
                 separators=None
                 ) -> None:

        if separators is None:
            separators = ["\n\n", "\n", " ", ""]
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = separators

    def from_text(self, text: str) -> List[str]:
        """
        Split text into chunks.
        
        Args:
        - text (str): Input text to split.
        
        Returns:
        - List[str]: List of chunks.
        """
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=self.separators,
        )

        return text_splitter.split_text(text)

    def from_text_new(self, text: str) -> List[str]:
        """
        Split text into chunks.

        Args:
        - text (str): Input text to split.

        Returns:
        - List[str]: List of chunks.
        """
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=self.separators,
        )

        return text_splitter.split_text(text)

    def from_documents(self, documents: List[Document]) -> List[Document]:
        """
        Documents text into chunks.

        Args:
        - documents List[Document]: Documents to split.

        Returns:
        - List[Document]: List of document chunks.
        """
        chunks = []

        for document in documents:
            texts = self.from_text(document.get_content())

            for text in texts:
                chunks.append(Document(text=text, metadata=document.get_metadata()))

        return chunks

    # [^,.;？！]+[,.;？！]?
    def _split(self, text: str) -> List[str]:
        splits = []

        token_size = num_tokens(text)
        if token_size <= self.chunk_size:
            return self._merge([{"text": text, "is_sentence": True, "token_size": token_size}])

    def _split_by_fns(self, text: str) -> Tuple[List[str], bool]:
        pass

    def _merge(self, splits: List[dict]) -> List[str]:
        pass
