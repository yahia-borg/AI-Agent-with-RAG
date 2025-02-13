from fastapi.security import APIKeyHeader, HTTPBearer
from fastapi import HTTPException, Request, status
from typing import Optional
from core.config import settings

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
http_bearer = HTTPBearer(auto_error=False)

class AuthMiddleware:
    def __init__(self):
        self.valid_keys = self._load_api_keys()

    def _load_api_keys(self) -> set:
        """Load valid API keys from key.txt"""
        try:
            with open("api_keys.txt", "r") as f:
                return {line.strip() for line in f if line.strip()}
        except FileNotFoundError:
            raise RuntimeError("API key file not found")

    async def __call__(self, request: Request):
        """Validate API key for each request"""
        api_key = await api_key_header(request)
        if not api_key or api_key not in self.valid_keys:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid or missing API Key"
            )
        request.state.api_key = api_key