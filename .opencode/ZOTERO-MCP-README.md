# Zotero MCP 配置说明

## 📋 前提条件

1. **已安装 Zotero 桌面版** 并运行中
2. **已安装茉莉花插件** (`jasminum_1.1.28.xpi`)

## 🔑 获取 Zotero API 凭证

### 步骤 1: 创建 API 密钥

1. 访问: https://www.zotero.org/settings/keys
2. 点击 **"Create a New Key"**
3. 权限设置:
   - ✅ Library Access: **Read and Write**
   - ✅ Files: **Read and Write**
   - ✅ Groups: 如果有群组，选 Read and Write
4. 复制生成的密钥 (类似: `aBcDeF123456789`)

### 步骤 2: 获取用户 ID

在浏览器访问 (替换 YOUR_API_KEY):
```bash
curl -H "Zotero-API-Key: YOUR_API_KEY" https://api.zotero.org/keys/current
```

或者 PowerShell:
```powershell
Invoke-RestMethod -Uri "https://api.zotero.org/keys/current" -Headers @{"Zotero-API-Key"="YOUR_API_KEY"}
```

响应中找到 `userID` (数字，如：`12345678`)

## ⚙️ 配置 MCP

编辑 `.opencode/mcp.json`:

```json
{
  "mcpServers": {
    "zotero": {
      "command": "npx",
      "args": ["-y", "@xevos117/mcp-zotero"],
      "env": {
        "ZOTERO_API_KEY": "你的密钥",
        "ZOTERO_USER_ID": "你的用户 ID",
        "UNPAYWALL_EMAIL": "your@email.com"
      }
    }
  }
}
```

## 🎯 可用的 Zotero 工具

| 工具 | 描述 |
|------|------|
| `search_library` | 搜索文献库 |
| `get_collections` | 获取所有分类 |
| `add_items_by_doi` | 通过 DOI 添加论文 |
| `get_item_fulltext` | 获取 PDF 全文 |
| `inject_citations` | Word 文档注入引用 |
| `find_and_attach_pdfs` | 批量查找 OA PDF |

## 🌸 茉莉花插件功能

茉莉花是 **Zotero 插件**，不是 MCP 服务器。在 Zotero 中直接使用：

- **右键 PDF** → 茉莉花抓取 → 抓取期刊元数据
- **小工具** → 在下载文件夹中查找附件
- **编辑器** → 首选项 → 茉莉花 → 配置

## 🧪 测试连接

重启 opencode 后，尝试：
- "搜索我的 Zotero 文献库中关于 AI 的论文"
- "获取分类 'Papers' 下的所有文献"
