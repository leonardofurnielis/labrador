
from typing import List, Optional

from pineflow.core.document.schema import Document
from pineflow.core.readers.base import BaseReader


class IngestionFlow():
    def __init__(self, 
                 transformers,
                 readers: List[BaseReader]=None):
        
        self.transformers = transformers
        self.readers = readers
    
    def _read_documents(self, documents: Optional[List[Document]]):
        input_documents = []
        
        if documents is not None:
            input_documents.extend(documents)
            
        if self.readers is not None:
            for reader in self.readers:
                input_documents.extend(reader.load_data())
        
        return input_documents    
        
    def _run_transformers(self, documents: List[Document], transformers):
        for transformer in transformers:
            documents = transformer(documents)
        
        return documents    
    
    def run(self, documents: List[Document]=None):
        input_documents = self._read_documents(documents)
        
        documents = self._run_transformers(input_documents, self.transformers)
        
        return documents or []
        
        
        