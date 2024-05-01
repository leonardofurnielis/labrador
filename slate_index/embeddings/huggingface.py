from typing import List, Literal

from slate_index.core.document import Document
from slate_index.core.embeddings import Embeddings

from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings as LangchainHuggingFaceEmbeddings

class HuggingFaceEmbeddings(Embeddings):

    def __init__(self, 
                 model_name: str= "sentence-transformers/all-MiniLM-L6-v2", 
                 device: Literal["cpu", "cuda"] = "cpu") -> None:
        
        model_kwargs = {
            "device": device
        }

        self._embed = LangchainHuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)
    
    def get_text_embedding(self, text: str) -> List[float]: 
        embedding_text = self._embed.embed_query(text) 

        return embedding_text

    def get_text_embeddings(self, texts: List[str]) -> List[List[float]]:

        embedding_texts = self._embed.embed_documents(texts=texts)

        return embedding_texts
    
    def get_documents_embedding(self, documents: List[Document]) -> List[List[float]]:

        embedding_documents = [self.get_text_embedding(doc.get_text()) for doc in documents]

        return embedding_documents

