============================================
Chroma
============================================

Chroma is the AI-native open-source vector database. In this vector store, embeddings are stored within a ChromaDB collection.

.. code-block:: bash

    pip install chromadb

ChromaVectorStore(collection_name, embedding, distance_strategy)
__________________________________________________________________

Initialize a ChromaVectorStore.

.. code-block:: python

    from spyder_index.vector_stores import ChromaVectorStore

| Parameters:

    - **collection_name** *(str)* – The name of the ChromaDB collection.
    - **embed_model** *(BaseEmbedding)* – Embedding model to use.
    - **distance_strategy** *(str, optional)* – The distance strategy for similarity search. Defaults to ``cosine``.

add_documents(documents)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds documents to the ChromaDB collection.

| Parameters:

    - **documents** *(Document)* – A list of Document objects to add to the collection.

query(query, top_k)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Performs a similarity search for top-k most similar documents.

| Parameters:

    - **query** *(str)* – The query text.
    - **top_k`** *(int)* – The number of top results to return. Defaults to ``4``.

delete(ids)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Deletes documents from the ChromaDB collection.

| Parameters:

    - **ids** *(list[str])* – A list of document IDs to delete. Defaults to ``None``.
