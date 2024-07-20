============================================
Coverage %
============================================

Indicates how much the KnowledgeBase has contributed to the answer's coverage. If the LLM response contains information from the KnowledgeBase, this percentage is going to be very high.

``KnowledgeBaseCoverage(embed_model, similarity_mode, similarity_threshold)``
____________________________________________________________________________

Initialize a KnowledgeBaseCoverage.

.. code-block:: python

    from spyder_index.evaluation import KnowledgeBaseCoverage

| Parameters:

    - **embed_model** *(BaseEmbedding)* – Embedding model to use.
    - **similarity_mode** *(str["cosine", "dot_product", "euclidean"], optional)* – The similarity strategy. Defaults to ``cosine``.
    - **similarity_threshold** *(int, optional)* – Embedding similarity threshold for "passing". Defaults to ``0.8``.

``evaluate(contexts, output)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Parameters:

    - **contexts** *(list[str])* – List of Strings used as LLM context.
    - **output** *(str)* – The LLM response based on given context.
