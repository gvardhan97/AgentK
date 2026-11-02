# AgentK — Agentic RAG + MCP Workspace

A full-stack learning project combining document RAG, MCP tool integration, and a bounded ReAct-style agent loop.

## Architecture
- `frontend/`: Next.js + TypeScript workspace
- `backend/`: Java 21 + Spring Boot API boundary
- `ai-service/`: Python FastAPI service for document ingestion, embeddings, retrieval, and generation
- `mcp-servers/weather/`: FastMCP weather tool server
- Chroma: local vector store

## RAG pipeline
Extract PDF/TXT -> normalize -> chunk with overlap -> embed -> store in Chroma -> embed query -> retrieve top-k -> inject context -> generate cited answer.

## Agent/MCP pipeline
The next milestone is to connect the agent to MCP tools: discover tools, validate arguments, invoke a tool, observe results, and continue until done or a step budget is reached. Display action names/status/duration in the UI, not private chain-of-thought.

## Run locally
1. Copy `.env.example` to `.env`; set `OPENAI_API_KEY`.
2. Run `docker compose up --build`.
3. Frontend: http://localhost:3000
4. AI health: http://localhost:8000/health
5. Spring health: http://localhost:8080/actuator/health

This is an initial development scaffold, not a production-ready deployment. Add authentication, persistent metadata, authorization, observability, tests, and approval gates before production use.
