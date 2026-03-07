# Cheatsheet — Dev Tier

**Cập nhật:** 2026-03-07 | Quick-reference card cho guide/dev/ (Modules 01–06)

> [!TIP]
> Cheatsheet này là bảng tra cứu nhanh — mỗi mục link về module gốc để đọc chi tiết.

---

## 1. CLI Commands — Top 20

| Command | Mô tả |
|---------|-------|
| `claude` | Interactive session |
| `claude "query"` | Session với initial prompt |
| `claude -p "query"` | Headless mode (print & exit) |
| `claude -c` | Tiếp tục conversation cuối |
| `claude -r "name"` | Resume session theo tên |
| `claude -w name` | Session trong git worktree riêng |
| `claude --model opus` | Chọn model (sonnet/opus/haiku) |
| `claude --remote "task"` | Tạo remote session (cloud) |
| `claude --teleport` | Resume cloud session về local |
| `claude --from-pr 123` | Resume session gắn với PR |
| `claude update` | Update Claude Code |
| `claude auth login` | Đăng nhập |
| `claude auth status` | Kiểm tra auth |
| `claude agents` | Liệt kê subagents |
| `claude mcp list` | Liệt kê MCP servers |
| `claude mcp add ...` | Thêm MCP server |
| `claude remote-control` | Bắt đầu Remote Control |
| `claude plugin install X` | Cài plugin |
| `claude plugin validate .` | Validate plugin structure |
| `claude mcp serve` | Chạy CC làm MCP server |

Xem chi tiết: [dev/02 — CLI Reference](../dev/02-cli-reference.md)

---

## 2. Slash Commands — Nhóm chức năng

### 2.1 Session

| Command | Mô tả |
|---------|-------|
| `/clear` | Reset context |
| `/compact [focus]` | Nén conversation |
| `/resume` | Resume session cũ |
| `/fork` | Fork session từ điểm hiện tại |
| `/rename name` | Đặt tên session |
| `/rewind` | Rewind code + conversation |
| `/export` | Xuất conversation ra text |

### 2.2 Model & Mode

| Command | Mô tả |
|---------|-------|
| `/model opus` | Chuyển model |
| `/fast on` | Toggle fast mode |
| `/plan` | Enter Plan Mode |
| `/sandbox` | Toggle sandbox mode |
| `/vim` | Toggle Vim editing |

### 2.3 Diagnostics

| Command | Mô tả |
|---------|-------|
| `/doctor` | Chẩn đoán cài đặt |
| `/cost` | Token usage |
| `/usage` | Plan limits & rate limits |
| `/context` | Visualize context usage |
| `/stats` | Daily usage, streaks |
| `/diff` | Interactive diff viewer |

### 2.4 Config & Tools

| Command | Mô tả |
|---------|-------|
| `/config` | Mở Settings |
| `/permissions` | Quản lý permissions |
| `/memory` | Edit CLAUDE.md, toggle auto-memory |
| `/hooks` | Quản lý hooks |
| `/agents` | Quản lý agents |
| `/mcp` | Quản lý MCP servers |
| `/plugin` | Plugin manager |
| `/ide` | Quản lý IDE integrations |

### 2.5 Actions

| Command | Mô tả |
|---------|-------|
| `/review` | Review PR (cần `gh`) |
| `/security-review` | Scan security vulnerabilities |
| `/remote-control` | Bắt đầu Remote Control |
| `/desktop` | Chuyển session sang Desktop app |
| `/install-github-app` | Setup GitHub Actions |

Xem chi tiết: [dev/02 — CLI Reference](../dev/02-cli-reference.md#23-slash-commands)

---

## 3. Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Cancel input/generation |
| `Ctrl+D` | Exit session |
| `Ctrl+L` | Clear screen |
| `Ctrl+R` | Reverse search history |
| `Ctrl+G` | Mở prompt trong text editor |
| `Ctrl+B` | Background running tasks |
| `Ctrl+F` (2x) | Kill background agents |
| `Ctrl+T` | Toggle task list |
| `Ctrl+V` | Paste image |
| `Esc+Esc` | Rewind / summarize |
| `Shift+Tab` | Chuyển permission mode |
| `Alt+P` | Đổi model (giữ prompt) |
| `Alt+T` | Toggle extended thinking |
| `\ + Enter` | Multiline input (mọi terminal) |

Xem chi tiết: [dev/02 — CLI Reference](../dev/02-cli-reference.md#24-keyboard-shortcuts)

---

## 4. Permission Modes

| Mode | Behavior |
|------|----------|
| `default` | Hỏi permission lần đầu mỗi tool |
| `acceptEdits` | Auto-accept file edits; hỏi trước commands |
| `plan` | Plan Mode — phân tích, không thực thi |
| `dontAsk` | Auto-deny trừ tools đã allow |
| `bypassPermissions` | Bỏ qua mọi prompts (isolated env only) |

### Permission rules — Copy-paste

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run *)",
      "Bash(git commit *)",
      "Edit(/docs/**)",
      "WebFetch(domain:example.com)"
    ],
    "deny": [
      "Bash(git push *)",
      "Bash(rm -rf *)"
    ]
  }
}
```

Xem chi tiết: [dev/01 — Setup](../dev/01-claude-code-setup.md#15-permission-system)

---

## 5. Settings & Config

### 5.1 Settings hierarchy (cao → thấp)

| Priority | Location | Sharing |
|:--------:|----------|---------|
| 1 | Managed (system path) | Org-wide |
| 2 | CLI arguments | Session |
| 3 | `.claude/settings.local.json` | Gitignored |
| 4 | `.claude/settings.json` | Git (team) |
| 5 | `~/.claude/settings.json` | Personal |

### 5.2 CLAUDE.md scopes

| Scope | Location | Priority |
|-------|----------|:--------:|
| Managed | System path | Cao nhất |
| Project | `.claude/CLAUDE.md` | ↑ |
| User | `~/.claude/CLAUDE.md` | ↓ |
| Local | `.claude/CLAUDE.local.md` | Thấp nhất |

**@imports syntax:**

```markdown
Xem @README cho project overview
Include @docs/git-instructions.md
```

### 5.3 Auto Memory

```text
~/.claude/projects/<project>/memory/
├── MEMORY.md          # 200 dòng đầu auto-load mỗi session
├── debugging.md       # Topic file — load on-demand
└── api-conventions.md
```

Toggle: `/memory` | Env: `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`

Xem chi tiết: [dev/01 — Setup](../dev/01-claude-code-setup.md)

---

## 6. Subagents — Quick Setup

### 6.1 File format

```yaml
---
name: code-reviewer
description: Reviews code for quality and security
tools: Read, Grep, Glob, Bash
model: inherit
maxTurns: 10
---

You are a senior code reviewer. When invoked:
1. Run git diff to see changes
2. Review for bugs, security, readability
3. Report: Critical → Warnings → Suggestions
```

Lưu tại: `.claude/agents/code-reviewer.md`

### 6.2 Frontmatter fields

| Field | Values | Default |
|-------|--------|---------|
| `name` | lowercase-dashes | (bắt buộc) |
| `description` | Mô tả ngắn | (bắt buộc) |
| `tools` | `Read, Grep, Glob, Bash` | Inherit all |
| `disallowedTools` | `Write, Edit` | None |
| `model` | `sonnet\|opus\|haiku\|inherit` | inherit |
| `permissionMode` | 5 modes | default |
| `maxTurns` | Number | — |
| `memory` | `user\|project\|local` | — |
| `background` | `true\|false` | false |
| `isolation` | `worktree` | — |
| `skills` | `[skill-1, skill-2]` | — |
| `mcpServers` | Server names/inline | — |

### 6.3 Agent scopes (priority cao → thấp)

| Location | Scope |
|----------|-------|
| `--agents '{json}'` (CLI) | Session |
| `.claude/agents/` | Project |
| `~/.claude/agents/` | User |
| Plugin `agents/` | Plugin |

### 6.4 Common patterns

| Pattern | Mô tả |
|---------|-------|
| Read-only researcher | `tools: Read, Grep, Glob` — chỉ đọc |
| Background worker | `background: true` — chạy nền |
| Isolated builder | `isolation: worktree` — worktree riêng |
| Quality gate | Hooks `PreToolUse` validate trước khi chạy |

Xem chi tiết: [dev/04 — Agents & Automation](../dev/04-agents-automation.md#41-subagents)

---

## 7. Agent Teams — Quick Setup

> [!WARNING]
> Agent Teams là tính năng EXPERIMENTAL — cần enable qua env var.

### 7.1 Enable

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### 7.2 Tạo team

```text
Create an agent team to refactor these modules in parallel.
Spawn 3 teammates: one for auth, one for database, one for API.
```

### 7.3 Điều khiển

| Action | Cách |
|--------|------|
| Cycle teammates | `Shift+Down` |
| Enter teammate | `Shift+Down` → `Enter` |
| Toggle task list | `Ctrl+T` |
| Shutdown 1 teammate | "Ask X teammate to shut down" |
| Cleanup toàn bộ | "Clean up the team" (từ lead) |

### 7.4 Best practices

```text
- 3–5 teammates tối ưu
- 5–6 tasks mỗi teammate
- Tránh file conflicts (file locking tự động)
- Shutdown teammates TRƯỚC cleanup từ lead
- Không hỗ trợ /resume, /rewind
```

[Nguồn: Claude Code Docs] [Cập nhật 03/2026]

Xem chi tiết: [dev/04 — Agents & Automation](../dev/04-agents-automation.md#42-agent-teams)

---

## 8. Git Workflows

### 8.1 Common commands

| Task | Prompt / Command |
|------|-----------------|
| Commit | `"create a commit for my changes"` |
| PR | `"create a pr for my changes"` |
| Merge conflicts | `"resolve merge conflicts in src/auth/login.ts"` |
| Worktree | `claude -w feature-auth` |
| Resume PR | `claude --from-pr 123` |

### 8.2 Scoped permissions cho git

```bash
claude -p "Look at staged changes and create commit" \
  --allowedTools "Bash(git diff *),Bash(git commit *)"
```

### 8.3 Worktrees

```bash
claude -w feature-auth    # Named worktree (.claude/worktrees/feature-auth)
claude -w                  # Auto-generate name
```

Xem chi tiết: [dev/06 — Dev Workflows](../dev/06-dev-workflows.md#61-git-workflows)

---

## 9. Plugin Commands

| Command | Mô tả |
|---------|-------|
| `/plugin` | Mở plugin manager (Discover/Installed/Errors) |
| `/plugin install X@marketplace` | Cài plugin |
| `/plugin uninstall X@marketplace` | Gỡ plugin |
| `/plugin disable X` | Tạm tắt |
| `/plugin enable X` | Bật lại |
| `/reload-plugins` | Reload không restart |
| `claude plugin validate .` | Validate structure |
| `claude --plugin-dir ./my-plugin` | Test local plugin |

### Plugin structure

```text
my-plugin/
├── .claude-plugin/
│   └── plugin.json      # Manifest (bắt buộc)
├── skills/              # Agent Skills
├── agents/              # Subagent definitions
├── hooks/               # Hook configs
├── .mcp.json            # MCP servers
└── settings.json        # Default settings
```

Xem chi tiết: [dev/05 — Plugins](../dev/05-plugins.md)

---

## 10. MCP Setup — Copy-paste

### 10.1 Thêm HTTP server

```bash
claude mcp add --transport http github https://api.githubcopilot.com/mcp/
```

### 10.2 Thêm Stdio server

```bash
claude mcp add --transport stdio airtable \
  --env AIRTABLE_API_KEY=YOUR_KEY \
  -- npx -y airtable-mcp-server
```

### 10.3 Windows (non-WSL)

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### 10.4 .mcp.json (project scope)

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    },
    "db": {
      "command": "npx",
      "args": ["-y", "@bytebase/dbhub", "--dsn", "postgresql://localhost:5432/dev"]
    }
  }
}
```

### 10.5 MCP scopes

| Scope | Location | Dùng khi |
|-------|----------|---------|
| `local` | `~/.claude.json` | Creds cá nhân (default) |
| `project` | `.mcp.json` | Team-shared |
| `user` | `~/.claude.json` | Personal, mọi projects |

Xem chi tiết: [dev/05 — Plugins](../dev/05-plugins.md#52-mcp)

---

## 11. IDE Integration

### 11.1 VS Code shortcuts

| Shortcut | Action |
|----------|--------|
| `Cmd/Ctrl+Shift+P` → "Claude Code" | Command Palette |
| `Cmd/Ctrl+Esc` | Focus input |
| `Cmd/Ctrl+Shift+Esc` | Mở trong tab mới |
| `Cmd/Ctrl+N` | New conversation |
| `Option/Alt+K` | Insert @-mention |

### 11.2 @-Mentions

```text
@auth                      # Fuzzy match files
@src/components/           # Trailing slash = folder
@terminal:dev-server       # Terminal output
@report.pdf pages 1-10    # PDF pages
```

### 11.3 VS Code modes

| Mode | Behavior |
|------|----------|
| Normal | Hỏi permissions (default) |
| Plan | Markdown review document |
| Auto-accept | Auto-accept edits, hỏi trước commands |

Xem chi tiết: [dev/03 — IDE Integration](../dev/03-ide-integration.md)

---

## 12. Debugging Checklist

| Bước | Hành động | Command |
|:----:|----------|---------|
| 1 | Chạy diagnostics | `/doctor` |
| 2 | Paste error + reproduction steps | Prompt trực tiếp |
| 3 | Screenshot/image | `Ctrl+V` paste hoặc drag & drop |
| 4 | Chrome debugging | `claude mcp add chrome-mcp -- npx @anthropic-ai/chrome-mcp` |
| 5 | Playwright testing | `claude mcp add playwright -- npx @anthropic-ai/playwright-mcp` |
| 6 | Sau 2 lần fail | `/clear` + rewrite prompt |
| 7 | Rewind nếu sai | `Esc+Esc` hoặc `/rewind` |

Xem chi tiết: [dev/06 — Dev Workflows](../dev/06-dev-workflows.md#64-debugging)

---

## 13. Environment Variables — Hay dùng

### 13.1 Authentication

```bash
ANTHROPIC_API_KEY              # API key
CLAUDE_CODE_USE_BEDROCK=1      # AWS Bedrock backend
CLAUDE_CODE_USE_VERTEX=1       # Google Vertex backend
```

### 13.2 Model & Output

```bash
CLAUDE_CODE_EFFORT_LEVEL=high           # low|medium|high
CLAUDE_CODE_MAX_OUTPUT_TOKENS=32000     # Max output tokens
CLAUDE_CODE_SUBAGENT_MODEL=haiku        # Model cho subagents
```

### 13.3 Feature toggles

```bash
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1              # Tắt auto memory
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1         # Bật Agent Teams
CLAUDE_CODE_DISABLE_FAST_MODE=1                # Tắt fast mode
CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1        # Tắt adaptive thinking
```

### 13.4 Bash & Execution

```bash
BASH_DEFAULT_TIMEOUT_MS=120000        # Default timeout (2 min)
BASH_MAX_TIMEOUT_MS=600000            # Max timeout (10 min)
CLAUDE_CODE_SHELL=bash                # Shell override
```

Xem chi tiết: [dev/02 — CLI Reference](../dev/02-cli-reference.md#26-environment-variables)

---

## 14. Headless Mode & CI/CD

### 14.1 Headless patterns

```bash
# Phân tích codebase
claude -p "list all API endpoints" --output-format json

# Pipe input
cat error.log | claude -p "explain root cause" > analysis.txt

# Structured output
claude -p "analyze code" --json-schema '{"type":"object","properties":{"bugs":{"type":"array"}}}'

# Giới hạn turns & budget
claude -p "fix tests" --max-turns 10 --max-budget-usd 5
```

### 14.2 GitHub Actions

```yaml
name: Claude Code
on:
  issue_comment:
    types: [created]
jobs:
  claude:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

Trigger: `@claude implement feature` trong issue/PR comment.

### 14.3 Fan-out pattern

```bash
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue" \
    --allowedTools "Edit,Bash(git commit *)"
done
```

Xem chi tiết: [dev/06 — Dev Workflows](../dev/06-dev-workflows.md#66-batch-operations)

---

## 15. Session Management

| Tình huống | Hành động |
|-----------|-----------|
| Chuyển task mới | `/clear` |
| Context đầy | `/compact` hoặc `/compact Focus on X` |
| Sau 2 lần fail | `/clear` + rewrite prompt |
| Thử approach khác | `claude -c --fork-session` |
| Đặt tên session | `/rename auth-refactor` |
| Rewind code + conversation | `Esc+Esc` |
| Resume session cũ | `claude -r` (interactive picker) |

### Session picker shortcuts

| Key | Function |
|-----|----------|
| `↑/↓` | Navigate |
| `Enter` | Resume |
| `P` | Preview |
| `R` | Rename |
| `/` | Search |
| `A` | Toggle dir / all projects |
| `B` | Filter by current branch |

Xem chi tiết: [dev/06 — Dev Workflows](../dev/06-dev-workflows.md#65-session-management)

---

## 16. Sandbox Mode

```text
/sandbox → Auto-allow (Bash auto-run) hoặc Regular permissions
```

### Filesystem & Network config

```json
{
  "sandbox": {
    "enabled": true,
    "filesystem": {
      "allowWrite": ["~/.kube", "//tmp/build"]
    },
    "network": {
      "allowedDomains": ["github.com", "*.npmjs.org"]
    }
  }
}
```

| Platform | Engine |
|----------|--------|
| macOS | Seatbelt (built-in) |
| Linux/WSL2 | bubblewrap (`apt install bubblewrap socat`) |
| Windows native | Planned |

Xem chi tiết: [dev/01 — Setup](../dev/01-claude-code-setup.md#17-sandbox-mode)

---

## Cross-references

- **Base tier cheatsheet:** [cheatsheet-base.md](cheatsheet-base.md)
- **Doc tier cheatsheet:** [cheatsheet-doc.md](cheatsheet-doc.md)
- **Skills guide:** [skills-guide.md](skills-guide.md)
- **Config architecture:** [config-architecture.md](config-architecture.md)
- **Model specs:** [model-specs.md](model-specs.md)
- **CLI setup chi tiết:** [dev/01](../dev/01-claude-code-setup.md)
- **CLI reference chi tiết:** [dev/02](../dev/02-cli-reference.md)
- **IDE integration:** [dev/03](../dev/03-ide-integration.md)
- **Agents & Automation:** [dev/04](../dev/04-agents-automation.md)
- **Plugins & MCP:** [dev/05](../dev/05-plugins.md)
- **Dev Workflows:** [dev/06](../dev/06-dev-workflows.md)
