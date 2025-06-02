# PsychdAI

An AI coaching app that builds and uses a dynamic knowledge graph per user.

## Tech Stack
- FastAPI (backend)
- PostgreSQL (auth DB)
- Neo4j (knowledge graph)
- React (frontend)
- Local LLM (via FastAPI API)

## How to Run (Locally)

1. Clone repo
2. `cd backend && pip install -r requirements.txt`
3. `cd frontend && npm install && npm start`
4. Start Neo4j (see neo4j/README.md)

## Project Goals
- Dynamic user memory via Neo4j
- LLM grounded in structured personal knowledge
