HuggingFace
============================================

Computing text embeddings using HuggingFace models.

_____

| **API Reference**

.. code-block:: python

    from spyder_index.embeddings import HuggingFaceEmbeddings

_____

| **HuggingFaceEmbeddings(model_name: str, device: Literal["cpu", "cuda"])**

Initialize a HuggingFaceEmbeddings.

- ``model_name`` (str, optional): Name of the HuggingFace model to be used. Defaults to ``sentence-transformers/all-MiniLM-L6-v2``.
- ``device`` (Literal["cpu", "cuda"], optional): Device to run the model on. Defaults to ``cpu``.

_____

| **get_query_embedding(query: str) -> List[float]**

Compute embedding for a query.

- ``text`` (str): Input query to compute embedding.

_____

| **get_embedding_from_texts(texts: List[str]) -> List[List[float]]**

Compute embeddings for a list of texts.

- ``texts`` (List[str])

_____

| **get_documents_embedding(documents: List[str]) -> List[List[float]]**

Compute embeddings for a list of Documents.

- ``documents`` (List[Documents])

