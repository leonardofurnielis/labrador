Directory
============================================

Provides functionality to load documents from a directory.

_____

| **API Reference**

.. code-block:: bash

    pip install docx2txt pypdf

.. code-block:: python

    from spyder_index.readers import DirectoryReader

_____

| **DirectoryReader(input_dir, extra_info, recursive)**

Initialize a DirectoryReader.

- ``input_dir`` (str): The directory path from which to load the documents.
- ``extra_info`` (Optional[dict]): Additional metadata to include in the document.
- ``recursive`` (Optional[bool]): Whether to recursively search for files. Defaults to ``False``.

_____

| **load_data()**

Loads data from the specified directory.
