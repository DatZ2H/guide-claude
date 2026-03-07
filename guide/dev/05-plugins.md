# Plugins & MCP Ecosystem

**Thời gian đọc:** 25 phút | **Mức độ:** Intermediate-Advanced
**Cập nhật:** 2026-03-07 | Models: xem [specs](../reference/model-specs.md)

---
depends-on: [dev/01-claude-code-setup, dev/02-cli-reference]
impacts: [dev/04-agents-automation, dev/06-dev-workflows]
---

Module này hướng dẫn hệ thống plugin của Claude Code — từ cài đặt plugin có sẵn đến tạo plugin riêng — và Model Context Protocol (MCP) để kết nối Claude Code với tools bên ngoài.

[Nguồn: Claude Code Docs — Plugins, MCP] [Cập nhật 03/2026]

---

## 5.1 Plugin là gì?

Plugin là package mở rộng Claude Code với skills, agents, hooks, MCP servers, và LSP servers. Plugin được phân phối qua marketplaces — catalog cho phép discover, install, và update tự động.

[Nguồn: Claude Code Docs — Discover and install plugins]

Hai cách tiếp cận mở rộng Claude Code:

| Cách | Skill names | Phù hợp khi |
|------|-------------|-------------|
| **Standalone** (`.claude/`) | `/hello` | Cá nhân, project-specific, thử nghiệm nhanh |
| **Plugin** (`.claude-plugin/plugin.json`) | `/plugin-name:hello` | Chia sẻ team, phân phối community, versioned releases |

> [!TIP]
> Bắt đầu với standalone trong `.claude/` để iterate nhanh, sau đó convert sang plugin khi cần chia sẻ.

---

## 5.2 Discover và install plugins

### /plugin command

Lệnh `/plugin` mở plugin manager với 4 tab:

| Tab | Chức năng |
|-----|-----------|
| **Discover** | Browse plugins từ marketplaces đã thêm |
| **Installed** | Xem, enable/disable, uninstall plugins |
| **Marketplaces** | Thêm, update, xóa marketplaces |
| **Errors** | Xem lỗi loading plugin |

Dùng **Tab** / **Shift+Tab** để chuyển tab.

[Nguồn: Claude Code Docs — Discover and install plugins]

### Official marketplace

Marketplace chính thức (`claude-plugins-official`) tự động có sẵn. Một số plugin phổ biến:

**Code intelligence (LSP):**

| Plugin | Language server | Binary cần cài |
|--------|----------------|-----------------|
| `pyright-lsp` | Pyright (Python) | `pyright-langserver` |
| `typescript-lsp` | TypeScript LS | `typescript-language-server` |
| `rust-analyzer-lsp` | rust-analyzer | `rust-analyzer` |
| `gopls-lsp` | gopls (Go) | `gopls` |

LSP plugins cho Claude khả năng **diagnostics tự động** (thấy lỗi ngay sau edit) và **code navigation** (go to definition, find references, hover info).

**External integrations:** GitHub, GitLab, Atlassian (Jira/Confluence), Slack, Sentry, Figma, Notion, Linear, Vercel, Firebase, Supabase.

**Development workflows:** `commit-commands` (git workflows), `pr-review-toolkit` (PR review agents), `plugin-dev` (toolkit tạo plugins).

[Nguồn: Claude Code Docs — Discover and install plugins] [Cập nhật 03/2026]

### Install plugin

```bash
# Install từ official marketplace
/plugin install plugin-name@claude-plugins-official

# Install với scope cụ thể
claude plugin install formatter@my-marketplace --scope project
```

### Plugin installation scopes

| Scope | Settings file | Phù hợp khi |
|-------|---------------|-------------|
| `user` | `~/.claude/settings.json` | Plugin cá nhân, dùng mọi project (default) |
| `project` | `.claude/settings.json` | Plugin team, shared qua version control |
| `local` | `.claude/settings.local.json` | Plugin project-specific, gitignored |
| `managed` | Managed settings | Plugin tổ chức (read-only) |

[Nguồn: Claude Code Docs — Plugins reference]

### Manage plugins

```bash
# Disable tạm thời (không uninstall)
/plugin disable plugin-name@marketplace-name

# Enable lại
/plugin enable plugin-name@marketplace-name

# Uninstall hoàn toàn
/plugin uninstall plugin-name@marketplace-name

# Reload plugins không cần restart
/reload-plugins
```

---

## 5.3 Marketplaces

Marketplace là catalog chứa plugins. Quy trình: thêm marketplace → browse → install plugins.

[Nguồn: Claude Code Docs — Plugin marketplaces]

### Thêm marketplace

```bash
# Từ GitHub repo
/plugin marketplace add owner/repo

# Từ Git URL (GitLab, Bitbucket...)
/plugin marketplace add https://gitlab.com/company/plugins.git

# Từ branch/tag cụ thể
/plugin marketplace add https://gitlab.com/company/plugins.git#v1.0.0

# Từ local path
/plugin marketplace add ./my-marketplace
```

### Quản lý marketplace

```bash
# Liệt kê marketplaces
/plugin marketplace list

# Update để fetch plugins mới nhất
/plugin marketplace update marketplace-name

# Xóa marketplace (sẽ uninstall plugins từ đó)
/plugin marketplace remove marketplace-name
```

### Team marketplace

Cấu hình `.claude/settings.json` để team tự động được prompt cài marketplace:

```json
{
  "extraKnownMarketplaces": {
    "company-tools": {
      "source": {
        "source": "github",
        "repo": "your-org/claude-plugins"
      }
    }
  },
  "enabledPlugins": {
    "code-formatter@company-tools": true
  }
}
```

[Nguồn: Claude Code Docs — Discover and install plugins]

---

## 5.4 Tạo plugin

### Plugin structure

```text
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Manifest (metadata)
├── commands/                # Skill markdown files (legacy)
├── skills/                  # Agent Skills (SKILL.md)
│   └── code-review/
│       └── SKILL.md
├── agents/                  # Subagent definitions
├── hooks/
│   └── hooks.json           # Hook configurations
├── .mcp.json                # MCP server definitions
├── .lsp.json                # LSP server configurations
├── settings.json            # Default settings
└── scripts/                 # Hook scripts
```

> [!WARNING]
> Chỉ `plugin.json` đặt trong `.claude-plugin/`. Mọi thư mục khác (commands/, agents/, skills/, hooks/) phải ở plugin root.

[Nguồn: Claude Code Docs — Plugins reference]

### Plugin manifest (plugin.json)

```json
{
  "name": "my-plugin",
  "description": "Mô tả ngắn gọn",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  },
  "homepage": "https://docs.example.com",
  "repository": "https://github.com/user/plugin",
  "license": "MIT",
  "keywords": ["keyword1", "keyword2"]
}
```

`name` là field duy nhất bắt buộc — dùng làm namespace cho skills (vd: `/my-plugin:hello`).

### Quickstart: tạo plugin đầu tiên

```bash
# 1. Tạo thư mục
mkdir -p my-plugin/.claude-plugin
mkdir -p my-plugin/skills/hello

# 2. Tạo manifest
cat > my-plugin/.claude-plugin/plugin.json << 'EOF'
{
  "name": "my-plugin",
  "description": "A greeting plugin",
  "version": "1.0.0"
}
EOF

# 3. Tạo skill
cat > my-plugin/skills/hello/SKILL.md << 'EOF'
---
description: Greet the user with a friendly message
---

Greet the user named "$ARGUMENTS" warmly.
EOF

# 4. Test locally
claude --plugin-dir ./my-plugin
```

Sau khi start, gõ `/my-plugin:hello Alex` để test.

[Nguồn: Claude Code Docs — Create plugins]

### Plugin components

**Skills** — Agent Skills với `SKILL.md`, Claude tự invoke theo context:

```yaml
---
name: code-review
description: Reviews code for best practices and potential issues
---

When reviewing code, check for:
1. Code organization and structure
2. Error handling
3. Security concerns
```

**Agents** — Subagents chuyên biệt trong `agents/`:

```yaml
---
name: security-reviewer
description: Specialized in security code review
---

Detailed system prompt for the agent...
```

**Hooks** — Event handlers trong `hooks/hooks.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format-code.sh"
          }
        ]
      }
    ]
  }
}
```

Hook events: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `UserPromptSubmit`, `SessionStart`, `SessionEnd`, `SubagentStart`, `SubagentStop`, `TeammateIdle`, `TaskCompleted`, `PreCompact`, và nhiều hơn.

Hook types: `command` (shell), `prompt` (LLM eval), `agent` (agentic verifier).

**LSP servers** — Code intelligence trong `.lsp.json`:

```json
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": {
      ".go": "go"
    }
  }
}
```

**Default settings** — `settings.json` tại plugin root, hiện chỉ hỗ trợ key `agent`:

```json
{
  "agent": "security-reviewer"
}
```

[Nguồn: Claude Code Docs — Plugins reference]

### Environment variable

`${CLAUDE_PLUGIN_ROOT}` — absolute path đến thư mục plugin. Dùng trong hooks, MCP servers, scripts để đảm bảo paths đúng bất kể vị trí cài đặt.

### Test và debug

```bash
# Test local plugin
claude --plugin-dir ./my-plugin

# Load nhiều plugins
claude --plugin-dir ./plugin-one --plugin-dir ./plugin-two

# Debug mode — xem chi tiết loading
claude --debug

# Validate plugin
claude plugin validate .
```

### Phân phối plugin

1. Publish lên marketplace (xem [5.3](#53-marketplaces))
2. Submit lên official marketplace tại [claude.ai/settings/plugins/submit](https://claude.ai/settings/plugins/submit) hoặc [platform.claude.com/plugins/submit](https://platform.claude.com/plugins/submit)
3. Versioning: semantic versioning (`MAJOR.MINOR.PATCH`) trong `plugin.json`

[Nguồn: Claude Code Docs — Plugin marketplaces]

---

## 5.5 MCP (Model Context Protocol)

MCP là giao thức mở cho phép Claude Code kết nối với tools, databases, và APIs bên ngoài. MCP servers cung cấp tools mà Claude có thể gọi trực tiếp trong conversation.

[Nguồn: Claude Code Docs — MCP]

### Ví dụ khả năng với MCP

- Implement features từ issue trackers: "Thêm feature mô tả trong JIRA issue ENG-4521 và tạo PR trên GitHub."
- Query databases: "Tìm 10 users gần nhất dùng feature X từ PostgreSQL."
- Monitor errors: "Check Sentry xem lỗi phổ biến nhất 24h qua."
- Automate workflows: "Tạo Gmail drafts mời 10 users vào feedback session."

### Cài đặt MCP servers

Ba loại transport:

**HTTP (khuyến nghị cho remote servers):**

```bash
# Thêm remote HTTP server
claude mcp add --transport http notion https://mcp.notion.com/mcp

# Với authentication header
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

**SSE (deprecated — dùng HTTP thay thế):**

```bash
claude mcp add --transport sse asana https://mcp.asana.com/sse
```

**Stdio (local processes):**

```bash
# Local MCP server
claude mcp add --transport stdio --env AIRTABLE_API_KEY=YOUR_KEY airtable \
  -- npx -y airtable-mcp-server
```

> [!WARNING]
> Trên Windows (không phải WSL), local MCP servers dùng `npx` cần wrapper `cmd /c`:
> ```bash
> claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
> ```

[Nguồn: Claude Code Docs — MCP] [Cập nhật 03/2026]

### MCP scopes

| Scope | Lưu tại | Phù hợp khi |
|-------|---------|-------------|
| `local` (default) | `~/.claude.json` | Server cá nhân, credentials nhạy cảm |
| `project` | `.mcp.json` (root project) | Team-shared, checked vào version control |
| `user` | `~/.claude.json` | Server dùng xuyên projects |

```bash
# Project scope — team shared
claude mcp add --transport http paypal --scope project https://mcp.paypal.com/mcp

# User scope — cá nhân, mọi project
claude mcp add --transport http hubspot --scope user https://mcp.hubspot.com/anthropic
```

### .mcp.json format

File `.mcp.json` tại project root (project scope) cho phép team dùng chung config:

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    },
    "db": {
      "command": "npx",
      "args": ["-y", "@bytebase/dbhub", "--dsn", "${DB_DSN:-postgresql://localhost:5432/dev}"],
      "env": {}
    }
  }
}
```

Hỗ trợ environment variable expansion: `${VAR}` và `${VAR:-default}`.

[Nguồn: Claude Code Docs — MCP]

### Quản lý MCP servers

```bash
# Liệt kê servers
claude mcp list

# Chi tiết server
claude mcp get github

# Xóa server
claude mcp remove github

# Kiểm tra status trong Claude Code
/mcp

# Import từ Claude Desktop
claude mcp add-from-claude-desktop

# Thêm từ JSON config
claude mcp add-json weather '{"type":"http","url":"https://api.weather.com/mcp"}'
```

### OAuth authentication

Nhiều remote MCP servers yêu cầu OAuth 2.0:

```bash
# 1. Thêm server
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp

# 2. Authenticate trong Claude Code
/mcp
# → Chọn server → Follow browser login flow
```

Với pre-configured OAuth credentials:

```bash
claude mcp add --transport http \
  --client-id your-client-id --client-secret --callback-port 8080 \
  my-server https://mcp.example.com/mcp
```

[Nguồn: Claude Code Docs — MCP]

### MCP resources và prompts

**Resources** — dữ liệu từ MCP servers, reference qua `@` mentions:

```text
Can you analyze @github:issue://123 and suggest a fix?
Compare @postgres:schema://users with @docs:file://database/user-model
```

**Prompts** — MCP servers expose prompts thành commands:

```text
/mcp__github__list_prs
/mcp__github__pr_review 456
```

### Plugin-provided MCP servers

Plugins có thể bundle MCP servers trong `.mcp.json` tại plugin root:

```json
{
  "mcpServers": {
    "plugin-db": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"]
    }
  }
}
```

Khi plugin enabled, MCP servers tự start. Xem trong `/mcp` — plugin servers hiển thị với indicator nguồn.

[Nguồn: Claude Code Docs — MCP]

### Claude Code as MCP server

Claude Code có thể hoạt động như MCP server cho ứng dụng khác:

```bash
claude mcp serve
```

Config cho Claude Desktop:

```json
{
  "mcpServers": {
    "claude-code": {
      "type": "stdio",
      "command": "claude",
      "args": ["mcp", "serve"],
      "env": {}
    }
  }
}
```

---

## 5.6 MCP Tool Search

Khi có nhiều MCP servers, tool definitions chiếm nhiều context window. Tool Search tự động bật khi MCP tools vượt 10% context — load tools on-demand thay vì preload tất cả.

[Nguồn: Claude Code Docs — MCP]

Cấu hình qua `ENABLE_TOOL_SEARCH`:

| Giá trị | Hành vi |
|---------|---------|
| `auto` (default) | Bật khi MCP tools > 10% context |
| `auto:<N>` | Custom threshold (vd: `auto:5` = 5%) |
| `true` | Luôn bật |
| `false` | Tắt, load tất cả MCP tools |

```bash
ENABLE_TOOL_SEARCH=auto:5 claude
```

> [!NOTE]
> Yêu cầu Sonnet 4+ hoặc Opus 4+. Haiku không hỗ trợ Tool Search.

---

## 5.7 MCP output limits

Claude Code cảnh báo khi MCP tool output vượt 10,000 tokens. Default max: 25,000 tokens.

```bash
# Tăng limit
export MAX_MCP_OUTPUT_TOKENS=50000
claude
```

Hữu ích khi MCP servers query large datasets, generate reports, hoặc process log files.

---

## 5.8 Managed MCP (cho tổ chức)

Hai option quản lý MCP cho enterprise:

**Option 1 — Exclusive control (`managed-mcp.json`):**

Deploy file tại system path — users không thể thêm/sửa MCP servers khác:

- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux/WSL: `/etc/claude-code/managed-mcp.json`
- Windows: `C:\Program Files\ClaudeCode\managed-mcp.json`

**Option 2 — Policy-based (allowlists/denylists):**

Trong managed settings, dùng `allowedMcpServers` và `deniedMcpServers` để restrict servers theo name, command, hoặc URL pattern:

```json
{
  "allowedMcpServers": [
    { "serverName": "github" },
    { "serverUrl": "https://mcp.company.com/*" },
    { "serverCommand": ["npx", "-y", "@company/approved-server"] }
  ],
  "deniedMcpServers": [
    { "serverUrl": "https://*.untrusted.com/*" }
  ]
}
```

Denylist luôn ưu tiên — server bị deny sẽ bị block dù có trong allowlist.

[Nguồn: Claude Code Docs — MCP] [Cập nhật 03/2026]

---

## 5.9 Troubleshooting

### Plugin issues

| Vấn đề | Nguyên nhân | Giải pháp |
|---------|-------------|-----------|
| `/plugin` không nhận | Version cũ | `claude --version` — cần ≥ 1.0.33 |
| Plugin không load | `plugin.json` lỗi | `claude plugin validate .` hoặc `/plugin validate` |
| Commands không hiện | Sai directory structure | Components phải ở plugin root, không trong `.claude-plugin/` |
| Hooks không fire | Script không executable | `chmod +x script.sh` |
| Skills không hiện | Cache cũ | `rm -rf ~/.claude/plugins/cache`, restart, reinstall |

### MCP issues

| Vấn đề | Nguyên nhân | Giải pháp |
|---------|-------------|-----------|
| Connection closed (Windows) | Thiếu `cmd /c` wrapper | `-- cmd /c npx -y @package` |
| Server không start | Command không tìm thấy | Verify binary trong `$PATH` |
| Tools không hiện | Config sai | Kiểm tra `.mcp.json` format |
| OAuth fail | Token hết hạn | `/mcp` → Clear authentication → re-login |
| Output bị cắt | Vượt token limit | `MAX_MCP_OUTPUT_TOKENS=50000` |

### Debug workflow

```bash
# 1. Kiểm tra plugin loading
claude --debug

# 2. Kiểm tra MCP server status
/mcp

# 3. Validate plugin structure
/plugin validate .

# 4. Xem errors tab
/plugin  # → Tab Errors
```

[Nguồn: Claude Code Docs — Plugins reference]

---

## 5.10 Tổng hợp lệnh

### Plugin CLI commands

| Lệnh | Mô tả |
|-------|--------|
| `claude plugin install <plugin> [-s scope]` | Install plugin |
| `claude plugin uninstall <plugin> [-s scope]` | Uninstall plugin |
| `claude plugin enable <plugin> [-s scope]` | Enable plugin |
| `claude plugin disable <plugin> [-s scope]` | Disable plugin |
| `claude plugin update <plugin> [-s scope]` | Update plugin |
| `claude plugin validate .` | Validate plugin structure |

### MCP CLI commands

| Lệnh | Mô tả |
|-------|--------|
| `claude mcp add --transport <type> <name> <url>` | Thêm remote server |
| `claude mcp add --transport stdio <name> -- <cmd>` | Thêm local server |
| `claude mcp add-json <name> '<json>'` | Thêm từ JSON config |
| `claude mcp add-from-claude-desktop` | Import từ Desktop |
| `claude mcp list` | Liệt kê servers |
| `claude mcp get <name>` | Chi tiết server |
| `claude mcp remove <name>` | Xóa server |
| `claude mcp reset-project-choices` | Reset project MCP approvals |
| `claude mcp serve` | Chạy Claude Code as MCP server |

### Slash commands (trong Claude Code)

| Lệnh | Mô tả |
|-------|--------|
| `/plugin` | Mở plugin manager (4 tabs) |
| `/plugin install <name>@<marketplace>` | Install plugin |
| `/plugin marketplace add <source>` | Thêm marketplace |
| `/reload-plugins` | Reload plugins không restart |
| `/mcp` | Xem MCP server status + authenticate |

---

← [Agents & Automation](04-agents-automation.md) | [Tổng quan](../base/00-overview.md) | [Dev Workflows →](06-dev-workflows.md)
