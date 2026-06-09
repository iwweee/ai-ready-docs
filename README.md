# 🚀 ai-ready-docs: The Standard for AI-Native Documentation

[![AIRD Compliant](https://img.shields.io/badge/AI--Ready-Docs-v1.1-blue)](https://github.com/iwweee/ai-ready-docs)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://spdx.org/licenses/mit.html)

**Stop writing documentation for humans. Start building APIs for LLMs.**

`ai-ready-docs` (AIRD) is not just a guide; it is a rigorous specification designed to transform documentation from "human-readable text" into "**AI-consumable interfaces**."

In the era of Agentic Workflows and RAG, the bottleneck is no longer the model's reasoning power, but the **quality and structure of the context** provided. AIRD eliminates ambiguity, minimizes token waste, and virtually erases LLM hallucinations by implementing a standardized interface between documents and AI.

---

## 🛑 The Problem: Human-Centric vs. AI-Native

Most documentation is written for humans. When fed into an LLM, this leads to:
- **Context Fragmentation**: The AI misses critical dependencies hidden in other files.
- **Token Bleed**: High noise-to-signal ratio wastes expensive context windows.
- **Hallucinations**: AI "guesses" the intent when structural cues are missing.

### 📊 The AIRD Advantage

| Dimension | Traditional Docs (Human-Centric) | AIRD Standard (AI-Native) |
| :--- | :--- | :--- |
| **Discovery** | Manual search / Random crawling | $\text{L1 Discovery} \rightarrow$ Instant mapping via `llms.txt` |
| **Parsing** | Heuristic chunking (Unpredictable) | $\text{L2 Structure} \rightarrow$ Deterministic hierarchy |
| **Cognition** | Reliance on LLM's general knowledge | $\text{L3 Context} \rightarrow$ Explicit `ai-context` blocks |
| **Maintenance** | Manual updates $\rightarrow$ Doc drift | $\text{L4 Evolution} \rightarrow$ Closed-loop `.ai-feedback` |

---

## 🏗️ The 4-Layer Protocol (AIRD Spec v1.1)

We define a layered architecture to ensure any documentation is truly "AI-Ready":

### 📡 L1: Discovery (The Map)
**Goal**: Immediate orientation.
- Implementation: `llms.txt`
- Result: The AI knows exactly where to find what, without scanning the entire repository.

### 🏗️ L2: Structure (The Skeleton)
**Goal**: Perfect chunking and retrieval.
- Implementation: Strict directory hierarchy and standardized file naming.
- Result: Zero-loss retrieval during RAG processes.

### 🧠 L3: Context (The Brain)
**Goal**: Eliminate assumptions.
- Implementation: `ai-context` blocks (Topic, Prerequisites, Critical-Warnings).
- Result: The AI understands *why* a piece of information matters and *what* must be true before proceeding.

### 🔄 L4: Evolution (The Loop)
**Goal**: Continuous self-improvement.
- Implementation: `.ai-feedback.md` mechanism.
- Result: Documentation that evolves based on actual AI failure points.

---

## 🛠️ Quick Start

### 1. Verify Compliance
Check if your current documentation meets the AIRD standard using our lightweight linter:
```bash
python aird_lint.py ./your-docs-folder
```

### 2. Implement the Standard
Follow the detailed specification to upgrade your docs:
👉 **[Read the Full SPEC.md](./SPEC.md)**

---

## 🌟 Adoption & Ecosystem

We are building a world where every project is `AI-Ready`.

- **Current Status**: v1.1 (Evolutionary Stage)
- **Goal**: To become the default documentation layer for autonomous AI agents.

If you've implemented AIRD in your project, please let us know or open a PR to be added to our **AIRD-Compliant Projects** list!

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
