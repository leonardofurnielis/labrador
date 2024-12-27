import os
from pathlib import Path
from typing import List, Optional

from langchain_community.document_loaders import JSONLoader as LangChainJSONLoader

from tempest.core.document import Document
from tempest.core.document_loaders import BaseLoader


class JSONLoader(BaseLoader):
    """JSON loader.

    Args:
        jq_schema (str, optional): jq schema to use to extract the data from the JSON.
        text_content (bool, optional): Flag to indicate whether the content is in string format. Default is ``False``
    """

    jq_schema: Optional[str] = None
    text_content: Optional[bool] = False

    def load_data(self, input_file: str, extra_info: Optional[dict] = None) -> List[Document]:
        """Loads data from the specified directory.
        
        Args:
            input_file (str): File path to load.
        """
        try:
            import jq  # noqa: F401
        except ImportError:
            raise ImportError("jq package not found, please install it with `pip install jq`")
        
        if not os.path.isfile(input_file):
            raise ValueError(f"File `{input_file}` does not exist")
        
        input_file = str(Path(input_file).resolve())
        
        lc_documents = LangChainJSONLoader(file_path=input_file,
                                  jq_schema=self.jq_schema,
                                  text_content=self.text_content).load()

        return [Document().from_langchain_format(doc=doc) for doc in lc_documents]
