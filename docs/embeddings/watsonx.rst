============================================
IBM watsonx.ai
============================================

Computing text embeddings using IBM watsonx.ai models.

| **API Reference**
---------------------

.. code-block:: bash

    pip install ibm-watsonx-ai

.. code-block:: python

    from spyder_index.embeddings import WatsonxEmbedding


| **WatsonxEmbedding(model_name, api_key, url, truncate_input_tokens, project_id, space_id)**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Initialize a WatsonxEmbedding.

| Parameters:

   - **model_name** *(str, optional)* – Name of the IBM watsonx.ai model to be used. Defaults to ``ibm/slate-30m-english-rtrvr``.
   - **api_key** *(str)* – Your API Key for accessing IBM watsonx.ai.
   - **url** *(str)* – Your service instance url.
   - **truncate_input_tokens** *(int)* – Represents the maximum number of input tokens accepted.
   - **project_id** *(str, optional)* – The ID of the watsonx.ai project.
   - **space_id** *(str, optional)* – The ID of the watsonx.ai space.

.. note::
   One of these parameters is required: [project_id, space_id].

.. note::
   For the watsonx.ai API endpoints: https://cloud.ibm.com/apidocs/watsonx-ai#endpoint-url

| **get_query_embedding(query)**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compute embedding for a query.

| Parameters:

   - **text** *(str)* – Input query to compute embedding.

| **get_texts_embedding(texts)**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compute embeddings for a list of texts.

| Parameters:

   - **texts** *(list[str])*

| **get_documents_embedding(documents)**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compute embeddings for a list of Documents.

| Parameters:

   - **documents** *(list[Documents])*

