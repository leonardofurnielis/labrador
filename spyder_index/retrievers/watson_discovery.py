import logging

from typing import List

from spyder_index.core.document import Document


class WatsonDiscoveryRetriever:
    """Provides functionality to interact with IBM Watson Discovery for querying documents.

    Args:
        hostname (str): Watson Discovery hostname.
        apikey (str): Watson Discovery apikey.
        project_id (str): Watson Discovery project ID.
        version (str, optional): Watson Discovery version. Defaults to ``2023-03-31``.
        disable_passages (bool, optional): Disable passage retrieval. Defaults to ``False``.
    """

    def __init__(self,
                 hostname: str,
                 apikey: str,
                 project_id: str,
                 version: str = '2023-03-31',
                 disable_passages: bool = False
                 ) -> None:
        try:
            from ibm_watson import DiscoveryV2
            from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

        except ImportError:
            raise ImportError("ibm-watson package not found, please install it with `pip install ibm-watson`")

        self.disable_passages = disable_passages
        self.project_id = project_id

        try:
            authenticator = IAMAuthenticator(apikey)
            self._client = DiscoveryV2(authenticator=authenticator,
                                       version=version)

            self._client.set_service_url(hostname)
        except Exception as e:
            logging.error(f"Error connecting to IBM Watson Discovery: {e}")
            raise

    def query(self, query: str, filter: str = None, top_k: int = 4) -> List:
        """Search your data in the Discovery API and return a list of documents.

        Args:
            query (str): Query text.
            filter (str, optional): Searches for documents that march the filter. Use Discovery Query Language syntax.
            top_k (int, optional): Number of top results to return. Defaults to ``4``.
        """
        from ibm_watson.discovery_v2 import QueryLargePassages

        results = self._client.query(
            project_id=self.project_id,
            natural_language_query=query,
            count=top_k,
            return_=["extracted_metadata.filename", "document_passages"],
            filter=filter,
            passages=QueryLargePassages(enabled=True, per_document=True, find_answers=False)
        ).get_result()

        return results
