from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel, Field

from spyder_index.core.document import Document

from llama_index.readers.file import PDFReader
from llama_index.readers.file import DocxReader
# from llama_index.readers.file import PptxReader
from llama_index.readers.file import HTMLTagReader

from llama_index.core import SimpleDirectoryReader


class DirectoryReader(BaseModel):
    input_dir: str = Field(default="")
    extra_info: Optional[dict] = Field(default=None)
    supported_file_reader: dict = {
        '.pdf': PDFReader(),
        '.docx': DocxReader(), 
        # '.pptx': PptxReader(), #download_loader('PptxReader'),
        '.html': HTMLTagReader(), 
        # '.txt': download_loader('UnstructuredReader'),
        }

    def load_data(self) -> List[Document]:

        llama_documents = SimpleDirectoryReader(
            input_dir=Path(self.input_dir).absolute(), 
            file_extractor=self.supported_file_loader, 
            required_exts=list(self.supported_file_loader.keys())).load_data()
        
        return [Document()._from_llama_index_format(doc=doc, metadata=self.extra_info) for doc in llama_documents]
