# Superpowers Skills 完整目录

> 来源：[obra/superpowers](https://github.com/obra/superpowers) @ `f2cbfbe` (Release v5.1.0)
> 路径：`.kimi/skills/`（软链接至 `superpowers/skills/`）

## 环境说明

当前运行环境为 **Kimi Code VS Code 扩展**，与 Claude Code 存在以下差异：

| 功能 | Claude Code | Kimi Code |
|------|-------------|-----------|
| 读取 Skill | `Skill` 工具 | `ReadFile` 工具 |
| 任务管理 | `TodoWrite` | `SetTodoList` |
| Namespace | `superpowers:name` | `name`（无前缀） |
| Visual Companion | 浏览器工具 | ❌ 不支持 |
| 设计文档路径 | `docs/superpowers/` | 本项目不适用，见下方说明 |

## 路径映射

Skill 文件中的 `superpowers:<name>` 引用等价于本目录下的 `<name>`：

- `superpowers:brainstorming` → `brainstorming/`
- `superpowers:writing-plans` → `writing-plans/`
- `superpowers:test-driven-development` → `test-driven-development/`
- ...以此类推

## 本项目特殊约定

本项目为 leetcode 算法练习仓库，**不适用**以下 Superpowers 默认行为：

1. **不创建 `docs/superpowers/` 目录**：设计文档/计划直接输出在对话中，或保存到项目根目录的临时 `.md` 文件
2. **不使用 git worktree**：本项目无需隔离工作区
3. **忽略 Visual Companion**：Kimi Code 无浏览器工具，所有设计讨论使用文本形式

## 可用 Skills

| Skill | 触发条件 | 路径 |
|-------|---------|------|
| **using-superpowers** | 每次对话开始时 | `using-superpowers/SKILL.md` |
| **brainstorming** | 任何创造性工作前（创建功能、构建组件、添加功能、修改行为） | `brainstorming/SKILL.md` |
| **writing-plans** | 有多步骤任务的 spec 或需求，在碰代码之前 | `writing-plans/SKILL.md` |
| **solving-leetcode-problems** | 刷 LeetCode 算法题，写代码前 | `solving-leetcode-problems/SKILL.md` |
| **test-driven-development** | 实现任何功能或修复 bug，在写实现代码之前 | `test-driven-development/SKILL.md` |
| **subagent-driven-development** | 在当前会话中执行独立任务的实现计划 | `subagent-driven-development/SKILL.md` |
| **executing-plans** | 有书面实现计划要在单独会话中执行（带审查检查点） | `executing-plans/SKILL.md` |
| **dispatching-parallel-agents** | 面对 2 个以上无共享状态或顺序依赖的独立任务 | `dispatching-parallel-agents/SKILL.md` |
| **systematic-debugging** | 遇到任何 bug、测试失败或意外行为，在提出修复前 | `systematic-debugging/SKILL.md` |
| **verification-before-completion** | 声称工作完成、修复成功或通过测试前 | `verification-before-completion/SKILL.md` |
| **requesting-code-review** | 完成任务、实现主要功能或合并前验证工作 | `requesting-code-review/SKILL.md` |
| **receiving-code-review** | 收到代码审查反馈，在实施建议前 | `receiving-code-review/SKILL.md` |
| **using-git-worktrees** | ⚠️ 本项目不适用：开始需要与当前工作区隔离的功能工作 | `using-git-worktrees/SKILL.md` |
| **finishing-a-development-branch** | 实现完成、所有测试通过，需要决定如何集成 | `finishing-a-development-branch/SKILL.md` |
| **writing-skills** | 创建新 Skill、编辑现有 Skill 或验证 Skill | `writing-skills/SKILL.md` |

## 读取方式

使用 `ReadFile` 工具读取对应路径的 `SKILL.md`，然后严格遵循其中的指令执行。
对于 `brainstorming` 中的 `visual-companion.md` 引用，忽略该部分。
