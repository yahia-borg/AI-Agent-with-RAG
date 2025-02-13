from qdrant_client import QdrantClient
from core.domain.exceptions import VectorDBException
from core.interface.victor_db import IVectorDatabase
from core.domain.entities import DocumentChunk
from core.config import settings
from typing import List

class QdrantVectorDB(IVectorDatabase):
    def __init__(self):
        self.client = QdrantClient(
            host=settings.qdrant_host,
            port=settings.qdrant_port
        )

    def upsert(self, chunks: List[DocumentChunk]) -> None:
        try:
            # Convert DocumentChunk objects to the format expected by Qdrant
            points = [
                {
                    "id": chunk.id,
                    "vector": chunk.vector,
                    "payload": chunk.payload
                }
                for chunk in chunks
            ]
            # Upsert points into Qdrant
            self.client.upsert(
                collection_name=settings.qdrant_collection_name,
                points=points
            )
            pass
        except Exception as e:
            raise VectorDBException(f"Upsert failed: {str(e)}")

    def search(self, query_vector: List[float], k: int = 5) -> List[DocumentChunk]:
        try:
            # Perform the search in Qdrant
            search_result = self.client.search(
                collection_name=settings.qdrant_collection_name,
                query_vector=query_vector,
                limit=k
            )
            # Convert search results to DocumentChunk objects
            chunks = [
                DocumentChunk(
                    id=result["id"],
                    vector=result["vector"],
                    payload=result["payload"]
                )
                for result in search_result
            ]
            return chunks
        except Exception as e:
            raise VectorDBException(f"Search failed: {str(e)}")