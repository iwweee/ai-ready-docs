---
ai-context:
  topic: "📄 AIRD Specification v1.1"
  prerequisites: ['Environment Installation', 'API Key Management', 'Authentication Setup', 'API Fundamentals']
  critical-warning: "Spec v1.1 introduces quantitative scoring and semantic dependency validation."
---

# 📄 AIRD Specification v1.1

## 1. Core Philosophy
**"Documentation is an API for LLMs."**
AIRD defines a standardized way to structure information so that Large Language Models (LLMs) can consume it with minimum token waste and maximum accuracy.

## 2. The Protocol Layers

### 🟢 L1: Discovery (The Map)
**Goal**: Enable AI to map the entire documentation in a single request.
- **Requirement**: A root-level `llms.txt` file.
- **Standard**: Must include: Project Overview $\rightarrow$ Core Index $\rightarrow$ Quickstart Links.

### 🔵 L2: Structure (The Skeleton)
**Goal**: Ensure seamless semantic chunking.
- **Requirements**:
    - **Strict Heading Hierarchy**: No skipping levels (e.g., H1 $\rightarrow$ H3).
    - **Deterministic Naming**: Consistent file naming conventions.

### 🟡 L3: Context (The Compass)
**Goal**: Eliminate "hidden assumptions" and provide instant grounding.
- **Required Component**: Every standalone page MUST begin with an **AI-Context Block**:
    ```yaml
    ---
    ai-context:
      topic: "Topic Name"
      prerequisites: ["file-path-1.md", "file-path-2.md"]
      critical-warning: "Critical constraint for AI"
    ---
    ```
- **Semantic Validation**: All `prerequisites` must resolve to existing files in the repository.

### 🔴 L4: Evolution (The Loop)
**Goal**: Create a feedback loop between AI and human authors.
- **Mechanism**: The `.ai-feedback.md` log.
- **Standard**: Implement the `Capture $\rightarrow$ Analyze $\rightarrow$ Refine $\rightarrow$ Verify` workflow to evolve L1-L3 layers based on AI failure points.

## 3. AI-Ready Scoring System (Quantitative Metric)

Compliance is measured on a 0-100 scale based on the following weights:

| Layer | Weight | Criteria |
| :--- | :--- | :--- |
| **L1** | 30% | Existence and completeness of `llms.txt`. |
| **L2** | 20% | Heading hierarchy consistency and structure. |
| **L3** | 40% | Presence of context blocks and resolution of prerequisites. |
| **L4** | 10% | Existence and activity of `.ai-feedback.md`. |

**Rankings**:
- **Elite (90-100)**: Fully AI-Ready.
- **High (70-89)**: AI-Compatible.
- **Medium (50-69)**: Partially AI-Ready.
- **Low (<50)**: Human-Centric.

## 4. Compliance Checklist
- [ ] `llms.txt` is present and maps core modules.
- [ ] All `.md` files start with a valid `ai-context` block.
- [ ] All `prerequisites` in context blocks are valid file paths.
- [ ] No heading level jumps in documentation.
- [ ] `.ai-feedback.md` is established for evolutionary tracking.
