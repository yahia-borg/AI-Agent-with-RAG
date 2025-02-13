from abc import ABC, abstractmethod
from typing import List
from core.domain.entities import DocumentChunk, QueryRequest

class IVectorDatabase(ABC):
    @abstractmethod
    def create_collection(self, name: str) -> bool:
        pass
    
    @abstractmethod
    def upsert_chunks(self, chunks: List[DocumentChunk]) -> int:
        pass
    
    @abstractmethod
    def search(self, request: QueryRequest) -> List[DocumentChunk]:
        pass