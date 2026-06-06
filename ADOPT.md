---
ai-context:
  topic: "AIRD Adoption Guide"
  prerequisites: ['AIRD_SPEC.md']
  critical-warning: ""
---

# 🚀 AIRD Adoption Guide

Welcome to the **AI-Ready Documentation (AIRD)** ecosystem. This guide will walk you through the process of transforming your la-human documentation into an AI-consumable interface.

## ⚡ Quick Start: The "3-Step AIRD-ify"

If you want to make your docs AI-ready in 10 minutes, follow these steps:

### Step 1: Run the Linter
Download `aird_lint_v4.py` and run it against your documentation folder.
```bash
python aird_lint_v4.py --suggest ./your-docs
```
The linter will tell you exactly where your L1, L2, and L3 layers are failing.

### Step 2: Create your L1 Map (`llms.txt`)
Don't just list files. Organize them by priority. 
- Use the `llms.txt.example` template.
- Ensure the most critical "entry-point" docs are at the top.

### Step 3: Add L3 Metadata Blocks
For every `.md` file, add a YAML block at the top:
```markdown
---
ai-context:
  topic: "Brief description of the page"
  user_intent: "What the user wants to achieve"
  prerequisites: ['Other-doc.md', 'Concept-X']
  critical-warning: "DANGER: Do not run in prod"
---
```

## 🏆 Climbing the Compliance Ladder

| Stage | Focus | Goal | Badge |
| :--- | :--- | :--- | :--- |
| **In-Progress** | L1 & L3 Existence | Get the map and metadata in place. | `Orange` |
| **Basic** | L1 & L3 Correctness | Ensure all core docs have metadata. | `Yellow` |
| **Full** | L1, L2, L3 Perfect | No heading jumps, perfect mapping. | `Green` |
| **Evolutionary** | L4 Feedback Loop | Establish `.ai-feedback.md` for self-healing docs. | `Purple` |

## 🛠 Recommended Tools
- **Linter**: `aird_lint_v4.py`
- **AI Assistant**: Prompt your AI to "Review this file and suggest a corresponding `.ai-feedback.md` entry if any information is missing."

---
*AIRD is a living standard. For the full technical specification, please refer to [AIRD_SPEC.md](./AIRD_SPEC.md).*
