Sentence Splitter
============================================

This Python class `SentenceSplitter` is designed to split input text into smaller chunks, particularly useful for processing large documents or texts. 
It provides methods to split text into chunks and to split a list of documents into chunks.

_____

| **API Reference**

.. code-block:: python

    from spyder_index.text_splitters import SentenceSplitter

_____

| **SentenceSplitter(chunk_size, chunk_overlap, separators)**

Initialize a SemanticSplitter.

| Parameters:

    - **chunk_size** *(int, optional)* – Size of each chunk. Default is ``512``.
    - **chunk_overlap** *(int, optional)* – Amount of overlap between chunks. Default is ``256``.
    - **separators** *(list[str], optional)* – List of separators used to split the text into chunks. Default separators are ``["\n\n", "\n", " ", ""]``.

_____

| **from_text(text)**

Split text into chunks.

| Parameters:

    - **text** *(str)* – Input text to split.

_____

| **from_documents(documents)**

Split text from a list of documents into chunks.

| Parameters:

    - **documents** *(list[Document])* – List of Documents.