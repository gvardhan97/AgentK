# Architecture

## Service boundaries
Next.js handles chat, uploads, citations, and execution status. Spring Boot owns application APIs and future workspace/session metadata. Python owns AI orchestration, ingestion, embeddings, retrieval, and model calls. MCP servers expose isolated typed tools.

## RAG
Document extraction -> text normalization -> overlapping chunks -> embeddings -> vector store. At query time, embed the question, retrieve top-k chunks, inject them into the prompt, and generate an answer constrained to those sources.

## Agent loop
Observe request -> select retrieval or tool action -> validate input -> execute with timeout -> observe result -> continue or respond. Set a maximum step count. Require approval for consequential side effects.

## Reliability
Validate tool inputs, bound timeouts/retries, avoid retrying non-idempotent actions blindly, return typed errors, and redact secrets from logs. Treat documents and tool output as untrusted data.
