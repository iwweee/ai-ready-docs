---
# METADATA
- Topic: Claude Opus 4.8 Release
- Provider: Anthropic
- Date: 2026-05-31
- Model_ID: claude-opus-4-8
- Reliability: Official Announcement
---

# 🚀 模型核心更新：Claude Opus 4.8

## 1. 关键性能提升
- **Agentic 能力**：在 agentic 任务中判断力更强，错误自检率提高（代码缺陷遗漏率比前代降低 4 倍）。
- **基准测试**：
  - **Super-Agent Benchmark**: 唯一端到端完成所有案例的模型，超越 GPT-5.5。
  - **Online-Mind2Web**: 评分 84%，显著领先 Opus 4.7 与 GPT-5.5。
  - **Legal Agent Benchmark**: 刷新最高纪录，all-pass 标准突破 10%。

## 2. 新功能特性
- **动态工作流 (Dynamic Workflows)**：【仅限 Claude Code】支持规划并并行运行数百个子代理，可处理数十万行代码的大规模迁移。
- **努力度控制 (Effort Control)**：用户可在 `claude.ai` 选择响应深度（低努力 $\rightarrow$ 快速/省额度；高努力 $\rightarrow$ 深度思考）。
- **Messages API 升级**：支持在消息数组内部插入 `system entries`，无需中断 Prompt Cache 即可中途更新指令。
- **快速模式 (Fast Mode)**：速度提升 2.5 倍，成本比前代降低 3 倍。

## 3. 价格与可用性
- **标准模式**：输入 \$5/M tokens $\mid$ 输出 \$25/M tokens。
- **快速模式**：输入 \$10/M tokens $\mid$ 输出 \$50/M tokens。
- **可用性**：现已全面开放，可通过 Claude API 调用。

## 4. 未来路线图 (Roadmap)
- **Project Glasswing**：即将发布更高智能等级的 `Mythos-class` 模型（目前仅小范围在网络安全领域测试）。
