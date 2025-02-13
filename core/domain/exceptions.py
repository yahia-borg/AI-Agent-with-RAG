from fastapi import HTTPException
from typing import Any

class ServiceException(HTTPException):
    def __init__(self, detail: Any, status_code: int):
        super().__init__(status_code=status_code, detail=detail)

class AuthException(ServiceException):
    def __init__(self, detail: str = "Authentication failed"):
        super().__init__(detail=detail, status_code=401)

class VectorDBException(ServiceException):
    def __init__(self, operation: str, error: str):
        super().__init__(
            detail=f"VectorDB {operation} failed: {error}",
            status_code=500
        )

class LLMException(ServiceException):
    def __init__(self, error: str):
        super().__init__(
            detail=f"LLM processing error: {error}",
            status_code=503
        )

class DocumentException(ServiceException):
    def __init__(self, error: str):
        super().__init__(
            detail=f"Document processing error: {error}",
            status_code=400
        )
class EmbeddingException(ServiceException):
    def __init__(self, error: str):
        super().__init__(
            detail=f"Embedding generation error: {error}",
            status_code=500
       )