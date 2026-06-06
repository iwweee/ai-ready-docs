---
ai-context:
  topic: "📄 AIRD Specification v1.0"
  prerequisites: ['Environment Installation', 'API Key Management', 'Authentication Setup', 'API Fundamentals']
  critical-warning: ""
---

# 📄 AIRD Specification v1.0

## 1. Core Philosophy
**"Documentation is an API for LLMs."**
AIRD (AI-Ready Documentation) defines a standardized way to structure information so that Large Language Models (LLMs) can consume it with minimum token waste and maximum accuracy.

## 2. The Protocol Layers

### 🟢 L1: Discovery (The Map)
**Goal**: Enable AI to map the entire documentation in a single request.
- **Requirement**: A root-level `llms.txt` file.
- **Standard**:
    - Must include: Project Overview $\rightarrow$ Core Index $\rightarrow$ Quickstart Links.
    - Format: Simple Markdown lists only.

### 🔵 L2: Structure (The Skeleton)
**Goal**: Ensure seamless semantic chunking.
- **Requirements**:
    - **Strict Heading Hierarchy**: No skipping levels (e.g., H1 $\rightarrow$ H3).
    - **Semantic Anchors**: First occurrence of critical terms must link to a `Glossary.md`.
    - **Noise Isolation**: Main content must be wrapped in `<main>` or `id="ai-content"` for HTML renders.

### 🟡 L3: Context (The Compass)
**Goal**: Eliminate "hidden assumptions" and provide instant grounding.
- **Required Component**: Every standalone page MUST begin with an **AI-Context Block** (YAML Frontmatter):
    ```yaml
    ---
    ai-context:
      topic: "Topic Name"
      prerequisites: ["Req 1", "Req 2"]
      depends-on: ["/path/to/dependency.md"]
      critical-warning: "Key warning for AI"
    ---
    ```
- **Absolute Referencing**: Use `[Term](link)` instead of "see above" or "here".

### 🔴 L4: Evolution (The Loop)
**Goal**: Create a feedback loop between AI and human authors.
- **Mechanism**: The `.ai-feedback` marker.
- **Standard**: When an AI detects a contradiction, it logs it in a structured format to trigger human review.

## 3. Compliance Checklist
A repo is `AIRD-Compliant` if:
- [ ] `curl /llms.txt` returns a valid site map.
- [ ] All pages contain a valid `AI-Context Block`.
- [ ] Heading hierarchy is logically consistent.
- [ ] Non-content noise (nav/footer) is isolated in HTML.
