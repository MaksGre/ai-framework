# AI Framework

> Building a lightweight AI framework for specialized AI assistants.

A lightweight AI framework written in Python to understand, design and implement the core building blocks behind modern LLM-powered applications.

Instead of relying on high-level frameworks, this project focuses on building them from scratch to gain a deeper understanding of their architecture and design.

                           AI Framework
                                  │
        ┌───────────────┬─────────┼─────────┐
        ▼               ▼         ▼         ▼
 Engineering       Vacancy      EVE      Industrial
    Mentor         Assistant   Assistant  Automation

---

## 🎯 Goals

- Build specialized AI assistants
- Design a clean and extensible AI architecture
- Build reusable abstractions
- Support multiple LLM providers
- Understand how modern AI frameworks work internally

---

## 🚀 Current Features

- ✅ LLM abstraction
- ✅ Ollama integration
- ✅ Agent abstraction

---

## 🗺️ Roadmap

### Phase 1 — Foundation

- [x] Project initialization
- [x] LLM abstraction
- [x] Ollama client
- [x] Agent

### Phase 2 — Engineering Mentor

- [ ] CLI chat interface
- [ ] Agent configuration
- [ ] Prompt Builder
- [ ] System prompt
- [ ] Engineering Mentor MVP

### Phase 3 — Core Framework

- [ ] Tool execution
- [ ] Conversation memory
- [ ] Prompt templates
- [ ] Structured outputs
- [ ] Planner
- [ ] RAG

### Phase 4 — Specialized Assistants

- [ ] Vacancy Assistant
- [ ] EVE Assistant
- [ ] Industrial Automation Assistant

### Phase 5 — Production

- [ ] Multi-agent workflows
- [ ] Observability

---

## 🛠 Tech Stack

- Python 3.12
- uv
- Ollama
- Qwen3
- httpx
- Pydantic

---

## 🏗 Architecture

The architecture diagrams are located in the `docs/diagrams` directory and evolve together with the project.

---

## 🎯 Vision

Agents define behavior.

Language models are interchangeable engines responsible only for text generation.

An agent combines:

- LLM
- Memory
- System Prompt
- Tools
- Configuration

This architecture allows the same agent to switch between different language models without losing its memory, personality or capabilities.

## 🤖 Planned Assistants

### 👨‍🏫 Engineering Mentor

Personal software engineering mentor.

### 💼 Vacancy Assistant

Career and interview assistant.

### 🚀 EVE Online Assistant

Game knowledge and market analysis.

### 🏭 Industrial Automation Assistant

Industrial automation knowledge assistant.

## 🧱 Design Principles

- Behavior belongs to agents, not models.
- Models are replaceable.
- Memory is independent from the LLM.
- Tools are reusable.
- Everything should work offline whenever possible.

## 📖 Philosophy

This project is built as an educational engineering project.

The objective is not to create yet another AI framework, but to understand how modern LLM-powered systems work by implementing them from first principles and applying them to real-world assistants.
