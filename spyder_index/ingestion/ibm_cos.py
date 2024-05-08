from pathlib import Path
from typing import List
from pydantic import BaseModel, Field

from spyder_index.core.document import Document

class IBMS3DirectoryLoader(BaseModel):
            ibm_api_key_id: str = Field(default="")
            ibm_service_instance_id: str = Field(default="")
            ibm_service_instance_id: str = Field(default="")
            s3_endpoint_url: str = Field(default="")

    def load_data(self, dir) -> List[Document]: 

        llama_documents = SimpleDirectoryReader(
            input_dir=Path(dir).absolute(), 
            file_extractor=self.supported_file_loader, 
            required_exts= list(self.supported_file_loader.keys())).load_data()

        return [Document()._from_llama_index_format(doc=doc) for doc in llama_documents]
