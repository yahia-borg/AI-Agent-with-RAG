from fastapi import APIRouter, Depends, HTTPException
from services.llm.llm_client import LLMClient
from services.retrivals.embeddings import EmbeddingGenerator
from services.retrivals.qdrant_adapter import QdrantVectorDB
from core.domain.entities import QueryRequest, QueryResponse
from api.middleware.auth import AuthMiddleware

router = APIRouter(dependencies=[Depends(AuthMiddleware())])

@router.post("/query", response_model=QueryResponse)
async def handle_query(request: QueryRequest):
    """Handle RAG query pipeline"""
    try:
        # Generate query embedding
        embedder = EmbeddingGenerator()
        query_vector = embedder.generate(request.query)
        
        # Retrieve relevant chunks
        vector_db = QdrantVectorDB()
        results = vector_db.search(query_vector, k=5)
        
        # Generate final response
        llm = LLMClient()
        context = "\n".join([chunk.content for chunk in results])
        prompt = f"Context: {context}\n\nQuestion: {request.query}"
        
        answer = await llm.generate(prompt)
        
        return QueryResponse(
            question=request.query,
            answer=answer,
            sources=[chunk.metadata["source"] for chunk in results]
        )
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))