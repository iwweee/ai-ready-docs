---
ai-context:
  topic: "AI-Ready Documentation (AIRD) Specification v1.0"
  prerequisites: ['Environment Installation', 'System Architecture']
  critical-warning: ""
---

# AI-Ready Documentation (AIRD) Specification v1.0

AIRD is a standard for making technical documentation "readable" and "actionable" for Large Language Models (LLMs). While humans read docs for understanding, LLMs read docs for context, constraints, and execution paths.

## The Three Layers of AIRD

### L1: Discovery Layer (The Map)
**Goal**: Allow an LLM to quickly map the documentation landscape without crawling every file.
- **Requirement**: A `llms.txt` file in the root directory.
- **Format**: A Markdown file listing core documentation, key entry points, and a brief overview of the project.
- **Verification**: Linter checks for existence of `llms.txt`.

### L2: Structural Layer (The Skeleton)
**Goal**: Ensure a logical, hierarchical flow that prevents the LLM from losing context.
- **Requirement**: Strict heading hierarchy.
- **Constraint**: No heading jumps (e.g., H1 $\rightarrow$ H3). Every heading must follow a logical sequence (H1 $\rightarrow$ H2 $\rightarrow$ H3).
- **Verification**: Linter flags "Heading jumps" as warnings.

### L3: Context Layer (The Metadata)
**Goal**: Provide a "fast-track" for the LLM to understand the purpose, prerequisites, and dangers of a specific file.
- **Requirement**: An `ai-context` YAML block at the top of every `.md` file (within the first 500 characters).
- **Fields**:
    - `topic`: A short string describing the file's purpose.
    - `prerequisites`: A list of concepts or other docs the LLM should "know" before processing this file.
    - `critical-warning`: High-priority alerts (e.g., "Do not run this script in production").
- **Verification**: Linter checks for the `ai-context:` marker.

## Compliance Levels

| Level | Requirement | Badge Status |
| :--- | :--- | :--- |
| **FULL** | L1, L2, and L3 all PASS/FIXED | `AI-Ready-FULL` (Green) |
| **BASIC** | L1 and L3 PASS/FIXED | `AI-Ready-BASIC` (Yellow) |
| **IN-PROGRESS** | Any layer failing or L2 warning | `AI-Ready-IN-PROGRESS` (Orange) |

## Evolution
This specification evolves as LLM context windows and retrieval capabilities improve. The Linter is the primary enforcement mechanism.
