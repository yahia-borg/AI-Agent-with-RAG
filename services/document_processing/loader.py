from core.domain.entities import DocumentChunk
from core.domain.exceptions import DocumentProcessingException
from pypdf import PdfReader
from typing import List

class DocumentLoader:
    def load(self, file_content: bytes) -> List[DocumentChunk]:
        """Load and parse PDF documents"""
        try:
            reader = PdfReader(file_content)
            return [
                DocumentChunk(
                    content=page.extract_text(),
                    metadata={
                        "source": "uploaded_document",
                        "page": page_number+1
                    },
                    vector=[]
                )
                for page_number, page in enumerate(reader.pages)
            ]
        except Exception as e:
            raise DocumentProcessingException(f"PDF loading failed: {str(e)}")