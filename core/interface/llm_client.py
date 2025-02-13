from abc import ABC, abstractmethod
from typing import AsyncGenerator

class ILanguageClient(ABC):
    @abstractmethod
    async def generate(self, prompt: str, **kwargs) -> str:
        pass
    
    @abstractmethod
    async def stream(self, prompt: str, **kwargs) -> AsyncGenerator[str, None]:
        pass

class IChatClient(ILanguageClient):
    @abstractmethod
    async def chat(self, messages: list, **kwargs) -> str:
        pass