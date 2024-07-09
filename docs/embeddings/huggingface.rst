HuggingFace
============================================

Computing text embeddings using HuggingFace models.

_____

| **API Reference**

.. code-block:: python

    from spyder_index.embeddings import HuggingFaceEmbeddings

_____

| **HuggingFaceEmbeddings(model_name, device)**

Initialize a HuggingFaceEmbeddings.

| Parameters:

- **model_name** *(str, optional)* – Name of the HuggingFace model to be used. Defaults to ``sentence-transformers/all-MiniLM-L6-v2``.
- **device** *(str["cpu", "cuda"], optional)* – Device to run the model on. Defaults to ``cpu``. 

_____

| **get_query_embedding(query)**

Compute embedding for a query.

| Parameters:

- **text** *(str)* – Input query to compute embedding.

_____

| **get_texts_embedding(texts)**

Compute embeddings for a list of texts.

| Parameters:

- **texts** *(List[str])*

_____

| **get_documents_embedding(documents)**

Compute embeddings for a list of Documents.

| Parameters:

- **documents** *(List[Documents])*

