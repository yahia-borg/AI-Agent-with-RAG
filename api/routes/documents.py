from fastapi import APIRouter, UploadFile, Depends, HTTPException
from services.document_processing.loader import DocumentLoader
from services.document_processing.splitter import DocumentSplitter
from services.retrivals.qdrant_adapter import QdrantVectorDB
from core.domain.entities import DocumentChunk
from api.middleware.auth import AuthMiddleware

router = APIRouter(dependencies=[Depends(AuthMiddleware())])

@router.post("/upload")
async def upload_document(file: UploadFile):
    """Process and store documents in Qdrant"""
    try:
        # Load document
        loader = DocumentLoader()
        chunks = loader.load(file.file.read())
        
        # Split document
        splitter = DocumentSplitter()
        processed_chunks = splitter.split(chunks)
        
        # Store in Qdrant
        vector_db = QdrantVectorDB()
        vector_db.upsert(processed_chunks)
        
        return {"message": f"Processed {len(processed_chunks)} chunks"}
    
    except Exception as e:
        raise HTTPException(500, detail=str(e))