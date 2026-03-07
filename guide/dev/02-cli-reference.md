# Claude Code — CLI Reference

**Thời gian đọc:** 30 phút | **Mức độ:** Intermediate-Advanced
**Cập nhật:** 2026-03-07 | Models: xem [specs](../reference/model-specs.md)

---
depends-on: [dev/01-claude-code-setup, base/03-prompt-engineering]
impacts: [dev/03-ide-integration, dev/04-agents-automation, dev/06-dev-workflows]
---

Tham chiếu đầy đủ cho Claude Code CLI — commands, flags, slash commands, keyboard shortcuts, input modes, environment variables, và output formats. Dùng như lookup table khi cần tra cứu nhanh.

[Nguồn: Claude Code Docs — CLI Reference, Interactive Mode] [Cập nhật 03/2026]

---

## 2.1 CLI Commands

Các lệnh chính để khởi chạy, tiếp tục, và quản lý Claude Code sessions.

[Nguồn: Claude Code Docs — CLI Reference]

| Command | Mô tả | Ví dụ |
|---------|--------|-------|
| `claude` | Bắt đầu interactive session | `claude` |
| `claude "query"` | Session mới với prompt ban đầu | `claude "explain this project"` |
| `claude -p "query"` | Print mode — trả lời rồi thoát (không interactive) | `claude -p "explain this function"` |
| `cat file \| claude -p "query"` | Xử lý piped content | `cat logs.txt \| claude -p "explain"` |
| `claude -c` | Tiếp tục conversation gần nhất trong thư mục hiện tại | `claude -c` |
| `claude -c -p "query"` | Tiếp tục conversation qua SDK (print mode) | `claude -c -p "Check for type errors"` |
| `claude -r "session" "query"` | Resume session theo ID hoặc tên | `claude -r "auth-refactor" "Finish this PR"` |
| `claude update` | Cập nhật lên version mới nhất | `claude update` |
| `claude auth login` | Đăng nhập. `--email` pre-fill email, `--sso` force SSO | `claude auth login --email user@example.com` |
| `claude auth logout` | Đăng xuất | `claude auth logout` |
| `claude auth status` | Trạng thái auth (JSON). `--text` cho human-readable | `claude auth status --text` |
| `claude agents` | Liệt kê subagents theo source | `claude agents` |
| `claude mcp` | Cấu hình MCP servers | Xem [dev/05](05-plugins.md) |
| `claude remote-control` | Bắt đầu Remote Control session | `claude remote-control` |

---

## 2.2 CLI Flags

Flags tùy chỉnh behavior khi khởi chạy Claude Code. Danh sách đầy đủ theo nhóm chức năng.

[Nguồn: Claude Code Docs — CLI Reference]

### Session & Conversation

| Flag | Mô tả |
|------|--------|
| `--continue`, `-c` | Load conversation gần nhất trong thư mục hiện tại |
| `--resume`, `-r` | Resume session theo ID hoặc tên, hoặc mở picker |
| `--fork-session` | Khi resume, tạo session ID mới thay vì dùng lại (kết hợp `--resume`/`--continue`) |
| `--from-pr` | Resume sessions linked với GitHub PR. Nhận PR number hoặc URL |
| `--session-id` | Dùng session ID cụ thể (phải là valid UUID) |
| `--no-session-persistence` | Không lưu session — không thể resume (print mode only) |

### Model & Output

| Flag | Mô tả |
|------|--------|
| `--model` | Chọn model: `sonnet`, `opus`, hoặc full name (`claude-sonnet-4-6`) |
| `--fallback-model` | Fallback model khi model chính bị overloaded (print mode only) |
| `--print`, `-p` | Print mode — trả lời rồi thoát, không interactive |
| `--output-format` | Format output cho print mode: `text`, `json`, `stream-json` |
| `--input-format` | Format input cho print mode: `text`, `stream-json` |
| `--json-schema` | Validated JSON output theo JSON Schema (print mode only) |
| `--include-partial-messages` | Include partial streaming events (cần `--print` + `--output-format stream-json`) |
| `--verbose` | Verbose logging — hiển thị full turn-by-turn output |
| `--version`, `-v` | In version number |
| `--max-turns` | Giới hạn số agentic turns (print mode only). Không giới hạn mặc định |
| `--max-budget-usd` | Giới hạn chi phí API (print mode only) |

### System Prompt

| Flag | Mô tả |
|------|--------|
| `--system-prompt` | **Thay thế** toàn bộ system prompt mặc định |
| `--system-prompt-file` | **Thay thế** bằng nội dung file |
| `--append-system-prompt` | **Thêm** vào cuối system prompt mặc định (an toàn nhất) |
| `--append-system-prompt-file` | **Thêm** nội dung file vào cuối system prompt |

`--system-prompt` và `--system-prompt-file` loại trừ nhau. Các `--append-*` flags có thể kết hợp với flag thay thế.

> [!TIP]
> Hầu hết trường hợp nên dùng `--append-system-prompt` — giữ lại default capabilities của Claude Code trong khi thêm instructions riêng.

### Permissions & Security

| Flag | Mô tả |
|------|--------|
| `--permission-mode` | Bắt đầu với permission mode cụ thể (`default`, `acceptEdits`, `plan`, `dontAsk`, `bypassPermissions`) |
| `--allowedTools` | Tools tự động chạy không cần approval. Xem [permission rule syntax](01-claude-code-setup.md#15-permission-system) |
| `--disallowedTools` | Tools bị loại khỏi context — không thể sử dụng |
| `--dangerously-skip-permissions` | Bỏ qua mọi permission prompts |
| `--allow-dangerously-skip-permissions` | Cho phép bypass nhưng không kích hoạt ngay (kết hợp với `--permission-mode`) |
| `--permission-prompt-tool` | MCP tool xử lý permission prompts ở non-interactive mode |
| `--tools` | Giới hạn built-in tools: `""` (tắt hết), `"default"` (tất cả), hoặc danh sách `"Bash,Edit,Read"` |

### Agents & Subagents

| Flag | Mô tả |
|------|--------|
| `--agent` | Chọn agent cho session (override setting `agent`) |
| `--agents` | Định nghĩa subagents động qua JSON. Xem [dev/04](04-agents-automation.md) |
| `--teammate-mode` | Chế độ hiển thị Agent Teams: `auto`, `in-process`, `tmux` |

**`--agents` JSON format:**

```json
{
  "reviewer": {
    "description": "Expert code reviewer",
    "prompt": "You are a senior code reviewer...",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet",
    "maxTurns": 10
  }
}
```

Các fields: `description` (bắt buộc), `prompt` (bắt buộc), `tools`, `disallowedTools`, `model` (`sonnet`/`opus`/`haiku`/`inherit`), `skills`, `mcpServers`, `maxTurns`.

### Working Directory & Files

| Flag | Mô tả |
|------|--------|
| `--add-dir` | Thêm working directories (validate mỗi path) |
| `--worktree`, `-w` | Chạy trong isolated git worktree tại `<repo>/.claude/worktrees/<name>` |

### MCP & Plugins

| Flag | Mô tả |
|------|--------|
| `--mcp-config` | Load MCP servers từ JSON file hoặc string |
| `--strict-mcp-config` | Chỉ dùng MCP servers từ `--mcp-config`, bỏ qua config khác |
| `--plugin-dir` | Load plugins từ directories (repeatable) |
| `--chrome` / `--no-chrome` | Bật/tắt Chrome browser integration |

### Settings & Debug

| Flag | Mô tả |
|------|--------|
| `--settings` | Path đến settings JSON file hoặc JSON string |
| `--setting-sources` | Comma-separated sources: `user`, `project`, `local` |
| `--betas` | Beta headers cho API requests (API key users only) |
| `--debug` | Debug mode. Filter theo category: `"api,hooks"`, `"!statsig,!file"` |
| `--disable-slash-commands` | Tắt tất cả skills và commands cho session |

### Remote & Web

| Flag | Mô tả |
|------|--------|
| `--remote` | Tạo web session mới trên claude.ai với task description |
| `--teleport` | Resume web session trong local terminal |
| `--ide` | Tự động connect IDE khi startup |

### Initialization

| Flag | Mô tả |
|------|--------|
| `--init` | Chạy initialization hooks rồi vào interactive mode |
| `--init-only` | Chạy initialization hooks rồi thoát |
| `--maintenance` | Chạy maintenance hooks rồi thoát |

---

## 2.3 Slash Commands

Gõ `/` trong session để xem danh sách, hoặc `/` + ký tự để filter. Một số commands phụ thuộc platform, plan, hoặc environment.

[Nguồn: Claude Code Docs — Interactive Mode]

### Session Management

| Command | Mô tả |
|---------|--------|
| `/clear` | Xóa conversation history, giải phóng context. Aliases: `/reset`, `/new` |
| `/compact [instructions]` | Compact conversation với optional focus instructions |
| `/resume [session]` | Resume conversation theo ID/tên hoặc mở picker. Alias: `/continue` |
| `/fork [name]` | Fork conversation tại điểm hiện tại |
| `/rename [name]` | Đổi tên session. Không có name → auto-generate |
| `/rewind` | Rewind conversation và/hoặc code. Alias: `/checkpoint` |
| `/exit` | Thoát CLI. Alias: `/quit` |

### Model & Mode

| Command | Mô tả |
|---------|--------|
| `/model [model]` | Chọn/đổi model. Left/right arrows để adjust effort level |
| `/fast [on\|off]` | Toggle fast mode |
| `/plan` | Vào Plan Mode từ prompt |
| `/vim` | Toggle Vim / Normal editing mode |
| `/sandbox` | Toggle sandbox mode |

### Information & Diagnostics

| Command | Mô tả |
|---------|--------|
| `/help` | Hiển thị help và available commands |
| `/cost` | Thống kê token usage |
| `/usage` | Plan usage limits và rate limit status |
| `/context` | Visualize context usage dạng colored grid |
| `/diff` | Interactive diff viewer — uncommitted changes và per-turn diffs |
| `/doctor` | Chẩn đoán và verify installation |
| `/status` | Settings interface (Status tab): version, model, account, connectivity |
| `/stats` | Visualize daily usage, session history, streaks, model preferences |
| `/release-notes` | Xem changelog đầy đủ |
| `/insights` | Phân tích sessions: project areas, patterns, friction points |

### Configuration

| Command | Mô tả |
|---------|--------|
| `/config` | Mở Settings interface. Alias: `/settings` |
| `/permissions` | Xem/update permissions. Alias: `/allowed-tools` |
| `/memory` | Edit CLAUDE.md, toggle auto-memory, xem memory entries |
| `/hooks` | Quản lý hook configurations |
| `/keybindings` | Mở/tạo keybindings config file |
| `/theme` | Đổi color theme (light, dark, daltonized, ANSI) |
| `/statusline` | Cấu hình status line |
| `/terminal-setup` | Cấu hình terminal keybindings (Shift+Enter...) |
| `/output-style [style]` | Đổi output style: Default, Explanatory, Learning, hoặc custom |
| `/extra-usage` | Cấu hình extra usage khi hết rate limit |
| `/privacy-settings` | Privacy settings (Pro/Max only) |

### Tools & Integrations

| Command | Mô tả |
|---------|--------|
| `/agents` | Quản lý agent configurations |
| `/mcp` | Quản lý MCP server connections và OAuth |
| `/chrome` | Cấu hình Chrome integration |
| `/ide` | Quản lý IDE integrations |
| `/plugin` | Quản lý plugins |
| `/reload-plugins` | Reload active plugins để apply pending changes |
| `/skills` | Liệt kê available skills |
| `/tasks` | Liệt kê và quản lý background tasks |

### Actions

| Command | Mô tả |
|---------|--------|
| `/init` | Khởi tạo project với CLAUDE.md |
| `/add-dir <path>` | Thêm working directory vào session |
| `/copy` | Copy response gần nhất vào clipboard. Nếu có code blocks → picker |
| `/export [filename]` | Export conversation ra plain text |
| `/review` | Review PR: code quality, security, test coverage. Cần `gh` CLI |
| `/security-review` | Phân tích changes trên branch hiện tại tìm security vulnerabilities |
| `/pr-comments [PR]` | Fetch comments từ GitHub PR. Cần `gh` CLI |
| `/feedback [report]` | Gửi feedback. Alias: `/bug` |

### Remote & Cross-surface

| Command | Mô tả |
|---------|--------|
| `/remote-control` | Bắt đầu Remote Control từ claude.ai. Alias: `/rc` |
| `/remote-env` | Cấu hình default remote environment cho teleport |
| `/desktop` | Chuyển session sang Desktop app. Alias: `/app` |
| `/mobile` | QR code download Claude mobile app. Aliases: `/ios`, `/android` |
| `/install-github-app` | Setup Claude GitHub Actions |
| `/install-slack-app` | Install Claude Slack app |

### Account

| Command | Mô tả |
|---------|--------|
| `/login` | Đăng nhập |
| `/logout` | Đăng xuất |
| `/upgrade` | Mở trang upgrade plan |
| `/passes` | Chia sẻ free week (nếu eligible) |
| `/stickers` | Order Claude Code stickers |

### MCP Prompts

MCP servers có thể expose prompts dạng commands với format `/mcp__<server>__<prompt>`. Được auto-discover từ connected servers.

---

## 2.4 Keyboard Shortcuts

Shortcuts có thể khác theo platform và terminal. Nhấn `?` để xem shortcuts cho environment hiện tại.

[Nguồn: Claude Code Docs — Interactive Mode]

> [!NOTE]
> **macOS users:** Option/Alt key shortcuts yêu cầu cấu hình Option as Meta trong terminal. iTerm2: Settings > Profiles > Keys > "Esc+". Terminal.app: Settings > Profiles > Keyboard > "Use Option as Meta Key". Chạy `/terminal-setup` để cài thêm bindings.

### General Controls

| Shortcut | Mô tả |
|----------|--------|
| `Ctrl+C` | Hủy input hoặc generation hiện tại |
| `Ctrl+D` | Thoát Claude Code session |
| `Ctrl+L` | Xóa terminal screen (giữ conversation history) |
| `Ctrl+O` | Toggle verbose output |
| `Ctrl+R` | Reverse search command history |
| `Ctrl+G` | Mở prompt trong text editor mặc định |
| `Ctrl+B` | Background running tasks. Tmux users: nhấn 2 lần |
| `Ctrl+F` | Kill tất cả background agents. Nhấn 2 lần trong 3s để confirm |
| `Ctrl+T` | Toggle task list trong terminal status area |
| `Ctrl+V` / `Cmd+V` (iTerm2) / `Alt+V` (Windows) | Paste image từ clipboard |
| `Esc` + `Esc` | Rewind hoặc summarize |
| `Shift+Tab` hoặc `Alt+M` | Toggle permission modes (Auto-Accept, Plan, Normal) |
| `Alt+P` (Windows/Linux) / `Option+P` (macOS) | Đổi model mà không xóa prompt |
| `Alt+T` (Windows/Linux) / `Option+T` (macOS) | Toggle extended thinking. Chạy `/terminal-setup` trước |
| `Up/Down arrows` | Điều hướng command history |
| `Left/Right arrows` | Cycle qua dialog tabs (permission dialogs, menus) |

### Text Editing

| Shortcut | Mô tả |
|----------|--------|
| `Ctrl+K` | Xóa đến cuối dòng (lưu text đã xóa) |
| `Ctrl+U` | Xóa toàn bộ dòng (lưu text đã xóa) |
| `Ctrl+Y` | Paste text đã xóa bằng `Ctrl+K`/`Ctrl+U` |
| `Alt+Y` (sau `Ctrl+Y`) | Cycle qua paste history |
| `Alt+B` | Di chuyển cursor lùi 1 word |
| `Alt+F` | Di chuyển cursor tới 1 word |

### Multiline Input

| Phương thức | Shortcut |
|-------------|----------|
| Quick escape | `\` + `Enter` (mọi terminal) |
| macOS default | `Option+Enter` |
| Shift+Enter | `Shift+Enter` (iTerm2, WezTerm, Ghostty, Kitty — không cần config) |
| Control sequence | `Ctrl+J` |
| Paste mode | Paste trực tiếp (cho code blocks, logs) |

> [!TIP]
> Terminals khác (VS Code, Alacritty, Zed, Warp) cần chạy `/terminal-setup` để cài `Shift+Enter` binding.

---

## 2.5 Input Modes

Claude Code hỗ trợ nhiều cách nhập input ngoài gõ text thông thường.

[Nguồn: Claude Code Docs — Interactive Mode]

### Bash Mode (`!`)

Gõ `!` ở đầu dòng để chạy bash command trực tiếp — không qua Claude:

```bash
! npm test
! git status
! ls -la
```

- Output được thêm vào conversation context
- Hỗ trợ `Ctrl+B` backgrounding
- History-based autocomplete: gõ partial command + `Tab`
- Thoát bằng `Escape`, `Backspace`, hoặc `Ctrl+U` trên prompt trống

### File Mentions (`@`)

Gõ `@` để trigger file path autocomplete. File được thêm vào context:

```text
@src/api/routes.ts — xem file này có bug gì không
```

### Reverse Search (`Ctrl+R`)

1. Nhấn `Ctrl+R` để bắt đầu search
2. Gõ query — search term được highlight trong kết quả
3. `Ctrl+R` lần nữa → cycle qua older matches
4. `Tab`/`Esc` → accept match và tiếp tục edit
5. `Enter` → accept và execute ngay
6. `Ctrl+C` → cancel, khôi phục input gốc

### Prompt Suggestions

Khi mở session, Claude Code hiển thị gợi ý prompt dựa trên git history. Sau mỗi response, gợi ý tiếp dựa trên conversation:

- `Tab` → accept suggestion
- `Enter` → accept và submit
- Bắt đầu gõ → dismiss

Tắt: `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false` hoặc toggle trong `/config`.

---

## 2.6 Vim Mode

Bật vim-style editing bằng `/vim` hoặc cấu hình vĩnh viễn qua `/config`.

[Nguồn: Claude Code Docs — Interactive Mode]

### Mode Switching

| Command | Action | Từ mode |
|---------|--------|---------|
| `Esc` | Vào NORMAL mode | INSERT |
| `i` | Insert trước cursor | NORMAL |
| `I` | Insert đầu dòng | NORMAL |
| `a` | Insert sau cursor | NORMAL |
| `A` | Insert cuối dòng | NORMAL |
| `o` | Mở dòng mới bên dưới | NORMAL |
| `O` | Mở dòng mới bên trên | NORMAL |

### Navigation (NORMAL mode)

| Command | Action |
|---------|--------|
| `h`/`j`/`k`/`l` | Di chuyển trái/xuống/lên/phải |
| `w` / `e` / `b` | Next word / end of word / previous word |
| `0` / `$` / `^` | Đầu dòng / cuối dòng / ký tự không trống đầu tiên |
| `gg` / `G` | Đầu input / cuối input |
| `f{char}` / `F{char}` | Jump tới/lùi tới ký tự |
| `t{char}` / `T{char}` | Jump tới trước/sau ký tự |
| `;` / `,` | Lặp lại / đảo ngược f/F/t/T |

### Editing (NORMAL mode)

| Command | Action |
|---------|--------|
| `x` | Xóa ký tự |
| `dd` / `D` | Xóa dòng / xóa đến cuối dòng |
| `dw`/`de`/`db` | Xóa word/to end/back |
| `cc` / `C` | Change dòng / change đến cuối dòng |
| `cw`/`ce`/`cb` | Change word/to end/back |
| `yy`/`Y` | Yank (copy) dòng |
| `yw`/`ye`/`yb` | Yank word/to end/back |
| `p` / `P` | Paste sau/trước cursor |
| `>>` / `<<` | Indent / dedent dòng |
| `J` | Join lines |
| `.` | Lặp lại thay đổi cuối |

### Text Objects (NORMAL mode)

Dùng với operators `d`, `c`, `y`:

| Command | Action |
|---------|--------|
| `iw`/`aw` | Inner/around word |
| `iW`/`aW` | Inner/around WORD (whitespace-delimited) |
| `i"`/`a"` | Inner/around double quotes |
| `i'`/`a'` | Inner/around single quotes |
| `i(`/`a(` | Inner/around parentheses |
| `i[`/`a[` | Inner/around brackets |
| `i{`/`a{` | Inner/around braces |

---

## 2.7 Environment Variables

Cấu hình Claude Code qua environment variables. Tất cả đều có thể set trong `settings.json` dưới key `env`.

[Nguồn: Claude Code Docs — Settings]

### Authentication & Backend

| Variable | Mô tả |
|----------|--------|
| `ANTHROPIC_API_KEY` | API key cho Claude SDK |
| `ANTHROPIC_AUTH_TOKEN` | Custom Authorization header (prefix `Bearer `) |
| `ANTHROPIC_CUSTOM_HEADERS` | Custom headers (`Name: Value`, newline-separated) |
| `ANTHROPIC_MODEL` | Model setting name |
| `CLAUDE_CODE_USE_BEDROCK` | Dùng AWS Bedrock backend |
| `CLAUDE_CODE_USE_VERTEX` | Dùng Google Vertex backend |
| `CLAUDE_CODE_USE_FOUNDRY` | Dùng Microsoft Foundry backend |
| `CLAUDE_CODE_SKIP_BEDROCK_AUTH` | Skip AWS auth cho Bedrock (dùng LLM gateway) |
| `CLAUDE_CODE_SKIP_VERTEX_AUTH` | Skip Google auth cho Vertex |
| `CLAUDE_CODE_SKIP_FOUNDRY_AUTH` | Skip Azure auth cho Foundry |

### Model Configuration

| Variable | Mô tả |
|----------|--------|
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | Override default Sonnet model |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | Override default Opus model |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | Override default Haiku model |
| `CLAUDE_CODE_SUBAGENT_MODEL` | Model dùng cho subagents |
| `CLAUDE_CODE_EFFORT_LEVEL` | Effort level: `low`, `medium`, `high` |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | Max output tokens (default: 32,000) |

### Feature Toggles

| Variable | Mô tả |
|----------|--------|
| `CLAUDE_CODE_DISABLE_AUTO_MEMORY` | `1` tắt auto memory; `0` force bật |
| `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` | `1` tắt adaptive reasoning cho Opus/Sonnet 4.6 |
| `CLAUDE_CODE_DISABLE_FAST_MODE` | `1` tắt fast mode |
| `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` | `1` tắt background task functionality |
| `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS` | `1` loại bỏ built-in git workflow instructions |
| `CLAUDE_CODE_DISABLE_CRON` | `1` tắt scheduled tasks |
| `CLAUDE_CODE_DISABLE_TERMINAL_TITLE` | `1` tắt auto-update terminal title |
| `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` | `false` tắt prompt suggestions (default: `true`) |
| `CLAUDE_CODE_ENABLE_TASKS` | `false` revert về TODO list cũ (default: `true`) |
| `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` | `1` bật Agent Teams (experimental) |
| `CLAUDE_CODE_DISABLE_1M_CONTEXT` | `1` tắt 1M context window support |

### Bash & Execution

| Variable | Mô tả |
|----------|--------|
| `BASH_DEFAULT_TIMEOUT_MS` | Default timeout cho bash commands |
| `BASH_MAX_TIMEOUT_MS` | Max timeout model có thể set |
| `BASH_MAX_OUTPUT_LENGTH` | Max characters trước khi middle-truncate |
| `CLAUDE_CODE_SHELL` | Override auto-detected shell (`bash`, `zsh`) |
| `CLAUDE_CODE_SHELL_PREFIX` | Prefix wrap mọi bash commands |
| `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` | Trở về project directory sau mỗi Bash command |

### Context & Compaction

| Variable | Mô tả |
|----------|--------|
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | % context capacity (1-100) trigger auto-compaction (default: ~95%) |
| `CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS` | Override token limit cho file reads |
| `CLAUDE_CODE_TASK_LIST_ID` | Chia sẻ task list giữa sessions (set cùng ID) |

### Privacy & Telemetry

| Variable | Mô tả |
|----------|--------|
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | Tắt autoupdater, bug command, error reporting, telemetry |
| `CLAUDE_CODE_ENABLE_TELEMETRY` | `1` bật OpenTelemetry |
| `CLAUDE_CODE_HIDE_ACCOUNT_INFO` | `1` ẩn email và org name khỏi UI |
| `DISABLE_AUTOUPDATER` | `1` tắt auto-update |
| `DISABLE_ERROR_REPORTING` | `1` opt out Sentry error reporting |
| `DISABLE_COST_WARNINGS` | `1` tắt cost warning messages |
| `DISABLE_PROMPT_CACHING` | `1` tắt prompt caching |

### Paths & Infrastructure

| Variable | Mô tả |
|----------|--------|
| `CLAUDE_CONFIG_DIR` | Custom directory cho config và data files |
| `CLAUDE_CODE_TMPDIR` | Override temp directory |
| `CLAUDE_CODE_SIMPLE` | `1` chạy với minimal system prompt + chỉ Bash/file tools |

### Enterprise & mTLS

| Variable | Mô tả |
|----------|--------|
| `CLAUDE_CODE_CLIENT_CERT` | Path đến client certificate cho mTLS |
| `CLAUDE_CODE_CLIENT_KEY` | Path đến client private key cho mTLS |
| `CLAUDE_CODE_CLIENT_KEY_PASSPHRASE` | Passphrase cho encrypted client key |
| `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` | Interval (ms) refresh credentials khi dùng `apiKeyHelper` |

---

## 2.8 Output Formats

Print mode (`-p`) hỗ trợ nhiều output formats cho scripting và automation.

[Nguồn: Claude Code Docs — CLI Reference]

### Text (default)

```bash
claude -p "list all routes"
```

Output plain text — phù hợp cho đọc trực tiếp hoặc pipe vào tools khác.

### JSON

```bash
claude -p "list all routes" --output-format json
```

Trả về JSON object với metadata (model, usage, messages). Phù hợp cho parsing programmatic.

### Stream JSON

```bash
claude -p "list all routes" --output-format stream-json
```

Trả về JSON objects trên từng line khi streaming. Kết hợp `--include-partial-messages` để nhận partial events.

### Structured Output (`--json-schema`)

```bash
claude -p "analyze this code" --json-schema '{
  "type": "object",
  "properties": {
    "bugs": {"type": "array", "items": {"type": "string"}},
    "score": {"type": "number"}
  },
  "required": ["bugs", "score"]
}'
```

Claude hoàn thành workflow bình thường rồi trả về validated JSON theo schema. Print mode only.

---

## 2.9 Background Tasks & Task List

Claude Code hỗ trợ chạy bash commands ở background và tracking task progress.

[Nguồn: Claude Code Docs — Interactive Mode]

### Background Commands

Hai cách chạy background:

1. **Prompt:** yêu cầu Claude chạy command ở background
2. **`Ctrl+B`:** chuyển command đang chạy sang background (tmux users: nhấn 2 lần)

Background tasks có unique ID — Claude dùng `TaskOutput` tool để lấy output. Tasks tự cleanup khi Claude Code thoát.

### Task List

Khi xử lý complex work, Claude tạo task list tracking progress trong terminal status area:

- `Ctrl+T` toggle hiển thị (tối đa 10 tasks)
- Tasks persist across context compactions
- Chia sẻ task list giữa sessions: `CLAUDE_CODE_TASK_LIST_ID=my-project claude`

### PR Review Status

Khi làm việc trên branch có open PR, footer hiển thị clickable PR link với color-coded status:

| Màu | Trạng thái |
|-----|------------|
| Green | Approved |
| Yellow | Pending review |
| Red | Changes requested |
| Gray | Draft |
| Purple | Merged |

`Cmd+click` (Mac) hoặc `Ctrl+click` (Windows/Linux) để mở PR. Auto-update mỗi 60 giây. Cần `gh` CLI.

---

## 2.10 Tham chiếu nhanh

Các patterns hay dùng nhất cho developer workflows.

### Piping & Composition

```bash
# Phân tích logs
cat error.log | claude -p "tìm root cause"

# Code review file cụ thể
git diff HEAD~1 | claude -p "review changes này"

# Batch processing
find . -name "*.py" | head -5 | xargs -I {} claude -p "refactor {}"

# Chain với tools khác
claude -p "generate test cases" --output-format json | jq '.result'
```

### Headless Automation

```bash
# CI/CD — giới hạn turns và budget
claude -p "run tests and fix failures" --max-turns 10 --max-budget-usd 2.00

# Structured output cho pipeline
claude -p "analyze security" --json-schema '{"type":"object","properties":{"issues":{"type":"array"}}}'

# Skip permissions cho container environment
claude -p "build project" --dangerously-skip-permissions
```

### Session Management

```bash
# Resume session cũ
claude -r "auth-refactor" "tiếp tục task này"

# Fork từ session hiện tại
claude --resume abc123 --fork-session

# Resume từ PR
claude --from-pr 123

# Web → local
claude --teleport
```

---

← [CC Setup](01-claude-code-setup.md) | [Tổng quan](../base/00-overview.md) | [IDE Integration →](03-ide-integration.md)
