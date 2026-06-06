---
ai-context:
  topic: "Gemini Omni Flash 能力规格书 (AI-Ready Version)"
  prerequisites: ['API Fundamentals', 'System Architecture']
  critical-warning: ""
---

# Gemini Omni Flash 能力规格书 (AI-Ready Version)

## 1. 定位与核心能力 (Core Positioning)
- **核心定位**：原生多模态生成模型 (Native Multimodal Generative Model)，专注于“从任何输入到任何输出”的创作。
- **关键能力**：将 Gemini 的推理能力与强大的生成能力结合，支持跨模态的理解与高保真视频生成。
- **核心特性**：
  - **全模态输入 $\rightarrow$ 视频输出**：支持图像、音频、视频和文本的任意组合作为输入，生成高质量视频。
  - **对话式视频编辑 (Conversational Video Editing)**：支持通过自然语言对视频进行多轮迭代编辑，且保持角色、物理效果和场景的一致性。
  - **世界知识增强**：利用 Gemini 的世界知识（历史、科学、文化）来驱动视频生成，使其不仅是“像真的”，而且是“符合逻辑的”。
  - **物理规律理解**：对重力、动能、流体动力学等物理特性有更深刻的直觉理解。

## 2. 功能矩阵 (Feature Matrix)

### 🎬 视频生成与编辑 (Video Generation & Editing)
- **动态修改**：可通过指令改变视频中的特定物体（如将雕塑改为气泡）或整体氛围（如调暗灯光）。
- **动作重塑**：能够修改视频中的动作，添加新角色或对象，将真实拍摄片段转化为超现实场景。
- **多轮精炼**：支持在不丢失原始场景线索的情况下，连续更改环境、视角、风格或细节。

### 🧬 复杂指令执行 (Complex Instruction Execution)
- **知识驱动创作**：能够处理极其复杂的 Prompt（例如：要求 26 个字母对应 26 个不寻常物品，并精准控制每帧时长和视觉样式）。
- **原理可视化**：能将复杂概念（如蛋白质折叠）转化为直观的粘土动画解释视频。

### 🔄 输入参考能力 (Reference Capabilities)
- **跨模态融合**：可以将图像作为角色参考 $\rightarrow$ 视频作为动作参考 $\rightarrow$ 音频作为节奏参考，最终融合成一个统一的输出。
- **风格迁移**：支持将特定图像的风格（如复古未来主义）迁移到生成的视频中。

## 3. 运行参数与安全 (Specs & Safety)

| 维度 | Gemini Omni Flash | 备注 |
| :--- | :--- | :--- |
| **输出模态** | 目前主攻视频 (Video) | 未来将支持图像和音频输出 |
| **输入模态** | 文本, 图像, 视频, 音频 (语音) | 实现真正的 Omni 输入 |
| **部署渠道** | Gemini App, Google Flow, YouTube Shorts | 逐步向开发者和企业 API 开放 |
| **安全机制** | SynthID 数字水印 | 所有生成视频均包含不可见水印，确保透明度 |
| **数字分身** | 支持 Avatars 功能 | 可生成外观和声音与用户一致的数字人视频 |

## 4. AI 选型建议 (Selection Guide)
- **优先调用场景**：
  - 需要【高质量视频生成】且要求【极高物理真实度】的任务。
  - 需要【通过对话快速迭代视频内容】的创意工作流。
  - 需要【将多模态参考资料 (图/影/音) 转化为统一视觉结果】的复杂创作。
- **对比 Gemini 3.5 Flash**：3.5 Flash 侧重于【Agent 执行力、代码和文本推理】；Omni Flash 侧重于【多模态创作与视频生成】。两者在 Agent 生态中应作为“大脑 (3.5)”与“画笔 (Omni)”的关系配合使用。

---
*Last Updated: 2026-06-02 | Source: Google Blog | Purified by 虾仔 🦞*
