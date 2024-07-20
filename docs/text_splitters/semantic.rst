============================================
Semantic Splitter
============================================

Semantic Splitter is a Python class designed to split text into chunks using semantic understanding. 
It utilizes pre-trained embeddings to identify breakpoints in the text and divide it into meaningful segments.

``SemanticSplitter(model_name, buffer_size, breakpoint_threshold_amount, device)``
________________________________________________________________________________

Initialize a SemanticSplitter.

.. code-block:: python

    from spyder_index.text_splitters import SemanticSplitter

| Parameters:

    - **embed_model** *(BaseEmbedding)* – Embedding model to use.
    - **buffer_size** *(int, optional)* – Size of the buffer for semantic chunking. Default is ``1``.
    - **breakpoint_threshold_amount** *(int, optional)* – Threshold percentage for detecting breakpoints. Default is ``95``.
    - **device** *(str["cpu", "cuda"], optional)* – Device to use for processing, either "cpu" or "cuda". Default is ``cpu``.

``from_text(text)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Split text into chunks.

| Parameters:

    - **text** *(str)* – Input text to split.

``from_documents(documents)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Split documents into chunks.

| Parameters:

    - **documents** *(list[Document])* – List of Documents.
