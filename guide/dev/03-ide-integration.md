# Claude Code — IDE & Surface Integration

**Thời gian đọc:** 25 phút | **Mức độ:** Intermediate
**Cập nhật:** 2026-03-07 | Models: xem [specs](../reference/model-specs.md)

---
depends-on: [dev/01-claude-code-setup, dev/02-cli-reference]
impacts: [dev/04-agents-automation, dev/06-dev-workflows]
---

Claude Code hoạt động trên nhiều surfaces: VS Code extension, JetBrains plugin, Desktop app, Remote Control (mobile/browser), và Web interface. Module này hướng dẫn cài đặt và cấu hình từng surface — workflow switching giữa các surfaces xem [dev/06](06-dev-workflows.md).

[Nguồn: Claude Code Docs] [Cập nhật 03/2026]

---

## 3.1 VS Code Extension

VS Code extension là cách chính thức để dùng Claude Code trong IDE — giao diện đồ họa tích hợp trực tiếp, hỗ trợ inline diffs, @-mentions, plan review, và conversation history.

[Nguồn: Claude Code Docs — VS Code]

### Yêu cầu

- VS Code 1.98.0 trở lên (hoặc Cursor)
- Tài khoản Anthropic (hoặc third-party provider — Bedrock, Vertex, Foundry)

### Cài đặt

Cách 1 — từ Marketplace:

```text
Cmd+Shift+X (Mac) / Ctrl+Shift+X (Win/Linux) → search "Claude Code" → Install
```

Cách 2 — link trực tiếp:

- VS Code: `vscode:extension/anthropic.claude-code`
- Cursor: `cursor:extension/anthropic.claude-code`

> [!NOTE]
> Extension bao gồm cả CLI — có thể chạy `claude` từ integrated terminal mà không cần cài riêng.

### Mở Claude Code panel

| Cách mở | Mô tả |
|---------|--------|
| Editor Toolbar | Click icon Spark (góc trên phải editor) — chỉ hiện khi có file mở |
| Activity Bar | Click icon Spark ở sidebar trái → xem sessions list |
| Command Palette | `Cmd+Shift+P` / `Ctrl+Shift+P` → "Claude Code" |
| Status Bar | Click "Claude Code" ở góc dưới phải — hoạt động cả khi không có file mở |

Lần đầu mở, checklist **Learn Claude Code** xuất hiện — click **Show me** để đi qua từng bước, hoặc X để bỏ qua. Mở lại: bỏ check **Hide Onboarding** trong Settings → Extensions → Claude Code.

### @-Mentions và file context

Dùng `@` để reference files/folders — Claude đọc nội dung và trả lời hoặc chỉnh sửa.

```text
> Explain the logic in @auth        (fuzzy match: auth.js, AuthService.ts...)
> What's in @src/components/        (trailing slash = folder)
```

- **Selected text**: Claude tự động thấy text đang highlight trong editor
- **Insert reference**: `Option+K` (Mac) / `Alt+K` (Win/Linux) → chèn `@file.ts#5-10` vào prompt
- **Drag files**: giữ `Shift` khi kéo file vào prompt box → attach
- **PDF**: hỗ trợ đọc theo trang (`@report.pdf` pages 1-10)
- **Toggle visibility**: click selection indicator để ẩn/hiện highlighted text khỏi Claude

### Review changes — Inline Diffs

Khi Claude muốn sửa file, VS Code hiển thị diff side-by-side rồi hỏi permission. Có thể accept, reject, hoặc yêu cầu sửa khác.

### Plan Review Mode

Trong prompt box, click mode indicator để chuyển permission mode:

| Mode | Hành vi |
|------|---------|
| Normal (default) | Claude hỏi permission trước mỗi action |
| Plan | Claude mô tả kế hoạch → mở markdown document để review + comment inline → chờ approval |
| Auto-accept | Claude sửa file không hỏi — vẫn hỏi trước khi chạy commands |

Set default trong VS Code settings: `claudeCode.initialPermissionMode`.

> [!TIP]
> Bắt đầu task phức tạp ở Plan mode → review approach → chuyển sang Auto-accept khi thực thi. Xem thêm [best practices](../base/06-mistakes-fixes.md).

### Conversation History

Click dropdown ở đầu Claude Code panel → browse theo thời gian (Today, Yesterday, Last 7 days...) hoặc search theo keyword. Hover session → rename hoặc remove.

**Resume remote sessions:** nếu dùng [Claude Code on the Web](#36-claude-code-on-the-web), mở tab **Remote** trong Past Conversations để resume web sessions trong VS Code (yêu cầu đăng nhập Claude.ai Subscription).

### Multiple Conversations

Mở Command Palette → **Open in New Tab** hoặc **Open in New Window** để chạy nhiều conversations song song. Mỗi conversation có history và context riêng.

Status dots trên spark icon: xanh = đang chờ permission, cam = Claude hoàn thành khi tab ẩn.

### Prompt Box Features

| Feature | Mô tả |
|---------|--------|
| `/` command menu | Attach files, switch model, toggle extended thinking, `/usage`, MCP, hooks, memory |
| Context indicator | Hiển thị % context window đã dùng — auto compact khi cần, hoặc `/compact` thủ công |
| Extended thinking | Bật qua command menu `/` — Claude suy nghĩ sâu hơn cho bài toán phức tạp |
| Multi-line | `Shift+Enter` thêm dòng mới |

---

## 3.2 VS Code — Commands & Shortcuts

Các VS Code commands (mở qua Command Palette) và keyboard shortcuts cho extension.

[Nguồn: Claude Code Docs — VS Code]

| Command | Shortcut | Mô tả |
|---------|----------|--------|
| Focus Input | `Cmd+Esc` / `Ctrl+Esc` | Toggle focus giữa editor và Claude |
| Open in New Tab | `Cmd+Shift+Esc` / `Ctrl+Shift+Esc` | Mở conversation mới trong editor tab |
| New Conversation | `Cmd+N` / `Ctrl+N` | Conversation mới (yêu cầu Claude đang focused) |
| Insert @-Mention | `Option+K` / `Alt+K` | Chèn reference file + selection (yêu cầu editor focused) |
| Open in Side Bar | — | Mở Claude ở left sidebar |
| Open in Terminal | — | Chuyển sang terminal mode |
| Open in New Window | — | Mở conversation ở cửa sổ riêng |
| Show Logs | — | Xem extension debug logs |
| Logout | — | Đăng xuất tài khoản |

### Reposition Panel

Kéo Claude panel tab đến bất kỳ vị trí nào trong VS Code:

- **Secondary sidebar** (phải): giữ Claude visible khi code
- **Primary sidebar** (trái): cùng Explorer, Search
- **Editor area**: mở như tab bên cạnh files

### Terminal Mode

Nếu thích giao diện CLI, bật `claudeCode.useTerminal` trong VS Code settings. Hoặc chạy `claude` trong integrated terminal (`Ctrl+`` `).

Khi dùng external terminal, chạy `/ide` trong Claude Code để connect tới VS Code.

### Chia sẻ giữa Extension và CLI

Extension và CLI chia sẻ conversation history. Resume extension conversation trong CLI:

```bash
claude --resume
```

Reference terminal output trong prompt:

```text
> Check errors in @terminal:dev-server
```

### Extension Settings

| Setting | Default | Mô tả |
|---------|---------|--------|
| `selectedModel` | `default` | Model cho conversations mới |
| `useTerminal` | `false` | Dùng terminal mode thay vì graphical panel |
| `initialPermissionMode` | `default` | `default`, `plan`, `acceptEdits`, `bypassPermissions` |
| `preferredLocation` | `panel` | `sidebar` hoặc `panel` (new tab) |
| `autosave` | `true` | Auto-save files trước khi Claude đọc/ghi |
| `useCtrlEnterToSend` | `false` | Dùng Ctrl/Cmd+Enter thay Enter để gửi |
| `respectGitIgnore` | `true` | Loại .gitignore patterns khỏi file searches |
| `disableLoginPrompt` | `false` | Tắt auth prompts (dùng cho third-party providers) |

> [!TIP]
> Thêm `"$schema": "https://json.schemastore.org/claude-code-settings.json"` vào `settings.json` để có autocomplete và validation.

### Extension vs CLI — So sánh

| Feature | CLI | VS Code Extension |
|---------|-----|-------------------|
| Commands/skills | Tất cả | Subset (gõ `/` để xem) |
| MCP config | Full | Partial (thêm qua CLI, quản lý qua `/mcp`) |
| Checkpoints | ✅ | ✅ |
| `!` bash shortcut | ✅ | ❌ |
| Tab completion | ✅ | ❌ |

### Checkpoints trong VS Code

Hover bất kỳ message nào → nút rewind với 3 options:

- **Fork conversation from here**: branch mới từ message này, giữ code changes
- **Rewind code to here**: revert file changes về điểm này, giữ conversation history
- **Fork + rewind**: cả hai

Chi tiết: xem [checkpointing](01-claude-code-setup.md#19-checkpointing--rewind).

---

## 3.3 VS Code — MCP & Browser

Mở rộng khả năng Claude Code bằng MCP servers và Chrome integration.

[Nguồn: Claude Code Docs — VS Code]

### MCP Servers

Thêm MCP server qua integrated terminal:

```bash
claude mcp add --transport http github https://api.githubcopilot.com/mcp/
```

Quản lý trong extension: gõ `/mcp` trong chat panel → enable/disable, reconnect, OAuth auth.

Chi tiết MCP: xem [dev/05](05-plugins.md).

### Chrome Integration

Yêu cầu [Claude in Chrome extension](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn) v1.0.36+.

```text
@browser go to localhost:3000 and check the console for errors
```

Claude mở tab mới, chia sẻ login state của browser — có thể truy cập sites đã đăng nhập.

---

## 3.4 JetBrains Plugin

Plugin cho IntelliJ IDEA, PyCharm, WebStorm, GoLand, PhpStorm, Android Studio — cung cấp diff viewing, selection context, và file references.

[Nguồn: Claude Code Docs — JetBrains]

### Cài đặt

1. Tìm **Claude Code** trên [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-) → Install
2. Restart IDE hoàn toàn

### Features

| Feature | Shortcut | Mô tả |
|---------|----------|--------|
| Quick launch | `Cmd+Esc` / `Ctrl+Esc` | Mở Claude Code từ editor |
| File reference | `Cmd+Option+K` / `Alt+Ctrl+K` | Chèn `@File#L1-99` |
| Diff viewing | — | Code changes hiển thị trong IDE diff viewer |
| Selection context | — | Selection/tab tự động share với Claude |
| Diagnostics | — | Lint, syntax errors tự động share |

### Cấu hình

Chạy `claude` → `/config` → set diff tool = `auto` để tự động detect IDE.

Plugin settings: **Settings → Tools → Claude Code [Beta]**

- **Claude command**: custom path (`claude`, `/usr/local/bin/claude`, `npx @anthropic/claude`)
- **WSL**: set `wsl -d Ubuntu -- bash -lic "claude"` (thay `Ubuntu` bằng distro name)
- **ESC key fix**: Settings → Tools → Terminal → bỏ check "Move focus to the editor with Escape"

### Remote Development

Plugin phải cài trên **remote host** (Settings → Plugin (Host)), không phải local client.

> [!NOTE]
> JetBrains plugin đang ở Beta — VS Code extension có nhiều features hơn. Xem [VS Code extension](#31-vs-code-extension) cho trải nghiệm đầy đủ nhất.

---

## 3.5 Desktop App

Claude Desktop app (tab Code) cung cấp giao diện đồ họa cho Claude Code với các tính năng bổ sung không có trong CLI hay extension.

[Nguồn: Claude Code Docs — Desktop] [Cập nhật 03/2026]

### Tính năng chính

| Feature | Mô tả |
|---------|--------|
| Visual diff review | Xem changes file-by-file, comment inline, submit batch (`Cmd/Ctrl+Enter`) |
| Code review | Click **Review code** trong diff view — Claude review focusing on compile errors, logic bugs, security |
| Live preview | Claude start dev server + embedded browser, auto-verify changes (screenshots, DOM, click, forms) |
| Parallel sessions | Mỗi session tự động có Git worktree riêng (`.claude/worktrees/`) |
| Scheduled tasks | Chạy Claude theo lịch (hourly, daily, weekdays, weekly, manual) |
| PR monitoring | CI status bar + auto-fix failing checks + auto-merge khi pass |
| Connectors | GitHub, Slack, Linear, Notion, Google Calendar... (MCP servers với GUI setup) |
| SSH sessions | Chạy Claude Code trên remote machine qua SSH |
| Remote sessions | Chạy trên Anthropic cloud — tiếp tục cả khi đóng app |

### Cài đặt và khởi chạy

Download từ [claude.ai](https://claude.ai) → mở tab **Code**. Trước khi gửi prompt, cấu hình:

1. **Environment**: Local / Remote / SSH connection
2. **Project folder**: chọn thư mục hoặc repo
3. **Model**: chọn từ dropdown (locked khi session bắt đầu)
4. **Permission mode**: Ask permissions / Auto accept edits / Plan / Bypass permissions

### Permission Modes

| Mode | Key | Hành vi |
|------|-----|---------|
| Ask permissions | `default` | Hỏi trước khi edit hoặc chạy commands |
| Auto accept edits | `acceptEdits` | Auto-accept edits, vẫn hỏi trước commands |
| Plan mode | `plan` | Chỉ phân tích + lên kế hoạch, không sửa code |
| Bypass permissions | `bypassPermissions` | Không hỏi gì — bật trong Settings, chỉ dùng trong sandbox/VM |

> [!WARNING]
> `dontAsk` mode chỉ có trong CLI, không có trong Desktop.

### Scheduled Tasks

Tạo: sidebar → **Schedule** → **+ New task**. Cấu hình: name, description, prompt, frequency.

| Frequency | Chi tiết |
|-----------|----------|
| Manual | Chỉ chạy khi click **Run now** |
| Hourly | Mỗi giờ (offset tự động lên đến 10 phút) |
| Daily | Chọn giờ, mặc định 9:00 AM |
| Weekdays | Giống Daily, bỏ Saturday/Sunday |
| Weekly | Chọn giờ + ngày |

Tasks chạy locally — app phải mở và máy phải thức. Nếu miss, Desktop catch-up 1 lần khi wake. File config: `~/.claude/scheduled-tasks/<task-name>/SKILL.md`.

### Live Preview & Auto-verify

Claude tự động start dev server, mở embedded browser, chụp screenshots, inspect DOM, click elements, fill forms, fix issues. Config trong `.claude/launch.json`:

```json
{
  "version": "0.0.1",
  "configurations": [
    {
      "name": "web",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["run", "dev"],
      "port": 3000
    }
  ]
}
```

Tắt auto-verify: thêm `"autoVerify": false` hoặc toggle từ Preview dropdown.

### SSH Sessions

Click environment dropdown → **+ Add SSH connection**:

- **Name**: label cho connection
- **SSH Host**: `user@hostname` hoặc host trong `~/.ssh/config`
- **SSH Port**: mặc định 22
- **Identity File**: path tới private key

Claude Code phải cài sẵn trên remote machine.

### Desktop vs CLI

| Feature | CLI | Desktop |
|---------|-----|---------|
| Permission modes | Tất cả (gồm `dontAsk`) | Không có `dontAsk` |
| Third-party providers | Bedrock, Vertex, Foundry | Không hỗ trợ |
| Session isolation | `--worktree` flag | Tự động worktrees |
| Multiple sessions | Separate terminals | Sidebar tabs |
| Recurring tasks | Cron jobs, CI | Scheduled tasks |
| Scripting/automation | `--print`, Agent SDK | Không hỗ trợ |
| Agent teams | ✅ | ❌ |
| File attachments | ❌ | ✅ (images, PDFs) |
| Linux | ✅ | ❌ (macOS + Windows only) |

### Di chuyển session

- **CLI → Desktop**: chạy `/desktop` trong terminal → Claude lưu session và mở trong Desktop app
- **Desktop → Web**: menu **Continue in** → Claude Code on the Web (push branch + tạo remote session)
- **Desktop → IDE**: menu **Continue in** → chọn IDE

### Shared Configuration

Desktop và CLI chia sẻ: CLAUDE.md, MCP servers (`~/.claude.json`, `.mcp.json`), hooks, skills, settings (`~/.claude/settings.json`).

> [!NOTE]
> MCP servers trong `claude_desktop_config.json` (chat app) KHÔNG hiện trong tab Code. Dùng `~/.claude.json` hoặc `.mcp.json` cho Claude Code.

---

## 3.6 Claude Code on the Web

Chạy Claude Code trên cloud infrastructure của Anthropic — không cần cài đặt local, phù hợp cho long-running tasks và parallel work.

[Nguồn: Claude Code Docs — Claude Code on the Web] [Cập nhật 03/2026]

### Khi nào dùng

- Trả lời câu hỏi về code architecture
- Bug fixes, routine tasks rõ ràng không cần steering liên tục
- Parallel work — nhiều bug fixes cùng lúc
- Repos chưa clone về máy
- Backend changes — viết tests rồi viết code pass tests

### Bắt đầu

1. Truy cập [claude.ai/code](https://claude.ai/code)
2. Connect GitHub account
3. Install Claude GitHub app trong repos
4. Chọn environment
5. Submit task → review diff → tạo PR

Có sẵn trên: Pro, Max, Team, Enterprise.

### Cách hoạt động

1. **Clone**: repo được clone vào Anthropic-managed VM
2. **Setup**: cloud environment + setup script (nếu có)
3. **Network**: internet access theo cấu hình (limited mặc định)
4. **Execution**: Claude phân tích code, sửa, chạy tests, kiểm tra
5. **Completion**: changes push lên branch, sẵn sàng tạo PR

### Cloud Environment

**Default image**: Ubuntu 24.04 với pre-installed toolchains — Python, Node.js, Ruby, PHP, Java, Go, Rust, C++, PostgreSQL 16, Redis 7.0.

**Setup scripts**: bash script chạy trước Claude Code launch, dùng để install dependencies:

```bash
#!/bin/bash
apt update && apt install -y gh
npm install
pip install -r requirements.txt
```

Setup scripts chỉ chạy khi tạo session mới, không chạy khi resume.

**Network access levels:**

| Level | Mô tả |
|-------|--------|
| Limited (default) | Cho phép common registries (npm, PyPI, RubyGems, crates.io...) + GitHub + cloud platforms |
| Full | Truy cập internet không giới hạn |
| No internet | Chỉ Anthropic API |

### Diff View & Iteration

Claude thay đổi files → diff stats hiện (`+12 -1`) → click mở diff viewer → comment inline → Claude sửa theo feedback → lặp lại đến khi ổn → tạo PR.

### Terminal ↔ Web

**Terminal → Web** — tạo remote session từ CLI:

```bash
claude --remote "Fix the authentication bug in src/auth/login.ts"
```

Task chạy trên cloud, check progress bằng `/tasks`. Chạy nhiều tasks song song:

```bash
claude --remote "Fix flaky test in auth.spec.ts"
claude --remote "Update the API documentation"
```

**Web → Terminal** — teleport web session về local:

```bash
claude --teleport           # interactive picker
claude --teleport <id>      # resume session cụ thể
```

Hoặc trong Claude Code: `/teleport` (hoặc `/tp`).

> [!NOTE]
> Session handoff chỉ một chiều: pull web → terminal được, push terminal → web phải dùng `--remote` tạo session mới.

---

## 3.7 Remote Control

Tiếp tục local Claude Code session từ phone, tablet, hoặc browser bất kỳ — session vẫn chạy trên máy local.

[Nguồn: Claude Code Docs — Remote Control] [Cập nhật 03/2026]

### Khác biệt với Web

| | Remote Control | Claude Code on the Web |
|-|---------------|----------------------|
| Chạy ở đâu | Máy local | Anthropic cloud |
| MCP/tools local | ✅ Có | ❌ Không |
| Cần máy bật | ✅ | ❌ |
| Use case | Đang làm việc, muốn tiếp từ thiết bị khác | Kick off task mới, không cần local setup |

### Yêu cầu

- Subscription: Pro, Max, Team, Enterprise
- Auth: `claude` → `/login` qua claude.ai
- Workspace trust: chạy `claude` trong project ít nhất 1 lần

### Bắt đầu session

**Session mới:**

```bash
claude remote-control              # hoặc với tên
claude remote-control "My Project"
```

Flags: `--name`, `--verbose`, `--sandbox` / `--no-sandbox`.

**Từ session đang chạy:**

```text
/remote-control           # hoặc /rc
/rc My Project
```

Terminal hiển thị URL + nhấn spacebar xem QR code.

### Connect từ thiết bị khác

- Mở URL session trong browser → [claude.ai/code](https://claude.ai/code)
- Scan QR code bằng Claude app (iOS/Android)
- Mở claude.ai/code → tìm session theo tên (icon computer + green dot = online)

### Bật cho mọi session

Chạy `/config` → **Enable Remote Control for all sessions** → `true`.

### Security

- Chỉ outbound HTTPS — không mở inbound ports
- Traffic qua Anthropic API qua TLS
- Multiple short-lived credentials, scoped và expire riêng

### Giới hạn

- 1 remote session tại một thời điểm per Claude Code instance
- Terminal phải mở — đóng terminal = kết thúc session
- Network outage > ~10 phút → session timeout

---

## 3.8 Tổng quan Surfaces

Bảng tóm tắt setup và tính năng chính của mỗi surface — để chọn đúng tool cho task.

[Nguồn: Claude Code Docs] [Cập nhật 03/2026]

| Surface | Cài đặt | Platforms | Diff review | Parallel sessions | Offline/local |
|---------|---------|-----------|-------------|-------------------|---------------|
| CLI | `curl` / `npm` | macOS, Linux, WSL, Win | Terminal-based | Separate terminals | ✅ |
| VS Code | Extension Marketplace | macOS, Linux, Win | Inline side-by-side | New Tab/Window | ✅ |
| JetBrains | Plugin Marketplace | macOS, Linux, Win | IDE diff viewer | Separate terminals | ✅ |
| Desktop | Download app | macOS, Win | Visual + inline comments | Sidebar + worktrees | ✅ |
| Remote Control | Từ CLI/session | Phone, tablet, browser | Qua claude.ai/code | 1 per instance | ✅ (chạy local) |
| Web | claude.ai/code | Browser | Diff + inline comments | ✅ Cloud parallel | ❌ (cloud) |

> [!TIP]
> Chọn surface theo task: CLI cho automation/scripting, VS Code cho daily coding, Desktop cho visual review + parallel work, Web cho long-running tasks không cần local setup. Chi tiết workflow switching: xem [dev/06](06-dev-workflows.md).

---

← [CLI Reference](02-cli-reference.md) | [Tổng quan](../base/00-overview.md) | [Agents & Automation →](04-agents-automation.md)
