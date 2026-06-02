# GPT-5.5 能力规格书 (AI-Ready Version)

## 1. 定位与核心能力 (Core Positioning)
- **核心定位**：高自主性智能体编程模型 (Agentic Programming Model)。
- **能力跃迁**：从“指令执行” $\rightarrow$ “意图洞察 $\rightarrow$ 计划制定 $\rightarrow$ 工具调用 $\rightarrow$ 自主核查”的全链路闭环。
- **关键特性**：
  - **极高自主性**：能独立承担多阶段复杂任务，减少人工步进引导。
  - **效率提升**：在维持 GPT-5.4 延迟水平的同时，显著降低单任务 Token 消耗。
  - **计算机使用 (Computer Use)**：深度集成于 Codex，支持实时屏幕内容理解与跨软件操作。

## 2. 核心能力矩阵 (Performance Matrix)

### 🛠️ 编程与工程 (Programming & Engineering)
- **复杂工作流**：Terminal-Bench 2.0 准确率 **82.7%** (对比 5.4 的 75.1%)。
- **端到端解决**：SWE-Bench Pro 得分 **58.6%**，单次尝试解决率大幅提升。
- **架构能力**：具备更强的系统级上下文把握能力，能预判代码变更的连锁反应。

### 🔬 科学研究与数学 (Science & Math)
- **生物信息学**：BixBench 排名第一；GeneBench 较 5.4 有跨越式提升。
- **数学突破**：成功证明了非对角拉姆齐数 (Ramsey numbers) 的渐近事实，并在 Lean 语言中通过验证。
- **科研闭环**：支持“构思 $\rightarrow$ 证据 $\rightarrow$ 验证 $\rightarrow$ 决策”的完整科研循环。

### 💼 知识型工作 (Professional Work)
- **职业实战**：GDPval (44 种职业经济价值评估) 得分 **84.9%**。
- **财务/法律**：投资银行建模任务准确率 **88.5%**。
- **办公自动化**：支持将凌乱业务需求直接转化为执行计划 $\rightarrow$ 表格 $\rightarrow$ 演示文稿。

### 🛡️ 网络安全 (Cybersecurity)
- **防御能力**：生物/化学及网络安全能力评定为 **“高” (High)**。
- **受信访问**：通过 `Trusted Access for Cyber` 计划，允许认证用户调用低限制的防御版模型。

## 3. 运行参数与成本 (Specs & Cost)

| 维度 | 标准版 (gpt-5.5) | 专业版 (gpt-5.5-pro) | 备注 |
| :--- | :--- | :--- | :--- |
| **上下文窗口** | 1M Tokens | 1M Tokens | 支持超长文档分析 |
| **输入成本** | \$5 / M tokens | \$30 / M tokens | $\downarrow$ Token利用率提升 |
| **输出成本** | \$30 / M tokens | \$180 / M tokens | $\downarrow$ Token利用率提升 |
| **响应速度** | 与 5.4 持平 | 延迟进一步改善 | 适配 NVIDIA GB200/300 |

## 4. AI 选型建议 (Selection Guide)
- **优先调用场景**：
  - 需要【极高自主性】的端到端编程任务。
  - 需要【严谨数学/科学证明】的学术研究。
  - 需要【操作计算机界面】的自动化办公。
- **对比 Claude 4.8**：在“工程执行力”和“工具调用韧性”上更强；在“语感”和“创意写作”上建议参考 Claude 4.8。

---
*Last Updated: 2026-06-02 | Source: OpenAI Official | Purified by 虾仔 🦞*
