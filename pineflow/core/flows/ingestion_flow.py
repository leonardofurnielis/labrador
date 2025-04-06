
from typing import List, Optional
from pineflow.core.document.schema import Document
from pineflow.core.readers.base import BaseReader


class IngestionFlow():

    def __init__(self, 
                 readers: List[BaseReader]=None):
        
        self.readers = readers
    
    def _read_documents(self, documents: Optional[List[Document]]):
        input_documents = List[Document] = []
        
        if documents is not None:
            input_documents.extend(documents)
            
        if self.readers is not None:
            for reader in self.readers:
                input_documents.extend(reader.load_data())
        
        return input_documents    
        
    def _transform(documents: List[Document], transformations):
        for transform in transformations:
            documents = transform(documents)
        
        return documents    
    
    def run(self, documents: List[Document]=None):
        input_documents = self._read_documents(documents)
        
        documents = self._transform(input_documents)
        
        documents = documents or []
        
        return documents
        
        
        