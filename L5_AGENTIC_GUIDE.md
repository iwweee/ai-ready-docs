# AIRD v1.2: The Actionable Layer (L5) & Evolutionary Loop

This document extends the AIRD v1.1 specification to support **Agentic Workflows** and **Self-Evolving Documentation**.

## 1. The L5 Execution Protocol Template

Whenever a document describes a process that an AI Agent should execute, add an `## Execution Protocol` section.

### Example: Git Branch Cleanup Protocol
```markdown
## Execution Protocol
- **Tools**: `git`, `shell`
- **Logic Chain**:
  1. `git branch --merged main` $\rightarrow$ Identify merged branches.
  2. Filter out `main`, `develop`, and protected branches using the `protected-branches.json` list.
  3. For each identified branch: `git branch -d <branch-name>`.
- **Success Criteria**: 
  - All merged feature branches are deleted.
  - No protected branches are touched.
  - Final count of deleted branches is reported.
- **Fallback**: 
  - If `git branch -d` fails (non-merged), attempt `git branch -D` ONLY after confirming with the user.
```

## 2. The Evolutionary Loop (L4 $\rightarrow$ PR)

In AIRD v1.2, `.ai-feedback.md` is the trigger for a **Documentation Patch**.

### The Automated Flow:
1. **Detection**: Agent detects a documentation gap while executing an L5 protocol.
2. **Logging**: Agent appends a structured entry to `.ai-feedback.md`:
   ```markdown
   - [ ] **Gap ID**: GAP-2026-001
       - **Target**: `docs/api.md`
       - **Issue**: Missing timeout value for `/v1/upload` endpoint.
       - **Proposed Fix**: Add "Timeout: 30s" to the `Request` section.
   ```
3. **Action**: The Agent (or a dedicated maintenance Agent) creates a new Git branch `ai-patch/GAP-2026-001`, applies the fix, and opens a PR.
4. **Human Review**: Human merges the PR $\rightarrow$ `.ai-feedback.md` item is marked as `Resolved`.

## 3. Ontology Mapping (The Semantic Layer)

To prevent hallucinations in complex domains, include an `ontology.json` in the root.

### Example `ontology.json`
```json
{
  "domain": "ProjectX-Cloud",
  "mappings": {
    "EdgeNode": "The physical compute unit located at the customer site, running k3s.",
    "ControlPlane": "The central management API hosted in AWS us-east-1.",
    "Soothe": "The proprietary internal synchronization protocol used for state delta updates."
  }
}
```
*Agent Instruction: Always consult `ontology.json` when encountering undefined technical terms in L3/L4 docs.*
