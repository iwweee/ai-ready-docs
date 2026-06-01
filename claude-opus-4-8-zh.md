---
# 元数据 (METADATA)
- 主题：Claude Opus 4.8 发布更新
- 提供方：Anthropic
- 日期：2026-05-31
- 模型 ID：claude-opus-4-8
- 可信度：官方公告
---

# 🚀 核心更新：Claude Opus 4.8

## 1. 关键性能提升
- **Agentic 能力（智能体能力）**：在 Agent 任务中表现出更敏锐的判断力；错误自检测能力显著增强（代码缺陷漏报率较前代降低了 4 倍）。
- **基准测试 (Benchmarks)**：
  - **Super-Agent Benchmark**：唯一能够端到端完成所有测试用例的模型，在成本对等的情况下击败了 GPT-5.5。
  - **Online-Mind2Web**：得分 84%，较 Opus 4.7 和 GPT-5.5 有显著提升。
  - **法律智能体基准测试 (Legal Agent Benchmark)**：创下历史最高分；首个在“全通过标准 (all-pass standard)”中突破 10% 的模型。

## 2. 新功能集
- **动态工作流 (Dynamic Workflows)**：[仅限 Claude Code] 能够在单个会话中规划并运行数百个并行子 Agent，用于处理代码库规模的迁移任务。
- **复杂度控制 (Effort Control)**：用户现在可以在 claude.ai 上选择响应深度（低复杂度 $\rightarrow$ 响应更快/节省配额；高复杂度 $\rightarrow$ 更深层的推理）。
- **Messages API 升级**：现在允许在消息数组内部插入系统条目 (system entries)，从而在不破坏提示词缓存 (prompt cache) 的情况下更新指令。
- **快速模式 (Fast Mode)**：速度提升 2.5 倍；成本比之前的模型便宜 3 倍。

## 3. 定价与可用性
- **标准模式 (Standard Mode)**：输入 $5/百万 tokens $\mid$ 输出 $25/百万 tokens。
- **快速模式 (Fast Mode)**：输入 $10/百万 tokens $\mid$ 输出 $50/百万 tokens。
- **可用性**：现已通过 Claude API 提供。

## 4. 路线图 (Roadmap)
- **Project Glasswing (蜻蜓计划)**：即将推出更高智能级别的模型（目前仅面向网络安全领域进行限量预览）。
