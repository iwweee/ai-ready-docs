# L4 Evolution: Feedback Workflow Guide

The `.ai-feedback.md` file is not just a log—it is the "sensor" for your documentation's evolution. This guide transforms the L4 mechanism into a repeatable operational workflow.

## 🔄 The Feedback Loop (Capture $\rightarrow$ Analyze $\rightarrow$ Refine $\rightarrow$ Verify)

### Step 1: Capture (The "Aha!" Moment)
When an AI agent fails to perform a task correctly, **do not just correct it in the chat.** Capture the failure.

**What to record in `.ai-feedback.md`:**
- **The Prompt**: What did you ask?
- **The Failure**: What did the AI get wrong? (e.g., "Hallucinated a non-existent API parameter")
- **The Evidence**: A link to the chat or a snippet of the wrong output.

### Step 2: Analyze (Root Cause Identification)
Determine which AIRD layer failed:
- **L1 (Discovery) Failure**: The AI didn't know the information existed or went to the wrong file.
- **L2 (Structure) Failure**: The AI found the file but got lost in the layout or couldn't find the specific section.
- **L3 (Context) Failure**: The AI found the info but misunderstood the prerequisites or ignored a critical warning.

### Step 3: Refine (The Fix)
Update your documentation based on the analysis:
- **Fix L1**: Update `llms.txt` to be more explicit about where information is located.
- **Fix L2**: Rearrange the hierarchy or rename files for better deterministic retrieval.
- **Fix L3**: Add a `critical-warning` or a new `prerequisite` to the `ai-context` block.

### Step 4: Verify (The Test)
Run the exact same prompt again with the updated documentation.
- **Success**: Mark the feedback item as `Resolved`.
- **Failure**: Re-analyze and repeat Step 2.

---

## 📈 Maintenance Schedule

- **Weekly Review**: Scan `.ai-feedback.md` for recurring patterns. If the same mistake happens 3+ times, it's a systemic failure in your L1-L3 layers.
- **Pruning**: Once a fix is verified and the documentation is stable, you can move resolved items to an archive to keep the feedback file lean.

## 💡 Pro Tip
If you are building a professional AI Agent, you can automate Step 1 by having the Agent itself append failures to `.ai-feedback.md` when it detects a "User Correction" in the conversation.
