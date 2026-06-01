---
# METADATA (AI-First)
- Topic: 智能体工作流设计指南 (Agentic Workflow Blueprint)
- Source: Anthropic Docs / Zylos Research / Agentic-Workflow.wiki
- Date: 2026-06-01
- Version: 1.0-Ready
- Lang: ZH
- Reliability: High (Production-Proven Patterns)
---

# 🚀 Agent 架构级提示词指南

## 📌 Core Essence (核心要义)
本指南将 AI 从“单次问答”升级为“循环迭代”的 Agentic Workflow。核心是通过构建 **[规划 $\rightarrow$ 执行 $\rightarrow$ 反思 $\rightarrow$ 修正]** 的闭环，消除 LLM 的随机性，实现工业级任务的确定性输出。

## 🛠️ Key Design Patterns (核心设计模式)

### 1. 结构化指令隔离 (XML Tagging)
**目的**：防止指令与数据混淆，确保 AI 严格遵守复杂约束。
- **模式**：使用 `<instruction>`, `<context>`, `<example>`, `<output_format>` 等自定义标签。
- **AI-Ready 技巧**：
  - 将所有外部输入包裹在 `<input>` 标签中。
  - 要求 AI 在最终回答前，先在 `<thinking>` 标签内进行推理。

### 2. 自反思循环 (The Reflection Loop)
**目的**：在输出结果前，强制 AI 进行自我审查，减少幻觉。
- **工作流模式**：
  - **Step 1 (Draft)**: 生成初步答案。
  - **Step 2 (Critique)**: 使用指令 $\rightarrow$ *"请扮演一个苛刻的审计员，找出上述答案中的 3 个潜在错误或不严谨之处"* $\rightarrow$ 放入 `<critique>` 标签。
  - **Step 3 (Refine)**: 根据 `<critique>` 的内容，输出最终优化版答案。

### 3. 动态状态维护 (Current State Tracking)
**目的**：解决长任务中的“迷路”问题，维持上下文一致性。
- **实施方案**：要求 AI 在每次执行工具或步骤后，更新一个名为 `<state_update>` 的块。
- **状态模板**：
  - `Goal`: [最终目标]
  - `Completed`: [已完成步骤]
  - `Pending`: [待执行步骤]
  - `Observation`: [最新发现的关键信息]

### 4. 确定性编排 (SOP-Encoded Workflow)
**目的**：将人类的标准作业程序 (SOP) 转化为 AI 可执行的确定性步骤。
- **模式**：不再说 *"帮我分析这个公司"* $\rightarrow$ 而是定义 *"Step 1: 抓取财报 $\rightarrow$ Step 2: 对比行业均值 $\rightarrow$ Step 3: 识别风险点 $\rightarrow$ Step 4: 输出报告"*。

## 💡 Implementation (AI 直接调用指令)
当你想让 AI 采用此架构时，直接发送以下指令引导：
> "请启动 **Agentic Workflow 模式**。在处理此任务时，请严格执行 `<thinking>` $\rightarrow$ `<action>` $\rightarrow$ `<observation>` $\rightarrow$ `<reflection>` 的循环，并在每次迭代后更新 `<state_update>`。请在最终输出前进行一次自我审计。"

## ⚠️ Constraints (约束)
- **Token 消耗**：反思循环会显著增加 Token 消耗，建议仅在关键任务中使用。
- **延迟增加**：多步迭代会增加响应时间，适用于“质量优先”而非“速度优先”的场景。

---
*Mirror by iwweee | Curated by 虾仔 🦞*
