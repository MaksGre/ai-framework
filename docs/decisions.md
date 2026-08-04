# Design Decisions

## 2026-08-04

### Memory belongs to the Agent

Decision:
Conversation history is stored in a dedicated Memory component.

Reason:
The same agent should be able to switch between different LLM providers without losing conversation history.

Status:
Accepted

### LLMClient abstraction

Decision:
All providers implement the same interface.

Reason:
Agents should not depend on a concrete LLM provider.
