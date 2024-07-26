from typing import List

from spyder_index.core.document import Document

from langchain_text_splitters.character import RecursiveCharacterTextSplitter


class SentenceSplitter():
    """
    Args:
        chunk_size (int, optional): Size of each chunk. Default is ``512``.
        chunk_overlap (int, optional): Amount of overlap between chunks. Default is ``256``.
        separators (List, optional): List of separators used to split the text into chunks.
    """

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
        """Split text into chunks.
        
        Args:
        - text (str): Input text to split.
        """

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=self.separators,
        )

        return text_splitter.split_text(text)

    def from_documents(self, documents: List[Document]) -> List[Document]:
        """Split documents into chunks.

        Args:
            documents (List[Document]): List of Documents
        """

        chunks = []

        for document in documents:
            texts = self.from_text(document.get_content())

            for text in texts:
                chunks.append(Document(text=text, metadata=document.get_metadata()))

        return chunks
