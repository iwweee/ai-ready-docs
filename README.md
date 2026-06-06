---
ai-context:
  topic: "🚀 ai-ready-docs"
  prerequisites: ['API Fundamentals', 'API Key Management', 'System Architecture']
  critical-warning: ""
---

# 🚀 ai-ready-docs

**Defining the standard for AI-Native Documentation.**

`ai-ready-docs` is not just a guide; it is a specification (**AIRD Spec v1.0**) designed to transform documentation from "human-readable text" into "AI-consumable APIs".

## 🎯 Goal
Reduce LLM hallucinations, minimize token waste, and accelerate agentic workflows by implementing a standardized interface between documents and AI.

## 🛠 The AIRD Specification
We define a 4-layer protocol to make any documentation truly AI-Ready:
- **L1 Discovery** $\rightarrow$ `llms.txt` for instant mapping.
- **L2 Structure** $\rightarrow$ Strict hierarchy for perfect chunking.
- **L3 Context** $\rightarrow$ `AI-Context Blocks` to eliminate assumptions.
- **L4 Evolution** $\rightarrow$ `.ai-feedback` for continuous improvement.

## 🛠 Validation
Verify if your documentation is AIRD-compliant using our lightweight linter:

```bash
python aird_lint.py ./your-docs-folder

👉 [Read the full SPEC.md](./SPEC.md)
