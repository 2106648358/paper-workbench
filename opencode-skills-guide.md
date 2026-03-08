# Opencode 技能与代理使用指南

本项目配置的 Opencode 技能集合和代理系统，用于论文写作和文献管理。

---

## 代理（Agents）配置

代理是专门的 AI 助手，用于特定任务和工作流。

### 1. context-keeper
**位置**: `.opencode/agents/context-keeper.md`

**类型**: subagent

**模型**: qwen/qwen3.5-plus

**用途**: 维护论文全局记忆库，确保上下文连贯

**权限**:
- 仅可读写 `PAPER_MEMORY.md`
- 禁止修改论文正文
- 禁止联网

**何时使用**:
```
@context-keeper 更新论文记忆库
@context-keeper 获取当前上下文快照
```

---

### 2. deep-research
**位置**: `.opencode/agents/deep-research.md`

**类型**: subagent

**模型**: qwen/qwen3.5-plus

**用途**: 深度学术研究和文献分析

**权限**:
- 只读模式（不修改文件）
- 允许联网（webfetch: allow）
- 可被 primary agent 调用

**何时使用**:
```
@deep-research 分析这个新想法的可行性
@deep-research 查找 HIIT 训练的最新研究
@deep-research 评估与现有论文的关联性
```

---

### 3. modular-planner
**位置**: `.opencode/agents/modular-planner.md`

**类型**: subagent

**模型**: qwen/qwen3.5-plus

**用途**: 设计模块化修改方案，规划不执行

**权限**:
- 只读模式（不修改文件）
- 禁止联网
- 可被 primary agent 调用

**何时使用**:
```
@modular-planner 设计第 3 章的修改方案
@modular-planner 分析这个新内容如何插入
@modular-planner 评估修改影响范围
```

---

### 任务权限配置

在 `opencode.json` 中配置 primary agent 可调用的 subagent：

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

这意味着 build 和 plan 代理可以自动调用这些 subagent 来完成复杂任务。

---

## 技能列表

### 1. skill-creator
**位置**: `.opencode/skills/skill-creator/`

**用途**: 创建、测试和优化新的 Opencode 技能

**何时使用**:
- 需要创建新的自定义技能
- 想要改进现有技能
- 运行技能评估测试

**常用命令**:
```
帮我创建一个新技能，用于 [任务描述]
运行技能测试
生成评估报告
打包我的技能
```

---

### 2. paper-writer
**位置**: `.opencode/skills/paper-writer/`

**用途**: 论文写作综合助手，整合 Zotero 文献管理

**何时使用**:
- 设计论文结构或大纲
- 撰写或修改论文章节
- 检查内容一致性
- 更新论文记忆库

**常用命令**:
```
帮我设计论文大纲
撰写 [章节] 部分
查找关于 [主题] 的文献
检查这段的一致性
更新论文记忆库
```

** Zotero 集成**:
- 搜索文献：`zotero_zotero_search_items`
- 获取全文：`zotero_zotero_get_item_fulltext`
- 获取引用：`zotero_zotero_get_item_metadata`
- 查看标注：`zotero_zotero_get_annotations`

---

### 3. literature-review
**位置**: `.opencode/skills/literature-review/`

**用途**: 文献综述助手，专业的文献搜索和分析

**何时使用**:
- 查找特定主题的文献
- 阅读和理解 PDF 全文
- 提取文献关键信息
- 生成文献综述

**常用命令**:
```
搜索关于 [关键词] 的文献
获取这篇文献的全文
提取这篇文献的标注
为这篇文献创建笔记
生成 APA 引用格式
用语义搜索查找相关文献
```

---

### 4. consistency-guard (参考技能)
**位置**: `skills/consistency-guard/`

**用途**: 检查修改后的内容一致性

**何时使用**:
- 修改论文后进行检查
- 确保术语和符号一致
- 验证引用格式

---

### 5. modular-edit (参考技能)
**位置**: `skills/modular-edit/`

**用途**: 控制论文修改范围，模块化编辑

**何时使用**:
- 进行局部内容修改
- 需要创建修改备份
- 追踪版本变更

---

### 6. long-context-memory (参考技能)
**位置**: `skills/long-context-memory/`

**用途**: 读写论文全局记忆库

**何时使用**:
- 开始新的写作任务前
- 需要保持长文本逻辑连贯
- 更新记忆库

---

## 配置文件

### opencode.json

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "github-mcp": { ... },
    "zotero": { ... }
  },
  "permission": {
    "skill": {
      "skill-creator": "allow",
      "paper-writer": "allow",
      "literature-review": "allow"
    }
  }
}
```

### 技能目录结构

```
.opencode/skills/
├── skill-creator/      # 技能开发工具
├── paper-writer/       # 论文写作助手
└── literature-review/  # 文献综述助手

skills/                 # 参考技能（旧格式）
├── consistency-guard/
├── long-context-memory/
└── modular-edit/
```

---

## Zotero MCP 配置

### 环境变量

在 `.opencode/mcp.json` 或系统环境中配置：

```json
{
  "ZOTERO_LOCAL": "true",
  "ZOTERO_LOCAL_KEY": "你的 API 密钥",
  "ZOTERO_LIBRARY_ID": "你的库 ID",
  "ZOTERO_ATTACHMENTS_DIR": "C:/Users/.../Zotero"
}
```

### 获取 Zotero API 密钥

1. 访问 https://www.zotero.org/settings/keys
2. 创建新的 API 密钥
3. 设置权限为"完整库访问"
4. 复制密钥到配置文件

### 查找库 ID

1. 访问 https://www.zotero.org/settings/keys
2. 查看"Your Key for API Version 3"
3. 库 ID 显示在密钥下方

---

## 最佳实践

### 技能使用

1. **明确意图**: 清楚说明你要做什么
2. **提供上下文**: 包含相关文件和信息
3. **分步执行**: 复杂任务分解为多个步骤
4. **及时检查**: 使用 consistency-guard 验证修改

### 文献管理

1. **及时标注**: 阅读时立即添加高亮和注释
2. **结构化笔记**: 使用统一模板记录信息
3. **定期整理**: 清理重复和无关文献
4. **建立联系**: 记录文献间的关系

### 论文写作

1. **先读后写**: 写作前读取 PAPER_MEMORY.md
2. **模块化**: 每次只修改一个部分
3. **备份优先**: 重要修改前创建备份
4. **同步更新**: 修改后更新记忆库

---

## 故障排除

### 技能未触发

确保：
- 技能描述包含相关关键词
- 使用具体的、多步骤的请求
- 技能权限设置为"allow"

### Zotero 连接失败

检查：
- API 密钥是否正确
- 网络是否通畅
- Zotero 桌面客户端是否运行

### 技能文件未加载

确认：
- SKILL.md 在正确的目录
- frontmatter 格式正确
- 技能名称符合规范

---

## 扩展技能

使用 skill-creator 创建新技能：

1. 说明技能用途
2. 定义输入输出格式
3. 创建测试用例
4. 运行评估
5. 迭代改进
6. 打包分享

---

## 参考资源

- [Opencode 官方文档](https://opencode.ai/docs/)
- [技能开发指南](.opencode/skills/skill-creator/README.md)
- [Zotero MCP 文档](.opencode/ZOTERO-MCP-README.md)
