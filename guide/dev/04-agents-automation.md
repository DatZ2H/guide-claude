# Agents & Automation

**Thời gian đọc:** 30 phút | **Mức độ:** Intermediate-Advanced
**Cập nhật:** 2026-03-07 | Models: xem [specs](../reference/model-specs.md)

---
depends-on: [dev/01-claude-code-setup, dev/02-cli-reference, dev/03-ide-integration]
impacts: [dev/05-plugins, dev/06-dev-workflows]
---

Module này hướng dẫn hệ thống subagents trong Claude Code — cách dùng built-in agents, tạo custom agents, và các patterns hiệu quả. Phần Agent Teams (experimental) và CI/CD orchestration sẽ được trình bày trong session tiếp theo (S20).

[Nguồn: Claude Code Docs] [Cập nhật 03/2026]

---

## 4.1 Subagents là gì?

Subagents là các AI assistants chuyên biệt chạy trong context window riêng với system prompt, tool access, và permissions độc lập. Khi Claude nhận task phù hợp với description của subagent, nó tự động delegate sang subagent đó. Subagent làm việc độc lập và trả kết quả về conversation chính.

[Nguồn: Claude Code Docs — Sub-agents]

Subagents giúp:

- **Bảo toàn context** — exploration và implementation chạy riêng, không chiếm context chính
- **Kiểm soát tool access** — giới hạn tools mỗi subagent được dùng
- **Tái sử dụng** — user-level subagents dùng được mọi project
- **Chuyên biệt hóa** — system prompt riêng cho từng domain
- **Tiết kiệm chi phí** — route tasks sang model rẻ hơn (vd: Haiku)

> [!IMPORTANT]
> Subagents KHÔNG THỂ spawn subagents khác. Nếu cần nested delegation, dùng [Skills](../reference/skills-list.md) hoặc chain subagents từ conversation chính.

---

## 4.2 Built-in subagents

Claude Code có sẵn các subagents tự động kích hoạt khi phù hợp. Tất cả đều inherit permissions từ conversation chính.

[Nguồn: Claude Code Docs — Sub-agents]

| Subagent | Model | Tools | Mục đích |
|----------|-------|-------|----------|
| **Explore** | Haiku (nhanh) | Read-only | File discovery, code search, codebase exploration |
| **Plan** | Inherit | Read-only | Research cho plan mode — gather context trước khi lập plan |
| **General-purpose** | Inherit | All tools | Complex research, multi-step operations, code modifications |
| **Bash** | Inherit | Terminal commands | Chạy commands trong context riêng |
| **statusline-setup** | Sonnet | Read, Edit | Configure status line (khi chạy `/statusline`) |
| **Claude Code Guide** | Haiku | Read-only | Trả lời câu hỏi về Claude Code features |

### Explore subagent

Khi Claude cần tìm kiếm hoặc phân tích codebase mà không cần chỉnh sửa, nó delegate sang Explore. Kết quả exploration ở trong context riêng, chỉ summary trả về conversation chính.

Claude chỉ định mức độ thoroughness khi invoke:
- **quick** — targeted lookups, tìm 1 file hoặc function cụ thể
- **medium** — balanced exploration
- **very thorough** — comprehensive analysis qua nhiều locations

### Plan subagent

Khi bạn ở [plan mode](../base/04-context-management.md) và Claude cần research codebase, nó delegate sang Plan subagent. Điều này ngăn infinite nesting vì subagents không thể spawn subagents khác.

### General-purpose subagent

Dùng cho tasks phức tạp cần cả exploration lẫn modification, complex reasoning, hoặc nhiều dependent steps. Có access tất cả tools.

---

## 4.3 Tạo custom subagent

Custom subagents được định nghĩa bằng file Markdown với YAML frontmatter. Có 2 cách tạo: interactive (`/agents`) hoặc manual (viết file trực tiếp).

[Nguồn: Claude Code Docs — Sub-agents]

### Cách 1: Interactive với /agents

```text
/agents
```

Chọn **Create new agent** → chọn scope (User-level hoặc Project-level) → chọn **Generate with Claude** hoặc viết thủ công → chọn tools → chọn model → chọn color → Save.

Subagent có hiệu lực ngay — không cần restart session.

### Cách 2: Viết file thủ công

Tạo file `.md` trong thư mục agents tương ứng:

```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer. When invoked, analyze the code and provide
specific, actionable feedback on quality, security, and best practices.
```

Phần frontmatter chứa config, phần body là system prompt. Subagent chỉ nhận system prompt này (cùng basic environment details), không nhận full Claude Code system prompt.

> [!NOTE]
> File-based subagents được load lúc session start. Nếu tạo thủ công giữa session, dùng `/agents` để load ngay.

---

## 4.4 Frontmatter fields

Bảng đầy đủ các fields hỗ trợ trong YAML frontmatter. Chỉ `name` và `description` là bắt buộc.

[Nguồn: Claude Code Docs — Sub-agents]

| Field | Bắt buộc | Mô tả |
|-------|:--------:|-------|
| `name` | ✅ | Identifier duy nhất — lowercase, dấu gạch ngang |
| `description` | ✅ | Khi nào Claude nên delegate sang subagent này |
| `tools` | | Tools được phép (allowlist). Inherit all nếu bỏ trống |
| `disallowedTools` | | Tools bị chặn (denylist) — loại khỏi inherited/specified list |
| `model` | | `sonnet`, `opus`, `haiku`, hoặc `inherit`. Default: `inherit` |
| `permissionMode` | | `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`, `plan` |
| `maxTurns` | | Số turns tối đa trước khi subagent dừng |
| `skills` | | Skills inject vào context lúc startup (full content, không chỉ tên) |
| `mcpServers` | | MCP servers available — tên server hoặc inline definition |
| `hooks` | | Lifecycle hooks scoped cho subagent này |
| `memory` | | Persistent memory scope: `user`, `project`, hoặc `local` |
| `background` | | `true` để luôn chạy background. Default: `false` |
| `isolation` | | `worktree` để chạy trong git worktree riêng biệt |

### Tools — allowlist và denylist

Dùng `tools` (allowlist) hoặc `disallowedTools` (denylist) để kiểm soát:

```yaml
---
name: safe-researcher
description: Research agent with restricted capabilities
tools: Read, Grep, Glob, Bash
disallowedTools: Write, Edit
---
```

Để giới hạn subagent types có thể spawn (khi chạy với `claude --agent`):

```yaml
---
name: coordinator
description: Coordinates work across specialized agents
tools: Agent(worker, researcher), Read, Bash
---
```

Chỉ `worker` và `researcher` được phép spawn. Bỏ `Agent` khỏi tools list = không spawn được subagent nào.

> [!NOTE]
> Cú pháp `Agent(type)` chỉ có hiệu lực khi agent chạy làm main thread với `claude --agent`. Subagents không thể spawn subagents khác nên field này không ảnh hưởng trong subagent definitions.

### Permission modes

| Mode | Hành vi |
|------|---------|
| `default` | Standard — prompt user khi cần |
| `acceptEdits` | Auto-accept file edits |
| `dontAsk` | Auto-deny prompts (tools đã allow vẫn hoạt động) |
| `bypassPermissions` | Skip mọi permission checks |
| `plan` | Read-only exploration |

> [!WARNING]
> `bypassPermissions` bỏ qua mọi kiểm tra — dùng cẩn thận. Nếu parent dùng `bypassPermissions`, subagent không thể override.

### Preload skills

Field `skills` inject full content của skill vào context subagent lúc startup:

```yaml
---
name: api-developer
description: Implement API endpoints following team conventions
skills:
  - api-conventions
  - error-handling-patterns
---
```

Subagents KHÔNG inherit skills từ conversation chính — phải list rõ từng skill cần dùng.

---

## 4.5 Agent scopes

Subagents lưu ở các vị trí khác nhau tùy phạm vi sử dụng. Khi trùng tên, vị trí priority cao hơn thắng.

[Nguồn: Claude Code Docs — Sub-agents]

| Vị trí | Scope | Priority |
|--------|-------|:--------:|
| `--agents` CLI flag | Session hiện tại | 1 (cao nhất) |
| `.claude/agents/` | Project hiện tại | 2 |
| `~/.claude/agents/` | Tất cả projects | 3 |
| Plugin `agents/` directory | Nơi plugin enabled | 4 (thấp nhất) |

### Session-level agents (CLI flag)

Truyền JSON khi launch Claude Code — chỉ tồn tại trong session đó, không lưu disk:

```bash
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer. Focus on code quality, security, and best practices.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  }
}'
```

Flag `--agents` chấp nhận JSON với các fields giống frontmatter: `description`, `prompt`, `tools`, `disallowedTools`, `model`, `permissionMode`, `mcpServers`, `hooks`, `maxTurns`, `skills`, `memory`. Field `prompt` tương đương markdown body trong file-based agents.

### Project-level agents

File `.claude/agents/*.md` — lý tưởng cho subagents đặc thù project. Commit vào version control để team cùng dùng.

### User-level agents

File `~/.claude/agents/*.md` — personal subagents dùng mọi project.

### Plugin agents

Đi kèm [plugins](05-plugins.md) đã cài. Xuất hiện trong `/agents` cùng custom agents.

### Quản lý agents

```bash
# Interactive — view, create, edit, delete
/agents

# CLI — list tất cả agents (grouped by source)
claude agents
```

### Disable specific subagents

Chặn Claude dùng subagent cụ thể qua [settings](../reference/config-architecture.md):

```json
{
  "permissions": {
    "deny": ["Agent(Explore)", "Agent(my-custom-agent)"]
  }
}
```

Hoặc qua CLI flag:

```bash
claude --disallowedTools "Agent(Explore)"
```

---

## 4.6 Persistent memory cho subagents

Field `memory` cho phép subagent lưu knowledge xuyên sessions — codebase patterns, debugging insights, architectural decisions.

[Nguồn: Claude Code Docs — Sub-agents]

```yaml
---
name: code-reviewer
description: Reviews code for quality and best practices
memory: user
---

You are a code reviewer. As you review code, update your agent memory with
patterns, conventions, and recurring issues you discover.
```

### Memory scopes

| Scope | Vị trí | Dùng khi |
|-------|--------|----------|
| `user` | `~/.claude/agent-memory/<name>/` | Knowledge áp dụng mọi project |
| `project` | `.claude/agent-memory/<name>/` | Knowledge project-specific, share qua version control |
| `local` | `.claude/agent-memory-local/<name>/` | Knowledge project-specific, KHÔNG commit |

Khi memory enabled:

- System prompt tự động include instructions read/write memory directory
- 200 dòng đầu `MEMORY.md` trong memory directory được inject vào context
- Tools Read, Write, Edit tự động enabled để quản lý memory files

### Tips sử dụng memory

- `user` là scope recommended mặc định. Dùng `project` hoặc `local` khi knowledge chỉ relevant cho 1 codebase
- Yêu cầu subagent tham khảo memory trước khi bắt đầu: "Review this PR, and check your memory for patterns you've seen before"
- Yêu cầu update memory sau task: "Save what you learned to your memory"
- Include memory instructions trực tiếp trong system prompt:

```markdown
Update your agent memory as you discover codepaths, patterns, library
locations, and key architectural decisions. This builds up institutional
knowledge across conversations.
```

---

## 4.7 Hooks cho subagents

Có 2 nơi configure hooks liên quan đến subagents.

[Nguồn: Claude Code Docs — Sub-agents]

### Hooks trong frontmatter (scoped cho subagent)

Chạy chỉ khi subagent đó active — tự cleanup khi subagent finish.

| Event | Matcher input | Khi nào fire |
|-------|---------------|-------------|
| `PreToolUse` | Tool name | Trước khi subagent dùng tool |
| `PostToolUse` | Tool name | Sau khi subagent dùng tool |
| `Stop` | (none) | Khi subagent finish (convert sang `SubagentStop` at runtime) |

Ví dụ — validate Bash commands + lint sau edits:

```yaml
---
name: code-reviewer
description: Review code changes with automatic linting
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-command.sh"
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "./scripts/run-linter.sh"
---
```

### Hooks trong settings.json (project-level lifecycle)

Respond khi subagents start hoặc stop trong main session:

| Event | Matcher input | Khi nào fire |
|-------|---------------|-------------|
| `SubagentStart` | Agent type name | Khi subagent bắt đầu |
| `SubagentStop` | Agent type name | Khi subagent hoàn thành |

```json
{
  "hooks": {
    "SubagentStart": [
      {
        "matcher": "db-agent",
        "hooks": [
          { "type": "command", "command": "./scripts/setup-db-connection.sh" }
        ]
      }
    ],
    "SubagentStop": [
      {
        "hooks": [
          { "type": "command", "command": "./scripts/cleanup-db-connection.sh" }
        ]
      }
    ]
  }
}
```

---

## 4.8 Patterns sử dụng subagents

Các patterns đã verified hiệu quả khi làm việc với subagents.

[Nguồn: Claude Code Docs — Sub-agents]

### Pattern 1: Isolate high-volume operations

Delegate tasks tạo nhiều output (chạy tests, fetch docs, process logs) sang subagent. Verbose output ở trong context riêng, chỉ summary trả về.

```text
Use a subagent to run the test suite and report only the failing tests
with their error messages
```

### Pattern 2: Parallel research

Spawn nhiều subagents đồng thời cho các investigations độc lập:

```text
Research the authentication, database, and API modules in parallel
using separate subagents
```

Mỗi subagent explore riêng, Claude tổng hợp findings. Hiệu quả nhất khi các research paths không phụ thuộc nhau.

> [!WARNING]
> Khi subagents hoàn thành, kết quả trả về main conversation. Nhiều subagents với detailed results có thể chiếm đáng kể context. Cho tasks cần sustained parallelism, cân nhắc Agent Teams.

### Pattern 3: Chain subagents

Cho multi-step workflows — mỗi subagent hoàn thành task, trả kết quả cho Claude, Claude pass context sang subagent tiếp:

```text
Use the code-reviewer subagent to find performance issues,
then use the optimizer subagent to fix them
```

### Pattern 4: Foreground vs Background

- **Foreground** (default) — block conversation chính. Permission prompts pass through đến user
- **Background** — chạy đồng thời. Claude prompt permissions trước khi launch, auto-deny gì chưa approved

```text
Run this in the background
```

Hoặc nhấn **Ctrl+B** để background task đang chạy. Nếu background subagent fail do thiếu permissions, có thể resume trong foreground.

Disable background tasks:

```bash
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1
```

### Pattern 5: Resume subagents

Mỗi invocation tạo instance mới. Để tiếp tục context cũ thay vì start fresh:

```text
Continue that code review and now analyze the authorization logic
```

Claude resume subagent với full conversation history — tool calls, results, reasoning. Transcripts lưu tại `~/.claude/projects/{project}/{sessionId}/subagents/agent-{agentId}.jsonl`.

Subagent transcripts tồn tại độc lập với main conversation:

- Main conversation compaction không ảnh hưởng subagent transcripts
- Có thể resume subagent sau khi restart Claude Code (cùng session)
- Auto-cleanup theo `cleanupPeriodDays` setting (default: 30 ngày)

### Auto-compaction

Subagents tự động compact ở ~95% capacity. Điều chỉnh:

```bash
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50
```

---

## 4.9 Khi nào dùng subagent vs main conversation

| Tình huống | Dùng | Lý do |
|-----------|------|-------|
| Cần back-and-forth, iterative refinement | Main conversation | Subagent không interactive |
| Nhiều phases share context (plan → implement → test) | Main conversation | Tránh re-gather context |
| Quick, targeted change | Main conversation | Subagent tốn latency gather context |
| Task tạo verbose output | Subagent | Giữ context chính sạch |
| Cần giới hạn tool access | Subagent | Enforce tool restrictions |
| Task self-contained, trả summary | Subagent | Tận dụng context isolation |

Cân nhắc dùng [Skills](../reference/skills-list.md) khi cần reusable prompts chạy trong main conversation context thay vì isolated subagent context.

---

## 4.10 Example subagents

Các ví dụ mẫu để bắt đầu nhanh — có thể customize hoặc dùng `/agents` → Generate with Claude.

[Nguồn: Claude Code Docs — Sub-agents]

### Code reviewer (read-only)

```markdown
---
name: code-reviewer
description: Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code.
tools: Read, Grep, Glob, Bash
model: inherit
---

You are a senior code reviewer ensuring high standards of code quality
and security.

When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately

Review checklist:
- Code is clear and readable
- No duplicated code
- Proper error handling
- No exposed secrets or API keys
- Input validation implemented
- Good test coverage

Provide feedback organized by priority:
- Critical issues (must fix)
- Warnings (should fix)
- Suggestions (consider improving)
```

### Debugger (read + write)

```markdown
---
name: debugger
description: Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues.
tools: Read, Edit, Bash, Grep, Glob
---

You are an expert debugger specializing in root cause analysis.

When invoked:
1. Capture error message and stack trace
2. Identify reproduction steps
3. Isolate the failure location
4. Implement minimal fix
5. Verify solution works

Focus on fixing the underlying issue, not the symptoms.
```

### Database query validator (hooks example)

Cho phép Bash nhưng validate chỉ read-only SQL queries qua `PreToolUse` hook:

```markdown
---
name: db-reader
description: Execute read-only database queries. Use when analyzing data or generating reports.
tools: Bash
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-readonly-query.sh"
---

You are a database analyst with read-only access.
Execute SELECT queries to answer questions about the data.
```

Script validation (`./scripts/validate-readonly-query.sh`):

```bash
#!/bin/bash
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

if echo "$COMMAND" | grep -iE '\b(INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|TRUNCATE)\b' > /dev/null; then
  echo "Blocked: Only SELECT queries are allowed" >&2
  exit 2  # Exit code 2 = block operation
fi
exit 0
```

---

## 4.11 Anti-patterns khi dùng Claude Code

Những patterns thoạt nhìn hợp lý nhưng thực tế làm giảm chất lượng và hiệu quả.

[Nguồn: Anthropic — Claude Code Best Practices]

### Kitchen Sink — Nhồi quá nhiều vào 1 prompt

Prompt dài > 500 token, attach nhiều file không liên quan, instructions có > 20 rules. Claude bị overwhelmed — ưu tiên sai, bỏ sót yêu cầu quan trọng.

**Fix:**

- 1 prompt = 1 task rõ ràng
- Chỉ include files Claude thực sự cần đọc hoặc sửa
- CLAUDE.md: giữ core conventions, không liệt kê mọi edge case

### Correcting Loop — Vòng lặp sửa lỗi không thoát

Claude sửa sai → bạn sửa → Claude sửa lại → vẫn sai. Sau 3+ iterations, output ngày càng tệ — context bị "poisoned" bởi corrections mâu thuẫn.

**Fix:**

- Sau 2-3 lần sửa không hiệu quả → dừng, conversation mới
- Viết lại prompt gốc với constraints rõ hơn thay vì patch
- `/clear` để reset context và thử approach khác

### Over-specified CLAUDE.md — Quá nhiều rules

CLAUDE.md > 200 dòng, rules cho edge cases hiếm, rules mâu thuẫn. Claude xử lý quá nhiều instructions → conflict → chọn rules sai.

**Fix:**

- CLAUDE.md: chỉ conventions bắt buộc và decisions đã chốt
- Rules tình huống cụ thể → đặt trong prompt khi cần, không global
- Định kỳ review và prune: xóa rules không còn relevant

### Trust-then-Verify Gap — Tin tuyệt đối output

Approve mọi tool call không đọc, commit code chưa test, apply changes không review diff.

**Fix:**

- Review mọi file change trước khi approve — đặc biệt `Edit`, `Write`, `Bash` destructive
- Chạy tests sau mỗi thay đổi đáng kể
- Git checkpoint trước mỗi task lớn

### Infinite Exploration — Khám phá không kết thúc

Claude chạy 10+ Read/Grep trước khi edit, hỏi clarification liên tục, tạo plan dài mà không bắt đầu.

**Fix:**

- Cung cấp đủ context từ đầu: file paths, function names, scope
- Viết rõ expected actions: "Edit file X, function Y, thay đổi Z"
- `/clear` nếu Claude trong exploration loop không thoát được

---

← [IDE Integration](03-ide-integration.md) | [Tổng quan](../base/00-overview.md) | [Plugins →](05-plugins.md)
