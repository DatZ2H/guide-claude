# Nghiên cứu: Xây dựng Workspace chuẩn Claude Code — Phenikaa-X

> Tài liệu nghiên cứu nội bộ — phân tích kiến trúc workspace, hiện trạng, và phương án xây dựng.
> Tiếp nối brainstorm sessions 1-4 (2026-03-10/11).
> **Phương hướng đã chốt:** Workspace chuẩn trước, scaffold sau. Kế thừa PNX → Robotics → Solution → Personal.
> [Cập nhật 03/2026]

---

## Mục lục

1. [Bối cảnh và phương hướng](#1-bối-cảnh-và-phương-hướng)
2. [Kiến trúc Claude Code — từ official docs 03/2026](#2-kiến-trúc-claude-code--từ-official-docs-032026)
3. [Hiện trạng workspace — kiểm kê chi tiết](#3-hiện-trạng-workspace--kiểm-kê-chi-tiết)
4. [Gap analysis — hiện trạng vs chuẩn](#4-gap-analysis--hiện-trạng-vs-chuẩn)
5. [Ánh xạ PNX→Robotics→Solution→Personal](#5-ánh-xạ-pnxroboticssolutionpersonal)
6. [Phương án: Personal-first](#6-phương-án-personal-first)
7. [Phản biện](#7-phản-biện)
8. [Checklist "90% capability"](#8-checklist-90-capability)
9. [Dữ liệu tham khảo từ official docs](#9-dữ-liệu-tham-khảo-từ-official-docs)
10. [Nguồn](#10-nguồn)

---

## 1. Bối cảnh và phương hướng

### 1.1. Insight cốt lõi

Từ brainstorm sessions 1-4, nhận ra:

> Dù làm project nào — guide, code, doc — thì cách tương tác với Claude vẫn giống nhau. Workspace chuẩn = mọi project đều hiệu quả.

Điều này dẫn đến thay đổi trọng tâm:
- **Trước:** "Nâng cấp Guide Claude content" (v10 roadmap, 4 delivery mechanisms)
- **Bây giờ:** "Xây workspace chuẩn" (infrastructure chuẩn → mọi project hưởng lợi → scaffold từ kinh nghiệm thực)

### 1.2. Phương hướng đã chốt

1. **Workspace trước, scaffold sau** — workspace hoạt động tốt → rút kinh nghiệm → scaffold tự nhiên
2. **Kế thừa top-down:** Phenikaa-X → Robotics → Solution → Personal
3. **Tận dụng official best practices** — không tự sáng tạo khi đã có chuẩn tốt
4. **Bắt đầu từ Personal** — impact ngay, 0 risk, giải quyết painpoint thật

### 1.3. Painpoints phải giải quyết

| Painpoint | Root cause | Workspace solution |
|-----------|-----------|-------------------|
| Mỗi session làm việc 1 kiểu | Methodology chưa encode, nằm trong đầu | Personal rules + CLAUDE.md |
| Claude quên sau compaction | Không có re-injection mechanism | SessionStart compact hook |
| Context phình → Claude bỏ qua rules | CLAUDE.md quá dài, trộn concerns | Tách: rules scoped, skills on-demand, hooks deterministic |
| Format check có, thinking check không | Chỉ có command hooks, chưa dùng prompt/agent hooks | prompt hooks cho semantic verification |
| 80% infrastructure chỉ cho 1 project | Skills/rules hardcode Guide Claude | Tách personal (reusable) vs project (specific) |

---

## 2. Kiến trúc Claude Code -- từ official docs 03/2026

### 2.1. 7 cơ chế mở rộng

| Cơ chế | Bản chất | Context cost | Load khi | Dùng khi |
|--------|----------|:------------:|----------|----------|
| **CLAUDE.md** | Advisory text | Mỗi request | Session start | "Luôn làm X" — conventions, build cmds |
| **Rules** (.claude/rules/) | Advisory text, scoped | Khi match path | File match hoặc launch | File-specific guidelines |
| **Skills** (.claude/skills/) | On-demand knowledge | Thấp (descriptions) | Invoke/detect | Quy trình lặp lại, reference |
| **Hooks** (settings.json) | Deterministic scripts | Zero | Event trigger | BẮT BUỘC: lint, format, block |
| **Subagents** (.claude/agents/) | Isolated workers | Isolated | Claude spawn | Context isolation, parallel |
| **Plugins** | Bundle everything | Varies | Install | Share cross-repo |
| **Output Styles** | System prompt mod | Low | Session | Tone/voice/format |

**Quy tắc chọn (official):**

> Claude NÊN biết mỗi session? → **CLAUDE.md**
> Chỉ khi edit loại file cụ thể? → **Rules**
> Quy trình gọi khi cần? → **Skills**
> PHẢI xảy ra, không phụ thuộc Claude? → **Hooks**
> Task cần isolation? → **Subagents**
> Chia sẻ cross-repo? → **Plugins**

[Nguồn: code.claude.com/docs/en/best-practices]

### 2.2. Hệ thống phân tầng settings

**Precedence (cao → thấp):**

| # | Tầng | Vị trí | Audience | Git |
|:-:|------|--------|----------|:---:|
| 1 | **Managed** | Server / MDM / file-based | Toàn tổ chức | N/A |
| 2 | **CLI args** | Command line | Session | N/A |
| 3 | **Local** | .claude/settings.local.json | Cá nhân per-project | No |
| 4 | **Project** | .claude/settings.json | Team per-repo | Yes |
| 5 | **User** | ~/.claude/settings.json | Cá nhân mọi project | No |

**Merge rules:**
- Arrays (permissions, hooks): **concatenate + deduplicate** từ mọi layer
- Scalars (model, language): **last wins** theo priority
- Managed: **KHÔNG override được**
- Hooks: **tất cả fire** — không override by name

**CLAUDE.md cũng additive:** Managed + User + Project = TẤT CẢ load vào context.

> [!WARNING]
> Tổng CLAUDE.md từ mọi layers phải ngắn. Nếu Managed (80 dòng) + User (80 dòng) + Project (80 dòng) = 240 dòng — vượt ngưỡng 200 dòng. Cần tối ưu TỔNG, không chỉ từng file.

[Nguồn: code.claude.com/docs/en/settings]

### 2.3. CLAUDE.md — include/exclude chuẩn

**Include:**
- Bash commands Claude không đoán được
- Code style rules KHÁC defaults
- Testing instructions, test runners
- Branch naming, PR conventions
- Architectural decisions cụ thể
- Environment quirks (env vars)
- Common gotchas

**Exclude:**
- Thứ Claude tự hiểu từ code
- Standard language conventions
- API docs dài (LINK thay vì copy)
- Thông tin thay đổi thường xuyên
- File-by-file descriptions
- Self-evident practices ("write clean code")
- Long explanations, tutorials

**Target: < 200 dòng per file.**

> "Keep it concise. For each line, ask: Would removing this cause Claude to make mistakes? If not, cut it."

> "Treat CLAUDE.md like code: review it when things go wrong, prune it regularly, and test changes by observing whether Claude's behavior actually shifts."

[Nguồn: code.claude.com/docs/en/memory, code.claude.com/docs/en/best-practices]

### 2.4. @import syntax

```text
@path/to/file                  ← relative to importing file
@~/path/to/file                ← from home directory
@./README.md                   ← from project root
```

- Recursive max **5 hops**
- Approval dialog lần đầu cho external imports
- Paths resolve relative to **file chứa import**, không phải CWD

**Pattern cho team:** Project CLAUDE.md import shared conventions:
```text
@../../pnx-claude-standards/conventions.md
@~/.claude/my-project-overrides.md
```

[Nguồn: code.claude.com/docs/en/memory]

### 2.5. Rules — user-level + path-scoped

**User-level rules** (`~/.claude/rules/`):
- Auto-load cho MỌI project
- Đặt personal methodology, coding preferences ở đây
- Ưu tiên thấp hơn project rules

**Path-scoped rules:**
```yaml
---
paths:
  - "src/api/**/*.ts"
---
# API Development Rules
...
```

- Chỉ load khi Claude đọc files match pattern
- Giảm context cost — không load unnecessary rules
- Hỗ trợ **symlinks** — chia sẻ rules cross-project

[Nguồn: code.claude.com/docs/en/memory]

### 2.6. Hooks — 18 events, 4 types

**4 hook types:**

| Type | Bản chất | Dùng khi |
|------|----------|----------|
| `command` | Shell script | Format, lint, file protection |
| `http` | POST to endpoint | External logging, audit |
| `prompt` | Single-turn LLM eval (Haiku) | Judgment: "xong chưa?", "đúng chưa?" |
| `agent` | Multi-turn verification + tools | Cần inspect files để verify |

**18 events:**

| Nhóm | Event | Block? | Dùng cho |
|------|-------|:------:|----------|
| Session | SessionStart | No | Inject context, show status |
| | SessionEnd | No | Cleanup |
| | PreCompact | No | Logging trước compact (chỉ command type) |
| User | UserPromptSubmit | Yes | Validate/transform user input |
| Tool | PreToolUse | Yes | Block dangerous actions |
| | PermissionRequest | Yes | Auto-approve/deny |
| | PostToolUse | No | Format check, lint |
| | PostToolUseFailure | No | Error logging |
| Agent | SubagentStart | No | Inject context cho subagent |
| | SubagentStop | Yes | Verify subagent output |
| | Stop | Yes | Verify completion before stop |
| Team | TeammateIdle | Yes | Quality gate |
| | TaskCompleted | Yes | Completion criteria |
| System | Notification | No | Desktop notification |
| | InstructionsLoaded | No | Debug rule loading |
| | ConfigChange | Yes | Audit settings changes |
| | WorktreeCreate | Yes | Custom worktree setup |
| | WorktreeRemove | No | Cleanup |

**Quan trọng:** PreCompact chỉ hỗ trợ `type: "command"`, KHÔNG có decision control. Dùng cho side effects (logging, cleanup). Để re-inject context sau compact → dùng SessionStart với matcher `compact`.

[Nguồn: code.claude.com/docs/en/hooks]

### 2.7. Subagents — persistent memory

**Built-in:**

| Agent | Model | Tools | Purpose |
|-------|-------|-------|---------|
| Explore | Haiku | Read-only | Search, analysis |
| Plan | Inherited | Read-only | Research for plans |
| general-purpose | Inherited | All | Complex tasks |

**Custom agents** (`.claude/agents/` hoặc `~/.claude/agents/`):

```yaml
---
name: reviewer
description: Review code changes for quality
tools: Read, Grep, Glob, Bash
model: sonnet
memory: project
---
You are a senior code reviewer...
```

**Key features:**
- **Persistent memory** (`memory: user|project|local`) — agent tích lũy knowledge qua sessions
- **Worktree isolation** (`isolation: worktree`) — chạy trong git worktree riêng
- **Background execution** — chạy concurrent, permissions pre-approved
- **Skill preloading** (`skills: [...]`) — inject skills vào agent startup
- **Scope:** CLI flag > Project .claude/agents/ > User ~/.claude/agents/ > Plugin

[Nguồn: code.claude.com/docs/en/sub-agents]

### 2.8. Skills — bundled + custom

**Bundled skills (ship sẵn):**

| Skill | Mô tả |
|-------|--------|
| `/simplify` | Review changed files cho reuse, quality, efficiency — 3 parallel agents |
| `/batch` | Parallel changes across codebase — 5-30 worktrees |
| `/debug` | Troubleshoot từ debug log |
| `/loop` | Recurring prompt theo schedule |
| `/claude-api` | Load API reference cho SDK |

**Custom skills** frontmatter:

| Field | Mô tả |
|-------|--------|
| `allowed-tools` | Restrict tools khi skill active |
| `model` | Override model |
| `context: fork` | Chạy trong isolated subagent |
| `agent` | Chọn subagent type cho fork |
| `disable-model-invocation: true` | Chỉ user gọi được |
| `user-invocable: false` | Chỉ Claude detect + gọi |
| `hooks` | Lifecycle hooks scoped cho skill |
| `memory` | Persistent memory cho skill |

**Dynamic injection:** `!`command`` syntax — shell command chạy trước, output thay vào skill content.

**Scope:** Managed > User ~/.claude/skills/ > Project .claude/skills/ > Plugin

[Nguồn: code.claude.com/docs/en/skills]

### 2.9. Output Styles — không chỉ là string

**Built-in:** Default, Explanatory, Learning

**Custom styles:** file `.md` trong `~/.claude/output-styles/` hoặc `.claude/output-styles/`:

```yaml
---
name: PNX Concise
description: Ngắn gọn, tiếng Việt, kỹ thuật
keep-coding-instructions: true
---
Trả lời ngắn gọn bằng tiếng Việt.
Thuật ngữ kỹ thuật giữ tiếng Anh.
...
```

**Shareable qua git** — project output-styles/ commit được.

[Nguồn: code.claude.com/docs/en/output-styles]

### 2.10. Settings keys quan trọng

| Key | Type | Mô tả |
|-----|------|--------|
| `model` | string | Default model |
| `language` | string | Response language |
| `outputStyle` | string | Style name hoặc custom |
| `permissions` | object | allow/deny/ask rules |
| `hooks` | object | Hook configurations |
| `sandbox` | object | Filesystem + network isolation |
| `env` | object | Environment variables |
| `attribution` | object | Git commit/PR attribution |
| `availableModels` | array | Restrict model selection |
| `companyAnnouncements` | array | Startup messages |
| `claudeMdExcludes` | array | Skip CLAUDE.md files |
| `alwaysThinkingEnabled` | bool | Extended thinking mặc định |

**Managed-only:**

| Key | Mô tả |
|-----|--------|
| `disableBypassPermissionsMode` | Block --dangerously-skip-permissions |
| `allowManagedHooksOnly` | Block user/project hooks |
| `allowManagedPermissionRulesOnly` | Chỉ managed permissions |
| `allowManagedMcpServersOnly` | Restrict MCP servers |
| `strictKnownMarketplaces` | Control plugin sources |

**JSON Schema:** Thêm `"$schema": "https://json.schemastore.org/claude-code-settings.json"` cho IDE autocomplete.

**Server-managed settings (beta):** Cấu hình qua Claude.ai admin console (Teams/Enterprise plan). Không cần MDM/Registry. Fetch lúc startup, poll hàng giờ.

[Nguồn: code.claude.com/docs/en/settings, code.claude.com/docs/en/server-managed-settings]

### 2.11. Managed settings deployment — Windows

3 cơ chế:
- **Server-managed (beta):** Claude.ai admin console — đơn giản nhất, không cần admin
- **Registry:** `HKLM\SOFTWARE\Policies\ClaudeCode` → key `Settings` (REG_SZ, JSON string)
- **File-based:** `C:\Program Files\ClaudeCode\managed-settings.json` + `CLAUDE.md`

[Nguồn: code.claude.com/docs/en/settings]

### 2.12. Environment variables

| Variable | Mô tả |
|----------|--------|
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | Trigger compaction % (1-100, default ~95) |
| `CLAUDE_CODE_EFFORT_LEVEL` | low / medium / high |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | Default 32K, max 64K |
| `CLAUDE_CODE_DISABLE_AUTO_MEMORY` | Tắt auto memory |
| `CLAUDE_CODE_SUBAGENT_MODEL` | Model cho subagents |

[Nguồn: code.claude.com/docs/en/settings]

### 2.13. Best practices — 5 anti-patterns tránh

| Anti-pattern | Biểu hiện | Fix |
|-------------|----------|-----|
| **Kitchen sink session** | Trộn nhiều task → context nhiễm | `/clear` giữa tasks |
| **Correcting over and over** | Context đầy failed attempts | Sau 2 lần sửa → `/clear` + prompt tốt hơn |
| **Over-specified CLAUDE.md** | Rules quan trọng bị mất | Prune ruthlessly, chuyển sang hooks nếu deterministic |
| **Trust-then-verify gap** | Không có cách verify output | **Highest-leverage:** cung cấp tests/scripts/screenshots |
| **Infinite exploration** | Request không scope → context phình | Scope narrowly hoặc dùng subagents |

> "Include tests, screenshots, or expected outputs so Claude can check itself. This is the single highest-leverage thing you can do."

[Nguồn: code.claude.com/docs/en/best-practices]

---

## 3. Hiện trạng workspace -- kiểm kê chi tiết

### 3.1. Personal layer (~/.claude/)

**Kiểm kê thực tế (2026-03-11):**

```
~/.claude/
├── CLAUDE.md              15 dòng — CHỈ emoji rules
├── settings.json          6 dòng  — model: sonnet, language: vi
├── rules/                 KHÔNG TỒN TẠI
├── agents/                KHÔNG TỒN TẠI
├── skills/                KHÔNG TỒN TẠI
├── output-styles/         KHÔNG TỒN TẠI
└── (system dirs: cache, plugins, projects, plans, tasks...)
```

**~/.claude/CLAUDE.md** nội dung thực tế:
```markdown
# CLAUDE.md — Global Instructions

## File Operations
<!-- Placeholder — thêm global file operation rules tại đây -->

## Icon & Emoji Rules
- ALLOWED (chỉ trong bảng và status markers): ⚠️ ✅ ❌ 🔴 🟡 🟢 🔵
- BANNED: Mọi emoji/icon khác
- Prose warnings/tips/notes: dùng Obsidian callout syntax
```

**~/.claude/settings.json** nội dung thực tế:
```json
{
  "preferences": {
    "default_model": "sonnet",
    "language": "vi"
  }
}
```

**Đánh giá:** Gần như trống. Không có methodology, workflow preferences, personal rules, agents, skills. 36 sessions kinh nghiệm chưa encode vào bất kỳ đâu.

### 3.2. Project layer — Guide Claude (.claude/)

**Kiểm kê thực tế:**

```
.claude/
├── CLAUDE.md              125 dòng — project context + skill index + emoji + rules
├── SETUP.md               93 dòng  — onboarding maintainer
├── settings.json          28 dòng  — 2 hooks (SessionStart + PostToolUse)
├── settings.local.json    66 dòng  — MCP permissions (personal, hardcode)
├── rules/ (7 files, 267 dòng tổng)
│   ├── writing-standards.md      48 — heading, code blocks, source, emoji
│   ├── reference-standards.md    28 — reference file format
│   ├── scaffold-standards.md     36 — template rules
│   ├── tier-base.md              26 — base tier audience
│   ├── tier-doc.md               27 — doc tier audience
│   ├── tier-dev.md               68 — dev tier audience
│   └── planning-standards.md     34 — plan format
├── hooks/ (2 files, 361 dòng tổng)
│   ├── format-check.py    140 — heading, code tags, source markers, emoji
│   └── link-check.py      221 — cross-link + anchor (standalone, không phải hook)
├── skills/ (9 folders, ~938 dòng tổng SKILL.md)
│   ├── session-start/      65  │ cross-ref-checker/   83
│   ├── version-bump/      106  │ module-review/      105
│   ├── doc-standard-enforcer/ 104 │ source-audit/   111
│   ├── upgrade-guide/     188  │ nav-update/         103
│   └── plan/               73
└── commands/ (5 files)
    ├── start.md            │ checkpoint.md
    ├── validate-doc.md     │ review-module.md
    └── weekly-review.md
```

**Đánh giá theo chức năng:**

| Thành phần | Đánh giá | Gap |
|------------|----------|-----|
| CLAUDE.md (125 dòng) | ~40% là bảng skills/commands — không cần, Claude auto-detect | Cần prune: bỏ skill index, tách emoji → personal, dùng @import |
| settings.json (2 hooks) | Hoạt động, nhưng thiếu $schema, env, permissions | Dùng 2/18 events, 1/4 hook types |
| Rules (7 files) | 100% format rules, 0% methodology rules | Đúng cho Guide Claude, 0% reusable |
| Skills (9) | 100% Guide Claude specific | 0/9 reusable cho project khác |
| Commands (5) | /start, /checkpoint reusable | 3/5 chỉ cho Guide Claude |
| Hooks (2 files) | format-check.py tốt, link-check.py standalone | Chỉ PostToolUse command hook |
| Agents | Không tồn tại | Thiếu hoàn toàn |

### 3.3. Managed layer

**Không tồn tại.** Không có managed-settings.json, không có managed CLAUDE.md, không có server-managed config.

### 3.4. Shared layers (Robotics / Solution)

**Không tồn tại.** Không có shared conventions, shared rules, shared agents.

### 3.5. Nhầm lẫn 3 khái niệm — đã giải mã

Từ brainstorm session 4, Đạt nhận ra đang trộn 3 thứ khác nhau. Claude Code tách bằng 3 cơ chế:

| Khái niệm | Cơ chế đúng | Bản chất | Hiện trạng |
|------------|------------|----------|------------|
| **Methodology** (cách làm việc) | CLAUDE.md + Rules + Skills | Advisory | Nằm trong đầu, chưa encode |
| **Enforcement** (bắt buộc tuân thủ) | Hooks | Deterministic | Chỉ format check |
| **Tone/Voice** | Settings + Output Styles | Configuration | Chỉ có language: vi |

---

## 4. Gap analysis -- hiện trạng vs chuẩn

### 4.1. Personal layer

| Component | Chuẩn | Hiện trạng | Gap | Priority |
|-----------|-------|-----------|-----|:--------:|
| CLAUDE.md | Methodology, workflow, < 100 dòng | 15 dòng emoji only | **Thiếu methodology** | CAO |
| settings.json | $schema, model, language, env, outputStyle | model + language only | **Thiếu env, outputStyle** | CAO |
| rules/ | Personal methodology áp dụng mọi project | Không tồn tại | **Thiếu hoàn toàn** | CAO |
| agents/ | Personal agents (explorer, reviewer) | Không tồn tại | **Thiếu hoàn toàn** | TRUNG BÌNH |
| skills/ | Reusable personal skills | Không tồn tại | **Thiếu** | TRUNG BÌNH |
| output-styles/ | Custom style cho PNX | Không tồn tại | **Thiếu** | THẤP |

### 4.2. Project layer (Guide Claude)

| Component | Chuẩn | Hiện trạng | Gap | Priority |
|-----------|-------|-----------|-----|:--------:|
| CLAUDE.md | < 200 dòng, context only, @import | 125 dòng, trộn concerns | **Cần prune + @import** | CAO |
| settings.json | $schema, hooks, permissions, env | 2 hooks, không schema | **Thiếu schema, env, perms** | TRUNG BÌNH |
| Rules | Format + methodology + path-scoped | 7 format-only rules | **0% methodology** | THẤP (có ở personal) |
| Hooks | 18 events, 4 types | 1 event, 1 type | **Dùng ~6%** | TRUNG BÌNH |
| Agents | Project-specific subagents | Không tồn tại | **Thiếu** | TRUNG BÌNH |
| Skills | Generic + project-specific | 9 project-specific | **0 reusable** (OK cho project này) | THẤP |

### 4.3. Managed + Shared layers

| Component | Chuẩn | Hiện trạng | Gap | Priority |
|-----------|-------|-----------|-----|:--------:|
| Managed settings | Security, model restrictions | Không tồn tại | **Thiếu hoàn toàn** | THẤP (chưa cần) |
| Managed CLAUDE.md | Company conventions | Không tồn tại | **Thiếu hoàn toàn** | THẤP |
| Shared conventions | @import files, shared rules | Không tồn tại | **Thiếu** | THẤP (chờ feedback) |

### 4.4. Tổng hợp gap — ưu tiên

```
CAO (làm ngay — impact mọi session):
  ├── Personal CLAUDE.md — encode methodology
  ├── Personal rules/ — workflow rules cho mọi project
  ├── Personal settings.json — env, outputStyle, schema
  └── Project CLAUDE.md — prune + @import

TRUNG BÌNH (làm sau Personal — project-specific):
  ├── Project settings.json — thêm hooks, env, permissions
  ├── Project agents/ — tạo agents cho Guide Claude
  ├── Personal agents/ — explorer, reviewer reusable
  └── Personal skills/ — daily workflow skills

THẤP (chờ feedback / chưa cần):
  ├── Managed layer — chưa có team dùng
  ├── Shared layers — chưa biết share gì
  ├── Output styles — nice-to-have
  └── Commands → Skills migration
```

---

## 5. Ánh xạ PNX→Robotics→Solution→Personal

### 5.1. Thách thức

Claude Code có 4 tầng settings nhưng PNX cần **5 tầng** logic:

```
PNX muốn:                    Claude Code native:
  Phenikaa-X (công ty)    →    Managed          ✅
  Robotics (phòng ban)    →    ???               ❌ không có
  Solution (nhóm)         →    ???               ❌ không có
  Personal                →    User (~/.claude/) ✅
  Per-project             →    Project (.claude/) ✅
```

### 5.2. Giải pháp: @import + symlinks tạo virtual layers

```
PNX Managed layer
  C:\Program Files\ClaudeCode\
  ├── managed-settings.json     Security, model policies
  └── CLAUDE.md                 PNX conventions (ngắn)

Robotics layer (virtual — shared files)
  pnx-claude-standards/robotics/
  ├── conventions.md            @import vào project CLAUDE.md
  ├── rules/                    symlink vào .claude/rules/
  ├── agents/                   symlink vào .claude/agents/
  └── skills/                   symlink vào .claude/skills/

Solution layer (virtual — shared files)
  pnx-claude-standards/solution/
  ├── conventions.md            @import vào project CLAUDE.md
  ├── rules/                    symlink vào .claude/rules/
  └── skills/                   symlink vào .claude/skills/

Personal layer
  ~/.claude/
  ├── CLAUDE.md                 Personal methodology
  ├── settings.json             Model, language, env
  ├── rules/                    Personal rules (mọi project)
  ├── agents/                   Personal agents
  ├── skills/                   Personal skills
  └── output-styles/            Custom styles

Project layer
  project/.claude/
  ├── CLAUDE.md                 Project context
  │   ├── @../../pnx-claude-standards/robotics/conventions.md
  │   └── @../../pnx-claude-standards/solution/conventions.md
  ├── settings.json             Project hooks, permissions
  ├── rules/                    Project rules + symlinks → shared
  ├── agents/                   Project agents + symlinks → shared
  └── settings.local.json       Personal per-project
```

### 5.3. Merge behavior cần hiểu

| Loại | Merge rule | Kế thừa thế nào |
|------|-----------|-----------------|
| CLAUDE.md | Additive (tất cả load) | Managed + User + Project (+ @imports) = tất cả trong context |
| Rules | Additive (tất cả load) | User rules + Project rules + symlinked rules = tất cả active |
| Settings arrays | Concatenate | Managed deny + User deny + Project deny = cộng dồn |
| Settings scalars | Last wins (priority) | Managed > Local > Project > User |
| Skills | Override by name | Managed > User > Project > Plugin |
| Hooks | All fire | Managed + User + Project = tất cả chạy |
| Agents | Override by name | CLI > Project > User > Plugin |

### 5.4. Thứ tự xây dựng

```
Bước 1: Personal layer (~/.claude/)        ← BÂY GIỜ
  └── Impact: mọi session, mọi project

Bước 2: Nâng cấp Project layer            ← SAU KHI Personal ổn
  └── Impact: Guide Claude + test workspace

Bước 3: Test với 1 kỹ sư                  ← SAU KHI Bước 2 ổn
  └── Input: quyết định shared layers cần gì

Bước 4: Shared layers (pnx-claude-standards)  ← SAU KHI có feedback
  └── Input: feedback từ Bước 3

Bước 5: Managed layer                     ← KHI team > 5 dùng
  └── Input: shared conventions đã ổn định
```

---

## 6. Phương án: Personal-first

### 6.1. Tại sao Personal trước

| Lý do | Giải thích |
|-------|-----------|
| Impact ngay | Mọi session, mọi project hưởng lợi — không chờ |
| 0 risk | Chỉ ảnh hưởng cá nhân |
| Giải quyết painpoint thật | "Mỗi session 1 kiểu" → encode methodology |
| Tạo ví dụ sống | Personal hoạt động → biết cái gì share |
| Official docs ủng hộ | "Test changes by observing behavior shifts" |
| Additive architecture | Thêm layer sau = thêm files, KHÔNG refactor cũ |

### 6.2. Bước 1 — Personal Workspace (2-3 sessions)

**Deliverables:**

```
~/.claude/
├── CLAUDE.md                    ← Methodology (< 80 dòng)
│   ├── Workflow: Explore → Plan → Implement → Verify
│   ├── Session discipline: /clear giữa tasks
│   ├── Context management: subagents cho exploration
│   ├── Decision-making: phân tích → user chốt → triển khai
│   └── Handoff: cuối session ghi progress
│
├── settings.json                ← Configuration
│   ├── $schema
│   ├── model: claude-sonnet-4-6
│   ├── language: vietnamese
│   ├── env.CLAUDE_AUTOCOMPACT_PCT_OVERRIDE: "80"
│   ├── env.CLAUDE_CODE_EFFORT_LEVEL: "medium"
│   └── permissions (personal defaults)
│
├── rules/                       ← Personal rules (mọi project)
│   ├── methodology.md           Verify-first, plan-before-implement
│   └── communication.md         Tiếng Việt, thuật ngữ Anh, emoji
│
├── agents/                      ← Personal agents
│   ├── explorer.md              Haiku, read-only, codebase search
│   └── reviewer.md              Sonnet, persistent memory, review
│
├── skills/                      ← Personal skills
│   └── session-handoff/SKILL.md Cuối session: ghi progress + next steps
│
└── output-styles/               ← Custom style
    └── pnx-concise.md           Concise, Vietnamese, technical
```

**Đồng thời nâng cấp Guide Claude .claude/:**
- @import tách CLAUDE.md (bỏ skill index, bỏ emoji → personal)
- $schema trong settings.json
- AUTOCOMPACT_PCT=80 trong env
- SessionStart compact hook (re-inject context)

### 6.3. Bước 2 — Test với 1 kỹ sư (2-3 sessions)

**Sau 2 tuần dùng Personal workspace:**
- Đánh giá: nhất quán hơn? Claude tuân thủ? Output tốt hơn?
- Tạo simplified version cho 1 kỹ sư
- QUICK-START.md (1 trang, 5 phút)
- Thu feedback 1-2 tuần

**Feedback quyết định:**
- Cần role-based? Hay 1 template đủ?
- Shared conventions nào thực sự cần?
- Guide modules nào kỹ sư tra cứu?

### 6.4. Bước 3+ — dựa trên data (quyết định sau)

Chỉ làm SAU KHI có feedback thực tế:
- pnx-claude-standards repo (nếu cần shared)
- Enhanced scaffold (nếu setup khó)
- Managed layer (nếu có Teams plan)
- Role-based templates (nếu roles thực sự khác)

---

## 7. Phản biện

### PB1: "Personal trước" = chậm cho team?

Team chưa có ai dùng Claude Code. "Chậm" so với gì? Nếu mai có kỹ sư mới → `/init` auto-generate CLAUDE.md + QUICK-START.md ngắn = đủ temporary.

### PB2: Methodology encode được không?

Bắt đầu từ official best practices (Explore → Plan → Implement → Commit) + PNX-specific từ 36 sessions. Iterate, không cần hoàn hảo lần đầu.

### PB3: Refactor khi thêm layers sau?

Claude Code merge rules là additive. Thêm layer = thêm files, KHÔNG refactor files cũ. Rules concatenate, hooks all fire, CLAUDE.md additive.

### PB4: CLAUDE.md tổng quá dài khi có nhiều layers?

Risk thực. Cần budget:
- Managed: < 30 dòng (security + language only)
- Personal: < 80 dòng (methodology)
- Project: < 100 dòng (context + @imports)
- **Tổng: < 210 dòng** — sát ngưỡng nhưng chấp nhận được nếu mỗi dòng đều cần thiết

Giảm bằng: rules (scoped, không always-load), skills (on-demand), hooks (zero context).

### PB5: Tốn sessions cho infrastructure?

5 sessions Personal workspace → tiết kiệm 50+ sessions work sau đó. ROI cao. Và deliverables có giá trị ngay lập tức.

### PB6: Session 3 cảnh báo "paralysis by analysis"

Đúng. Phương án Personal-first giải quyết: Bước 1 = 2-3 sessions rồi DÙNG. Không phải 7 sessions planning rồi mới bắt đầu.

### PB7: Sao không build managed/shared trước rồi personal?

Managed cần biết enforce cái gì — chưa biết nếu chưa dùng. Shared cần biết share cái gì — chưa biết nếu chỉ 1 người dùng. Personal → kinh nghiệm → shared.

---

## 8. Checklist "90% capability"

Thay vì mục tiêu mơ hồ "tiệm cận 90%", 10 tiêu chí đo lường được:

| # | Tiêu chí | Đo bằng | Hiện trạng |
|:-:|----------|---------|:----------:|
| 1 | CLAUDE.md < 200 dòng, dùng @import | Đếm dòng | ❌ 125 dòng, 0 import |
| 2 | Personal methodology encoded | ~/.claude/ có rules + CLAUDE.md | ❌ Gần trống |
| 3 | Rules scoped theo path | Paths frontmatter, không load unnecessary | ✅ 5/7 rules có paths |
| 4 | Hooks deterministic cho enforcement | Hooks thay vì advisory cho critical rules | ❌ Chỉ format check |
| 5 | Subagents cho context isolation | .claude/agents/ có ít nhất 1 agent | ❌ Không tồn tại |
| 6 | Compaction handling | SessionStart compact hook re-inject | ❌ Không có |
| 7 | Verification loop | Format + semantic checks (prompt/agent hooks) | ❌ Chỉ format |
| 8 | Token optimization | Haiku exploration, Sonnet work, Opus architecture | ❌ Chỉ Sonnet |
| 9 | Session consistency | Mỗi session follow cùng workflow | ❌ Mỗi session 1 kiểu |
| 10 | Env optimized | AUTOCOMPACT, EFFORT_LEVEL configured | ❌ Default values |

**Hiện tại: 1/10 ✅ = ~10%**

**Sau Bước 1: target 8/10 ✅**

---

## 9. Dữ liệu tham khảo từ official docs

### 9.1. CLAUDE.md best practices (trích nguyên văn)

> "Keep it concise. For each line, ask: Would removing this cause Claude to make mistakes? If not, cut it. Bloated CLAUDE.md files cause Claude to ignore your actual instructions!"

> "Target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence."

> "If Claude keeps doing something you don't want despite having a rule against it, the file is probably too long and the rule is getting lost."

> "Treat CLAUDE.md like code: review it when things go wrong, prune it regularly, and test changes by observing whether Claude's behavior actually shifts."

> "Most best practices are based on one constraint: Claude's context window fills up fast, and performance degrades as it fills."

> "Include tests, screenshots, or expected outputs so Claude can check itself. This is the single highest-leverage thing you can do."

### 9.2. Features decision matrix (trích nguyên văn)

| Feature | What it does | When to use it |
|---------|-------------|---------------|
| CLAUDE.md | Persistent context loaded every conversation | Project conventions, "always do X" rules |
| Skill | Instructions, knowledge, and workflows Claude can use | Reusable content, reference docs, repeatable tasks |
| Subagent | Isolated execution context that returns summarized results | Context isolation, parallel tasks, specialized workers |
| Agent teams | Coordinate multiple independent Claude Code sessions | Parallel research, new feature development |
| MCP | Connect to external services | External data or actions |
| Hook | Deterministic script that runs on events | Predictable automation, no LLM involved |

### 9.3. CLAUDE.md vs Rules vs Skills (trích nguyên văn)

| Aspect | CLAUDE.md | .claude/rules/ | Skill |
|--------|-----------|----------------|-------|
| Loads | Every session | Every session, or when matching files opened | On demand, when invoked or relevant |
| Scope | Whole project | Can be scoped to file paths | Task-specific |
| Best for | Core conventions and build commands | Language-specific or directory-specific guidelines | Reference material, repeatable workflows |

### 9.4. Include/Exclude table (trích nguyên văn)

| Include | Exclude |
|---------|---------|
| Bash commands Claude can't guess | Anything Claude can figure out by reading code |
| Code style rules that differ from defaults | Standard language conventions Claude already knows |
| Testing instructions and preferred test runners | Detailed API documentation (link to docs instead) |
| Repository etiquette (branch naming, PR conventions) | Information that changes frequently |
| Architectural decisions specific to your project | Long explanations or tutorials |
| Developer environment quirks (required env vars) | File-by-file descriptions of the codebase |
| Common gotchas or non-obvious behaviors | Self-evident practices like "write clean code" |

### 9.5. Permission rule syntax

Format: `Tool` hoặc `Tool(specifier)`. Evaluation: **deny → ask → allow** (first match wins).

```
Bash(npm run *)        → commands starting with "npm run"
Read(./.env)           → reading .env file
Edit(/docs/**)         → edits in project docs/
WebFetch(domain:x.com) → requests to x.com
Agent(Explore)         → explore subagent
```

Path prefixes: `//` = absolute, `~/` = home, `/` = project root, `./` = relative.

### 9.6. Hook configuration pattern

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/check.sh",
            "timeout": 30
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "matcher": "compact",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Re-read CLAUDE.md for context after compaction'"
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Has the task been fully completed? Check if there are remaining TODOs or untested changes."
          }
        ]
      }
    ]
  }
}
```

### 9.7. Custom subagent configuration

```yaml
---
name: reviewer
description: Reviews code changes for quality and consistency
tools: Read, Grep, Glob, Bash
model: sonnet
memory: project
---
You are a senior code reviewer. Focus on:
- Logic errors and edge cases
- Security vulnerabilities
- Performance issues
- Code readability
```

### 9.8. Custom output style

```yaml
---
name: PNX Concise
description: Concise Vietnamese technical output
keep-coding-instructions: true
---
Respond concisely in Vietnamese.
Keep technical terms in English.
Use Obsidian callout syntax for warnings/tips.
No emoji except: ⚠️ ✅ ❌ 🔴 🟡 🟢 🔵
```

---

## 10. Nguồn

### Official Documentation (code.claude.com/docs/en/)

| Page | Nội dung chính |
|------|---------------|
| [memory](https://code.claude.com/docs/en/memory) | CLAUDE.md, @import, rules, auto memory |
| [best-practices](https://code.claude.com/docs/en/best-practices) | Anti-patterns, workflow, verification |
| [settings](https://code.claude.com/docs/en/settings) | 4-layer system, merge rules, all keys, env vars |
| [hooks](https://code.claude.com/docs/en/hooks) | 18 events, 4 types, configuration |
| [sub-agents](https://code.claude.com/docs/en/sub-agents) | Custom agents, persistent memory, isolation |
| [skills](https://code.claude.com/docs/en/skills) | Frontmatter, bundled skills, Agent Skills standard |
| [plugins](https://code.claude.com/docs/en/plugins) | Marketplace, distribution |
| [output-styles](https://code.claude.com/docs/en/output-styles) | Custom styles, built-in styles |
| [permissions](https://code.claude.com/docs/en/permissions) | Rule syntax, modes, security |
| [server-managed-settings](https://code.claude.com/docs/en/server-managed-settings) | Beta, web console |

### Community

| Nguồn | Nội dung |
|-------|---------|
| [claudefa.st](https://claudefa.st/) | Community framework, skill activation, context conservation |
| [agentskills.io](https://agentskills.io) | Agent Skills open standard |

### Research nội bộ

| File | Nội dung |
|------|---------|
| brainstorm-session-2026-03-10.md | Sessions 1-3: painpoints, mâu thuẫn, phản biện |
| brainstorm-session-2026-03-11.md | Session 4: scaffold cho team, 5 quyết định |
| research-upgrade-strategy-2026.md | 5 strategic options, D+ recommendation |
| research-claude-code-2026.md | 29 gaps analysis, 33 sources |

---

> [!NOTE]
> File này là TÀI LIỆU NGHIÊN CỨU — ghi nhận kiến trúc chuẩn, hiện trạng, gaps, và phương án.
> Mọi quyết định cần user confirm trước khi triển khai.

> [Nguồn: code.claude.com/docs/en/ (03/2026) | Kiểm kê thực tế ~/.claude/ và .claude/ | Brainstorm sessions 1-4]
> [Cập nhật 03/2026]
