# Dev Workflows

**Thời gian đọc:** 30 phút | **Mức độ:** Intermediate-Advanced
**Cập nhật:** 2026-03-07 | Models: xem [specs](../reference/model-specs.md)

---
depends-on: [dev/01-claude-code-setup, dev/02-cli-reference, dev/03-ide-integration, dev/04-agents-automation]
impacts: [reference/ecosystem-overview]
---

Module này tổng hợp các workflow thực tế khi dùng Claude Code cho development — từ git, testing, code review, debugging đến session management, batch operations, remote workflows, và cross-surface patterns.

[Nguồn: Claude Code Docs — Common Workflows, Best Practices] [Cập nhật 03/2026]

---

## 6.1 Git Workflows

Claude Code tích hợp sâu với git — tạo commits, PRs, branches, và xử lý merge conflicts trực tiếp từ conversation.

[Nguồn: Claude Code Docs — Common Workflows]

### Commits

Mô tả thay đổi bằng ngôn ngữ tự nhiên — Claude tạo commit message phù hợp:

```text
create a commit for my changes with a descriptive message
```

Hoặc scope hẹp hơn với `--allowedTools`:

```bash
claude -p "Look at my staged changes and create an appropriate commit" \
  --allowedTools "Bash(git diff *),Bash(git log *),Bash(git status *),Bash(git commit *)"
```

[Nguồn: Claude Code Docs — Headless]

### Pull Requests

```text
create a pr for my changes
```

Claude tự summarize changes, tạo PR title + description, và chạy `gh pr create`. Sau khi tạo, session tự động link với PR — resume sau bằng:

```bash
claude --from-pr 123
```

### Branches và Worktrees

Dùng `--worktree` (`-w`) để chạy nhiều Claude sessions song song trên cùng repo mà không conflict:

```bash
# Session 1: feature mới
claude --worktree feature-auth

# Session 2: bug fix song song
claude --worktree bugfix-123

# Auto-generate tên
claude --worktree
```

Worktrees được tạo tại `<repo>/.claude/worktrees/<name>` với branch `worktree-<name>`. Khi exit:
- Không có thay đổi: worktree tự xóa
- Có thay đổi: Claude hỏi giữ hay xóa

> [!TIP]
> Thêm `.claude/worktrees/` vào `.gitignore` để tránh hiển thị untracked files.

Chi tiết worktrees trong subagents: xem [dev/04 — Subagent Worktrees](04-agents-automation.md).

### Merge Conflicts

```text
resolve the merge conflicts in src/auth/login.ts
```

Claude đọc conflict markers, phân tích both sides, và chọn resolution phù hợp. Nên review kết quả trước khi commit.

---

## 6.2 Testing

Claude Code hỗ trợ full testing workflow — từ viết tests đến chạy và fix failures.

[Nguồn: Claude Code Docs — Common Workflows]

### Viết tests

```text
find functions in NotificationsService.swift that are not covered by tests
```

```text
add tests for the notification service, covering edge cases
```

Claude phân tích test files hiện có để match style, framework, và assertion patterns đã dùng trong project.

### Chạy và fix failures

```text
run the test suite and fix any failures
```

Trong headless mode — hữu ích cho CI:

```bash
claude -p "Run the test suite and fix any failures" \
  --allowedTools "Bash,Read,Edit"
```

### Verification-first approach

Best practice quan trọng nhất: **cho Claude cách verify kết quả**.

[Nguồn: Claude Code Docs — Best Practices]

| Strategy | Trước | Sau |
|----------|-------|-----|
| Test cases | "implement validateEmail" | "write validateEmail. test: user@example.com → true, invalid → false. run tests after" |
| Visual verify | "make dashboard look better" | "[paste screenshot] implement this design, screenshot result and compare" |
| Root cause | "build is failing" | "build fails with [error]. fix and verify build succeeds. address root cause" |

---

## 6.3 Code Review

Claude Code có thể review code với nhiều góc nhìn khác nhau — từ general review đến security-focused.

[Nguồn: Claude Code Docs — Common Workflows, Best Practices]

### Review tự động

```text
review my recent code changes for security issues
```

```text
summarize the changes I've made to the authentication module
```

### Custom review agents

Tạo subagent chuyên review trong `.claude/agents/`:

```markdown
---
name: security-reviewer
description: Reviews code for security vulnerabilities
tools: Read, Grep, Glob, Bash
model: opus
---
You are a senior security engineer. Review code for:
- Injection vulnerabilities (SQL, XSS, command injection)
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure data handling

Provide specific line references and suggested fixes.
```

[Nguồn: Claude Code Docs — Best Practices]

### Writer/Reviewer pattern

Dùng 2 sessions riêng biệt — session review có clean context, không bị bias bởi code vừa viết:

| Session A (Writer) | Session B (Reviewer) |
|--------------------|-----------------------|
| `Implement rate limiter for API` | |
| | `Review rate limiter in @src/middleware/rateLimiter.ts. Look for edge cases, race conditions` |
| `Address review feedback: [paste]` | |

---

## 6.4 Debugging

Claude Code hỗ trợ debugging qua nhiều kênh — từ error messages đến screenshots và MCP tools.

[Nguồn: Claude Code Docs — Common Workflows]

### Error-driven debugging

```text
I'm seeing this error when I run npm test: [paste error]
```

```text
suggest a few ways to fix the @ts-ignore in user.ts
```

> [!TIP]
> Cung cấp command để reproduce, steps to reproduce, và ghi chú error intermittent hay consistent giúp Claude debug chính xác hơn.

### Screenshots và images

Claude Code hỗ trợ phân tích hình ảnh:

- **Drag & drop** ảnh vào Claude Code window
- **Ctrl+V** paste ảnh từ clipboard
- **Path**: `"Analyze this image: /path/to/screenshot.png"`

Hữu ích cho UI debugging, design comparison, error screenshots, và diagram analysis.

### /doctor diagnostics

```text
/doctor
```

Chạy diagnostics kiểm tra configuration, permissions, và environment. Chi tiết: xem [dev/01](01-claude-code-setup.md).

### MCP debugging tools

Kết nối Chrome hoặc Playwright qua MCP để debug UI trực tiếp:

```bash
# Chrome MCP — cho phép Claude điều khiển browser
claude mcp add chrome-mcp -- npx @anthropic-ai/chrome-mcp

# Playwright MCP — automated browser testing
claude mcp add playwright -- npx @anthropic-ai/playwright-mcp
```

Chi tiết MCP setup: xem [dev/05](05-plugins.md).

---

## 6.5 Session Management

Quản lý sessions hiệu quả là kỹ năng quan trọng — ảnh hưởng trực tiếp đến chất lượng output.

[Nguồn: Claude Code Docs — Common Workflows, Best Practices]

### Resume conversations

```bash
# Tiếp tục conversation gần nhất
claude --continue       # hoặc -c

# Chọn từ danh sách sessions
claude --resume         # hoặc -r (interactive picker)

# Resume theo tên
claude --resume auth-refactor

# Resume session linked với PR
claude --from-pr 123
```

Trong session đang chạy:

```text
/resume             # mở picker
/resume auth-refactor  # resume theo tên
```

### Đặt tên sessions

```text
/rename auth-refactor
```

Trong picker, nhấn `R` để rename. Best practice: đặt tên sớm khi bắt đầu task mới — dễ tìm lại hơn.

### Session picker shortcuts

| Phím | Chức năng |
|------|-----------|
| `↑`/`↓` | Di chuyển giữa sessions |
| `Enter` | Chọn và resume |
| `P` | Preview session content |
| `R` | Rename session |
| `/` | Search filter |
| `A` | Toggle current directory / all projects |
| `B` | Filter theo git branch hiện tại |

### Context management

```text
/clear              # Reset context — dùng giữa tasks không liên quan
/compact             # Summarize để giải phóng context
/compact Focus on API changes  # Compact với hướng dẫn cụ thể
```

> [!IMPORTANT]
> Sau 2 lần sửa cùng một lỗi mà Claude vẫn sai: chạy `/clear` và viết prompt mới tốt hơn. Clean session + better prompt luôn hiệu quả hơn session dài với nhiều corrections.

### Checkpointing và Rewind

Mỗi prompt tạo checkpoint tự động. Nhấn `Esc + Esc` hoặc `/rewind` để mở menu:

- **Restore code and conversation** — revert cả hai
- **Restore conversation** — rewind messages, giữ code hiện tại
- **Restore code** — revert files, giữ conversation
- **Summarize from here** — compact từ điểm này, giải phóng context

Checkpoints persist across sessions — đóng terminal vẫn rewind được sau.

[Nguồn: Claude Code Docs — Checkpointing]

### Fork sessions

```bash
claude --continue --fork-session
```

Tạo branch mới từ conversation hiện tại — thử approach khác mà không mất session gốc. Forked sessions hiển thị grouped trong picker.

[Nguồn: Claude Code Docs — Sessions]

---

## 6.6 Batch Operations và Headless Mode

Dùng `claude -p` để tích hợp Claude Code vào scripts, CI/CD, và automation pipelines.

[Nguồn: Claude Code Docs — Headless, Best Practices]

### Piping data

```bash
# Pipe input → Claude → output
cat build-error.txt | claude -p 'explain the root cause of this build error' > output.txt

# Linting với Claude
cat code.py | claude -p 'analyze this code for bugs' --output-format json > analysis.json
```

### Output formats

| Format | Flag | Khi nào dùng |
|--------|------|-------------|
| Text | `--output-format text` | Default — simple integrations |
| JSON | `--output-format json` | Scripts cần metadata (session ID, cost) |
| Stream JSON | `--output-format stream-json` | Real-time processing |

### Structured output với JSON Schema

```bash
claude -p "Extract function names from auth.py" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"functions":{"type":"array","items":{"type":"string"}}}}'
```

### Fan-out pattern

Distribute tasks across nhiều Claude invocations song song:

```bash
# Bước 1: Generate task list
claude -p "List all Python files needing migration" > files.txt

# Bước 2: Loop through
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue. Return OK or FAIL." \
    --allowedTools "Edit,Bash(git commit *)"
done
```

### CI/CD integration

```json
{
  "scripts": {
    "lint:claude": "claude -p 'you are a linter. look at changes vs main and report issues related to typos. report filename:line on one line, description on second line.'"
  }
}
```

Chi tiết GitHub Actions và GitLab CI/CD: xem [dev/04](04-agents-automation.md).

---

## 6.7 Remote Workflows

Claude Code hỗ trợ làm việc từ xa qua Remote Control và Web interface — tiếp tục session từ bất kỳ thiết bị nào.

[Nguồn: Claude Code Docs — Remote Control, Claude Code on the Web]

### Remote Control (local → mobile/browser)

Remote Control kết nối claude.ai/code hoặc Claude app (iOS/Android) với session đang chạy trên máy local. Code vẫn chạy local — web/mobile chỉ là window.

```bash
# Bắt đầu remote session mới
claude remote-control
claude remote-control --name "My Project"

# Từ session đang chạy
/remote-control
/rc
```

Flags: `--verbose`, `--sandbox`/`--no-sandbox`.

Kết nối từ thiết bị khác:
- Mở session URL hiển thị trong terminal
- Scan QR code (nhấn `Space` để hiện)
- Mở claude.ai/code → tìm session trong list

Bật auto cho mọi session: `/config` → Enable Remote Control → `true`.

### Claude Code on the Web (cloud)

Chạy Claude Code trên cloud infrastructure — không cần local setup:

```bash
# Từ terminal — tạo web session mới
claude --remote "Fix authentication bug in src/auth/login.ts"

# Nhiều tasks song song
claude --remote "Fix flaky test"
claude --remote "Update API docs"
claude --remote "Refactor logger"
```

### /teleport (web → local)

Kéo web session về terminal local:

```text
/teleport           # hoặc /tp — interactive picker
```

```bash
claude --teleport          # picker từ CLI
claude --teleport <id>     # resume session cụ thể
```

Yêu cầu: clean git state, đúng repo, branch available, cùng account.

### So sánh Remote Control vs Web

| | Remote Control | Claude Code on the Web |
|--|----------------|----------------------|
| Code chạy ở | Local machine | Anthropic cloud |
| MCP servers | Có (local) | Không |
| Cần local setup | Có | Không |
| Dùng khi | Đang làm local, muốn tiếp từ mobile | Task mới, không cần local, parallel work |

---

## 6.8 Cross-Surface Patterns

Claude Code hoạt động trên nhiều surfaces — mỗi surface phù hợp cho scenarios khác nhau. Setup từng surface: xem [dev/03](03-ide-integration.md).

[Nguồn: Claude Code Docs — Best Practices] [Ứng dụng Kỹ thuật]

### Chọn surface theo task

| Task | Surface khuyến nghị | Lý do |
|------|---------------------|-------|
| Scripting, automation, CI/CD | Terminal CLI | Full control, piping, headless mode |
| Daily coding, file editing | VS Code extension | Inline diffs, @-mentions, integrated terminal |
| Visual review, parallel sessions | Desktop app | Multi-session UI, visual diffs |
| Long-running tasks, remote repos | Web (claude.ai/code) | Cloud infra, không cần local |
| Monitor, quick steering | Mobile (Remote Control) | Convenience, anywhere access |

### Workflow switching patterns

**Pattern 1: Plan locally → Execute remotely**

```bash
# 1. Plan mode — explore và lên kế hoạch
claude --permission-mode plan
# → "Analyze auth system and create migration plan"

# 2. Execute trên cloud
claude --remote "Execute migration plan in docs/migration-plan.md"
```

**Pattern 2: Terminal → Mobile monitoring**

```bash
# 1. Bắt đầu task dài trên terminal
claude
# → "Refactor entire auth module..."

# 2. Bật remote control
/rc

# 3. Scan QR → monitor từ mobile
```

**Pattern 3: Web → Local finish**

```bash
# 1. Kick off trên web (claude.ai/code)
# → "Implement new API endpoints"

# 2. Khi cần local tools/testing
/teleport
# → Tiếp tục với full local environment
```

**Pattern 4: Writer/Reviewer across surfaces**

```text
VS Code (Writer): implement feature
Terminal (Reviewer): claude -p "review @src/feature.ts for edge cases" --output-format json
```

---

## 6.9 Extended Thinking trong Workflows

Extended thinking được bật mặc định — Claude tự suy luận trước khi trả lời. Effort level kiểm soát mức độ thinking: `low` cho tasks đơn giản, `high` cho complex reasoning.

[Nguồn: Claude Code Docs — Extended Thinking] [Cập nhật 03/2026]

### Cấu hình thinking

| Scope | Cách cấu hình |
|-------|---------------|
| Effort level | `/model` hoặc `CLAUDE_CODE_EFFORT_LEVEL` (low/medium/high) |
| `ultrathink` | Thêm "ultrathink" vào prompt — set effort high cho turn đó |
| Toggle | `Alt+T` bật/tắt cho session hiện tại |
| Global default | `/config` → toggle thinking mode |

Extended thinking hữu ích nhất cho: architectural decisions, challenging bugs, multi-step planning, và tradeoff evaluation.

---

## 6.10 Best Practices tổng hợp

[Nguồn: Claude Code Docs — Best Practices]

### Context management

- **`/clear` giữa tasks không liên quan** — tránh kitchen sink session
- **Dùng subagents cho investigation** — exploration chạy context riêng, giữ main context sạch
- **Scope investigations** — "check auth flow in src/auth/" thay vì "investigate authentication"
- **Track context usage** qua [status line](01-claude-code-setup.md)

### Prompt effectiveness

- **Scope cụ thể** — file nào, scenario nào, test preferences
- **Reference patterns** — `"look at HotDogWidget.php, follow the pattern"`
- **Mô tả symptoms** — `"login fails after session timeout, check src/auth/"`
- **Dùng `@` references** — `@src/utils/auth.js` thay vì mô tả path

### Workflow patterns

- **Explore → Plan → Implement → Commit** — tách exploration khỏi implementation
- **Verification-first** — luôn cung cấp cách verify (tests, scripts, screenshots)
- **Course-correct sớm** — `Esc` để dừng, redirect ngay khi thấy sai hướng
- **Checkpoint trước risky changes** — `Esc + Esc` để rewind nếu cần

Chi tiết anti-patterns: xem [dev/04 — Anti-patterns](04-agents-automation.md#411-anti-patterns-khi-dùng-claude-code).

---

← [Plugins](05-plugins.md) | [Tổng quan](../base/00-overview.md)
