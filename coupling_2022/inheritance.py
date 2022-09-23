from typing import Any

from elasticsearch import Elasticsearch
from requests_aws4auth import AWS4Auth


DEV_HOST: str = "localhost:8700"


def create_elastic_client(host: str = DEV_HOST) -> Elasticsearch:
    awsauth = AWS4Auth(service="elb")
    return Elasticsearch(
        hosts=[host],
        http_auth=awsauth,
        verify_certs=True,
    )


# NOTE: we could also use protocols here to make find_hits independent of the Elasticsearch
def find_hits(
    client: Elasticsearch,
    query: dict[str, Any],
    size: int,
    index: str,
    **kwargs: Any,
) -> list[dict[str, Any]]:
    response = client.search(
        query=query,
        size=size,
        index=index,
        **kwargs,
    )
    return response["hits"]["hits"]


# class Elastic(Elasticsearch):
#     def __init__(self, index_name: str, host: str) -> None:
#         awsauth = AWS4Auth(
#             service="elb",
#         )
#         super().__init__(
#             hosts=[host],
#             http_auth=awsauth,
#             verify_certs=True,
#         )
#         self.index_name = index_name

#     def find_hits(
#         self,
#         query: dict[str, Any],
#         size: int,
#         index: str,
#         **kwargs: Any,
#     ) -> list[dict[str, Any]]:
#         response = self.search(
#             query=query,
#             size=size,
#             index=index or self.index_name,
#             **kwargs,
#         )
#         return response["hits"]["hits"]


# class DevElastic(Elastic):
#     def __init__(self, index_name: str) -> None:
#         super().__init__(
#             host="localhost:8700",
#             index_name=index_name,
#         )
