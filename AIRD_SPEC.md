---
ai-context:
  topic: "AI-Ready Documentation (AIRD) Specification v1.2"
  prerequisites: ['Environment Installation', 'System Architecture']
  critical-warning: ""
---

# AI-Ready Documentation (AIRD) Specification v1.2

AIRD is a standard for making technical documentation "readable" and "actionable" for Large Language Models (LLMs). While humans read docs for understanding, LLMs read docs for context, constraints, and execution paths.

## The Five Layers of AIRD

### L1: Discovery Layer (The Map)
**Goal**: Allow an LLM to quickly map the documentation landscape without crawling every file.
- **Requirement**: A `llms.txt` file in the root directory.
- **Format**: A Markdown file listing core documentation, key entry points, and a brief overview of the project.
- **Verification**: Linter checks for existence of `llms.txt`.

### L2: Structural Layer (The Skeleton)
**Goal**: Ensure a logical, hierarchical flow that prevents the LLM from losing context.
- **Requirement**: Strict heading hierarchy.
- **Constraint**: No heading jumps (e.g., H1 $\rightarrow$ H3).
- **Verification**: Linter flags "Heading jumps" as warnings.

### L3: Context Layer (The Metadata)
**Goal**: Provide a "fast-track" for the LLM to understand the purpose and dangers of a specific file.
- **Requirement**: An `ai-context` YAML block at the top of every `.md` file.
- **Fields**: `topic`, `user_intent`, `prerequisites`, `critical-warning`.
- **Verification**: Linter checks for the `ai-context:` marker.

### L4: Evolution Layer (The Feedback Loop)
**Goal**: Transform documentation from a static asset into a living system based on AI interaction data.
- **Requirement**: A `.ai-feedback.md` file to capture AI-detected inconsistencies or gaps.
- **Mechanism**: AI agents record failures $\rightarrow$ Humans review $\rightarrow$ Docs are updated.
- **Verification**: Linter checks for the existence of the feedback mechanism.

### L5: Actionable Layer (The Execution Protocol) $\leftarrow$ NEW in v1.2
**Goal**: Move from "Information Retrieval" to "Autonomous Execution". Docs should define *how* to act.
- **Requirement**: An `## Execution Protocol` section in documents that describe processes, APIs, or workflows.
- **Components**:
    - **Tool Mapping**: Explicitly name the tools/APIs to be used (e.g., "Use `gh-api` for this step").
    - **Logic Chain**: A step-by-step sequence of operations (e.g., Step 1: Validate $\rightarrow$ Step 2: Execute $\rightarrow$ Step 3: Verify).
    - **Success Criteria**: Clear, machine-verifiable definitions of what a "successful" outcome looks like.
    - **Fallback Path**: What the Agent should do if the primary path fails (e.g., "If API returns 404, check `ontology.json` for alias").
- **Verification**: Linter checks for `## Execution Protocol` in identified workflow docs.

## Compliance Levels

| Level | Requirement | Badge Status |
| :--- | :--- | :--- |
| **FULL** | L1, L2, and L3 all PASS/FIXED | `AI-Ready-FULL` (Green) |
| **EVOLUTIONARY** | L1-L4 all PASS/FIXED | `AI-Ready-EVO` (Purple) |
| **AGENTIC** | L1-L5 all PASS/FIXED | `AI-Ready-AGENT` (Gold) $\leftarrow$ NEW |
| **IN-PROGRESS** | Any layer failing or L2 warning | `AI-Ready-IN-PROGRESS` (Orange) |

## Evolution
This specification evolves as LLM context windows and retrieval capabilities improve. The Linter is the primary enforcement mechanism.
