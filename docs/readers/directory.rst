============================================
Directory
============================================

Provides functionality to load documents from a directory.

| **API Reference**
---------------------

.. code-block:: bash

    pip install docx2txt pypdf

.. code-block:: python

    from spyder_index.readers import DirectoryReader

_____

| **DirectoryReader(input_dir, extra_info, recursive)**

Initialize a DirectoryReader.

| Parameters:

    - **input_dir** *(str)* – The directory path from which to load the documents.
    - **extra_info** *(dict, optional)* – Additional metadata to include in the document.
    - **recursive** *(bool, optional)* – Whether to recursively search for files. Defaults to ``False``.

_____

| **load_data()**

Loads data from the specified directory.
