============================================
JSON
============================================

Loads data from JSON.

API Reference
---------------------

.. code-block:: bash

    pip install jq

.. code-block:: python

    from spyder_index.readers.file import JSONReader

JSONReader(input_file, jq_schema, text_content)
________________________________________________

Initialize a JSONReader.

| Parameters:

    - **input_file** *(str)* – File path to read.
    - **jq_schema** *(str)* – The jq schema to use to extract the data from the JSON.
    - **text_content** *(bool, optional)* – Flag to indicate whether the content is in string format. Default is ``False``

load_data()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Loads the document from specified directory.
