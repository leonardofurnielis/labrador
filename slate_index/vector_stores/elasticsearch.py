import uuid
import logging
from typing import List, Optional

from slate_index.core.document import Document
from slate_index.core.embeddings import Embeddings
from slate_index.core.vector_stores import VectorStoreQueryResult

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

class ElasticsearchVectorStore():

    def __init__(self, 
                 index_name: str, 
                 es_hostname: str,
                 es_user: str,
                 es_password: str,
                 dims_length: int,
                 embedding: Embeddings,
                 batch_size: int = 200,
                 ssl: bool = False,
                 distance_strategy: str = "cosine",
                 text_field:str  = "text",
                 vector_field:str  = "embedding",
                 ) -> None:
        
        #  TO-DO: Add connections types e.g: cloud
        self._embed = embedding
        self.index_name = index_name
        self.batch_size = batch_size
        self.dims_length = dims_length
        self.distance_strategy = distance_strategy
        self.vector_field = vector_field
        self.text_field = text_field

        self._client = Elasticsearch(
         hosts=[es_hostname],
         basic_auth=(
             es_user,
             es_password
         ),
         verify_certs=ssl,
         ssl_show_warn=False
        )

        try:
            self._client.info() 
        except Exception as e:
            logging.error(f"Error connecting to Elasticsearch: {e}")
            raise

    def _create_index_if_not_exists(self) -> None:

        if self._client.indices.exists(index=self.index_name):
            logging.info(f"Index {self.index_name} already exists. Skipping creation.")

        else:
            if self.dims_length is None:
                raise ValueError(
                    "Cannot create index without specifying dims_length. "
                    "When the index doesn't already exist."
                )
            
            if self.distance_strategy not in ["cosine", "dot_product", "l2_norm"]:
                raise ValueError(f"Similarity {self.distance_strategy} not supported.")
            
            index_mappings = {
                "properties":{
                    self.text_field: { "type" : "text" },
                    self.vector_field: {
                        "type": "dense_vector",
                        "dims": self.dims_length,
                        "index": True,
                        "similarity": self.distance_strategy,
                    },
                    "metadata": {
                        "properties": {
                            "creation_date": {"type": "keyword"},
                            "file_name": {"type": "keyword"},
                            "file_type": {"type": "keyword"},
                            "page": {"type": "keyword"},
                        }
                    }
                }
            }

            print(f"Creating index {self.index_name}")

            self._client.indices.create(index=self.index_name, mappings=index_mappings)

    def add_documents(self, documents: List[Document], create_index_if_not_exists: bool = True) -> None:
        if create_index_if_not_exists:
            self._create_index_if_not_exists()

        vector_store_data = []
        for doc in documents:
            _id = doc.doc_id if doc.doc_id else str(uuid.uuid4())
            _metadata = doc.get_metadata()
            vector_store_data.append({
                "_index": self.index_name,
                "_id": _id,
                self.text_field: doc.get_text(),
                self.vector_field: self._embed.get_text_embedding(doc.get_text()),
                "metadata": _metadata,
                "metadata.creation_date": _metadata["creation_date"] if _metadata["creation_date"] else None,
                "metadata.file_name": _metadata["file_name"] if _metadata["file_name"] else None,
                "metadata.file_type": _metadata["file_type"] if _metadata["file_type"] else None,
                "metadata.page": _metadata["page"] if _metadata["page"] else None,
            })

        bulk(self._client, vector_store_data, chunk_size=self.batch_size, refresh=True)
        print(f"Added {len(vector_store_data)} documents to `{self.index_name}`")

    def similarity_search(self, query: str, top_k: int = 4) -> List[VectorStoreQueryResult]:
        """Query index for top k most similar documents."""

        query_embedding = self._embed.get_text_embedding(query)
        es_query = {}

        #  TO-DO: Add elasticsearch `filter` option
        es_query["knn"] = {
            # "filter": filter,
            "field": self.vector_field,
            "query_vector": query_embedding,
            "k": top_k,
            "num_candidates": top_k * 10,
            }

        response = self._client.search(index=self.index_name, 
                                       **es_query, 
                                       size=top_k, 
                                       _source={"excludes": [self.vector_field]})

        hits = response["hits"]["hits"]

        docs_and_scores = [VectorStoreQueryResult( 
                    document=Document(
                    doc_id=hit["_id"],
                    text=hit["_source"]["text"],
                    metadata=hit["_source"]["metadata"],
                ), 
                confidence=hit["_score"])
            for hit in hits
        ]

        return docs_and_scores

    def delete(self, ids: Optional[List[str]] = None) -> None:

        if ids is None:
            raise ValueError("No ids provided to delete.")

        for id in ids:
            self._client.delete(index=self.index_name, id=id)        