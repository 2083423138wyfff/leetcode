# Agent Skills

> **IMPORTANT**: 本项目使用 Superpowers 开发方法论 Skills。相关任务优先读取 SKILL.md 中的指令，而非依赖预训练知识。

## 来源

- 仓库：[obra/superpowers](https://github.com/obra/superpowers)
- 版本：`f2cbfbe` (Release v5.1.0)
- 位置：`.kimi/skills/`（软链接至 `superpowers/skills/`）
- 完整目录：见 `.kimi/skills/INDEX.md`

## 环境适配（Kimi Code VS Code 扩展）

本项目运行环境为 **Kimi Code VS Code 扩展**，与 Superpowers 原生的 Claude Code 环境存在差异：

| 功能 | Claude Code | Kimi Code（本环境） |
|------|-------------|---------------------|
| 读取 Skill | `Skill` 工具 | `ReadFile` 工具 |
| 任务管理 | `TodoWrite` | `SetTodoList` |
| Skill 引用 | `superpowers:name` | `name`（无前缀） |
| Visual Companion | 浏览器工具 | ❌ 不支持 |

### 关键适配规则

1. **使用 `ReadFile` 读取 SKILL.md**：忽略 `using-superpowers` 中关于 `Skill` 工具的指令
2. **使用 `SetTodoList` 管理任务**：忽略关于 `TodoWrite` 的引用
3. **Namespace 映射**：`superpowers:<name>` 等价于 `<name>`
4. **忽略 Visual Companion**：`brainstorming` 中的浏览器相关功能不适用

## 本项目特殊约定

本项目为 leetcode 算法练习仓库，不适用以下 Superpowers 默认行为：

- **不创建 `docs/superpowers/` 目录**：设计文档直接输出在对话中
- **不使用 git worktree**：无需隔离工作区

## 常用 Skills

| Skill | 何时使用 |
|-------|---------|
| `using-superpowers` | 每次对话开始时建立规则 |
| `brainstorming` | 创建功能/组件前 |
| `writing-plans` | 有 spec 后，写代码前 |
| `solving-leetcode-problems` | 刷 LeetCode 算法题，写代码前 |
| `test-driven-development` | 实现功能或修复 bug 前 |
| `systematic-debugging` | 遇到 bug 或测试失败 |
| `verification-before-completion` | 声称完成前 |

完整列表和详细触发条件见 `.kimi/skills/INDEX.md`。
