Semantic Splitter
============================================

Semantic Splitter is a Python class designed to split text into chunks using semantic understanding. 
It utilizes pre-trained embeddings to identify breakpoints in the text and divide it into meaningful segments.

_____

| **API Reference**

.. code-block:: python

    from spyder_index.text_splitters import SemanticSplitter

_____

| **SemanticSplitter(model_name, buffer_size, breakpoint_threshold_amount, device)**

Initialize a SemanticSplitter.

- ``model_name``: Name of the pre-trained embeddings model to use. Default is ``sentence-transformers/all-MiniLM-L6-v2``.
- ``buffer_size``: Size of the buffer for semantic chunking. Default is ``1``.
- ``breakpoint_threshold_amount``: Threshold percentage for detecting breakpoints. Default is ``95``.
- ``device``: Device to use for processing, either "cpu" or "cuda". Default is ``cpu``.

_____

| **from_text(text)**

Split text into chunks.

- ``text``: Input text to split.

_____

| **from_documents(documents)**

Split text from a list of documents into chunks.

- ``documents``: List of Documents.