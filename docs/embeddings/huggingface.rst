============================================
Hugging Face
============================================

Computing text embeddings using Hugging Face models.

| API Reference
---------------------

.. code-block:: python

    from spyder_index.embeddings import HuggingFaceEmbedding


| HuggingFaceEmbedding(model_name, device)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Initialize a HuggingFaceEmbedding.

| Parameters:

    - **model_name** *(str, optional)* – Name of the Hugging Face model to be used. Defaults to ``sentence-transformers/all-MiniLM-L6-v2``.
    - **device** *(str["cpu", "cuda"], optional)* – Device to run the model on. Defaults to ``cpu``. 

| get_query_embedding(query)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compute embedding for a query.

| Parameters:

    - **text** *(str)* – Input query to compute embedding.

| get_texts_embedding(texts)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compute embeddings for a list of texts.

| Parameters:

    - **texts** *(List[str])*

| get_documents_embedding(documents)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compute embeddings for a list of Documents.

| Parameters:

    - **documents** *(List[Documents])*

