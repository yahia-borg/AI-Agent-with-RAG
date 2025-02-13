# AI-Agent-with-RAG

Tech-stack:
- Fastapi
- ollama
- Qdrant
- langchain

## Setup Instructions

Follow these steps to set up the project:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/AI-Agent-with-RAG.git
    cd AI-Agent-with-RAG
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a `.env` file in the root directory and add the necessary environment variables. Refer to `.env.example` for the required variables.

5. **Run the application:**
    ```bash
    python main.py
    ```

6. **Run tests:**
    ```bash
    pytest
    ```