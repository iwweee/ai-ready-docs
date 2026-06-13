# L4 Evolution: Feedback Workflow Guide (v1.2 Updated)

The `.ai-feedback.md` file is no longer just a log—it is the **trigger** for the documentation's self-evolution.

## 🔄 The Evolutionary Loop (Capture $\rightarrow$ Patch $\rightarrow$ Review $\rightarrow$ Merge)

### Step 1: Capture (Detection)
When an AI agent fails to perform a task correctly or finds a gap, it must record it structurally in `.ai-feedback.md`.

**Format for AI Agents:**
- `[ ] **Gap ID**: [YYYY-MM-DD-ID]`
- `Target`: [Path to file]
- `Issue`: [What is missing or incorrect]
- `Proposed Fix`: [Exact text change suggested]

### Step 2: Patch (The Action)
Instead of waiting for a weekly review, the agent (or a specialized "Doc-Agent") can now:
1. Create a branch: `ai-patch/<Gap-ID>`.
2. Apply the `Proposed Fix` to the target file.
3. Commit and push to GitHub.
4. Open a Pull Request with the label `ai-generated-doc-patch`.

### Step 3: Review (The Human Guardrail)
The human maintainer reviews the PR. 
- **If correct**: Merge the PR.
- **If incorrect**: Request changes or close the PR.

### Step 4: Verify (Closing the Loop)
Once the PR is merged, the corresponding item in `.ai-feedback.md` is marked as `Resolved` (checked off).

---

## 📈 Maintenance Schedule (v1.2)

- **Continuous**: Agents log gaps as they happen.
- **Daily/Weekly**: Human reviews the `ai-generated-doc-patch` PR queue.
- **Pruning**: Archive resolved issues to keep the feedback file lean.

## 💡 Pro Tip
Combine L5 Execution Protocols with this loop. If an agent fails to follow an L5 protocol because the "Success Criteria" were ambiguous, the agent should immediately log a gap in the L5 section of that document.
