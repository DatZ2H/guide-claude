# Research: Claude Code 2026 — Cơ sở đánh giá nâng cấp Guide Claude

> Nghiên cứu nội bộ — tổng hợp từ 33 nguồn (21 Tier 1 Anthropic + 1 Tier 2 + 11 Tier 3 Community)
> Claude Code version: **2.1.71** (07/03/2026) | Official docs: **60 pages** tại code.claude.com/docs
> [Cập nhật 03/2026]

---

## 1. Nguồn tham khảo (tóm tắt)

**Tier 1 — Anthropic official (21 nguồn):** code.claude.com/docs/en/ — overview, best-practices, memory, skills, sub-agents, agent-teams, plugins, hooks, hooks-guide, common-workflows, cli-usage, features-overview, model-config, checkpointing, permissions, scheduled-tasks, costs, changelog, llms.txt

**Tier 2 (1):** sshh.io (Anthropic engineer ecosystem)

**Tier 3 — Community (11):** aiorg.dev, Builder.io, HumanLayer, Morph, ykdojo (4.8k stars), disler (hooks mastery), shanraisshan, F22 Labs, Nick Tune, awesome-claude-code (21.6k stars)

> [!NOTE]
> Domain docs đã chuyển: `docs.anthropic.com/en/docs/claude-code/*` --> `code.claude.com/docs/en/*` (301/308 redirect). Mọi link trong guide cần cập nhật.

---

## 2. Kiến trúc mở rộng Claude Code (6 lớp)

| Feature | Chức năng | Context cost |
|---------|-----------|--------------|
| **CLAUDE.md** | Persistent context mỗi session | Mỗi request |
| **Skills** | Knowledge + invocable workflows | Thấp (descriptions only) |
| **Subagents** | Isolated workers với context riêng | Isolated |
| **Agent Teams** | Multi-session coordination | Riêng biệt |
| **MCP** | Kết nối external services | Mỗi request |
| **Hooks** | Deterministic scripts | Zero |
| **Plugins** | Bundle skills+hooks+agents+MCP | Tùy thành phần |

**Chọn feature:**
- "Luôn làm X" → CLAUDE.md | Repeatable workflows → Skills | Context isolation → Subagents
- External data → MCP | Deterministic automation → Hooks | Bundle & share → Plugins

---

## 3. Thay đổi quan trọng theo feature

### 3.1. CLAUDE.md — Mở rộng

| Tính năng mới | Chi tiết |
|---------------|----------|
| **@import syntax** | `@README.md`, `@docs/instructions.md` — recursive max 5 hops, approval dialog lần đầu |
| **CLAUDE.local.md** | Personal per-project, auto-gitignore |
| **claudeMdExcludes** | Setting loại bỏ CLAUDE.md cụ thể (monorepo) |
| **/init command** | Auto-generate CLAUDE.md từ codebase analysis |
| **Managed policy** | OS-level deploy cho enterprise |

Best practices: target <200 dòng, ~100-150 instructions tối đa (system prompt đã chiếm ~50).

### 3.2. Skills — Thiết kế lại

Commands đã merge vào Skills (`.claude/commands/` vẫn hoạt động nhưng skills được khuyến nghị).

**Frontmatter mới:**

| Field | Mô tả |
|-------|-------|
| `allowed-tools` | Restrict tools |
| `model` | sonnet/opus/haiku |
| `context: fork` | Chạy trong subagent |
| `agent: Explore` | Agent type khi fork |
| `hooks` | Hooks scoped to skill |
| `disable-model-invocation` | Chỉ user invoke |
| `user-invocable: false` | Chỉ Claude invoke |

**Dynamic injection:** `` !`gh pr diff` `` — chạy command TRƯỚC khi gửi prompt.

**Bundled skills:** `/simplify`, `/batch` (parallel changes), `/debug`, `/loop` (recurring), `/claude-api`

**Context budget:** 2% context window (~16,000 chars). Quá nhiều skills → một số bị exclude. Check `/context`.

### 3.3. Subagents — Hoàn toàn mới

**Built-in:**

| Agent | Model | Tools | Mục đích |
|-------|-------|-------|----------|
| Explore | Haiku | Read-only | File discovery, code search |
| Plan | Inherit | Read-only | Research cho planning |
| general-purpose | Inherit | All | Complex multi-step tasks |
| Claude Code Guide | Haiku | Docs | Trả lời câu hỏi về Claude Code |

**Custom agents** tại `.claude/agents/` — YAML frontmatter với: name, description, tools, model, permissionMode, maxTurns, skills, mcpServers, hooks, memory, background, isolation (worktree).

**Persistent memory:** `memory: user|project|local` — auto-inject MEMORY.md vào system prompt.

**Patterns:** Isolate high-volume ops, parallel research, chain agents, writer/reviewer, resume context.

### 3.4. Agent Teams — Experimental

- Multi-session coordination, peer-to-peer messaging + shared task list
- **Disabled by default** — enable qua env var
- Team lead + teammates (independent Claude Code instances)
- Display: in-process (Shift+Down cycle) | tmux | auto
- Best: 3-5 teammates, 5-6 tasks each, ~7x token cost
- Limitations: không resume, lead fixed, không nested, split panes không work trên Windows Terminal

### 3.5. Plugins — Packaging layer

- Bundle skills + hooks + agents + MCP + LSP servers
- Namespace: `/my-plugin:review`
- Install qua `/plugin` command hoặc marketplace
- **LSP servers** (.lsp.json): precise "go to definition" + "find references" + auto error detection
- Plugin manifest: `.claude-plugin/plugin.json`
- npm support: custom registries, version pinning

### 3.6. Hooks — Mở rộng đáng kể

**16+ event types** (guide hiện chỉ có PostToolUse):

| Nhóm | Events |
|------|--------|
| Session | SessionStart, SessionEnd, PreCompact |
| User | UserPromptSubmit |
| Tool | PreToolUse, PermissionRequest, PostToolUse, PostToolUseFailure |
| Agent | SubagentStart, SubagentStop, Stop |
| Team | TeammateIdle, TaskCompleted |
| System | Notification, InstructionsLoaded, ConfigChange, WorktreeCreate, WorktreeRemove |

**Hook types mới:** command (truyền thống), **http** (POST endpoint), **prompt** (single-turn LLM eval), **agent** (multi-turn verification)

### 3.7. CLI — Flags mới đáng chú ý

| Flag | Mô tả |
|------|-------|
| `--worktree` / `-w` | Start trong git worktree |
| `--agents` | Define custom subagents via JSON |
| `--from-pr` | Resume session từ PR number |
| `--permission-mode` | plan/acceptEdits/dontAsk/bypassPermissions |
| `--json-schema` | Validated structured JSON output |
| `--max-budget-usd` | Giới hạn chi phí |
| `--remote` / `--teleport` | Web session ↔ local |
| `--chrome` | Chrome browser integration |
| `--fallback-model` | Auto fallback khi model overloaded |

**Surfaces mới:** Desktop app, Web (claude.ai/code), Chrome extension, Remote Control, Slack, iOS app

### 3.8. Model & Costs

| Alias | Model | Mục đích |
|-------|-------|----------|
| `default` | Opus 4.6 (Max/Premium) / Sonnet 4.6 (Pro/Standard) | Mặc định |
| `sonnet` | Sonnet 4.6 | Daily coding |
| `opus` | Opus 4.6 | Complex reasoning |
| `haiku` | Haiku 4.5 | Fast, simple |
| `opusplan` | Opus (plan) → Sonnet (execute) | Hybrid |

- **Opus 4.0/4.1 removed** — auto-migrate to 4.6
- **Effort levels:** low/medium/high — `ultrathink` keyword → high cho turn đó
- **1M Context:** Opus 4.6 + Sonnet 4.6, extra pricing sau 200K tokens
- **Chi phí trung bình:** ~$6/dev/day, <$12 cho 90% users, ~$100-200/month Sonnet

### 3.9. Checkpointing & Permissions

- Tự động track edits, `Esc+Esc` hoặc `/rewind` mở rewind menu
- 4 options: restore code+conversation, restore conversation, restore code, summarize from here
- **Permission modes:** default, acceptEdits, plan (read-only), dontAsk, bypassPermissions
- **Rule syntax:** `Tool(specifier)`, glob patterns, domain filters — eval: deny → ask → allow

### 3.10. Scheduled Tasks

- `/loop 5m <prompt>` — recurring, session-scoped, max 50 tasks, 3-day expiry
- One-time reminders bằng ngôn ngữ tự nhiên
- Tools: CronCreate, CronList, CronDelete

---

## 4. Gap Analysis — Guide Claude v9.1 vs Claude Code 2026

### A. HOÀN TOÀN THIẾU (18 items)

| # | Hạng mục | Impact |
|---|----------|--------|
| 1 | Subagents system (built-in + custom + persistent memory) | CAO |
| 2 | Agent Teams (multi-session coordination) | Thấp (experimental) |
| 3 | Plugins & Marketplace (packaging, namespace, LSP) | Trung bình |
| 4 | Bundled skills (`/simplify`, `/batch`, `/debug`, `/loop`, `/claude-api`) | CAO |
| 5 | `@import` syntax trong CLAUDE.md | Trung bình |
| 6 | `CLAUDE.local.md` | Trung bình |
| 7 | `/init` command | Trung bình |
| 8 | `/rewind` + Checkpoints (Esc+Esc, 4 restore options) | CAO |
| 9 | `context: fork` cho skills | Trung bình |
| 10 | Dynamic injection (`` !`command` ``) trong skills | Trung bình |
| 11 | Prompt-based hooks + Agent-based hooks | Trung bình |
| 12 | HTTP hooks | Thấp |
| 13 | Desktop app, Web, Chrome extension, Remote Control, /teleport | Trung bình |
| 14 | `--worktree` / `-w` flag + git worktree workflow | CAO |
| 15 | Permission modes (plan, acceptEdits, dontAsk, bypassPermissions) | CAO |
| 16 | `--agents` CLI flag (dynamic subagent definition) | Trung bình |
| 17 | `--json-schema` (structured outputs) | Thấp |
| 18 | Code intelligence plugins (LSP) | Thấp |

### B. CẦN CẬP NHẬT (7 items — đã có nhưng lệch/thiếu)

| # | Hạng mục | Chi tiết |
|---|----------|----------|
| 1 | Skills frontmatter | Thiếu nhiều fields mới (allowed-tools, context:fork, hooks, model) |
| 2 | Hooks | Guide chỉ có PostToolUse, thiếu 16 event types khác |
| 3 | Context management | Thiếu `/compact <focus>`, summarize from here, 70% rule |
| 4 | Best practices | Chưa có verification-first, anti-patterns, explore>plan>code |
| 5 | CLI flags | Thiếu 20+ flags mới |
| 6 | Extended thinking | Thiếu ultrathink, adaptive reasoning, effort levels |
| 7 | Auto memory | Thiếu chi tiết 200-line limit, topic files, /memory command |

### C. CÓ THỂ SAI / LẠC HẬU (4 items)

| # | Hạng mục | Chi tiết |
|---|----------|----------|
| 1 | Domain links | `docs.anthropic.com` → cần chuyển `code.claude.com/docs` |
| 2 | Terminology | "custom commands" → "skills" là primary term |
| 3 | Model specs | Opus 4.0/4.1 removed; Opus 4.6 = current; Sonnet 4.5 → 4.6 |
| 4 | Thinking features | "Adaptive Thinking" giờ là Opus 4.6 default behavior với effort levels |

---

## 5. Module Impact Matrix

### Priority CAO (core content lệch nhiều)

| Module | Cần cập nhật | Hạng mục chính |
|--------|-------------|----------------|
| base/04-context-management | CAO | /compact focus, Esc+Esc summarize, checkpoints, 70% rule |
| base/05-tools-features | CAO | Skills redesign, bundled skills, subagents, plugins |
| dev/01-claude-code-setup | CAO | @import, CLAUDE.local.md, /init, permission modes |
| dev/02-cli-reference | CAO | 20+ flags mới, surfaces mới |
| dev/04-agents-automation | CAO | Subagents docs, Agent Teams, --agents flag |
| dev/05-plugins | CAO | Plugins, marketplace, code intelligence |
| dev/06-dev-workflows | CAO | Plan Mode, worktrees, fan-out, parallel patterns |
| ref/config-architecture | CAO | Skills frontmatter, agents, hooks types mới |
| ref/workflow-patterns | CAO | Plan Mode, worktrees, fan-out, verification-first |
| ref/skills-list | CAO | Bundled skills, frontmatter reference |
| ref/skills-guide | CAO | Skills redesign hoàn toàn |

### Priority TRUNG BÌNH

| Module | Cần cập nhật | Hạng mục chính |
|--------|-------------|----------------|
| base/01-quick-start | Trung bình | /init, surfaces mới |
| base/02-setup | Trung bình | Surfaces mới, /init |
| base/03-prompt-engineering | Trung bình | Verification-first, explore>plan>code, delegation spectrum |
| base/06-mistakes-fixes | Trung bình | Anti-patterns mới, security review cho AI code |
| dev/03-ide-integration | Trung bình | Desktop app, Chrome extension, Remote Control |
| doc/05-claude-code-doc | Trung bình | Skills mới cho doc workflows |
| ref/ecosystem-overview | Trung bình | Plugins, Agent Teams, community resources |

### Priority THẤP

| Module | Lý do |
|--------|-------|
| base/00-overview | Version link ok |
| base/07-evaluation | Ít ảnh hưởng |
| doc/01→04, doc/06 | Content ổn định |

---

## 6. Best Practices — Đồng thuận cộng đồng (3+ nguồn)

| # | Practice | Đã có trong guide? |
|---|---------|-------------------|
| 1 | CLAUDE.md là file quan trọng nhất — không optional | Có (dev/01) |
| 2 | Verification-first: cho Claude cách tự kiểm tra | **Thiếu** |
| 3 | `/clear` giữa unrelated tasks — fresh sessions per task | Có (base/04) |
| 4 | Plan trước khi code cho task > 3 files | **Thiếu** (Plan Mode) |
| 5 | Commit thường xuyên, ít nhất mỗi giờ | Có (base/06) |
| 6 | Subagents cho research — giữ main context sạch | **Thiếu** |
| 7 | Review `git diff` trước khi approve — đặc biệt security | Có (cơ bản) |
| 8 | Compact tại 70%, không đợi 90% | **Thiếu** |
| 9 | Reference patterns thay vì describe conventions | Có (cơ bản) |
| 10 | Scope tight — "what" + "why", không specify "how" | Có (base/03) |

---

## 7. Community Patterns đáng bổ sung cho Guide

### Workflow Patterns

| Pattern | Mô tả | Priority |
|---------|-------|----------|
| **Interview Pattern** | Claude "phỏng vấn" trước feature lớn → SPEC.md → /clear → execute | Trung bình |
| **Handoff Document** | Chủ động tóm tắt tiến độ → fresh session với handoff file | Trung bình |
| **Writer/Reviewer** | Session A viết, Session B (clean) review — giảm bias | Trung bình |
| **Terminal-First** | Describe → build → review git diff → commit. IDE = viewer | Thấp |
| **Fan-out Migration** | Parallel Claude invocations xử lý nhiều files | Trung bình |

### Hook Patterns

| Pattern | Mô tả | Priority |
|---------|-------|----------|
| **Block-at-submit** | Validate tại PreToolUse, KHÔNG write-time | CAO (insight) |
| **Pre-commit Gate** | Test pass → tạo flag file → hook check flag trước commit | Trung bình |
| **Prompt Context Injection** | UserPromptSubmit hook inject git status, project context | Trung bình |

### Delegation Spectrum

| Delegate hoàn toàn | Giám sát chặt |
|---------------------|---------------|
| Test generation, boilerplate | Auth flows, payment logic |
| Migrations, renames | Data mutations, security paths |
| Doc generation, linting | AI code chứa 1.5-2x security bugs hơn human |

### Anti-patterns tổng hợp

| Anti-pattern | Fix |
|-------------|-----|
| Kitchen Sink Session | `/clear` giữa tasks |
| Over-specified CLAUDE.md (>200 dòng) | Ruthless pruning, dùng skills/imports |
| Trust without verify | Tests + screenshots + scripts |
| Correct > 2 lần cùng lỗi | `/clear` + better prompt |
| Blanket permission approval | Wildcard syntax + periodic audit |
| Vibe coding cho production | TDD + plan mode + review |

---

## 8. Định hướng nâng cấp

### Approach đề xuất

1. Chạy `/upgrade-guide` → phát hiện stale refs + broken links cụ thể
2. Tạo plan cho từng priority group (CAO → Trung bình → Thấp)
3. Bắt đầu từ Priority CAO (11 modules, ảnh hưởng nhiều nhất)
4. `/module-review` từng module sau cập nhật
5. Checkpoint sau mỗi module
6. Version bump sau khi hoàn thành Priority CAO

### Nguyên tắc

- **KHÔNG viết lại toàn bộ** — chỉ cập nhật/bổ sung phần lệch
- **Giữ tone + conventions** — tiếng Việt, thuật ngữ tiếng Anh, callout syntax
- **Source markers** — mọi nội dung mới cần `[Nguồn: code.claude.com/docs/en/...]`
- **Verify trước khi viết** — features thay đổi nhanh, check official docs

### Thống kê

| Metric | Số liệu |
|--------|--------|
| Tổng gap items | 18 thiếu + 7 cần update + 4 có thể sai = **29** |
| Community patterns đáng bổ sung | 10 (consensus 3+ nguồn) |
| Priority CAO modules | 11 files |
| Priority Trung bình modules | 7 files |

---

> [Nguồn: Tổng hợp từ 33 nguồn — 21 Tier 1 Anthropic + 1 Tier 2 + 11 Tier 3 Community]
> File này là TÀI LIỆU NGHIÊN CỨU — không phải guide content. Dùng làm input cho planning.
