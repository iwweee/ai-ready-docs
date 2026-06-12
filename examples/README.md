# AI-Ready Examples Gallery

This directory provides concrete implementations of the AIRD v1.1 specification. 
Instead of reading the SPEC, copy these structures to make your project AI-native.

## 📂 Available Examples

### 1. [Python Library](./python-lib/)
**Focus**: API discovery and usage constraints.
- **Ideal for**: Open-source libraries, SDKs, internal utility tools.
- **Key Feature**: L3 `ai-context` blocks that warn AI about thread-safety and dependency versions.

### 2. [System Architecture](./system-arch/)
**Focus**: Managing complexity and cross-document dependencies.
- **Ideal for**: Enterprise software, microservices, complex game engines.
- **Key Feature**: L1 $\rightarrow$ L3 mapping that prevents "context fragmentation" across multiple architectural layers.

### 3. [Agent SOP](./agent-sop/)
**Focus**: Deterministic execution and result verification.
- **Ideal for**: AI-driven workflows, automated research agents, complex prompt chains.
- **Key Feature**: L4 feedback loop integrated into the operational process.

---
**Quick Start**: 
1. Pick a scenario that matches your project.
2. Copy the file structure.
3. Replace the content with your actual project details.
