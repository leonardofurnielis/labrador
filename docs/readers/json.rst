JSON
============================================

Loads data from JSON.

_____

| **API Reference**

.. code-block:: python

    from spyder_index.readers.file import JSONReader

_____

| **JSONReader(input_file: str, jq_schema: str, text_content: bool)**

Initialize a JSONReader.

- ``input_file`` (str): File path to read.
- ``jq_schema`` (str): The jq schema to use to extract the data from the JSON.
- ``text_content`` (bool): Flag to indicate whether the content is in string format. Default is ``False``

_____

| **load_data() -> List[Document]**

Loads data from the specified directory.