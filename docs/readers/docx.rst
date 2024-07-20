============================================
Docx
============================================

Loads data from Microsoft Word (Docx) format.

API Reference
---------------------

.. code-block:: bash

    pip install docx2txt

.. code-block:: python

    from spyder_index.readers.file import DocxReader

DocxReader(input_file)
________________________

Initialize a DocxReader.

| Parameters:

    - **input_file** *(str)* – File path to read.

load_data()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Loads the document from specified directory.
