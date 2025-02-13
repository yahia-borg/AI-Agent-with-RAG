#!/bin/bash

set -e

# Initialize directories
mkdir -p ./documents/{raw,processed}
mkdir -p ./data/{qdrant,redis}
chmod -R 755 ./documents ./data

# Initialize Qdrant
docker compose exec qdrant curl -X PUT "${QDRANT_URL}/collections/default" \
  -H "Content-Type: application/json" \
  -d '{"vectors": {"size": 768, "distance": "Cosine"}}'

# Pre-download models
docker compose exec ollama ollama pull ${LLM_MODEL}
docker compose exec ollama ollama pull ${EMBED_MODEL}

echo "System initialized successfully"