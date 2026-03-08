# OpenCode 论文写作 Skills 配置指南

本指南帮助你在任何项目目录中配置 OpenCode + Qwen 大模型，使用论文写作相关的 Skills。

---

## 📁 一、目录结构

配置完成后的目录结构如下：

```
your-project/
├── .opencode/
│   └── skills/
│       ├── doc-coauthoring/
│       │   └── SKILL.md
│       ├── docx/
│       │   └── SKILL.md
│       ├── pdf/
│       │   └── SKILL.md
│       └── xlsx/
│           └── SKILL.md
├── opencode.json
└── AGENTS.md (可选)
```

---

## 🚀 二、快速配置步骤

### 步骤 1：创建 Skills 目录

```bash
# 进入你的项目目录
cd /path/to/your-project

# 创建 OpenCode 配置目录
mkdir -p .opencode/skills
```

### 步骤 2：下载 Skills

#### 方式 A：使用 Git 克隆（推荐）

```bash
# 克隆 anthropics/skills 仓库
git clone --depth 1 https://github.com/anthropics/skills.git /tmp/anthropics-skills

# 复制论文相关的 skills
cp -r /tmp/anthropics-skills/skills/doc-coauthoring .opencode/skills/
cp -r /tmp/anthropics-skills/skills/docx .opencode/skills/
cp -r /tmp/anthropics-skills/skills/pdf .opencode/skills/
cp -r /tmp/anthropics-skills/skills/xlsx .opencode/skills/

# 清理临时文件
rm -rf /tmp/anthropics-skills
```

#### 方式 B：手动下载

访问 https://github.com/anthropics/skills/tree/main/skills 下载以下文件夹：
- `doc-coauthoring`
- `docx`
- `pdf`
- `xlsx`

然后放入 `.opencode/skills/` 目录。

### 步骤 3：创建配置文件

在项目根目录创建 `opencode.json`：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": {
    "default": "qwen-max"
  },
  "provider": {
    "openai": {
      "api_key": "${DASHSCOPE_API_KEY}",
      "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1"
    }
  },
  "permission": {
    "skill": {
      "*": "allow"
    }
  }
}
```

### 步骤 4：配置 API 密钥

#### Windows PowerShell
```powershell
# 临时设置（当前会话有效）
$env:DASHSCOPE_API_KEY="sk-your-api-key-here"

# 永久设置
setx DASHSCOPE_API_KEY "sk-your-api-key-here"
```

#### macOS / Linux
```bash
# 临时设置（当前会话有效）
export DASHSCOPE_API_KEY="sk-your-api-key-here"

# 永久设置（添加到 ~/.bashrc 或 ~/.zshrc）
echo 'export DASHSCOPE_API_KEY="sk-your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

获取 API 密钥：https://dashscope.console.aliyun.com/apiKey

---

## 📚 三、Skills 说明

### 3.1 doc-coauthoring（⭐ 核心推荐）

**用途**：结构化论文协作写作流程

**功能**：
- 三阶段写作：背景收集 → 结构优化 → 读者测试
- 逐节构建：摘要、引言、方法、实验、结论
- 自动检查论文逻辑和一致性

**使用示例**：
```
使用 doc-coauthoring 技能帮我写毕业论文
```

```
开始 doc-coauthoring 流程，我要写一篇关于深度学习的论文
```

---

### 3.2 docx

**用途**：Word 文档创建和编辑

**功能**：
- 创建符合学术格式的 .docx 论文
- 生成目录、页眉页脚、页码
- 处理表格、图片、公式
- 跟踪修改和批注

**使用示例**：
```
使用 docx 技能创建论文草稿，格式要求：A4 纸、小四字体、1.5 倍行距
```

```
用 docx 技能给我的论文添加目录和页码
```

---

### 3.3 pdf

**用途**：PDF 文件处理

**功能**：
- 从 PDF 提取文本和表格
- 合并/拆分 PDF 文件
- OCR 扫描文档
- 添加水印、加密

**使用示例**：
```
使用 pdf 技能从这篇参考文献中提取引用信息
```

```
用 pdf 技能把我写好的论文转换成 PDF
```

---

### 3.4 xlsx

**用途**：Excel 数据处理

**功能**：
- 处理实验数据
- 生成统计表格
- 数据可视化准备

**使用示例**：
```
使用 xlsx 技能整理实验数据表格
```

---

## 💡 四、使用方式

### 4.1 在 OpenCode TUI 中使用

启动 OpenCode：
```bash
opencode
```

#### 调用特定 Skill
```
使用 doc-coauthoring 技能帮我写论文
```

#### 让模型自动选择 Skill
```
帮我写一篇关于机器学习的综述论文
```

#### 查看可用 Skills
```
/tools
```

### 4.2 完整写作流程示例

```
# 1. 开始论文写作流程
使用 doc-coauthoring 技能，我要写一篇毕业论文

# 2. 提供论文主题和背景
主题：基于深度学习的图像识别
背景：...（提供你的研究背景）

# 3. 逐节构建论文
现在我们开始写引言部分

# 4. 格式化输出
使用 docx 技能将论文导出为 Word 文档

# 5. 处理参考文献
使用 pdf 技能从这些 PDF 中提取引用
```

---

## ⚙️ 五、可选配置

### 5.1 使用其他 Qwen 模型

修改 `opencode.json`：

```json
{
  "model": {
    "default": "qwen-plus"  // 或 qwen-turbo / qwen-max-longcontext
  }
}
```

| 模型 | 适用场景 |
|------|----------|
| `qwen-max` | 复杂论文写作（推荐） |
| `qwen-plus` | 日常写作任务 |
| `qwen-turbo` | 快速简单任务 |
| `qwen-max-longcontext` | 超长论文/多文档分析 |

### 5.2 创建 AGENTS.md（可选）

在项目根目录创建 `AGENTS.md`，提供论文写作偏好：

```markdown
# 论文写作偏好

## 格式要求
- 使用 A4 纸张
- 正文字体：小四 (12pt)
- 行距：1.5 倍
- 引用格式：APA 第 7 版

## 写作风格
- 学术正式语气
- 避免第一人称
- 被动语态优先

## 论文结构
1. 摘要 (300-500 字)
2. 引言
3. 相关工作
4. 方法
5. 实验
6. 结论
7. 参考文献
```

### 5.3 配置 MCP（可选）

如需使用 GitHub 搜索文献代码：

```json
{
  "mcp": {
    "github-mcp": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-github"],
      "environment": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "你的 GitHub Token"
      }
    }
  }
}
```

---

## ⚠️ 六、注意事项

### 6.1 兼容性说明

| 功能 | Claude 原生 | OpenCode + Qwen |
|------|-------------|-----------------|
| SKILL.md 加载 | ✅ | ✅ |
| 核心写作流程 | ✅ | ✅ |
| Artifacts 文件创建 | ✅ | ⚠️ 部分支持 |
| Sub-agents 子代理 | ✅ | ❌ 不支持 |

**建议**：核心论文写作功能完全可用，文件创建使用 OpenCode 内置工具替代。

### 6.2 常见问题

**Q: Skills 没有加载？**
```bash
# 检查目录结构
ls -la .opencode/skills/

# 验证 SKILL.md 存在
cat .opencode/skills/doc-coauthoring/SKILL.md
```

**Q: 模型响应不符合预期？**
- 尝试使用 `qwen-max` 替代 `qwen-plus`
- 在 prompt 中明确指定使用的 skill 名称
- 在 AGENTS.md 中提供更多上下文

**Q: 如何验证配置成功？**
```bash
# 启动 OpenCode 后运行
/mcp
# 或
/tools
```

---

## 🔗 七、参考资料

- OpenCode 官方文档：https://opencode.ai/docs
- OpenCode Skills 文档：https://opencode.ai/docs/skills/
- Qwen 模型文档：https://help.aliyun.com/zh/dashscope/
- Anthropic Skills 仓库：https://github.com/anthropics/skills

---

## 📝 八、快速检查清单

配置前确认：

- [ ] 已安装 OpenCode (`opencode --version`)
- [ ] 已获取 DashScope API 密钥
- [ ] 已设置 `DASHSCOPE_API_KEY` 环境变量
- [ ] 已创建 `.opencode/skills/` 目录
- [ ] 已下载 SKILL.md 文件
- [ ] 已创建 `opencode.json` 配置文件
- [ ] 已验证目录结构正确

---

**最后更新**: 2026 年 3 月 7 日

**适用版本**: OpenCode v1.0+
