from pydantic import BaseModel
from typing import List, Dict

class DocumentChunk(BaseModel):
    content: str
    metadata: Dict
    vector: List[float]

class QueryRequest(BaseModel):
    query: str
    collection: str = "default"

class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: List[str]