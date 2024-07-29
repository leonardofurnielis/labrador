from typing import List, Tuple

from spyder_index.core.document import Document

from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from spyder_index.core.text_splitters.utils import (
    split_by_regex,
    split_by_sep,
    split_by_sentence_tokenizer,
    split_by_char,
    tokenizer
)


class SentenceSplitter:
    """SentenceSplitter is designed to split input text into smaller chunks,
    particularly useful for processing large documents or texts.

    Args:
        chunk_size (int, optional): Size of each chunk. Default is ``512``.
        chunk_overlap (int, optional): Amount of overlap between chunks. Default is ``256``.
        separator (str, optional): Separators used to split the text into chunks.
    """

    def __init__(self,
                 chunk_size: int = 512,
                 chunk_overlap: int = 256,
                 separator="\n\n\n"
                 ) -> None:

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separator = separator

        self._split_fns = [
            split_by_sep(self.separator),
            split_by_sentence_tokenizer()
        ]
        self._sub_split_fns = [
            split_by_regex("[^,.;？！]+[,.;？！]?"),
            split_by_sep(" "),
            split_by_char()
        ]

    def from_text(self, text: str) -> List[str]:
        """Split text into chunks.
        
        Args:
        - text (str): Input text to split.
        """

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            # separators=self.separators,
        )

        return text_splitter.split_text(text)

    def from_text_new(self, text: str) -> List[str]:
        splits = self._split(text)
        chunks = self._merge(splits)

        return chunks

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

    def _split(self, text: str) -> List[dict]:

        token_size = len(tokenizer(text))
        if token_size <= self.chunk_size:
            return [{"text": text, "is_sentence": True, "token_size": token_size}]

        text_splits = []
        text_splits_by_fns, is_sentence = self._split_by_fns(text)

        for text_split_by_fns in text_splits_by_fns:
            token_size = len(tokenizer(text))
            if token_size <= self.chunk_size:
                text_splits.append({"text": text_split_by_fns, "is_sentence": is_sentence, "token_size": token_size})

            else:
                recursive_text_splits = self._split(text_split_by_fns)
                text_splits.extend(recursive_text_splits)

        return text_splits

    def _split_by_fns(self, text: str) -> Tuple[List[str], bool]:

        for split_fn in self._split_fns:
            splits = split_fn(text)
            if len(splits) > 1:
                return splits, True

        for split_fn in self._sub_split_fns:
            splits = split_fn(text)
            if len(splits) > 1:
                return splits, False

    def _merge(self, splits: List[dict]) -> List[str]:
        pass
