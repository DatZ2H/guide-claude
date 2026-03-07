# Claude Code — Setup & Configuration

**Thời gian đọc:** 25 phút | **Mức độ:** Intermediate
**Cập nhật:** 2026-03-07 | Models: xem [specs](../reference/model-specs.md)

---
depends-on: [base/02-setup, reference/config-architecture]
impacts: [dev/02-cli-reference, dev/03-ide-integration, dev/04-agents-automation]
---

Module này hướng dẫn cài đặt, xác thực, và cấu hình Claude Code CLI — công cụ coding agent chạy trong terminal. Dành cho developer muốn setup môi trường làm việc hoàn chỉnh trước khi sử dụng.

[Nguồn: Claude Code Docs] [Cập nhật 03/2026]

---

## 1.1 Cài đặt

Claude Code hỗ trợ nhiều phương thức cài đặt trên macOS, Linux, WSL, và Windows.

[Nguồn: Claude Code Docs — Overview]

### Native Install (khuyến nghị)

Native install tự động cập nhật ở background.

**macOS, Linux, WSL:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**

```powershell
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD:**

```batch
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

> [!IMPORTANT]
> Windows yêu cầu [Git for Windows](https://git-scm.com/downloads/win). Cài trước nếu chưa có.

### Homebrew (macOS/Linux)

```bash
brew install --cask claude-code
```

Homebrew không tự cập nhật — chạy `brew upgrade claude-code` định kỳ.

### WinGet (Windows)

```powershell
winget install Anthropic.ClaudeCode
```

WinGet không tự cập nhật — chạy `winget upgrade Anthropic.ClaudeCode` định kỳ.

### Đăng nhập lần đầu

```bash
cd your-project
claude
```

Lần đầu chạy sẽ mở browser để đăng nhập. Cần [Claude subscription](https://claude.com/pricing) hoặc [Anthropic Console](https://console.anthropic.com/) account.

---

## 1.2 CLAUDE.md — Hệ thống Instructions

CLAUDE.md là file markdown chứa instructions mà Claude đọc ở đầu mỗi session. Đây là cách chính để cung cấp context bền vững cho project.

[Nguồn: Claude Code Docs — Memory]

### Scopes và vị trí

| Scope | Vị trí | Mục đích | Chia sẻ |
|-------|--------|----------|---------|
| **Managed policy** | `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS), `/etc/claude-code/CLAUDE.md` (Linux), `C:\Program Files\ClaudeCode\CLAUDE.md` (Windows) | Org-wide, IT quản lý | Tất cả users |
| **Project** | `./CLAUDE.md` hoặc `./.claude/CLAUDE.md` | Team-shared | Git (commit) |
| **User** | `~/.claude/CLAUDE.md` | Cá nhân, mọi project | Không |
| **Local** | `./CLAUDE.local.md` | Cá nhân, project này | Không (gitignored) |

**Thứ tự ưu tiên:** Managed > Project > User > Local (scope cụ thể hơn override scope rộng hơn).

CLAUDE.md ở thư mục cha được load đầy đủ khi khởi động. CLAUDE.md ở subdirectories load on-demand khi Claude đọc files trong đó.

### Viết instructions hiệu quả

- **Kích thước:** target dưới 200 dòng mỗi file. File dài hơn tốn context và giảm adherence
- **Cấu trúc:** dùng markdown headers và bullets để nhóm instructions liên quan
- **Cụ thể:** "Dùng 2-space indentation" tốt hơn "format code cho đẹp"
- **Nhất quán:** kiểm tra conflict giữa các CLAUDE.md files định kỳ

Chạy `/init` để tự generate CLAUDE.md ban đầu từ codebase analysis.

### @imports — nhúng files bổ sung

CLAUDE.md hỗ trợ nhúng files khác bằng cú pháp `@path/to/file`:

```markdown
Xem @README cho project overview và @package.json cho npm commands.

## Additional Instructions
- Git workflow @docs/git-instructions.md
```

- Relative paths resolve từ file chứa import, không phải working directory
- Hỗ trợ recursive imports (tối đa 5 cấp)
- Lần đầu gặp external imports, Claude Code hiện dialog xác nhận

### Loại trừ CLAUDE.md không liên quan

Trong monorepo, dùng `claudeMdExcludes` để skip files từ teams khác:

```json
{
  "claudeMdExcludes": [
    "**/monorepo/CLAUDE.md",
    "/home/user/other-team/.claude/rules/**"
  ]
}
```

**So sánh với claude.ai:** Project Instructions (claude.ai) tương đương Folder Instructions (Cowork/Claude Code) về chức năng, nhưng khác về versioning và sharing. Xem chi tiết tại [Config Architecture](../reference/config-architecture.md).

---

## 1.3 `.claude/rules/` — Path-specific Rules

Rules cho phép tổ chức instructions thành nhiều files, có thể scope theo đường dẫn file cụ thể.

[Nguồn: Claude Code Docs — Memory]

### Cấu trúc

```text
your-project/
├── .claude/
│   ├── CLAUDE.md
│   └── rules/
│       ├── code-style.md
│       ├── testing.md
│       └── security.md
```

Rules không có `paths` frontmatter được load cùng lúc với `.claude/CLAUDE.md`. Rules có `paths` chỉ load khi Claude đọc files matching pattern.

### Path-specific rules với frontmatter

```yaml
## file: .claude/rules/api-design.md
paths:
  - "src/api/**/*.ts"
```

Nội dung phía dưới frontmatter là rules markdown thường (headings, bullets). Rules này chỉ load khi Claude đọc files matching pattern.

Glob patterns hỗ trợ:

| Pattern | Matches |
|---------|---------|
| `**/*.ts` | Tất cả TypeScript files |
| `src/**/*` | Tất cả files trong `src/` |
| `*.md` | Markdown files ở project root |
| `src/components/*.tsx` | React components trong thư mục cụ thể |

Hỗ trợ brace expansion: `"src/**/*.{ts,tsx}"`.

### Symlinks — chia sẻ rules giữa projects

```bash
ln -s ~/shared-claude-rules .claude/rules/shared
ln -s ~/company-standards/security.md .claude/rules/security.md
```

### User-level rules

Rules cá nhân tại `~/.claude/rules/` áp dụng cho mọi project. User-level rules load trước project rules (project rules có priority cao hơn).

---

## 1.4 Auto Memory

Auto Memory cho phép Claude tự tích lũy knowledge qua các sessions mà không cần bạn viết gì. Claude tự quyết định lưu gì dựa trên corrections và patterns phát hiện.

[Nguồn: Claude Code Docs — Memory]

### Bật/tắt

Auto Memory **bật mặc định**. Để tắt:

- Trong session: `/memory` → toggle auto memory
- Trong settings: `"autoMemoryEnabled": false`
- Environment variable: `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`

### Cấu trúc lưu trữ

```text
~/.claude/projects/<project>/memory/
├── MEMORY.md          # Index — 200 dòng đầu load mỗi session
├── debugging.md       # Topic file — load on-demand
├── api-conventions.md # Topic file — load on-demand
└── ...
```

- `MEMORY.md` là entrypoint — **chỉ 200 dòng đầu** được load vào context mỗi session
- Nội dung sau dòng 200 không được load tự động
- Topic files không load lúc startup — Claude đọc on-demand khi cần
- Mỗi git repo chia sẻ một memory directory (bao gồm worktrees)
- Auto memory là machine-local, không chia sẻ qua cloud

### Quản lý

Chạy `/memory` để:
- Xem danh sách CLAUDE.md và rules đang load
- Toggle auto memory on/off
- Mở memory folder để edit/xóa

Auto memory files là plain markdown — bạn có thể edit hoặc xóa bất cứ lúc nào.

---

## 1.5 Permission System

Claude Code dùng hệ thống phân quyền nhiều tầng để cân bằng giữa productivity và safety.

[Nguồn: Claude Code Docs — Permissions]

### Permission tiers

| Loại tool | Ví dụ | Cần approval | "Don't ask again" |
|-----------|-------|:------------:|-------------------|
| Read-only | File reads, Grep | Không | N/A |
| Bash commands | Shell execution | Có | Vĩnh viễn (per project + command) |
| File modification | Edit/write files | Có | Đến hết session |

### 5 Permission modes

Cấu hình qua `defaultMode` trong settings:

| Mode | Mô tả |
|------|--------|
| `default` | Hỏi permission lần đầu dùng mỗi tool |
| `acceptEdits` | Tự động accept file edit permissions |
| `plan` | Plan Mode — Claude phân tích nhưng không sửa files hoặc chạy commands |
| `dontAsk` | Auto-deny trừ khi đã allow qua `/permissions` hoặc `permissions.allow` |
| `bypassPermissions` | Bỏ qua mọi permission prompts |

> [!WARNING]
> `bypassPermissions` chỉ dùng trong môi trường isolated (containers, VMs). Admin có thể chặn mode này bằng `disableBypassPermissionsMode: "disable"` trong managed settings.

### Permission rule syntax

Rules theo format `Tool` hoặc `Tool(specifier)`. Thứ tự đánh giá: **deny → ask → allow** (deny luôn thắng).

**Bash wildcards:**

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run *)",
      "Bash(git commit *)",
      "Bash(* --version)"
    ],
    "deny": [
      "Bash(git push *)"
    ]
  }
}
```

Khoảng trắng trước `*` quan trọng: `Bash(ls *)` match `ls -la` nhưng không match `lsof`. `Bash(ls*)` match cả hai.

**Read/Edit patterns** (theo gitignore spec):

| Pattern | Ý nghĩa | Ví dụ |
|---------|----------|-------|
| `//path` | Absolute path từ filesystem root | `Read(//Users/alice/secrets/**)` |
| `~/path` | Từ home directory | `Read(~/Documents/*.pdf)` |
| `/path` | Relative từ project root | `Edit(/src/**/*.ts)` |
| `path` | Relative từ current directory | `Read(*.env)` |

**WebFetch:** `WebFetch(domain:example.com)` — giới hạn theo domain.

**MCP:** `mcp__puppeteer__puppeteer_navigate` — giới hạn theo MCP tool cụ thể.

Quản lý permissions trong session: chạy `/permissions`.

---

## 1.6 Sandbox Mode

Sandboxing cung cấp filesystem và network isolation ở OS-level, giảm thiểu permission prompts và tăng autonomy cho Claude Code.

[Nguồn: Claude Code Docs — Sandboxing]

### Bật sandbox

```text
/sandbox
```

Chọn giữa 2 modes:

| Mode | Mô tả |
|------|--------|
| **Auto-allow** | Bash commands trong sandbox tự động chạy không cần approval. Commands ngoài sandbox fallback về permission flow thường |
| **Regular permissions** | Mọi bash commands vẫn qua permission flow, nhưng sandbox vẫn enforce filesystem/network restrictions |

### Filesystem isolation

- Mặc định: read/write trong working directory và subdirectories
- Blocked: không thể modify files ngoài working directory
- Configurable: thêm paths qua `sandbox.filesystem.allowWrite`

```json
{
  "sandbox": {
    "enabled": true,
    "filesystem": {
      "allowWrite": ["~/.kube", "//tmp/build"]
    }
  }
}
```

### Network isolation

- Chỉ approved domains mới truy cập được
- Domain mới trigger permission prompt (hoặc auto-block nếu `allowManagedDomainsOnly` = true)
- Restrictions áp dụng cho tất cả subprocesses

```json
{
  "sandbox": {
    "network": {
      "allowedDomains": ["github.com", "*.npmjs.org"]
    }
  }
}
```

### Platform support

| Platform | Engine |
|----------|--------|
| macOS | Seatbelt (built-in) |
| Linux | bubblewrap (`sudo apt-get install bubblewrap socat`) |
| WSL2 | bubblewrap (giống Linux) |
| WSL1 | Không hỗ trợ |
| Windows native | Planned |

---

## 1.7 Settings Hierarchy

Claude Code có 5 lớp settings, scope cụ thể hơn override scope rộng hơn.

[Nguồn: Claude Code Docs — Settings]

### Thứ tự ưu tiên (cao → thấp)

| # | Scope | Vị trí | Chia sẻ |
|---|-------|--------|---------|
| 1 | **Managed** | Server, plist/registry, hoặc `managed-settings.json` | IT-deployed |
| 2 | **CLI arguments** | Command line flags | N/A |
| 3 | **Local** | `.claude/settings.local.json` | Không (gitignored) |
| 4 | **Project** | `.claude/settings.json` | Git (commit) |
| 5 | **User** | `~/.claude/settings.json` | Không |

**Managed settings file paths:**
- macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
- Linux/WSL: `/etc/claude-code/managed-settings.json`
- Windows: `C:\Program Files\ClaudeCode\managed-settings.json`

**Array settings** (như `permissions.allow`, `sandbox.filesystem.allowWrite`) được **merge** qua các scopes — không replace.

**Deny rules luôn thắng:** nếu tool bị deny ở bất kỳ level nào, không level nào khác có thể allow nó.

> [!NOTE]
> CLI flags và environment variables → xem chi tiết tại [dev/02 CLI Reference](02-cli-reference.md).

### Status line

Hiển thị thông tin custom trong Claude Code UI:

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statusline.sh"
  }
}
```

Script nhận environment variable `CLAUDE_PROJECT_DIR` và output plain text single line. Ví dụ:

```bash
#!/bin/bash
echo "$(git branch --show-current) • $(node --version)"
```

### Xem settings đang active

Chạy `/status` trong session để xem sources và origins của settings hiện tại.

---

## 1.8 Checkpointing & Rewind

Claude Code tự động track file edits, cho phép rewind về trạng thái trước đó nếu có vấn đề.

[Nguồn: Claude Code Docs — Checkpointing]

### Cách hoạt động

- Mỗi user prompt tạo một checkpoint mới
- Checkpoints persist across sessions (giữ lại khi resume)
- Tự động cleanup sau 30 ngày (configurable)
- Chỉ track edits qua Claude's file tools — **không track** thay đổi từ bash commands (`rm`, `mv`, `cp`)

### Rewind

Nhấn `Esc` + `Esc` hoặc chạy `/rewind` để mở rewind menu. Chọn checkpoint rồi chọn action:

| Action | Mô tả |
|--------|--------|
| **Restore code and conversation** | Revert cả code và conversation |
| **Restore conversation** | Rewind conversation, giữ code hiện tại |
| **Restore code** | Revert files, giữ conversation |
| **Summarize from here** | Compress conversation từ điểm đó trở đi thành summary (giải phóng context) |

**Summarize vs Compact:** Summarize target một phần conversation (giữ phần đầu nguyên vẹn). `/compact` summarize toàn bộ.

---

## 1.9 `/doctor` — Diagnostics

Chạy `/doctor` khi gặp vấn đề. Command này kiểm tra:

[Nguồn: Claude Code Docs — Troubleshooting]

- Installation type, version, search functionality
- Auto-update status và available versions
- Invalid settings files (malformed JSON, incorrect types)
- MCP server configuration errors
- Keybinding configuration problems
- Context usage warnings (large CLAUDE.md, high MCP token usage)
- Plugin và agent loading errors

---

## 1.10 Tổng hợp: Cấu hình từ zero đến production

Workflow setup cho developer mới:

1. **Cài đặt** Claude Code (native install khuyến nghị)
2. **Đăng nhập** — `claude` → browser auth
3. **`/init`** — generate CLAUDE.md từ codebase
4. **Tạo `.claude/rules/`** — thêm path-specific rules nếu cần
5. **`/permissions`** — setup allow/deny rules cho workflow
6. **`/sandbox`** — bật sandbox nếu muốn giảm permission prompts
7. **`/doctor`** — verify mọi thứ hoạt động

**Tips:**
- Giữ CLAUDE.md dưới 200 dòng — dùng `@imports` hoặc `.claude/rules/` khi cần mở rộng
- Dùng `.claude/settings.local.json` cho preferences cá nhân (không commit vào git)
- Review auto memory định kỳ qua `/memory`
- Xem thêm setup cho claude.ai (web/mobile) tại [base/02 Setup](../base/02-setup.md)
- Kiến trúc đầy đủ 6 lớp cấu hình: [Config Architecture](../reference/config-architecture.md)

---

← [Tổng quan](../base/00-overview.md) | [CLI Reference →](02-cli-reference.md)
