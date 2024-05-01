from typing import Literal, List

from langchain_experimental.text_splitter import SemanticChunker
from slate_index.embeddings import HuggingFaceEmbeddings
from slate_index.core.document import Document

class SemanticSplitter():

    def __init__(self, 
                 model_name = "sentence-transformers/all-MiniLM-L6-v2", 
                 buffer_size: int = 1,
                 breakpoint_threshold_amount: int = 95,
                 device: Literal["cpu", "cuda"] = "cpu") -> None:
        
        self.buffer_size = buffer_size
        self.breakpoint_threshold_amount = breakpoint_threshold_amount
        self._embed = HuggingFaceEmbeddings(model_name=model_name, device=device)


    def from_text(self, text: str) -> List[str]: 
        
        text_splitter = SemanticChunker(
            embeddings=self._embed,
            buffer_size=self.buffer_size, 
            breakpoint_threshold_amount=self.breakpoint_threshold_amount)
        
        return text_splitter.split_text(text)
    
    def from_documents(self, documents: List[Document]) -> List[Document]:     
        chunks = []
        
        for document in documents:
            texts = self.from_text(document.get_text())

            for text in texts:
                chunks.append(Document(text=text, metadata=document.get_metadata()))

        return chunks
    