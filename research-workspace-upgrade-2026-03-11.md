# Nghiên cứu: Nâng cấp không gian làm việc Claude — Phân tích hiện trạng & kiến trúc

> Tài liệu nghiên cứu nội bộ — tổng hợp phát hiện từ session brainstorm 4 (2026-03-11)
> Mục đích: capture sự thật và phát hiện, KHÔNG đưa ra khuyến nghị — dùng làm input cho brainstorm tiếp
> [Cập nhật 03/2026]

---

## Mục lục

1. [Bối cảnh — tại sao nghiên cứu này](#1-bối-cảnh)
2. [Hiện trạng .claude/ — kiểm kê chi tiết](#2-hiện-trạng-claude)
3. [Hiện trạng _scaffold/ — kiểm kê chi tiết](#3-hiện-trạng-scaffold)
4. [Kiến trúc Claude Code 03/2026 — từ official docs](#4-kiến-trúc-claude-code-032026)
5. [Phân tích gap — hiện trạng vs kiến trúc chuẩn](#5-phân-tích-gap)
6. [Phát hiện quan trọng](#6-phát-hiện-quan-trọng)
7. [Các hướng đã thảo luận — chưa chốt](#7-các-hướng-đã-thảo-luận)
8. [Dữ liệu thô từ official docs](#8-dữ-liệu-thô-từ-official-docs)

---

## 1. Bối cảnh

### Tại sao nghiên cứu này

Trong quá trình brainstorm v10 (session 1-3, ngày 09-10/03/2026), phát hiện:
- Câu hỏi không chỉ là "nâng cấp guide content" mà là "không gian làm việc với Claude đã đúng chuẩn chưa?"
- Mọi project đều cần không gian làm việc hiệu quả VỚI Claude trước — content/guide là bước sau
- Scaffold hiện tại được thiết kế cho người đã biết cách — không giúp người mới từ zero (painpoint đã nhận ra từ session 2)

### Góc nhìn của Đạt

- Thứ tự: Phenikaa-X → Robotics → Solution → Personal (hoặc ngược lại) — tầng sau cần kế thừa từ tầng trước
- Cần bàn giao không gian làm việc — người mới clone repo = có environment sẵn
- Nhận ra đang nhầm lẫn giữa 3 khái niệm: cách làm việc (methodology), rules mong muốn (workflow enforcement), và tone/voice của Claude

### Scope nghiên cứu

- Kiểm kê .claude/ hiện tại (23 files infrastructure)
- Kiểm kê _scaffold/ hiện tại (22 files templates)
- Nghiên cứu official docs Claude Code 03/2026 (6 trang chính)
- So sánh hiện trạng vs kiến trúc chuẩn

---

## 2. Hiện trạng .claude/

### Kiểm kê files

```
.claude/
├── CLAUDE.md              126 dòng — project context + skill index + rules
├── SETUP.md               93 dòng  — onboarding cho maintainer Guide Claude
├── settings.json          28 dòng  — 2 hooks (SessionStart + PostToolUse)
├── settings.local.json    66 dòng  — permissions (MCP, Bash, WebFetch)
├── rules/ (7 files)
│   ├── writing-standards.md      48 dòng — heading, code blocks, source markers, emoji
│   ├── reference-standards.md    28 dòng — reference file format
│   ├── scaffold-standards.md     36 dòng — template rules
│   ├── tier-base.md              26 dòng — base tier audience rules
│   ├── tier-doc.md               27 dòng — doc tier audience rules
│   ├── tier-dev.md               68 dòng — dev tier audience rules
│   └── planning-standards.md     34 dòng — plan format
├── hooks/ (2 files)
│   ├── format-check.py    140 dòng — heading hierarchy, code tags, source markers, emoji
│   └── link-check.py      221 dòng — cross-link + anchor verification
├── skills/ (9 folders, mỗi folder có SKILL.md)
│   ├── session-start/     65 dòng
│   ├── version-bump/      106 dòng
│   ├── cross-ref-checker/ 83 dòng
│   ├── doc-standard-enforcer/ 104 dòng
│   ├── module-review/     105 dòng
│   ├── source-audit/      111 dòng
│   ├── upgrade-guide/     188 dòng
│   ├── nav-update/        103 dòng
│   └── plan/              73 dòng
└── commands/ (5 files)
    ├── start.md           ← quick orientation
    ├── checkpoint.md      ← quick commit
    ├── validate-doc.md    ← module syntax check
    ├── review-module.md   ← deep module review
    └── weekly-review.md   ← project health check
```

### Đánh giá theo chức năng

| Thành phần | Đánh giá | Ghi chú |
|------------|----------|---------|
| CLAUDE.md | Hoạt động cho Guide Claude | 40% là bảng skills/commands — Claude tự detect skills qua description, không cần liệt kê |
| Rules (7 files) | Đúng pattern — auto-load theo path | Toàn bộ về FORMAT tài liệu, không có rule nào về METHODOLOGY làm việc |
| Hooks (2 files) | format-check.py hoạt động tốt | Chỉ dùng 1/16+ event types (PostToolUse). link-check.py là standalone, không hook |
| Skills (9) | Chuyên biệt cho Guide Claude | 0/9 skills có thể reuse cho project khác |
| Commands (5) | /start và /checkpoint reusable | /validate-doc, /review-module, /weekly-review chỉ cho Guide Claude |
| settings.json | Minimal, đúng | Chỉ 2 hooks — có thể mở rộng nhiều |
| settings.local.json | Hardcode MCP cụ thể | Không portable — mỗi người dùng MCP khác |

### Phát hiện từ kiểm kê

1. **80% infrastructure phục vụ duy nhất Guide Claude** — không reuse được cho project khác
2. **Không có .claude/agents/** — thiếu hoàn toàn custom subagents
3. **Không dùng @import** — CLAUDE.md tự chứa mọi thứ thay vì modular
4. **Hook chỉ kiểm format, không kiểm logic** — painpoint đã nhận ra: "có format check nhưng thiếu thinking check"
5. **link-check.py chất lượng cao** — xử lý Windows paths, URL encoding, anchor normalization, caching. Portable sang project khác

---

## 3. Hiện trạng _scaffold/

### Kiểm kê files

```
_scaffold/
├── README-scaffold.md              Entry point — workflow 4 bước
├── CLAUDE-template.md              170 dòng, 20+ placeholders
├── project-state-template.md       Project tracking template
├── VERSION                         "1.0"
├── checklists/
│   ├── daily-workflow.md           5-phase workflow
│   └── new-project-checklist.md    Step-by-step setup (3 phases)
├── project-instructions/           4 templates cho claude.ai Projects
│   ├── README.md
│   ├── template-basic.md
│   ├── template-code-review.md     Hardcode ROS2/Nav2/Python
│   ├── template-tech-doc.md
│   └── template-troubleshooting.md Hardcode AMR/SLAM
├── global-instructions/
│   └── global-CLAUDE-phenikaa-x.md PNX-specific
├── examples/
│   ├── dev-example/                Minimal working config (4 files)
│   └── guide-claude/               Advanced config snapshot v9.0 (4 files)
└── skill-templates/
    ├── SKILL-template/SKILL-template.md  112 dòng
    └── rule-template.md                  Với so sánh Rules vs CLAUDE.md vs Skills
```

### Đánh giá theo tiêu chí chuyển giao

| Tiêu chí | Điểm | Chi tiết |
|-----------|:-----:|---------|
| Người biết Claude Code tự setup | 7/10 | Setup 30 phút nếu đọc đúng thứ tự |
| Người mới tự setup | 4/10 | Kẹt ở "điền gì vào template" — 20 placeholders quá nhiều |
| Template generic | 6/10 | ~60% generic, ~40% PNX/Robotics-specific |
| Knowledge tập trung | 5/10 | Setup steps rải qua 8 files, 3 folders |
| Đầy đủ | 7/10 | Thiếu: hook writing guide, decision tree, onboarding path, .gitignore |
| Ví dụ | 9/10 | dev-example và guide-claude example rất tốt |

### Thiếu gì quan trọng

| Thiếu | Tại sao quan trọng |
|-------|-------------------|
| Hook writing guide | Có settings.json example nhưng không có hướng dẫn viết hook mới |
| Decision tree | "Khi nào cần rules? Khi nào cần skills? Khi nào cần hooks?" → Không có |
| Methodology guide | Scaffold dạy SETUP (cấu hình), không dạy WORKFLOW (cách làm việc hiệu quả) |
| .gitignore template | Người mới có thể commit .env, credentials |
| Generic global-CLAUDE.md | Chỉ có version PNX, người ngoài PNX phải tự viết |
| Troubleshooting | "settings.json không hoạt động?" → Không có |
| "Why" behind each piece | Template cho biết WHAT (cấu trúc), không cho biết WHY (tại sao cần) |
| Templates theo layer | Chỉ có 1 CLAUDE-template cho mọi level — không phân biệt managed/project/user |

---

## 4. Kiến trúc Claude Code 03/2026

### Nguồn

Nghiên cứu từ 6 trang official docs tại code.claude.com/docs/en/:
- overview, memory, best-practices, settings, features-overview, skills, hooks-guide, permissions

### 4.1. Hệ thống phân lớp — 4 tầng settings

| Tầng | Vị trí | Audience | Git-tracked | Priority |
|------|--------|----------|:-----------:|:--------:|
| **Managed** | System dirs + MDM | Toàn tổ chức | N/A (IT deploy) | Cao nhất — không override được |
| **Project** | .claude/settings.json | Team (per repo) | Yes | 2 |
| **Local** | .claude/settings.local.json | Cá nhân (per repo) | No (gitignored) | 3 |
| **User** | ~/.claude/settings.json | Cá nhân (mọi project) | No | Thấp nhất |

**Merge rules:**
- Arrays (permissions allow/deny): CỘNG DỒN từ mọi layer
- Scalars (model, language): LAST WINS theo priority
- Managed settings: KHÔNG thể override bởi bất kỳ layer nào

### 4.2. Hệ thống CLAUDE.md — 3+ tầng

| Scope | Vị trí | Mục đích | Shared |
|-------|--------|----------|--------|
| **Managed policy** | `C:\Program Files\ClaudeCode\CLAUDE.md` (Windows) | Tổ chức — security, standards | Toàn bộ user |
| **Project** | `./CLAUDE.md` hoặc `./.claude/CLAUDE.md` | Team — project context | Team qua git |
| **User** | `~/.claude/CLAUDE.md` | Cá nhân — preferences | Chỉ mình |

**Load order:** Walk up directory tree từ cwd. Subdirectory CLAUDE.md load on-demand khi Claude đọc files trong đó.

**@import syntax:** `@path/to/file` trong CLAUDE.md — recursive max 5 hops, approval dialog lần đầu.

**Khuyến nghị official:** < 200 dòng per file. Dài hơn → giảm adherence.

### 4.3. 6 cơ chế mở rộng — Phân biệt rõ

| Cơ chế | Bản chất | Khi nào load | Context cost | Dùng khi |
|--------|----------|-------------|:------------:|----------|
| **CLAUDE.md** | Advisory text | Mỗi session, tự động | Mỗi request | "Luôn làm X" — conventions, build commands, architecture |
| **Rules** (.claude/rules/) | Advisory text, scoped | Theo path match | Chỉ khi match | Rules cho loại file cụ thể (Python style khi edit .py) |
| **Skills** (.claude/skills/) | On-demand knowledge/workflow | Khi gọi hoặc Claude detect | Thấp (descriptions only) | Quy trình lặp lại, reference material, /command workflows |
| **Hooks** (settings.json) | Deterministic scripts | Trên event cụ thể | Zero | BẮT BUỘC xảy ra — lint, format, block, notify |
| **Subagents** (.claude/agents/) | Isolated workers | Khi Claude spawn | Isolated | Context isolation, parallel tasks, specialized workers |
| **Plugins** | Bundle skills+hooks+agents+MCP | Khi install | Tùy thành phần | Chia sẻ setup giữa repos/teams |

**Quy tắc chọn (từ official docs):**
- Claude NÊN biết mỗi session? → CLAUDE.md
- Chỉ khi edit loại file cụ thể? → Rules
- Quy trình gọi khi cần? → Skills
- PHẢI xảy ra, không phụ thuộc Claude? → Hooks
- Task cần isolation? → Subagents
- Chia sẻ cross-repo? → Plugins

### 4.4. Hooks — 16+ event types

| Nhóm | Events |
|------|--------|
| Session | SessionStart, SessionEnd, PreCompact |
| User | UserPromptSubmit |
| Tool | PreToolUse, PermissionRequest, PostToolUse, PostToolUseFailure |
| Agent | SubagentStart, SubagentStop, Stop |
| Team | TeammateIdle, TaskCompleted |
| System | Notification, InstructionsLoaded, ConfigChange, WorktreeCreate, WorktreeRemove |

**4 loại hook:**
- `command` — shell script (truyền thống)
- `http` — POST tới endpoint
- `prompt` — single-turn LLM evaluation (Haiku mặc định)
- `agent` — multi-turn verification với tool access

**Guide Claude hiện chỉ dùng:** 1 event type (PostToolUse), 1 loại hook (command).

### 4.5. Skills — Thay đổi quan trọng

- **Commands đã merge vào Skills** — `.claude/commands/` vẫn hoạt động nhưng skills được khuyến nghị
- **Frontmatter mới:** allowed-tools, model, context:fork, agent, hooks, disable-model-invocation, user-invocable
- **Bundled skills:** /simplify, /batch, /debug, /loop, /claude-api
- **Context budget:** 2% context window (~16,000 chars) cho skill descriptions
- **Skill scope:** Enterprise > Personal > Project. Plugin skills dùng namespace

### 4.6. Settings keys quan trọng

| Key | Loại | Mục đích |
|-----|------|----------|
| `outputStyle` | string | Tone & voice ("Concise", "Explanatory", hoặc text tự do) |
| `language` | string | Ngôn ngữ response ("vietnamese", "english"...) |
| `model` | string | Default model |
| `permissions` | object | allow/deny/ask rules |
| `hooks` | object | Hook configurations |
| `companyAnnouncements` | array | Startup messages |
| `sandbox` | object | OS-level isolation |
| `attribution.commit` | string | Git commit trailer |

### 4.7. Managed-only settings (chỉ dùng ở tầng managed)

| Setting | Mục đích |
|---------|----------|
| `allowManagedHooksOnly` | Block user/project hooks, chỉ cho managed hooks |
| `allowManagedPermissionRulesOnly` | Chỉ rules từ managed settings |
| `allowManagedMcpServersOnly` | Chỉ MCP servers do admin approve |
| `disableBypassPermissionsMode` | Không cho dùng --dangerously-skip-permissions |
| `blockedMarketplaces` | Block plugin sources |

### 4.8. Shared rules across projects

Official docs xác nhận 2 cơ chế:
1. **Symlinks:** `.claude/rules/` supports symlinks — resolved and loaded normally, circular detected
2. **Plugins:** Bundle skills + hooks + agents + MCP → install qua /plugin hoặc marketplace

---

## 5. Phân tích gap — Hiện trạng vs Kiến trúc chuẩn

### 5.1. Không gian cá nhân (~/.claude/)

| Aspect | Hiện trạng | Kiến trúc chuẩn | Gap |
|--------|-----------|-----------------|-----|
| CLAUDE.md | Chỉ có emoji rules | Personal methodology, workflow preferences | Thiếu methodology |
| settings.json | Không rõ nội dung | model, outputStyle, language, personal permissions | Chưa cấu hình đúng |
| rules/ | Không có | Personal coding preferences (áp dụng mọi project) | Thiếu hoàn toàn |
| agents/ | Không có | Personal agents (áp dụng mọi project) | Thiếu hoàn toàn |

### 5.2. Không gian project (.claude/)

| Aspect | Hiện trạng | Kiến trúc chuẩn | Gap |
|--------|-----------|-----------------|-----|
| CLAUDE.md | 126 dòng, trộn context + skill index + emoji rules | < 100 dòng, chỉ project context + build commands | Quá dài, trộn concerns |
| Rules | 7 files — toàn về format tài liệu | Path-scoped coding rules + format rules | Đúng mục đích cho Guide Claude, nhưng không chuyển giao |
| Skills | 9 skills — chuyên biệt Guide Claude | Generic + project-specific skills | 0 reusable skills |
| Commands | 5 commands | Merge vào skills (commands vẫn hoạt động) | Chưa migrate |
| Hooks | 1 event type, 1 hook type | 16+ events, 4 hook types | Dùng 6% khả năng |
| Agents | Không có | Custom subagents (.claude/agents/) | Thiếu hoàn toàn |
| @import | Không dùng | CLAUDE.md dùng @import cho modularity | Chưa áp dụng |

### 5.3. Không gian tổ chức (Managed)

| Aspect | Hiện trạng | Kiến trúc chuẩn | Gap |
|--------|-----------|-----------------|-----|
| Managed CLAUDE.md | Không tồn tại | Company-wide instructions, security | Thiếu hoàn toàn |
| managed-settings.json | Không tồn tại | Security rules, denied tools, approved MCPs | Thiếu hoàn toàn |
| Department rules | Không tồn tại | Shared rules qua symlinks hoặc plugins | Thiếu hoàn toàn |

### 5.4. Scaffold

| Aspect | Hiện trạng | Kiến trúc chuẩn | Gap |
|--------|-----------|-----------------|-----|
| Layer structure | 1 template cho mọi level | Templates cho mỗi layer (managed/project/user) | Không phân biệt layers |
| Hook templates | Không có | Template + guide cho viết hooks | Thiếu hoàn toàn |
| Agent templates | Không có | Template cho custom subagents | Thiếu hoàn toàn |
| Decision tree | Không có | "CLAUDE.md vs Rules vs Skills vs Hooks — khi nào dùng gì" | Thiếu — gây nhầm lẫn |
| Onboarding path | Không có | Guided journey cho người mới từ zero | Thiếu — painpoint đã xác định |

### 5.5. Sự nhầm lẫn 3 khái niệm — Giải mã

Đạt nhận ra đang nhầm lẫn giữa 3 khái niệm. Claude Code tách chúng bằng 3 cơ chế khác nhau:

| Khái niệm | Cơ chế Claude Code | Bản chất | Ví dụ |
|------------|-------------------|----------|-------|
| **Cách làm việc** (methodology) | CLAUDE.md + Skills | Advisory — Claude đọc và CỐ tuân thủ | "Verify trước commit", "Plan Mode cho task phức tạp" |
| **Rules mong muốn** (output enforcement) | Hooks + Rules | Deterministic (hooks) hoặc Advisory scoped (rules) | format-check.py LUÔN chạy sau edit; Python style CHỈ khi edit .py |
| **Tone & voice** | Settings (`outputStyle`, `language`) | Configuration — thay đổi behavior mặc định | `"outputStyle": "Concise"`, `"language": "vietnamese"` |

**Quan trọng:**
- CLAUDE.md = advisory — Claude đọc nhưng CÓ THỂ quên, đặc biệt khi file dài
- Hooks = deterministic — LUÔN chạy, Claude không kiểm soát
- Settings = configuration — thay đổi system behavior, không phải instruction

---

## 6. Phát hiện quan trọng

### PH1: .claude/ hiện tại hiệu quả cho Đạt, nhưng không chuyển giao được

- 80% infrastructure phục vụ Guide Claude cụ thể
- Người khác clone repo → có infrastructure nhưng không biết TẠI SAO mỗi phần tồn tại
- Skills, rules, hooks đều hardcode Guide Claude logic

### PH2: Thiếu hoàn toàn 2 tầng trong hệ thống 4 tầng

- Managed (PNX company-wide): không tồn tại
- Department (Robotics shared rules): không tồn tại
- Chỉ có Project + Personal (một phần)

### PH3: Dùng CLAUDE.md cho mọi thứ thay vì dùng đúng cơ chế

- Emoji enforcement → nên là hook (deterministic), đang là rule (advisory)
- Skill index trong CLAUDE.md → không cần, Claude tự detect qua description
- Personal methodology → nên ở ~/.claude/CLAUDE.md, đang trộn vào project CLAUDE.md

### PH4: Hooks chưa khai thác

- Claude Code có 16+ event types, 4 hook types
- Guide Claude chỉ dùng 1 event type (PostToolUse) và 1 hook type (command)
- Các event hữu ích chưa dùng: SessionStart (inject context), PreToolUse (block actions), Stop (verify completion), Notification (alert user), PreCompact (preserve context)

### PH5: Scaffold thiếu hướng dẫn "tại sao"

- Templates dạy WHAT (cấu trúc gì), không dạy WHY (tại sao cần)
- Không có decision tree: khi nào dùng CLAUDE.md vs Rules vs Skills vs Hooks
- Không có onboarding path cho người từ zero
- Knowledge rải qua 8+ files — không có 1 entry point duy nhất

### PH6: Personal layer (~/.claude/) gần như trống

- CLAUDE.md chỉ có emoji rules
- Không có methodology, workflow preferences, model selection
- 36 sessions kinh nghiệm vẫn nằm trong đầu Đạt, chưa encode
- Đây có thể là root cause của "mỗi session làm việc 1 kiểu khác nhau"

### PH7: Symlinks + Plugins = giải pháp cho department layer

- Official docs xác nhận .claude/rules/ supports symlinks
- Plugin marketplace cho phép bundle và distribute setup
- Cả 2 cơ chế đều production-ready — không cần tự build

### PH8: outputStyle là setting, không phải instruction

- Trước đó có thể đang cố dùng CLAUDE.md để kiểm soát tone/voice
- Claude Code có setting riêng: `outputStyle` (string) và `language` (string)
- Đặt trong settings.json, không phải CLAUDE.md

---

## 7. Các hướng đã thảo luận — Chưa chốt

### Hướng A: Nâng cấp từ dưới lên (Personal → Project → Managed → Scaffold)

**Ý tưởng:** Bắt đầu từ personal layer (~/.claude/), rồi lan ra.

**Ưu điểm:**
- Ảnh hưởng ngay tới mọi session của Đạt
- Ít risk — chỉ thay đổi cá nhân trước
- Mỗi bước tạo ví dụ sống cho bước sau

**Câu hỏi chưa trả lời:**
- Personal methodology encode cái gì? (Đạt biết implicit nhưng chưa explicit)
- outputStyle nào phù hợp? Cần test
- Bao nhiêu rules ở personal vs project?

### Hướng B: Nâng cấp từ trên xuống (Managed → Project → Personal → Scaffold)

**Ý tưởng:** Bắt đầu từ company-wide standards, enforce xuống.

**Ưu điểm:**
- Nền tảng cho mọi user/project
- Security rules có sẵn từ đầu

**Câu hỏi chưa trả lời:**
- Deploy managed settings bằng cách nào trên Windows? (file system vs Group Policy)
- Những security rules nào cần enforce? Cần review với team
- Managed settings có ảnh hưởng performance không?

### Hướng C: Nâng cấp scaffold trước — tạo "golden template"

**Ý tưởng:** Thiết kế scaffold đúng chuẩn trước, rồi áp dụng cho chính .claude/.

**Ưu điểm:**
- Thiết kế 1 lần, dùng nhiều nơi
- Scaffold trở thành specification

**Câu hỏi chưa trả lời:**
- Scaffold cho Guide Claude hay cho generic project?
- Scaffold nên có bao nhiêu layers? (risk over-engineering cho team nhỏ)

### Hướng D: Song song — nâng cấp .claude/ + cập nhật scaffold cùng lúc

**Ý tưởng:** Làm .claude/ → rút kinh nghiệm → cập nhật scaffold ngay.

**Câu hỏi chưa trả lời:**
- Resource đủ không? (1 maintainer)
- Scope creep risk?

> [!NOTE]
> Chưa có hướng nào được chốt. Các hướng trên là ghi nhận từ trao đổi, cần brainstorm thêm.

---

## 8. Dữ liệu thô từ official docs

### 8.1. CLAUDE.md — Best practices (trích nguyên văn)

> "Keep it concise. For each line, ask: Would removing this cause Claude to make mistakes? If not, cut it. Bloated CLAUDE.md files cause Claude to ignore your actual instructions!"

> "Target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence."

> "If Claude keeps doing something you don't want despite having a rule against it, the file is probably too long and the rule is getting lost."

> "Treat CLAUDE.md like code: review it when things go wrong, prune it regularly, and test changes by observing whether Claude's behavior actually shifts."

Include table từ docs:

| Include | Exclude |
|---------|---------|
| Bash commands Claude can't guess | Anything Claude can figure out by reading code |
| Code style rules that differ from defaults | Standard language conventions Claude already knows |
| Testing instructions and preferred test runners | Detailed API documentation (link to docs instead) |
| Repository etiquette (branch naming, PR conventions) | Information that changes frequently |
| Architectural decisions specific to your project | Long explanations or tutorials |
| Developer environment quirks (required env vars) | File-by-file descriptions of the codebase |
| Common gotchas or non-obvious behaviors | Self-evident practices like "write clean code" |

### 8.2. Features decision matrix (trích nguyên văn)

| Feature | What it does | When to use it |
|---------|-------------|---------------|
| CLAUDE.md | Persistent context loaded every conversation | Project conventions, "always do X" rules |
| Skill | Instructions, knowledge, and workflows Claude can use | Reusable content, reference docs, repeatable tasks |
| Subagent | Isolated execution context that returns summarized results | Context isolation, parallel tasks, specialized workers |
| Agent teams | Coordinate multiple independent Claude Code sessions | Parallel research, new feature development |
| MCP | Connect to external services | External data or actions |
| Hook | Deterministic script that runs on events | Predictable automation, no LLM involved |

### 8.3. CLAUDE.md vs Rules vs Skills (trích nguyên văn)

| Aspect | CLAUDE.md | .claude/rules/ | Skill |
|--------|-----------|----------------|-------|
| Loads | Every session | Every session, or when matching files opened | On demand, when invoked or relevant |
| Scope | Whole project | Can be scoped to file paths | Task-specific |
| Best for | Core conventions and build commands | Language-specific or directory-specific guidelines | Reference material, repeatable workflows |

### 8.4. Skill vs Subagent (trích nguyên văn)

| Aspect | Skill | Subagent |
|--------|-------|---------|
| What it is | Reusable instructions, knowledge, or workflows | Isolated worker with its own context |
| Key benefit | Share content across contexts | Context isolation. Work happens separately, only summary returns |
| Best for | Reference material, invocable workflows | Tasks that read many files, parallel work, specialized workers |

### 8.5. Hook event types đầy đủ

| Event | Matcher field | Khi nào fire |
|-------|-------------|-------------|
| SessionStart | how session started (startup/resume/clear/compact) | Bắt đầu hoặc resume session |
| SessionEnd | reason (clear/logout/other) | Kết thúc session |
| UserPromptSubmit | (không có matcher) | User submit prompt, trước Claude xử lý |
| PreToolUse | tool name | Trước tool call — có thể BLOCK |
| PermissionRequest | tool name | Khi permission dialog xuất hiện |
| PostToolUse | tool name | Sau tool call thành công |
| PostToolUseFailure | tool name | Sau tool call thất bại |
| Notification | notification type | Claude cần attention |
| SubagentStart | agent type | Spawn subagent |
| SubagentStop | agent type | Subagent hoàn thành |
| Stop | (không có matcher) | Claude xong responding |
| TeammateIdle | (không có matcher) | Agent team member idle |
| TaskCompleted | (không có matcher) | Task marked completed |
| InstructionsLoaded | (không có matcher) | CLAUDE.md hoặc rules loaded |
| ConfigChange | config source | Settings/skills file thay đổi |
| PreCompact | trigger (manual/auto) | Trước compaction |
| WorktreeCreate | (không có matcher) | Tạo worktree |
| WorktreeRemove | (không có matcher) | Xóa worktree |

### 8.6. 4 loại hooks

| Type | Cách hoạt động | Dùng khi |
|------|----------------|----------|
| command | Chạy shell command, đọc stdin JSON, trả exit code | Rules đơn giản, format, lint |
| http | POST event data tới URL endpoint | External services, audit logging |
| prompt | Single-turn LLM eval (Haiku mặc định) | Judgment calls — "task đã xong chưa?" |
| agent | Multi-turn verification với tool access | Cần inspect files/run commands để verify |

### 8.7. Permission rule syntax

Format: `Tool` hoặc `Tool(specifier)`. Evaluation order: **deny → ask → allow**.

| Rule | Matches |
|------|---------|
| `Bash` | All bash commands |
| `Bash(npm run *)` | Commands starting with "npm run" |
| `Read(./.env)` | Reading .env file |
| `Read(./src/**)` | All files under src/ recursively |
| `Edit(/docs/**)` | Edits in project docs/ |
| `WebFetch(domain:example.com)` | Requests to example.com |
| `Agent(Explore)` | Explore subagent |
| `Skill(deploy *)` | Deploy skill with any arguments |

### 8.8. Managed settings deployment — Windows

- Registry (admin): `HKLM\SOFTWARE\Policies\ClaudeCode` với `Settings` REG_SZ
- File-based: `C:\Program Files\ClaudeCode\managed-settings.json`
- CLAUDE.md: `C:\Program Files\ClaudeCode\CLAUDE.md`

---

> [!NOTE]
> File này là TÀI LIỆU NGHIÊN CỨU — ghi nhận sự thật và phát hiện.
> Không chứa khuyến nghị hay kế hoạch thực thi.
> Dùng làm input cho brainstorm sessions tiếp theo.

---

> [Nguồn: code.claude.com/docs/en/ — overview, memory, best-practices, settings, features-overview, skills, hooks-guide, permissions | Kiểm kê thực tế .claude/ và _scaffold/ | Brainstorm sessions 1-4]
> [Cập nhật 03/2026]
