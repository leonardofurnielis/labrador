Coverage %
============================================

Indicates how much the KnowledgeBase has contributed to the answer's coverage. If the LLM response contains information from the KnowledgeBase, this percentage is going to be very high.

_____

| **API Reference**

.. code-block:: python

    from spyder_index.evaluation import KnowledgeBaseCoverage

_____

| **KnowledgeBaseCoverage(embed_model_name, similarity_mode, similarity_threshold)**

Initialize a KnowledgeBaseCoverage.

PARAMETERS:
- **embed_model_name** *(str)* – Name of the HuggingFace model to be used. Defaults to ``sentence-transformers/all-MiniLM-L6-v2``.
- **similarity_mode** *(dict, optional)* – The similarity strategy. Defaults to ``cosine``.
- **similarity_threshold** *(bool, optional)* – Embedding similarity threshold for "passing". Defaults to ``0.8``.

_____

| **evaluate(contexts, response)**

PARAMETERS:
- **contexts** *(list[str])* – List of Strings used as LLM context.
- **response** *(str)* – The LLM response based on given context.
