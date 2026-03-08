---
name: literature-review
description: 文献综述助手。使用 Zotero MCP 搜索、阅读、分析和综合学术文献。在需要查找文献、阅读 PDF、提取关键信息、生成文献综述时使用此技能。
compatibility: opencode
---

# 文献综述助手

专门用于文献搜索、阅读、分析和综述写作的技能。

## 使用场景

- 查找特定主题的文献
- 阅读和理解 PDF 全文
- 提取文献的关键信息
- 生成文献综述
- 管理参考文献

## 工作流程

### 1. 文献搜索

**搜索策略：**
1. 确定关键词和同义词
2. 使用布尔逻辑组合搜索
3. 筛选相关文献
4. 记录搜索结果

**搜索命令示例：**
```
搜索关于 "高强度间歇训练" 和 "耐力" 的文献
查找 2020 年以后发表的 HIIT 研究
搜索作者 "Thomas Stöggl" 的所有文献
```

**使用 Zotero 搜索：**
- `zotero_zotero_search_items` - 主搜索工具
- `zotero_zotero_search_by_tag` - 按标签搜索
- `zotero_zotero_get_recent` - 最近添加的文献

### 2. 文献筛选

**筛选标准：**
- 相关性：与研究问题的关联程度
- 质量：研究设计、样本量、统计方法
- 时效性：优先考虑近 5 年的研究
- 可获取性：能否获取全文

**筛选流程：**
1. 阅读标题和摘要
2. 快速浏览方法和结果
3. 决定是否纳入
4. 添加标签和笔记

### 3. 深度阅读

**阅读顺序：**
1. 摘要 - 了解研究概况
2. 引言 - 理解研究背景和问题
3. 方法 - 评估研究设计
4. 结果 - 提取关键发现
5. 讨论 - 理解作者解释和局限

**使用 Zotero 工具：**
- `zotero_zotero_get_item_fulltext` - 获取全文内容
- `zotero_zotero_get_item_metadata` - 获取引用信息
- `zotero_zotero_get_annotations` - 提取标注
- `zotero_zotero_get_notes` - 查看笔记

### 4. 信息提取

**提取模板：**
```markdown
## 文献信息
- **标题**: 
- **作者**: 
- **年份**: 
- **期刊**: 
- **DOI**: 

## 研究问题
- 

## 研究方法
- 研究设计: 
- 参与者: 
- 干预方案: 
- 测量指标: 

## 主要发现
- 

## 研究局限
- 

## 与本研究的关系
- 
```

**创建笔记：**
使用 `zotero_zotero_create_note` 为重要文献添加结构化笔记。

### 5. 文献综合

**综合方法：**
1. 按主题分组文献
2. 识别共同发现和分歧
3. 按时间线梳理发展脉络
4. 指出研究空白

**综述结构：**
```markdown
# 文献综述

## 主题 1：[名称]
- 主要研究发现
- 代表文献：[引用 1], [引用 2]
- 争议或分歧

## 主题 2：[名称]
- ...

## 研究空白
- 现有研究的不足
- 本研究如何填补空白
```

## 可用工具

### Zotero MCP 工具

**搜索：**
- `zotero_zotero_search_items` - 搜索文献（支持 titleCreatorYear 和 everything 模式）
- `zotero_zotero_search_by_tag` - 按标签搜索
- `zotero_zotero_advanced_search` - 高级搜索（多条件）

**获取内容：**
- `zotero_zotero_get_item_metadata` - 获取元数据（支持 markdown 和 bibtex 格式）
- `zotero_zotero_get_item_fulltext` - 获取全文
- `zotero_zotero_get_item_children` - 获取附件和笔记

**管理：**
- `zotero_zotero_get_collections` - 查看所有分类
- `zotero_zotero_get_collection_items` - 获取某分类下的文献
- `zotero_zotero_get_recent` - 最近添加的文献
- `zotero_zotero_create_note` - 创建笔记
- `zotero_zotero_create_annotation` - 创建标注

**语义搜索：**
- `zotero_zotero_semantic_search` - AI 赋能的语义搜索
- `zotero_zotero_update_search_database` - 更新语义搜索数据库

## 输出格式

### 引用格式

**APA 格式：**
```
作者。（年份）.标题。期刊名，卷号 (期号), 页码。https://doi.org/xxx
```

**MLA 格式：**
```
作者."标题."期刊名，卷号，期号，年份，页码.
```

**BibTeX 格式：**
```bibtex
@article{key,
  author = {作者},
  title = {标题},
  journal = {期刊名},
  year = {年份},
  volume = {卷号},
  number = {期号},
  pages = {页码},
  doi = {DOI}
}
```

### 笔记格式

```markdown
# 笔记标题

## 摘要
[用自己的话总结]

## 关键引用
> [直接引用原文]

## 我的思考
[个人评论和想法]

## 相关研究
- [相关文献 1]
- [相关文献 2]
```

## 最佳实践

1. **及时记录**：阅读时立即添加标注和笔记
2. **结构化整理**：使用统一的模板提取信息
3. **定期回顾**：每周回顾已读文献
4. **建立联系**：记录文献之间的关系
5. **版本管理**：重要修改前创建备份

## 禁止行为

- 直接复制大段原文（避免抄袭）
- 不阅读全文就引用
- 忽略研究的局限性
- 断章取义地引用结果

## 快速命令

- "搜索关于 [主题] 的文献"
- "获取这篇文献的全文"
- "提取这篇文献的标注"
- "为这篇文献创建笔记"
- "生成这篇文献的 APA 引用"
- "查看 [分类] 下的所有文献"
- "搜索我最近添加的文献"
- "用语义搜索查找 [概念] 相关文献"

## 参考文件

- `skills/paper-writer/` - 论文写作综合助手
- `skills/consistency-guard/` - 一致性检查
- `skills/long-context-memory/` - 长文本记忆管理
