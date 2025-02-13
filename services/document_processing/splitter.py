from core.domain.entities import DocumentChunk
from core.domain.exceptions import DocumentException
from typing import List

class DocumentSplitter:
    def split(self, chunks: List[DocumentChunk]) -> List[DocumentChunk]:
        """Split documents into chunks with overlap"""
        try:
            overlap = 50  # Define overlap size
            chunk_size = 100  # Define chunk size
            new_chunks = []
            for chunk in chunks:
                text = chunk.text
                start = 0
                while start < len(text):
                    end = min(start + chunk_size, len(text))
                    new_chunk_text = text[start:end]
                    new_chunks.append(DocumentChunk(text=new_chunk_text))
                    start += chunk_size - overlap
            chunks = new_chunks
            return chunks  # Simplified for example
        except Exception as e:
            raise DocumentException(f"Splitting failed: {str(e)}")