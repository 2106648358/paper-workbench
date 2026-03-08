# Opencode 代理配置完成报告

## 配置摘要

已成功为当前论文写作项目配置 3 个专用代理（Agents）。

---

## 代理列表

| 代理名称 | 类型 | 模型 | 温度 | 联网 | 主要用途 |
|----------|------|------|------|------|----------|
| **context-keeper** | subagent | qwen/qwen3.5-plus | 0.1 | ❌ | 维护论文记忆库 |
| **deep-research** | subagent | qwen/qwen3.5-plus | 0.3 | ✅ | 学术研究分析 |
| **modular-planner** | subagent | qwen/qwen3.5-plus | 0.2 | ❌ | 修改方案设计 |

---

## 文件结构

```
E:\paper\
├── .opencode/
│   └── agents/
│       ├── context-keeper.md      ✅ 已创建
│       ├── deep-research.md       ✅ 已创建
│       └── modular-planner.md     ✅ 已创建
│
├── opencode.json                  ✅ 已更新（添加任务权限）
└── opencode-skills-guide.md       ✅ 已更新（添加代理说明）
```

---

## 权限配置

### context-keeper
```yaml
permission:
  webfetch: deny
  write:
    "PAPER_MEMORY.md": allow
    "*": deny
  edit:
    "PAPER_MEMORY.md": allow
    "*": deny
  task:
    "*": allow
```

### deep-research
```yaml
permission:
  webfetch: allow    # 允许联网搜索
  task:
    "*": allow       # 可被 primary agent 调用
```

### modular-planner
```yaml
permission:
  webfetch: deny
  task:
    "*": allow       # 可被 primary agent 调用
```

---

## 使用方式

### 1. 手动调用（推荐）

在对话框中使用 `@` 提及代理：

```
@context-keeper 请更新论文记忆库，我刚修改了第 3 章

@deep-research 帮我查找关于"高强度间歇训练对耐力影响"的最新研究

@modular-planner 我想在第 2 章添加一个新的实验结果，请设计修改方案
```

### 2. 自动调用

配置后，build 和 plan 等 primary agent 可以根据任务需要自动调用这些 subagent。

例如：
- 当你要求修改论文时，build agent 可能自动调用 `modular-planner` 设计修改方案
- 修改完成后，可能自动调用 `context-keeper` 更新记忆库

---

## 与其他组件的集成

### 与 Skills 配合

- **paper-writer** 技能可以调用 `context-keeper` 更新记忆
- **literature-review** 技能可以与 `deep-research` 协作进行深度研究
- **skill-creator** 可用于创建新的代理

### 与 Zotero MCP 配合

`deep-research` 代理可以：
1. 使用 `webfetch` 联网搜索
2. 调用 Zotero MCP 查找和管理文献
3. 与 `literature-review` 技能协作生成综述

---

## 下一步建议

1. **创建 PAPER_MEMORY.md**：
   ```markdown
   # 论文记忆库

   ## 核心论点
   - 

   ## 术语与符号表
   - 

   ## 章节摘要
   - 

   ## 待办事项
   - 
   ```

2. **测试代理功能**：
   - 尝试使用 `@context-keeper` 创建初始记忆库
   - 使用 `@deep-research` 进行文献调研
   - 使用 `@modular-planner` 规划下一次修改

3. **根据使用反馈调整**：
   - 如果需要更多代理，使用 `skill-creator` 创建
   - 根据实际需求调整温度和权限配置

---

## 配置文件

### opencode.json（任务权限部分）

```json
{
  "agent": {
    "build": {
      "permission": {
        "task": {
          "context-keeper": "allow",
          "deep-research": "allow",
          "modular-planner": "allow"
        }
      }
    },
    "plan": {
      "permission": {
        "task": {
          "context-keeper": "allow",
          "deep-research": "allow",
          "modular-planner": "allow"
        }
      }
    }
  }
}
```

---

## 参考文档

- [Opencode 官方代理文档](https://opencode.ai/docs/agents/)
- [技能与代理使用指南](opencode-skills-guide.md)
- [Zotero MCP 配置](.opencode/ZOTERO-MCP-README.md)

---

**配置完成时间**: 2026-03-08
**模型**: qwen/qwen3.5-plus
**项目**: 论文写作系统
