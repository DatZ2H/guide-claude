# Agents & Automation

**Thời gian đọc:** 30 phút | **Mức độ:** Intermediate-Advanced
**Cập nhật:** 2026-03-07 | Models: xem [specs](../reference/model-specs.md)

---
depends-on: [dev/01-claude-code-setup, dev/02-cli-reference, dev/03-ide-integration]
impacts: [dev/05-plugins, dev/06-dev-workflows]
---

Module này hướng dẫn hệ thống agents trong Claude Code — từ subagents (stable) đến Agent Teams (experimental), orchestration patterns, Git Worktrees, headless mode, và CI/CD integration.

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

## 4.12 Agent Teams (Experimental)

Agent Teams cho phép điều phối nhiều Claude Code instances làm việc song song. Một session đóng vai trò lead, phân công tasks và tổng hợp kết quả. Các teammates làm việc độc lập trong context window riêng và giao tiếp trực tiếp với nhau.

> [!WARNING]
> Agent Teams là tính năng experimental, disabled mặc định. Enable bằng cách thêm `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` vào settings hoặc environment. Có các [limitations](#limitations-của-agent-teams) về session resumption, task coordination, và shutdown behavior.

[Nguồn: Claude Code Docs — Agent Teams] [Cập nhật 03/2026]

### So sánh Subagents vs Agent Teams

Cả hai đều cho phép parallelize work, nhưng hoạt động khác nhau. Chọn dựa trên việc workers có cần giao tiếp với nhau không.

| | Subagents | Agent Teams |
|---|---|---|
| **Context** | Context riêng; kết quả trả về caller | Context riêng; hoàn toàn độc lập |
| **Communication** | Chỉ report kết quả về main agent | Teammates message trực tiếp với nhau |
| **Coordination** | Main agent quản lý tất cả | Shared task list, tự phối hợp |
| **Best for** | Tasks focused, chỉ cần kết quả | Work phức tạp cần discussion và collaboration |
| **Token cost** | Thấp hơn: results summarized về main | Cao hơn: mỗi teammate là instance riêng |

Dùng subagents khi cần workers nhanh, focused, report kết quả. Dùng Agent Teams khi teammates cần share findings, challenge lẫn nhau, và tự coordinate.

### Khi nào dùng Agent Teams

Agent Teams hiệu quả nhất cho:

- **Research & review** — nhiều teammates investigate các khía cạnh khác nhau đồng thời
- **New modules/features** — mỗi teammate own một phần riêng biệt
- **Debugging competing hypotheses** — test nhiều theories song song, converge nhanh hơn
- **Cross-layer coordination** — changes span frontend, backend, tests — mỗi layer một teammate

Agent Teams tốn nhiều tokens hơn single session. Không phù hợp cho sequential tasks, same-file edits, hoặc work có nhiều dependencies.

### Kiến trúc

| Component | Vai trò |
|-----------|---------|
| **Team lead** | Session chính — tạo team, spawn teammates, coordinate work |
| **Teammates** | Claude Code instances riêng biệt, mỗi cái work trên assigned tasks |
| **Task list** | Danh sách work items chung — teammates claim và complete |
| **Mailbox** | Hệ thống messaging giữa các agents |

Teams và tasks lưu locally:

- Team config: `~/.claude/teams/{team-name}/config.json`
- Task list: `~/.claude/tasks/{team-name}/`

---

## 4.13 Thiết lập và điều khiển Agent Teams

Enable Agent Teams và configure display, task management, hooks.

[Nguồn: Claude Code Docs — Agent Teams] [Cập nhật 03/2026]

### Enable

Thêm vào `settings.json` hoặc environment variable:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### Display modes

| Mode | Mô tả | Yêu cầu |
|------|--------|----------|
| **In-process** (default) | Tất cả teammates chạy trong terminal chính. `Shift+Down` để cycle qua teammates | Không cần setup thêm |
| **Split panes** | Mỗi teammate có pane riêng, nhìn output đồng thời | tmux hoặc iTerm2 |

Default là `"auto"` — dùng split panes nếu đang trong tmux session, in-process nếu không.

```json
{
  "teammateMode": "in-process"
}
```

Hoặc CLI flag cho single session:

```bash
claude --teammate-mode in-process
```

> [!NOTE]
> Split-pane mode không hỗ trợ trong VS Code integrated terminal, Windows Terminal, hoặc Ghostty.

### Tạo team

Mô tả task và team structure bằng natural language:

```text
Create an agent team to refactor these modules in parallel.
Spawn 3 teammates: one for auth, one for database, one for API layer.
Use Sonnet for each teammate.
```

Claude tạo team, spawn teammates, coordinate work dựa trên prompt.

### Quản lý tasks

Shared task list coordinate work across team. Tasks có 3 states: **pending**, **in progress**, **completed**. Tasks có thể depend on other tasks — pending task với unresolved dependencies không thể claimed.

- **Lead assigns** — chỉ định task cho teammate cụ thể
- **Self-claim** — sau khi finish task, teammate tự pick up task tiếp theo

Task claiming dùng file locking để tránh race conditions.

### Tương tác trực tiếp với teammates

Mỗi teammate là full Claude Code session. Có thể message bất kỳ teammate nào:

- **In-process mode**: `Shift+Down` cycle qua teammates → type message. `Enter` xem session, `Escape` interrupt, `Ctrl+T` toggle task list
- **Split-pane mode**: click vào pane của teammate

### Plan approval cho teammates

Yêu cầu teammate plan trước khi implement — teammate ở read-only plan mode cho đến khi lead approve:

```text
Spawn an architect teammate to refactor the auth module.
Require plan approval before they make any changes.
```

Lead review plan và approve/reject. Nếu reject, teammate revise và resubmit.

### Hooks cho Agent Teams

Dùng hooks để enforce quality gates khi teammates hoàn thành work.

| Event | Khi nào fire | Exit code 2 |
|-------|-------------|-------------|
| `TeammateIdle` | Teammate sắp idle | Send feedback, giữ teammate working |
| `TaskCompleted` | Task đang được mark complete | Block completion, send feedback |

### Shutdown & cleanup

```text
# Shut down teammate cụ thể
Ask the researcher teammate to shut down

# Cleanup toàn bộ team (chạy từ lead)
Clean up the team
```

> [!WARNING]
> Luôn dùng lead để cleanup. Teammates không nên run cleanup — có thể để resources trong trạng thái inconsistent. Shut down tất cả teammates trước khi cleanup.

### Limitations của Agent Teams

- **No session resumption** — `/resume` và `/rewind` không restore in-process teammates
- **Task status can lag** — teammates đôi khi không mark tasks completed, block dependent tasks
- **Shutdown chậm** — teammates finish current request trước khi shutdown
- **One team per session** — cleanup team hiện tại trước khi tạo team mới
- **No nested teams** — teammates không thể spawn teams riêng
- **Lead cố định** — không thể promote teammate lên lead
- **Permissions set at spawn** — tất cả teammates inherit lead's permission mode

---

## 4.14 Git Worktrees — parallel sessions

Git Worktrees cho phép chạy nhiều Claude Code sessions song song trên cùng repository mà không conflict. Mỗi worktree có working directory riêng với files và branch riêng, nhưng share repository history.

[Nguồn: Claude Code Docs — Common Workflows] [Cập nhật 03/2026]

### Tạo worktree

Dùng flag `--worktree` (`-w`) để tạo isolated worktree và start Claude trong đó:

```bash
# Tạo worktree với tên cụ thể
claude --worktree feature-auth

# Tạo worktree khác cho task khác
claude --worktree bugfix-123

# Auto-generate tên ngẫu nhiên
claude --worktree
```

Worktrees tạo tại `<repo>/.claude/worktrees/<name>`, branch từ default remote branch. Branch name: `worktree-<name>`.

### Subagent worktrees

Subagents cũng có thể dùng worktree isolation. Thêm `isolation: worktree` vào frontmatter:

```yaml
---
name: parallel-worker
description: Works on isolated changes
isolation: worktree
---
```

Worktree tự động cleanup khi subagent finish mà không có changes.

### Cleanup

- **Không có changes** — worktree và branch tự động xóa
- **Có changes/commits** — Claude prompt giữ hay xóa

> [!TIP]
> Thêm `.claude/worktrees/` vào `.gitignore` để tránh worktree contents xuất hiện như untracked files.

---

## 4.15 Headless mode & orchestration patterns

Claude Code có thể chạy non-interactive (headless) cho automation, scripting, và orchestration.

[Nguồn: Claude Code Docs — Common Workflows] [Cập nhật 03/2026]

### Headless mode (`claude -p`)

Chạy Claude với prompt trực tiếp, không cần interactive session:

```bash
# Basic headless
claude -p "analyze this codebase and list all API endpoints"

# Với permission mode
claude --permission-mode plan -p "suggest improvements for the auth system"

# Pipe data qua Claude
cat build-error.txt | claude -p "explain the root cause of this build error"

# Output format
claude -p "list all TODO comments" --output-format json
```

Output formats: `text` (default), `json` (full conversation log), `stream-json` (real-time).

### Orchestration pattern: Command → Agent → Skill

Pattern phân tầng cho workflow automation — mỗi layer có scope và trigger khác nhau:

| Layer | Cơ chế | Scope | Ví dụ |
|-------|--------|-------|-------|
| **Command** | `.claude/commands/` | Session entry point, user-triggered | `/start`, `/checkpoint` |
| **Agent** | `.claude/agents/` hoặc `--agent` | Autonomous worker, isolated context | `code-reviewer`, `debugger` |
| **Skill** | `.claude/skills/` | Reusable prompt, inject vào context | `claude-api`, `doc-standard-enforcer` |

Workflow ví dụ:

1. User chạy `/review-module` (command) → command prompt chứa instructions
2. Claude delegate sang `code-reviewer` agent → agent có system prompt riêng, tools giới hạn
3. Agent load `api-conventions` skill → skill inject coding standards vào context

Mỗi layer có thể dùng độc lập hoặc kết hợp tùy complexity.

[Nguồn: Claude Code Docs — Sub-agents, Skills] [Cập nhật 03/2026]

---

## 4.16 CI/CD Integration

Claude Code tích hợp với GitHub Actions và GitLab CI/CD để automate code review, PR creation, và implementation tasks.

[Nguồn: Claude Code Docs — GitHub Actions, GitLab CI/CD] [Cập nhật 03/2026]

### GitHub Actions

Setup nhanh nhất: chạy `/install-github-app` trong Claude Code terminal. Hoặc manual:

1. Install [Claude GitHub App](https://github.com/apps/claude)
2. Thêm `ANTHROPIC_API_KEY` vào repository secrets
3. Copy workflow file vào `.github/workflows/`

Basic workflow:

```yaml
name: Claude Code
on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
jobs:
  claude:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

Trigger bằng `@claude` trong issue hoặc PR comment:

```text
@claude implement this feature based on the issue description
@claude fix the TypeError in the user dashboard component
@claude review this PR for security issues
```

CLI arguments qua `claude_args`:

```yaml
claude_args: "--max-turns 5 --model claude-sonnet-4-6"
```

Hỗ trợ AWS Bedrock và Google Vertex AI cho enterprise environments.

### GitLab CI/CD

> [!NOTE]
> GitLab CI/CD integration hiện ở beta. Maintained bởi GitLab.

Setup: thêm `ANTHROPIC_API_KEY` masked variable + Claude job vào `.gitlab-ci.yml`:

```yaml
stages:
  - ai

claude:
  stage: ai
  image: node:24-alpine3.21
  rules:
    - if: '$CI_PIPELINE_SOURCE == "web"'
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
  before_script:
    - apk update
    - apk add --no-cache git curl bash
    - curl -fsSL https://claude.ai/install.sh | bash
  script:
    - >
      claude
      -p "${AI_FLOW_INPUT:-'Review this MR and suggest improvements'}"
      --permission-mode acceptEdits
      --allowedTools "Bash Read Edit Write mcp__gitlab"
```

Cả hai platforms đều:

- Đọc `CLAUDE.md` cho project standards
- Hỗ trợ AWS Bedrock và Google Vertex AI
- Sandbox execution trong isolated runners

---

## 4.17 Community patterns

Một số patterns từ cộng đồng Claude Code — không phải official, nhưng được nhiều người dùng áp dụng.

[Ghi chú: patterns từ cộng đồng, không phải Anthropic official. Dùng tham khảo, tự đánh giá phù hợp.]

### RIPER Framework

Framework 5 phases cho structured workflow với Claude Code:

| Phase | Mục đích | Claude được phép |
|-------|----------|-----------------|
| **R**esearch | Khám phá codebase, hiểu context | Chỉ đọc, hỏi questions |
| **I**nnovate | Brainstorm solutions | Đề xuất approaches, so sánh trade-offs |
| **P**lan | Lập kế hoạch chi tiết | Viết plan, xác nhận với user |
| **E**xecute | Implement changes | Edit code theo plan đã approved |
| **R**eview | Kiểm tra kết quả | Review, test, iterate |

Áp dụng bằng cách include phase instructions trong prompt hoặc CLAUDE.md.

### Ralph Wiggum Technique

Yêu cầu Claude giải thích plan trước khi implement — nếu giải thích không hợp lý, plan có vấn đề. Đặt tên theo nguyên tắc "nếu Ralph Wiggum hiểu được thì plan đủ rõ ràng."

Dùng khi: cần verify Claude hiểu đúng yêu cầu trước khi execute changes phức tạp.

---

← [IDE Integration](03-ide-integration.md) | [Tổng quan](../base/00-overview.md) | [Plugins →](05-plugins.md)
