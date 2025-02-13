from typing import List
from langchain_community.embeddings import OllamaEmbeddings
from core.config import settings
from core.domain.exceptions import EmbeddingException

class EmbeddingGenerator:
    def __init__(self):
        self.client = OllamaEmbeddings(
            model=settings.embedding_model,
            base_url=f"http://{settings.ollama_host}:{settings.ollama_port}"
        )

    def generate(self, text: str) -> List[float]:
        try:
            return self.client.embed_query(text)
        except Exception as e:
            raise EmbeddingException(f"Embedding failed: {str(e)}")