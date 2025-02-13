from typing import AsyncGenerator
from core.domain.exceptions import LLMException
from langchain_community.llms import Ollama
from core.interface.llm_client import ILLMClient
from core.config import settings

class LLMClient(ILLMClient):
    def __init__(self):
        self.client = Ollama(
            model=settings.llm_model,
            base_url=f"http://{settings.ollama_host}:{settings.ollama_port}"
        )

    async def generate(self, prompt: str) -> str:
        try:
            return await self.client.ainvoke(prompt)
        except Exception as e:
            raise LLMException(f"Generation failed: {str(e)}")

    async def stream(self, prompt: str) -> AsyncGenerator[str, None]:
        try:
            async for chunk in self.client.astream(prompt):
                yield chunk
        except Exception as e:
            raise LLMException(f"Streaming failed: {str(e)}")