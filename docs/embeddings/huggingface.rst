============================================
Hugging Face
============================================

Computing text embeddings using Hugging Face models.

``HuggingFaceEmbedding``
___________________________________________

Initialize a HuggingFaceEmbedding.

.. code-block:: python

    from spyder_index.embeddings import HuggingFaceEmbedding

| **Parameters**:

    - **model_name** *(str, optional)* – Name of the Hugging Face model to be used. Defaults to ``sentence-transformers/all-MiniLM-L6-v2``.
    - **device** *(str["cpu", "cuda"], optional)* – Device to run the model on. Defaults to ``cpu``.

``get_query_embedding``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compute embedding for a query.

| **Parameters**:

    - **text** *(str)* – Input query to compute embedding.

| **Returns**:

    - ``List[float]``

``get_texts_embedding``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compute embeddings for a list of texts.

| **Parameters**:

    - **texts** *(List[str])*

| **Returns**:

    - ``List[List[float]]``

``get_documents_embedding``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compute embeddings for a list of Documents.

| **Parameters**:

    - **documents** *(List[Documents])*

| **Returns**:

    - ``List[List[float]]``
