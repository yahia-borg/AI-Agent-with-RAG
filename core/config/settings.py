from pydantic import BaseSettings

class Settings(BaseSettings):
    qdrant_host: str = "localhost"
    qdrant_port: int = 6333
    ollama_host: str = "localhost"
    ollama_port: int = 11434
    embedding_model: str = "nomic-embed-text"
    llm_model: str = "mistral:7b-instruct"
    chunk_size: int = 1000
    chunk_overlap: int = 200

    class Config:
        env_file = ".env"

settings = Settings()