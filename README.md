# AI Framework

> Building a lightweight AI framework for specialized AI assistants.

A lightweight AI framework written in Python to understand, design and implement the core building blocks behind modern LLM-powered applications.

Instead of relying on high-level frameworks, this project focuses on building them from scratch to gain a deeper understanding of their architecture and design.

                           AI Framework
                                  │
                 ┌────────────────┼────────────────┐
                 ▼                ▼                ▼
          Engineering         Engineering       Future
            Mentor             Vacancy         Assistants
                                                   │
                                      ┌────────────┴────────────┐
                                      ▼                         ▼
                                    EVE              Industrial Automation

---

## 🎯 Goals

- Build specialized AI assistants
- Design a clean and extensible AI architecture
- Build reusable abstractions
- Support multiple LLM providers
- Understand how modern AI frameworks work internally

---

## 🚀 Current Features

### Core framework

- ✅ LLM abstraction
- ✅ Ollama integration
- ✅ Agent abstraction
- ✅ Conversation memory
- ✅ Tool execution
- ✅ Tool registry
- ✅ Context builder
- ✅ Prompt builder
- ✅ File discovery and loading
- ✅ CLI interface

### Agents

- ✅ Engineering Mentor
- ✅ Engineering Vacancy

### Tools

- ✅ File tool
- ✅ Calculator tool

---

## 🤖 Agents

### 👨‍🏫 Engineering Mentor

An engineering assistant focused on software development and architecture.

It can:

- analyze project files;
- perform architectural code review;
- inspect related files when necessary;
- use tools to work with the project;
- maintain conversation context through memory.

Example:

```text
> @ai/agents/base.py

Проведи архитектурный code review.

Если для проверки своих выводов тебе нужны связанные классы
или зависимости, самостоятельно изучи соответствующие файлы проекта.

Не делай предположений о коде, который ты не проверил.
Отделяй реальные проблемы от возможных улучшений.
```

The `@file` syntax allows a file from the project to be used as context.

---

### 💼 Engineering Vacancy

An assistant for analyzing software engineering vacancies.

It can:

- analyze vacancy descriptions;
- identify mandatory and desirable requirements;
- identify technologies, tools and architectural approaches;
- compare requirements with the developer's known experience;
- identify knowledge and experience gaps;
- prioritize gaps;
- suggest a preparation plan;
- generate a tailored cover letter when enough information is available.

The assistant accepts the vacancy description directly as user input.

---

## 🧠 Architecture

The core architecture is built around several independent components:

```text
                         ┌─────────────┐
                         │     CLI     │
                         └──────┬──────┘
                                │
                                ▼
                         ┌─────────────┐
                         │    Agent    │
                         └──────┬──────┘
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
        ┌──────────┐      ┌──────────┐      ┌──────────┐
        │   LLM    │      │  Memory  │      │  Tools   │
        └──────────┘      └──────────┘      └──────────┘
              │                                  │
              ▼                                  ▼
        ┌──────────┐                      ┌──────────────┐
        │  Ollama  │                      │ Tool Registry│
        └──────────┘                      └──────────────┘

                         Agent
                           │
                           ▼
                    Context Builder
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           Finder        Loader    Prompt Builder
```

Architecture diagrams are located in `docs/diagrams` and evolve together with the project.

---

## 🧩 Core Components

### Agent

The central abstraction responsible for coordinating:

- LLM
- Memory
- System Prompt
- Context
- Tools

The agent implements the basic agent loop:

```text
User request
     │
     ▼
Context Builder
     │
     ▼
Memory
     │
     ▼
LLM
     │
     ├─── text ──────────────► Response
     │
     └─── tool call
              │
              ▼
           Tool
              │
              ▼
         Tool result
              │
              └──────────────► LLM
```

### Memory

Stores conversation messages and tool calls.

The current implementation provides bounded in-memory conversation history.

### Tools

Tools extend agent capabilities beyond text generation.

The current MVP includes:

- `FileTool`
- `CalculatorTool`

Tools are registered through `ToolRegistry`.

### Context Builder

Responsible for preparing additional context before sending a request to the agent.

For example, the `@file` syntax allows a project file to be loaded and transformed into an analysis prompt.

### LLM

The LLM is treated as an interchangeable component.

The current implementation uses Ollama with Qwen3.

---

## 🛠 Tech Stack

- Python 3.12+
- uv
- Ollama
- Qwen3
- httpx
- Pydantic
- prompt-toolkit

---

## 🚀 Running

Make sure Ollama is running and the required model is available.

Then run:

```bash
uv run python main.py
```

The application starts an interactive CLI.

Use:

```text
exit
```

or:

```text
выход
```

to quit.

---

## 🗺️ Roadmap

### Phase 1 — Foundation

- [x] Project initialization
- [x] LLM abstraction
- [x] Ollama client
- [x] Agent

### Phase 2 — Engineering Mentor MVP

- [x] CLI chat interface
- [x] Agent configuration
- [x] Prompt Builder
- [x] System prompt
- [x] Conversation memory
- [x] Tool execution
- [x] File discovery and loading
- [x] Engineering Mentor MVP

### Phase 3 — Engineering Vacancy

- [x] Vacancy agent
- [x] Vacancy analysis prompt
- [x] Requirement / gap analysis
- [x] Cover letter support

### Phase 4 — Future Framework Capabilities

- [ ] Structured outputs
- [ ] Planner
- [ ] RAG
- [ ] Streaming
- [ ] Async execution
- [ ] Multi-agent workflows
- [ ] Observability
- [ ] Additional LLM providers

### Phase 5 — Specialized Assistants

- [ ] EVE Assistant
- [ ] Industrial Automation Assistant

---

## 🔮 Future Improvements

The following ideas are intentionally outside the current MVP and are kept as future work:

- automated tests;
- more robust error handling;
- configurable agent loop limits;
- richer memory implementations;
- persistent memory;
- improved context management;
- better tool error handling;
- configurable LLM parameters;
- support for additional LLM providers;
- asynchronous tool execution;
- streaming responses;
- structured outputs;
- multi-agent workflows;
- observability and tracing;
- more sophisticated vacancy / candidate profile handling.

The goal is to keep the MVP small while preserving a clear path for further development.

---

## 🧱 Design Principles

- Behavior belongs to agents, not models.
- Models are replaceable.
- Memory is independent from the LLM.
- Tools are reusable.
- Dependencies are explicitly provided to agents.
- Everything should work offline whenever possible.

---

## 🎯 Vision

Agents define behavior.

Language models are interchangeable engines responsible only for text generation.

An agent combines:

- LLM
- Memory
- System Prompt
- Tools
- Context
- Configuration

This architecture allows the same agent abstraction to work with different language models without coupling agent behavior to a specific model implementation.

---

## 📖 Philosophy

This project is built as an educational engineering project.

The objective is not to create yet another AI framework, but to understand how modern LLM-powered systems work by implementing them from first principles and applying them to real-world assistants.
