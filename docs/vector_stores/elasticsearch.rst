Elasticsearch
============================================

Provides functionality to interact with Elasticsearch for storing and querying document embeddings. 
It facilitates adding documents, performing similarity searches, and deleting documents from an Elasticsearch index.

_____

| **API Reference**

.. code-block:: bash

    pip install elasticsearch

.. code-block:: python

    from spyder_index.vector_stores import ElasticsearchVectorStore

_____

| **ElasticsearchVectorStore(index_name, es_hostname, es_user, es_password, dims_length, embedding, batch_size, ssl, distance_strategy, text_field, vector_field)**

Initialize a ElasticsearchVectorStore.

| Parameters:

- **index_name** *(str)* – The name of the Elasticsearch index.
- **es_hostname** *(str)* – The hostname of the Elasticsearch instance.
- **es_user** *(str)* – The username for authentication.
- **es_password** *(str)* – The password for authentication.
- **dims_length** *(int)* – The length of the embedding dimensions.
- **embedding** *(Embeddings)* – An instance of embeddings.
- **batch_size** *(int, optional)* – The batch size for bulk operations. Defaults to ``200``.
- **ssl** *(bool, optional)* – Whether to use SSL. Defaults to ``False``.
- **distance_strategy** *(str, optional)* – The distance strategy for similarity search. Defaults to ``cosine``.
- **text_field** *(str, optional)* – The name of the field containing text. Defaults to ``text``.
- **vector_field** *(str, optional)* – The name of the field containing vector embeddings. Defaults to ``embedding``.

_____

| **add_documents(documents, create_index_if_not_exists)**

Adds documents to the Elasticsearch index.

| Parameters:

- **documents** *(Document)* – A list of Document objects to add to the index.
- **create_index_if_not_exists** *(bool, optional)* – Whether to create the index if it doesn't exist. Defaults to ``True``.

_____

| **similarity_search(query, top_k)**

Performs a similarity search based on the documents most similar to the query.

| Parameters:

- **query** *(str)* – The query text.
- **top_k`** *(int)* – The number of top results to return. Defaults to ``4``.

_____

| **delete(ids)**

Deletes documents from the Elasticsearch index.

| Parameters:

- **ids** *(list[str])* – A list of document IDs to delete. Defaults to ``None``.