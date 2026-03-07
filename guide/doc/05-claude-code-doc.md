# Claude Code cho Documentation & Technical Writing

**Thời gian đọc:** 35 phút | **Mức độ:** Intermediate | **Audience:** Technical Writing, Documentation
**Cập nhật:** 2026-03-07 | Models: xem [specs](../reference/model-specs.md)

---
depends-on: [../reference/model-specs, ../reference/claude-code-setup, ../reference/skills-list, ../reference/config-architecture]
impacts: [base/00-overview, base/04-context-management]
---

Module này hướng dẫn sử dụng Claude Code (CC) — CLI agent chạy trong terminal — cho documentation và technical writing workflow. Nếu bạn không viết code, đây vẫn là công cụ mạnh cho quản lý tài liệu có Git, batch editing, và quality assurance tự động.

> [!NOTE]
> Module này focus vào **non-coding documentation workflow**. Nếu bạn dùng CC để viết code, tham khảo official docs tại https://code.claude.com/docs.
> Nếu bạn chỉ cần tạo/sửa file đơn lẻ mà không cần Git → xem [Cowork Setup](03-cowork-setup.md).

**Config & Commands reference:** [Claude Code Setup](../reference/claude-code-setup.md)

[Nguồn: Claude Code Docs]

---

## 5.1 Claude Code là gì — cho Non-coders

Claude Code là CLI agent chạy trong terminal, dùng chung kiến trúc với Claude Desktop (Cowork) nhưng được thiết kế cho môi trường có Git và file system access rộng hơn. Điểm khác biệt cốt lõi: thay vì chat qua UI, bạn làm việc trong terminal với workflow tự động hóa và batch operations. Section này giải thích khi nào dùng CC thay vì Cowork hoặc claude.ai — đặc biệt cho các kỹ sư documentation không viết code.

| Tình huống | claude.ai | Claude Desktop (Cowork) | Claude Code |
|---|---|---|---|
| Chat & brainstorm | ✅ Tốt nhất | ✅ | ✅ |
| Sửa 1 file đơn lẻ | ✅ | ✅ Tốt nhất | ✅ |
| Batch edit nhiều file | ❌ | ⚠️ Hạn chế | ✅ Tốt nhất |
| Git commit & branch | ❌ | ❌ | ✅ Tốt nhất |
| CI/CD integration | ❌ | ❌ | ✅ Tốt nhất |
| Custom hooks & automation | ❌ | ❌ | ✅ Tốt nhất |

### So sánh chi tiết theo tình huống documentation

Bảng dưới mở rộng từ bảng tổng quan trên — tập trung vào các tình huống documentation thực tế:

| Tình huống | claude.ai | Cowork | Claude Code |
|------------|-----------|--------|-------------|
| Brainstorm cấu trúc SOP mới | ✅ Tốt nhất | ✅ | ✅ |
| Viết 1 SOP từ outline | ✅ (copy-paste) | ✅ Tốt nhất | ✅ |
| Edit nhiều module cùng lúc | ❌ | ⚠️ Hạn chế | ✅ Tốt nhất |
| Kiểm tra cross-links toàn bộ docs | ❌ | Viết prompt mỗi lần | ✅ Slash commands tự động |
| Quản lý glossary nhất quán | Paste thủ công | ✅ Scan folder | ✅ Batch + commit |
| Version control tài liệu | ❌ | ❌ | ✅ Git tích hợp sẵn |
| Audit trail thay đổi | ❌ | ❌ Chưa hỗ trợ | ✅ Git history |
| Scheduled review định kỳ | ❌ | ✅ Scheduled Tasks | ❌ (cron) |
| CI/CD validation docs | ❌ | ❌ | ✅ Non-interactive mode |
| Rollback khi viết nhầm | ❌ | ❌ | ✅ `git revert` |

### Kiến trúc bên dưới

Ba công cụ dùng chung kiến trúc agent Anthropic, nhưng môi trường thực thi khác nhau:

- **claude.ai** — Web interface. Không có file system access. Input/output qua clipboard.
- **Cowork** — Claude Desktop, chạy trong folder bạn chọn. File access trực tiếp, không cần terminal. Thiếu Git.
- **Claude Code** — CLI terminal. Full file system access + Git. Automation qua hooks và CI/CD.

### Quy tắc chọn công cụ

```text
Cần brainstorm / viết nội dung → claude.ai
      ↓ nếu cần tạo/sửa file
Không cần Git → Cowork đủ rồi
      ↓ nếu cần version control / batch edit
Claude Code
```

[Ứng dụng Kỹ thuật]

**Ví dụ điển hình** — dự án tài liệu kỹ thuật Phenikaa-X:

| Phase trong documentation cycle | Công cụ | Lý do |
|----------------------------------|---------|-------|
| Lập outline module mới | claude.ai | Tương tác nhanh, không cần file |
| Viết nháp và tạo file | Cowork | File access trực tiếp, không cần terminal |
| Kiểm tra cross-links và heading | Claude Code | `/validate-doc` chạy tự động |
| Bump version, update changelog | Claude Code | Git + batch update nhiều file |
| Review nội dung với team | claude.ai | Paste đoạn cần feedback, không cần file access |

## 5.2 Cài đặt & First Session

Hướng dẫn cài đặt Claude Code qua npm, verify bằng `claude --version`, và khởi tạo first session trong thư mục dự án. Lệnh `/init` tạo `CLAUDE.md` mẫu — bước nên làm ngay với project mới. Section này đi kèm checklist nhanh để xác nhận môi trường sẵn sàng.

Xem thêm: [Claude Code Setup — Quick Setup Checklist](../reference/claude-code-setup.md#quick-setup-checklist).

[Nguồn: Claude Code Docs — Installation]

### Cài đặt

**Yêu cầu:** Node.js v18+, Git (khuyến nghị), Pro plan trở lên.

```bash
# Bước 1: Cài đặt global
npm install -g @anthropic-ai/claude-code

# Bước 2: Verify
claude --version    # phải in ra version number

# Bước 3: Mở terminal trong thư mục project
cd /path/to/your-doc-project
claude              # lần đầu → mở browser để xác thực Anthropic account
```

> [!NOTE]
> Windows: CC chạy native trên PowerShell/CMD hoặc qua WSL2. Nếu dùng WSL2, đặt project files trong WSL filesystem (không phải `/mnt/c/`) để tránh latency khi đọc nhiều file.

### First Session Walkthrough

Sau khi `claude` khởi động và xác thực thành công:

**Bước 1 — Khởi tạo project:**

```text
/init
```

Lệnh này tạo `CLAUDE.md` mẫu trong thư mục hiện tại. Mở file và điền thông tin project (xem template tại [CLAUDE.md Reference](../reference/claude-code-setup.md#claudemd-reference)).

**Bước 2 — Verify Claude đọc đúng context:**

```text
Bạn đang làm việc trong project nào? Mô tả ngắn folder structure.
```

Claude phải trả lời dựa trên `CLAUDE.md` vừa tạo. Nếu không, kiểm tra file có đúng vị trí không.

**Bước 3 — Chạy orientation command:**

```text
/start
```

Đọc `VERSION`, git status, và 5 commits gần nhất. Nên chạy mỗi khi mở session.

**Bước 4 — Test edit cơ bản:**

```text
Đọc file README.md và tóm tắt cấu trúc project.
```

Claude đọc file thực, không cần upload. Nếu thành công, workflow cơ bản đã sẵn sàng.

### Checklist sau cài đặt

```text
□ claude --version in ra version number
□ /init tạo CLAUDE.md thành công
□ Chỉnh CLAUDE.md: project context, language rules, writing standards
□ Claude trả lời đúng khi hỏi "bạn đang làm việc trong project nào"
□ Test: yêu cầu Claude đọc 1 file thực trong project
```

Xem thêm: [Claude Code Setup — Quick Setup Checklist](../reference/claude-code-setup.md#quick-setup-checklist).

## 5.3 Cấu hình 4 lớp (User → Project → Local → Managed)

Claude Code có hệ thống cấu hình 4 lớp theo thứ tự ưu tiên tăng dần: **User** (`~/.claude/CLAUDE.md`) → **Project** (`CLAUDE.md` tại root) → **Local** (`.claude/CLAUDE.md`, không commit) → **Managed** (enterprise policy). Mỗi lớp kế thừa và override lớp dưới. Section này giải thích cách cấu hình từng lớp cho documentation project — language rules, writing standards, emoji policy — và khi nào dùng `.claude/rules/` thay vì CLAUDE.md chính.

Xem thêm: [Claude Code Setup — CLAUDE.md Reference](../reference/claude-code-setup.md#claudemd-reference).

[Nguồn: Claude Code Docs — Configuration]

### 4 lớp cấu hình chi tiết

| Lớp | Vị trí file | Scope | Commit vào Git |
|-----|-------------|-------|----------------|
| **User** | `~/.claude/CLAUDE.md` | Mọi project trên máy | Không |
| **Project** | `./CLAUDE.md` hoặc `./.claude/CLAUDE.md` | Project hiện tại, toàn team | Có |
| **Local** | `./.claude/CLAUDE.local.md` | Cá nhân, chỉ project này | Không (gitignored) |
| **Managed** | Enterprise policy | Toàn organization | Do admin quản lý |

**Thứ tự ưu tiên:** Managed > Local > Project > User. Lớp hẹp hơn override lớp rộng hơn.

### Nên đặt gì ở lớp nào

| Nội dung | Lớp phù hợp | Lý do |
|----------|-------------|-------|
| Preferred language, emoji rules cá nhân | User | Áp dụng mọi project |
| Writing standards, folder structure | Project | Shared với team qua Git |
| Local path shortcuts, personal preferences | Local | Không ảnh hưởng người khác |
| Security policies, tool restrictions | Managed | Admin enforce |

### Template CLAUDE.md cho Documentation Project

```markdown
# CLAUDE.md — {{project_name}}

## Project context
{{mô tả ngắn, đối tượng, phase hiện tại}}

## Folder structure
guide/             # module files (00-11)
guide/reference/   # reference files
.claude/           # config, commands, skills

## Language rules
- Ngôn ngữ chính: Tiếng Việt
- Thuật ngữ kỹ thuật: giữ tiếng Anh
- Placeholders: {{variable}}

## Writing standards
- Heading hierarchy: # → ## → ### — KHÔNG skip level
- Code blocks luôn có language tag
- Cross-links dùng relative paths

## Rules — PHẢI tuân thủ
1. /checkpoint trước khi edit module lớn
2. Đọc VERSION trước khi edit bất kỳ module nào
3. KHÔNG tự ý xóa file mà không hỏi
```

Xem thêm: [Claude Code Setup — CLAUDE.md Reference](../reference/claude-code-setup.md#claudemd-reference).

### Path-specific rules: `.claude/rules/`

Ngoài CLAUDE.md chính, có thể tạo rules áp dụng chỉ cho một thư mục con. Claude load file này tự động khi làm việc trong thư mục đó — không load khi làm việc nơi khác.

**Cấu trúc:**

```text
.claude/
└── rules/
    ├── guide.md          # chỉ load khi làm việc trong guide/
    └── reference.md      # chỉ load khi làm việc trong guide/reference/
```

**Ví dụ `.claude/rules/guide.md`:**

```markdown
# Rules cho thư mục guide/

- Luôn đọc module header (dòng 1-6) trước khi edit bất kỳ file nào
- Mọi section phải có ít nhất 1 source marker: [Nguồn: ...] hoặc [Ứng dụng Kỹ thuật]
- Sau khi edit: nhắc user chạy /validate-doc để kiểm tra
- KHÔNG hardcode version number — đọc file VERSION thay vì ghi trực tiếp
```

**Khi nào dùng `.claude/rules/` thay vì CLAUDE.md chính:**

- Rules quá specific cho một thư mục, không cần load khi làm việc nơi khác
- CLAUDE.md chính đã dài — tách ra để giảm context load và tăng compliance
- Nhiều người dùng cùng project với workflow khác nhau trên từng thư mục

## 5.4 Plan Mode — Explore → Plan → Execute → Commit

Plan Mode là workflow 4 bước: Claude đọc context (Explore), đề xuất approach và xin approve (Plan), thực hiện (Execute), rồi save kết quả (Commit). Kích hoạt bằng toggle Plan Mode trong session hoặc thêm "think step by step" vào prompt. [Cập nhật 03/2026] Với documentation, nên dùng Plan Mode khi rewrite module lớn, refactor cấu trúc nhiều file, hoặc batch update cross-references — skip Plan khi chỉ sửa lỗi nhỏ hoặc thêm vài dòng.

[Nguồn: Claude Code Docs — Plan Mode]

### 4 giai đoạn của Plan Mode

| Giai đoạn | Claude làm gì | Bạn làm gì |
|-----------|--------------|------------|
| **1. Explore** | Đọc files liên quan, hiểu context hiện tại | Chờ — không interrupt |
| **2. Plan** | Đề xuất approach, liệt kê steps cụ thể | Review, approve hoặc adjust |
| **3. Execute** | Thực hiện từng bước theo plan đã duyệt | Quan sát, approve từng edit nếu cần |
| **4. Commit** | Tóm tắt thay đổi, đề xuất commit message | Commit hoặc tiếp tục chỉnh |

**Kích hoạt Plan Mode:**

- Toggle "Plan Mode" trong Claude Code UI, hoặc
- Thêm vào prompt: `Trước khi làm, hãy lên kế hoạch và chờ tôi approve`

> [!TIP]
> Dùng Plan Mode khi: rewrite module lớn, refactor cấu trúc nhiều file, batch update cross-references.
> Skip Plan Mode khi: sửa lỗi nhỏ, thêm vài dòng, format fix đơn giản.

### Ví dụ thực tế: Rewrite Module 05

**Tình huống:** Module 05 hiện viết cho AMR engineers (robot-focused). Cần rewrite theo hướng Documentation-first cho mọi kỹ sư Phenikaa-X.

**Prompt khởi đầu:**

```text
Tôi cần rewrite Module 05 từ AMR-focused sang Documentation-first.
Trước khi làm gì, hãy:
1. Đọc guide/05-context-management.md (module cần rewrite)
2. Đọc guide/00-overview.md (để hiểu định hướng mới)
3. Đề xuất kế hoạch thay đổi cụ thể — section nào sửa gì
Chờ tôi approve trước khi bắt đầu edit.
```

**Phase 1 — Explore:** Claude đọc cả hai file, phân tích các section còn AMR-specific.

**Phase 2 — Plan (Claude đề xuất):**

```text
Kế hoạch rewrite Module 05:

1. Intro: bỏ "context cho AMR navigation" → "context management cho mọi tác vụ"
2. Section 5.1: giữ concept, đổi ví dụ từ LiDAR/SLAM → viết SOP/báo cáo kỹ thuật
3. Section 5.3: bỏ code example ROS → thêm ví dụ documentation workflow
4. Section 5.5: thêm "Context cho Documentation Projects" — hiện đang thiếu
5. Cross-links: update 3 links AMR-specific → module 12

Ước tính: 5 edits, không thay đổi heading structure.
Proceed?
```

**Bạn review và approve** — hoặc adjust trước khi Claude execute. Ví dụ: "Bước 3 giữ code example nhưng thêm ví dụ doc song song."

**Phase 3 — Execute:** Claude thực hiện từng edit, hiển thị diff. Bạn approve từng bước hoặc approve toàn bộ.

**Phase 4 — Commit:**

```text
Claude: Đã hoàn thành 5 edits theo kế hoạch.
Đề xuất commit: "Ref: Module 05 — rewrite từ AMR-focused sang Documentation-first"
Chạy /validate-doc 05 để kiểm tra trước khi commit?
```

[Ứng dụng Kỹ thuật]

### Khi nào KHÔNG dùng Plan Mode

| Tình huống | Hành động tốt hơn |
|------------|-------------------|
| Sửa typo, lỗi chính tả | Prompt trực tiếp |
| Thêm 1-2 dòng vào section | Edit trực tiếp |
| Format fix (spacing, language tag) | `/validate-doc` + auto-fix |
| Bạn biết chính xác cần làm gì | Viết prompt chi tiết, skip plan |

## 5.5 Slash Commands & Custom Commands

Slash commands là workflow được đóng gói thành file markdown trong `.claude/commands/`, gọi bằng `/command-name` trong session. Custom commands phù hợp cho documentation project vì chuẩn hóa các tác vụ lặp lại. Section này hướng dẫn tạo custom command từ đầu và trình bày các ví dụ thực tế từ Guide Claude: `/start`, `/checkpoint`, `/validate-doc`.

[Nguồn: Claude Code Docs — Custom Slash Commands]

### Cấu trúc `.claude/commands/`

Mỗi file trong `.claude/commands/` là một slash command. Tên file = tên command.

```text
.claude/commands/
├── start.md            # → /start
├── checkpoint.md       # → /checkpoint
├── validate-doc.md     # → /validate-doc <số>
├── review-module.md    # → /review-module <số>
└── weekly-review.md    # → /weekly-review
```

Command file là plain markdown — viết instructions cho Claude thực hiện. Dùng `$ARGUMENTS` để nhận tham số từ user.

### 4 Commands thiết yếu — Guide Claude

**`/start` — Orientation đầu session:**

Đọc `VERSION`, `git status --short`, `git log --oneline -5` rồi in một block ≤6 dòng. Rules: không đọc `project-state.md` (tốn token), không liệt kê từng file — chỉ đếm.

**`/checkpoint` — Quick commit:**

Workflow tuần tự: `git status` → `git diff --stat` → đề xuất commit message (tiếng Việt, ≤72 ký tự) → hỏi confirm ("Commit & push" / "Commit only" / "Edit message"). Rules: không tự ý commit, không `git add -A`, cảnh báo nếu có `.bak` trong changes.

**`/validate-doc <số>` — Kiểm tra module:**

Nhận argument là số module (hoặc full path). Chạy 5 checks tự động:
- Heading hierarchy (không skip level)
- Cross-links (broken link detection + anchor check)
- Code blocks (language tag)
- Source markers (format đúng)
- Version reference (không hardcode)

Output: `✅ Passed all checks` hoặc danh sách issues kèm line number.

**`/weekly-review` — Review tổng thể project:**

Chạy cuối tuần hoặc cuối sprint. Review tiến độ, outstanding issues, và đề xuất next actions. Không nhận argument.

### Tạo custom command mới

Ví dụ: command kiểm tra nhất quán thuật ngữ. Tạo file `.claude/commands/glossary-check.md`:

```markdown
Kiểm tra nhất quán thuật ngữ. Argument: $ARGUMENTS (file hoặc folder).

1. Đọc glossary tại `guide/reference/glossary.md`
2. Scan file/folder trong $ARGUMENTS
3. Tìm: thuật ngữ sai chuẩn, thuật ngữ bị Việt hóa
4. Output: danh sách (file, line) + đề xuất sửa

Rules: KHÔNG tự sửa file — chỉ report.
```

Gọi bằng: `/glossary-check guide/05-context-management.md`

### Commands vs Skills — khi nào dùng cái nào

| Tiêu chí | Commands | Skills |
|----------|----------|--------|
| Kích hoạt | Thủ công: `/tên` | Tự động khi context khớp trigger |
| Tham số | `$ARGUMENTS` — truyền khi gọi | Không nhận tham số trực tiếp |
| Phù hợp | Workflow tuần tự rõ ràng, gọi chủ động | Tác vụ lặp lại, có điều kiện tự nhận biết |
| Tạo mới | Thêm file `.md` vào `.claude/commands/` | Thêm thư mục chứa `SKILL.md` vào `.claude/skills/` |

**Quy tắc đơn giản:** Bạn gọi chủ động, tác vụ rõ ràng → Command. Claude tự nhận ra cần làm khi gặp loại request nhất định → Skill.

## 5.6 Skills cho Documentation

Skills là agent chuyên biệt được gọi từ main session để thực hiện tác vụ có quy trình cố định. Phân biệt hai loại: **invocable** (user trigger thủ công) và **reference** (Claude tự load context). Section này hướng dẫn tạo custom skill cho documentation workflow, giải thích `disable-model-invocation`, và phân tích cost/benefit. Ví dụ thực tế: `doc-standard-enforcer` từ project này.

Xem thêm: [Skills List](../reference/skills-list.md).

[Nguồn: Claude Code Docs — Skills]

### Skills Ecosystem

Skills phân loại theo hai trục — Type × Trust:

| | Official | Community |
|--|----------|-----------|
| **Pre-built** | docx, xlsx, pptx, pdf | — |
| **Standalone** | doc-coauthoring, internal-comms | docs-review, obsidian-markdown, mermaidjs-v11... |
| **Plugin** | productivity, product-management | — |

Pre-built Skills tự kích hoạt — không cần cài. Standalone Skills cần thêm thư mục vào `.claude/skills/` (project-level) hoặc cài qua `npx @skill-hub/cli install`. Community Skills chưa có badge `[Approved PX]` cần đọc SKILL.md và test kỹ trước khi dùng. Xem đầy đủ: [Skills List](../reference/skills-list.md).

### Invocable vs Reference Skills

**Invocable** — user trigger thủ công, gọi theo tên hoặc trigger phrase rõ ràng trong `description`:

| Skill | Trigger |
|-------|---------|
| `module-review` | `/review-module 06` |
| `version-bump` | "bump version", "lên version vX.X" |
| `cross-ref-checker` | "kiểm tra cross-references trong module" |

**Reference (auto-trigger)** — Claude tự kích hoạt khi context khớp với `description` field, không cần user gọi tường minh:

| Skill | Auto-trigger khi... |
|-------|---------------------|
| `doc-standard-enforcer` | "edit module", "viết section", "thêm content", "sửa module" |
| `session-start` | "bắt đầu session", "tiếp tục", "còn lại gì cần làm" |

### Tạo Custom Skill: doc-standard-enforcer

Cấu trúc tối thiểu một custom skill:

```text
.claude/skills/
└── doc-standard-enforcer/
    └── SKILL.md        # bắt buộc — frontmatter + instructions
```

Nội dung `SKILL.md` — phần frontmatter quyết định trigger:

```markdown
---
name: doc-standard-enforcer
description: >
  Auto-activate khi user tạo hoặc edit nội dung trong guide/. Trigger khi user nói
  "edit module", "viết section", "thêm content", "update guide", "sửa module".
  Enforces writing standards cho Guide Claude project.
---

# Doc Standard Enforcer

## Rules — PHẢI tuân thủ khi viết/edit

- Heading hierarchy: # → ## → ### — KHÔNG skip level
- Code blocks luôn có language tag
- Cross-links dùng relative paths
- Source markers: [Nguồn: ...], [Ứng dụng Kỹ thuật], [Cập nhật MM/YYYY]
- KHÔNG hardcode version number

## Trước khi edit
1. Đọc VERSION để biết version hiện tại
2. Đọc file cần edit đầy đủ trước khi bắt đầu
```

[Ứng dụng Kỹ thuật]

### `disable-model-invocation`

Thêm vào frontmatter để tắt auto-trigger — skill chỉ kích hoạt khi user gọi tường minh:

```yaml
---
name: my-skill
disable-model-invocation: true
description: >
  Mô tả để người đọc hiểu — không dùng để Claude tự activate.
---
```

Dùng khi:
- Skill có side effects (ghi file, commit) — muốn user chủ động trigger
- Description rộng, dễ false positive activation
- Skill chỉ dành cho maintainer, không muốn tự kích hoạt trong conversation thông thường

### Context cost — SKILL.md load mỗi session

Mỗi `SKILL.md` trong `.claude/skills/` được đọc vào context khi mở session — kể cả khi skill không được dùng trong session đó.

| Skills | Token overhead ước tính |
|--------|------------------------|
| 1 skill (~50 dòng) | ~500–800 tokens |
| 5 skills | ~3000 tokens/session |

**Nguyên tắc giữ skills lean:**
- `SKILL.md` chỉ chứa trigger conditions và rules cốt lõi — không phải toàn bộ workflow
- Workflow chi tiết đặt vào Commands (`.claude/commands/`) — chỉ load khi gọi
- Khi `SKILL.md` vượt 100 dòng → tách instructions sang file riêng, link từ SKILL.md

## 5.7 Subagents cho Review & Research

Subagents là Claude instance độc lập chạy song song hoặc tuần tự với main session, cấu hình qua `.claude/agents/`. Pattern hữu ích nhất cho documentation: **Writer/Reviewer** — main session viết, subagent review theo checklist độc lập không bị bias từ writing context. Section này giải thích khi nào dùng subagent thay vì main session, và cách cấu hình `.claude/agents/` template.

[Nguồn: Claude Code Docs — Sub-agents]

### Concept

Subagent là Claude instance chạy trong isolated context — không chia sẻ conversation history với main session. Main session gửi task, subagent thực hiện rồi trả summary. Điểm mấu chốt: subagent không bị bias bởi context trước đó, nên phù hợp cho review độc lập.

```text
Main session (Writer)          Subagent (Reviewer)
┌─────────────────────┐       ┌─────────────────────┐
│ Viết SOP onboarding │──────→│ Review SOP theo      │
│ trong guide/        │       │ checklist độc lập    │
│                     │←──────│ Trả về: issues list  │
└─────────────────────┘       └─────────────────────┘
```

### Writer/Reviewer Pattern cho Documentation

Pattern hiệu quả nhất: tách writing và reviewing thành hai sessions riêng biệt.

**Session A — Writer (main session):**

```text
Viết SOP cho quy trình onboarding kỹ sư mới tại Phenikaa-X.
Output: file guide/sop-onboarding.md theo writing standards trong CLAUDE.md.
```

**Session B — Reviewer (subagent):**

```text
Review file guide/sop-onboarding.md vừa tạo. Kiểm tra:
1. Consistency với existing SOPs trong guide/
2. Style guide compliance (heading hierarchy, source markers, language rules)
3. Cross-links có trỏ đúng file tồn tại không
4. Thuật ngữ nhất quán với glossary
Output: danh sách issues có line number, xếp theo severity.
```

Reviewer không biết Writer đã cân nhắc gì — nên sẽ bắt được lỗi mà Writer "mù" vì đã nhìn quá lâu.

### Cấu hình `.claude/agents/`

Tạo file `.claude/agents/doc-reviewer.md`:

```markdown
---
name: doc-reviewer
description: Reviews documentation for quality and consistency
tools: Read, Grep, Glob, Bash
model: sonnet
---

Bạn là document reviewer chuyên kiểm tra chất lượng tài liệu kỹ thuật.

## Checklist review

- Heading hierarchy: # → ## → ### — không skip level
- Cross-link integrity: mọi relative link phải trỏ đến file tồn tại
- Terminology consistency: thuật ngữ kỹ thuật giữ tiếng Anh, không Việt hóa
- Style guide compliance: code blocks có language tag, source markers đúng format
- Câu context mở đầu: mỗi section ## hoặc ### phải có 1-2 câu giải thích

## Output format

Trả về danh sách issues, mỗi issue một dòng:
[Category] L{line}: mô tả vấn đề
```

[Ứng dụng Kỹ thuật]

### Khi nào dùng Subagent thay vì Main Session

| Tình huống | Main session | Subagent |
|------------|-------------|----------|
| Viết nội dung mới | ✅ | — |
| Review nội dung vừa viết | ⚠️ Bị bias | ✅ Tốt hơn |
| Context đã gần đầy (session dài) | ⚠️ Chậm, hay quên | ✅ Context sạch |
| Nhiều file cần review song song | ❌ Tuần tự | ✅ Chạy parallel |
| Sửa lỗi nhỏ, thêm vài dòng | ✅ | ❌ Overkill |
| Research trước khi viết | ✅ Đủ rồi | ✅ Nếu research scope rộng |

> [!TIP]
> Không cần subagent cho mọi review. Với module nhỏ (<100 dòng) hoặc edit đơn giản, `/validate-doc` trong main session đã đủ. Subagent hữu ích nhất khi review module lớn hoặc kiểm tra consistency across nhiều file.

## 5.8 Session Management

Các lệnh quản lý session: `/clear` (reset context, giữ file), `/rewind` (undo về checkpoint trước), `/rename` (đặt tên để resume sau), `/compact` (tóm tắt context dài). Flag CLI: `--continue` resume session gần nhất, `--resume <id>` resume session cụ thể. Section này cũng đề cập hai failure pattern phổ biến — kitchen sink và over-correction — cùng cách tránh.

Xem thêm: [Claude Code Setup — Essential Commands](../reference/claude-code-setup.md#essential-commands).

[Nguồn: Claude Code Docs — Session Management]

### `/clear` — Reset quan trọng nhất

Reset toàn bộ conversation context nhưng giữ nguyên file trên disk. Dùng `/clear` mỗi khi chuyển sang task không liên quan — đây là lệnh quan trọng nhất cho session hygiene.

```text
# Vừa xong edit module 05 → chuyển sang review module 08
/clear
# Context giờ sạch — Claude không còn "nhớ" edits module 05
```

**Khi nào `/clear`:** Xong một block công việc hoàn chỉnh. Chuyển task. Cảm thấy Claude bắt đầu "nhầm" context cũ vào task mới.

### `/rewind` — Undo mistakes

Quay lại trạng thái trước đó — undo cả code changes lẫn conversation. Khác với `git revert` (chỉ undo file), `/rewind` khôi phục cả conversation state.

```text
# Claude vừa edit sai hướng → undo toàn bộ turn vừa rồi
/rewind
# Quay lại trước bước edit cuối — file + conversation đều rollback
```

### `/compact` — Nén context dài

Khi session dài (nhiều file đọc, nhiều edits), context window dần đầy. `/compact` tóm tắt conversation hiện tại thành bản rút gọn — giữ thông tin quan trọng, bỏ chi tiết thừa.

```text
# Session đã edit 6 files, đọc 10 files — context gần đầy
/compact
# Claude tóm tắt: "Đã edit modules 03, 05, 07. Đang review cross-links."
```

Có thể thêm custom instruction: `/compact Tập trung vào cross-link changes, bỏ qua format fixes`.

### `/rename` — Đặt tên session

Đặt tên có ý nghĩa để dễ tìm lại khi resume.

```text
/rename module-12-sections-5-6
```

### `--continue` và `--resume` — Tiếp tục session

```bash
claude --continue              # resume session gần nhất
claude --resume "module-12-sections-5-6"   # resume session cụ thể theo tên
```

Hữu ích khi đóng terminal giữa chừng hoặc muốn quay lại task hôm trước.

### 3 Failure Patterns phổ biến

**1. Kitchen Sink Session** — quá nhiều tasks trong 1 session:

Triệu chứng: Claude bắt đầu confuse context module 03 với module 07, apply style fix của file A vào file B.

Cách tránh: `/clear` giữa mỗi task không liên quan. Một session nên focus vào 1 block công việc — ví dụ "edit sections 12.5–12.6" chứ không phải "edit module 12 + review module 03 + bump version".

**2. Over-correction Loop** — sửa cùng một lỗi nhiều lần qua lại:

Triệu chứng: Claude sửa heading level → bạn yêu cầu sửa lại → Claude sửa khác → lại sai. Vòng lặp 3-4 turns.

Cách tránh: `/clear`, viết prompt mới rõ ràng hơn với ví dụ cụ thể thay vì sửa đi sửa lại. Prompt tốt hơn hiệu quả hơn nhiều lần sửa.

**3. Over-specified CLAUDE.md** — file quá dài, rules bị ignore:

Triệu chứng: CLAUDE.md >200 dòng, Claude tuân thủ các rules đầu file nhưng quên rules cuối file.

Cách tránh: Giữ CLAUDE.md ≤200 dòng. Chuyển rules chi tiết sang `.claude/rules/` (path-specific) hoặc Skills. Rules quan trọng nhất đặt đầu file.

Xem thêm: [Claude Code Setup — Essential Commands](../reference/claude-code-setup.md#essential-commands).

## 5.9 Git Integration cho Documentation

Claude Code tích hợp Git natively: tạo branch, commit, đọc git history trong session. Section này hướng dẫn thiết lập Git workflow cho documentation project — branch naming convention, commit message format, và hooks tự động hóa validation trước mỗi commit. Ví dụ thực tế lấy từ Guide Claude project.

[Nguồn: Claude Code Docs — Git Integration]

### Branch Naming Convention

Quy ước đặt tên branch giúp team hiểu mục đích ngay từ tên:

| Prefix | Dùng khi | Ví dụ |
|--------|----------|-------|
| `feat/` | Thêm module hoặc section mới | `feat/add-module-07` |
| `fix/` | Sửa lỗi nội dung, broken links | `fix/broken-crosslinks` |
| `docs/` | Cập nhật README, changelog | `docs/update-readme` |
| `ref/` | Refactor cấu trúc, không đổi nội dung | `ref/reorganize-reference` |

Khai báo convention trong CLAUDE.md để Claude tuân thủ khi tạo branch:

```text
## Git workflow
- Branch naming: feat/<topic>, fix/<topic>, docs/<topic>
- Main branch: master — luôn tạo PR thay vì push trực tiếp
```

### Commit Message Conventions

Commit message nên ngắn gọn, mô tả *what changed*. Ngôn ngữ tùy team — Guide Claude dùng tiếng Việt:

```text
# Pattern: <Action>: <scope> — <mô tả ngắn>
Thêm cross-link module 03 → config-architecture
Ref: Module 05 — rewrite từ AMR-focused sang Documentation-first
Fix: broken anchor link section 12.3
Bump v5.1 → v6.0: Phase 4 Full Rewrite
```

Khai báo trong CLAUDE.md — Claude sẽ đọc `git log` để follow convention tự động.

### Hooks — Tự động hóa trước và sau mỗi session

CC hỗ trợ hooks trong `.claude/settings.json` — chạy shell commands tự động theo sự kiện.

**PreToolUse hook — validate trước khi commit:**

```jsonc
// .claude/settings.json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash(git commit*)",
        "hooks": [{
          "type": "command",
          "command": "bash .claude/hooks/pre-commit-doc.sh"
        }]
      }
    ]
  }
}
```

Script `pre-commit-doc.sh` có thể kiểm tra:

```bash
#!/bin/bash
# Check heading hierarchy trong các file .md đã staged
STAGED_MD=$(git diff --cached --name-only -- '*.md')
for f in $STAGED_MD; do
  # Detect heading skip: ## ngay sau # mà không có ## trung gian
  if grep -Pn '^#{4,}' "$f" | head -1; then
    echo "BLOCK: Heading skip detected in $f"
    exit 1
  fi
done
```

**SessionStart hook — inject context khi mở session:**

```jsonc
{
  "hooks": {
    "SessionStart": [{
      "hooks": [{
        "type": "command",
        "command": "echo \"Project $(cat VERSION) | Branch: $(git branch --show-current) | Modified: $(git status --short | wc -l) files\""
      }]
    }]
  }
}
```

Output hiển thị ngay khi session bắt đầu — không cần gõ `/start` thủ công.

[Ứng dụng Kỹ thuật]

### Ví dụ thực tế — Guide Claude project

```text
Branch:  feat/claude-code-docs
Commits: tiếng Việt, pattern "<Action>: <scope> — <detail>"
Hooks:   SessionStart inject version + branch + file count
Flow:    /checkpoint → commit → validate → push → PR to master
```

Toàn bộ convention được khai báo trong `.claude/CLAUDE.md` section `## Git workflow` — Claude đọc mỗi session và follow tự động, không cần nhắc lại.

## 5.10 Verification & Quality Assurance

"Give Claude a way to verify its work" — đây là practice có đòn bẩy cao nhất khi dùng Claude Code cho documentation. Thay vì chỉ yêu cầu "viết tốt", cung cấp tiêu chí pass/fail rõ ràng để Claude tự kiểm tra output. Section này trình bày 3 strategy verification và nguyên tắc "trust but verify" từ Mintlify.

[Nguồn: Claude Code Docs — Best Practices]

### 3 Verification Strategies

| Strategy | Cách dùng | Ví dụ |
|----------|-----------|-------|
| **Verification criteria trong prompt** | Thêm checklist vào cuối prompt — Claude tự kiểm tra trước khi trả kết quả | "Viết SOP, sau đó kiểm tra: mỗi step có action verb, heading hierarchy đúng, không hardcode version" |
| **Automated checks qua commands** | Chạy slash command hoặc skill sau khi edit | `/validate-doc 05` — kiểm tra heading, language tags, cross-links, source markers |
| **Subagent review** | Dùng isolated reviewer không bị bias bởi writing context | "Dùng subagent review Module 03 cho consistency với existing SOPs" |

### Verification criteria trong prompt

Pattern đơn giản nhất — thêm checklist vào prompt:

```text
Viết SOP quy trình deploy firmware cho AMR.

Sau khi viết xong, tự kiểm tra:
- [ ] Mỗi step bắt đầu bằng action verb (Mở, Chạy, Kiểm tra...)
- [ ] Heading hierarchy đúng: ## section → ### subsection
- [ ] Không hardcode version — tham chiếu {{VERSION}}
- [ ] Có ít nhất 1 source marker: [Nguồn: ...] hoặc [Ứng dụng Kỹ thuật]
- [ ] Cross-links dùng relative paths, không absolute URLs
Nếu có item fail, sửa trước khi trả kết quả.
```

Claude sẽ iterate nội bộ trước khi output — giảm edit rounds cho user.

### Automated checks — `/validate-doc`

Command `/validate-doc` chạy 5 checks tự động:

```text
/validate-doc 05

Output:
✅ Heading hierarchy: OK
✅ Code blocks: all have language tags
❌ Cross-links: L47 "../guide/03-xxx.md#section" — anchor not found
✅ Source markers: 4 found, format OK
✅ Version reference: no hardcoded version
```

Kết hợp với `cross-ref-checker` skill — phát hiện broken links across toàn bộ `guide/`:

```text
Kiểm tra cross-references trong module 05.
# Skill cross-ref-checker tự kích hoạt, scan tất cả relative links
```

### Nguyên tắc "Trust but Verify"

> [!WARNING]
> "Don't publish something just because Claude suggested it." — Mintlify engineering team đã học bài này khi dùng CC viết documentation: output quality cao, nhưng occasional hallucination về API endpoints hoặc code examples vẫn xảy ra. [Nguồn: Mintlify Blog]

**Checklist trước khi publish:**

- Code examples: chạy thử hoặc cross-check với source code
- API endpoints/URLs: verify bằng browser hoặc `curl`
- Version numbers: đối chiếu với `VERSION` file hoặc changelog
- Feature availability: verify tại official docs — features thay đổi thường xuyên
- Cross-links: chạy `/validate-doc` — Claude tự check nhưng vẫn có thể miss

[Ứng dụng Kỹ thuật]

## 5.11 Permissions & Safety

Claude Code có hệ thống permissions granular: cho phép hoặc deny từng tool (Read, Write, Edit, Bash) theo scope. Section này hướng dẫn cấu hình permissions tối giản cho documentation workflow — mở đủ quyền để edit docs, khóa những gì không cần. Bao gồm sandbox mode cho review an toàn.

Xem thêm: [Claude Code Setup — Permission Templates](../reference/claude-code-setup.md#permission-templates).

[Nguồn: Claude Code Docs — Permissions]

### `/permissions` — Xem và chỉnh sửa

Gõ `/permissions` trong session để xem rules hiện tại và chỉnh sửa trực tiếp.

Rules được lưu trong `.claude/settings.json` (shared, commit vào git) hoặc `.claude/settings.local.json` (cá nhân, gitignored).

### Allow/Deny Patterns

```jsonc
// .claude/settings.json
{
  "permissions": {
    "allow": [
      "Read",              // đọc mọi file
      "Edit guide/**",     // edit markdown trong guide/
      "Bash(git *)"        // git operations
    ],
    "deny": [
      "Write .env",        // không ghi file nhạy cảm
      "Bash(rm *)",        // không xóa file
      "Bash(curl *)"       // không gọi external URLs
    ]
  }
}
```

**Template cho documentation project:**

| Rule | Lý do |
|------|-------|
| `allow Read` | Claude cần đọc mọi file để hiểu context |
| `allow Edit guide/**` | Chỉ cho phép edit trong thư mục docs |
| `allow Bash(git *)` | Git operations: commit, branch, status |
| `deny Bash(rm *)` | Ngăn xóa file — dùng git revert thay thế |
| `deny Write .env` | Không ghi file chứa secrets |

### Sandbox Mode

Sandbox mode giới hạn network access và file system — hữu ích khi review tài liệu từ nguồn không tin cậy hoặc test skill mới.

Kích hoạt:

```bash
claude --sandbox
```

Trong sandbox: Claude đọc file bình thường nhưng không thể gọi external URLs, chạy arbitrary bash, hoặc ghi file ngoài thư mục project.

**Khi nào dùng sandbox:**

- Review pull request từ contributor bên ngoài
- Test skill/command mới trước khi deploy cho team
- Dry-run workflow phức tạp trước khi approve

### `--dangerously-skip-permissions`

> [!WARNING]
> Flag `--dangerously-skip-permissions` bỏ qua toàn bộ permission checks — Claude có thể đọc, ghi, xóa bất kỳ file nào và chạy bất kỳ command nào mà không hỏi. Chỉ dùng trong môi trường sandbox hoặc CI/CD pipeline có kiểm soát. KHÔNG dùng trên máy cá nhân với dữ liệu quan trọng.

```bash
# CI/CD pipeline — chạy trong container isolated
claude -p "Validate all modules" --dangerously-skip-permissions

# KHÔNG BAO GIỜ làm thế này trên máy cá nhân
# claude --dangerously-skip-permissions  ← NGUY HIỂM
```

## 5.12 Token Optimization & Cost

Claude Code tính token mỗi API call — context càng lớn, cost càng cao. Section này trình bày các đòn bẩy giảm cost mà không giảm chất lượng: model selection, compact strategy, đọc file thông minh, và slash commands thay prompt dài.

Xem thêm: [Model Specs & Pricing](../reference/model-specs.md).

[Nguồn: Claude Code Docs — Token Usage]

### Model Selection — đòn bẩy lớn nhất

Chọn model phù hợp giảm cost 5-20x mà không ảnh hưởng output quality cho tác vụ đơn giản.

| Model | Khi nào dùng | Ví dụ documentation |
|-------|-------------|---------------------|
| **Haiku** | Tác vụ đơn giản, format check | Batch rename headings, check language tags |
| **Sonnet** | Editing, review, viết nội dung (default) | Viết section mới, `/validate-doc`, `/checkpoint` |
| **Opus** | Phân tích kiến trúc, refactor phức tạp | Rewrite module, multi-file consistency review |

Chuyển model trong session:

```text
/model opus       # trước tác vụ phức tạp
# ... làm việc ...
/model sonnet     # quay lại default khi xong
```

Xem flowchart chọn model chi tiết: [Model Specs](../reference/model-specs.md).

### `/compact` — Nén context khi session dài

`/compact` tóm tắt conversation hiện tại, giải phóng context window. Thêm custom instruction để giữ thông tin quan trọng:

```text
/compact Focus on cross-link changes, bỏ qua format fixes
/compact Giữ lại danh sách files đã edit và issues còn open
```

**Khi nào compact:** Sau 10+ turns, sau khi đọc nhiều file lớn, hoặc khi Claude bắt đầu chậm hoặc quên context trước đó.

### Đọc file thông minh — `offset`/`limit`

Với file >500 dòng, đọc toàn bộ tốn token không cần thiết. Chỉ đọc phần cần thiết:

```text
# Thay vì đọc toàn bộ module 700 dòng:
Đọc guide/12-claude-code-documentation.md

# Đọc chỉ section cần edit:
Đọc guide/12-claude-code-documentation.md từ dòng 672 đến 704
```

Khai báo trong CLAUDE.md để Claude tự áp dụng:

```text
## Token optimization
- Đọc file có offset/limit khi file > 500 dòng
```

### Effort Level

Biến môi trường `CLAUDE_CODE_EFFORT_LEVEL` điều chỉnh thinking depth — ảnh hưởng trực tiếp đến token usage:

```bash
# Low effort — format fixes, simple edits
CLAUDE_CODE_EFFORT_LEVEL=low claude -p "Fix typos in README.md"

# Default — editing, review thông thường
claude

# High effort — complex analysis, architectural decisions
CLAUDE_CODE_EFFORT_LEVEL=high claude -p "Review toàn bộ cross-references"
```

### Slash Commands vs Typed Prompts — token savings

Slash commands tiết kiệm token đáng kể so với gõ prompt dài:

| Cách gọi | Input tokens |
|-----------|-------------|
| Gõ prompt 5 dòng mô tả workflow | ~200 tokens |
| `/checkpoint` (command file ~10 dòng) | ~50 tokens |
| Skill auto-activate (0 prompt input) | 0 prompt tokens |

Commands và Skills load instructions từ file — không cần gõ lại mỗi lần. Skills auto-activate còn hiệu quả hơn: khi context match trigger, skill kích hoạt mà user không cần gõ gì — 0 prompt tokens cho phần kích hoạt.

> [!TIP]
> Kết hợp 3 đòn bẩy cho cost optimization tốt nhất: (1) chọn đúng model, (2) `/compact` khi session dài, (3) dùng commands/skills thay prompt dài. Với project documentation thông thường, Sonnet + `/compact` mỗi 10 turns đã đủ.

## 5.13 Batch & Automation

Claude Code hỗ trợ non-interactive mode qua `claude -p "prompt"` — chạy một lần, trả kết quả, thoát. Kết hợp với pipe, fan-out, và CI integration để tự động hóa documentation tasks mà không cần mở session interactive.

[Nguồn: Claude Code Docs — CLI Usage]

### `claude -p` — Non-interactive Mode

Chạy một prompt duy nhất, nhận output, thoát:

```bash
# Scan broken cross-links, output CSV
claude -p "Scan guide/ tìm broken cross-links, output dạng CSV: file,line,broken_link"

# Generate changelog từ git diff
claude -p "Đọc git log --oneline -10, viết changelog entry cho VERSION update"
```

Thêm `--output-format json` để nhận structured output — dễ parse trong script:

```bash
claude -p "List all ## headings in guide/05-workflow-recipes.md" \
  --output-format json
```

### Pipe Input/Output

Pipe file content trực tiếp vào Claude — không cần Claude tự đọc:

```bash
# Liệt kê recipe names từ module
cat guide/05-workflow-recipes.md | claude -p "Liệt kê tất cả recipe names (## headings)"

# Pipe git diff để tạo commit message
git diff --staged | claude -p "Viết commit message tiếng Việt, ≤72 ký tự"
```

### Fan-out Pattern — Batch nhiều file

Chạy Claude song song trên từng file — mỗi instance nhận 1 file:

```bash
for file in guide/*.md; do
  claude -p "Check heading hierarchy in $file. Return OK or list violations." \
    --allowedTools "Read" &
done
wait
```

Flag `--allowedTools "Read"` giới hạn Claude chỉ được đọc — không edit, không bash. An toàn cho batch validation.

### CI Integration — GitHub Actions

Chạy docs linting tự động trong PR check:

```yaml
# .github/workflows/docs-lint.yml
name: Docs Lint
on: [pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install -g @anthropic-ai/claude-code
      - name: Validate changed docs
        run: |
          CHANGED=$(git diff --name-only origin/master -- 'guide/*.md')
          for f in $CHANGED; do
            claude -p "Validate $f: heading hierarchy, language tags, cross-links. Output: OK or violations list." \
              --allowedTools "Read,Glob,Grep" \
              --dangerously-skip-permissions
          done
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

> [!WARNING]
> `--dangerously-skip-permissions` chấp nhận được trong CI container — môi trường ephemeral, không có dữ liệu nhạy cảm. KHÔNG dùng trên máy cá nhân (xem [12.11](#1211-permissions--safety)).

[Ứng dụng Kỹ thuật]

## 5.14 Plugins & MCP cho Documentation

MCP (Model Context Protocol) cho phép Claude Code kết nối external services — GitHub, Notion, Slack — qua standardized interface. Plugins cung cấp tools (đọc/ghi data), còn Skills dạy Claude *cách dùng* tools đó trong workflow cụ thể.

[Nguồn: Claude Code Docs — MCP]

### Thêm MCP Server

```bash
# Thêm GitHub MCP — đọc issues, PRs, comments
claude mcp add github

# Thêm Notion MCP — query databases, đọc pages
claude mcp add notion

# Xem danh sách MCP servers đã kết nối
claude mcp list
```

Sau khi add, Claude có thể gọi tools từ MCP server trực tiếp trong session.

### Plugins hữu ích cho Documentation

| Plugin | Dùng cho | Ví dụ |
|--------|----------|-------|
| **GitHub** | PR management, issue tracking | "Tạo PR comment tóm tắt changes trong guide/" |
| **Notion** | Knowledge base, cross-reference | "Query Notion database tìm SOPs liên quan đến module 05" |
| **Slack** | Notifications, review requests | "Gửi summary review vào channel #docs" |
| **Filesystem** | Đọc files ngoài project scope | Access shared docs từ thư mục khác |

### "MCP provides tools, Skills teach how to use them"

MCP server cung cấp *capabilities* (đọc Notion page, tạo GitHub PR). Nhưng Claude không tự biết *khi nào* và *cách nào* dùng tools đó trong documentation workflow. Đó là vai trò của Skills:

```text
MCP (tool):   notion-search → trả về danh sách pages
Skill (how):  "Khi user nói 'kiểm tra cross-ref', search Notion
               cho SOPs liên quan, so sánh với guide/ content"
```

Kết hợp: MCP mở rộng khả năng, Skill chuẩn hóa cách dùng.

### Approve Permissions cho Plugins

Mỗi MCP tool cần approve lần đầu sử dụng. Có thể pre-approve trong `.claude/settings.json`:

```jsonc
{
  "permissions": {
    "allow": [
      "mcp__github__list_issues",
      "mcp__notion__search"
    ]
  }
}
```

> [!TIP]
> Chỉ pre-approve tools bạn hiểu rõ. MCP tools có thể đọc/ghi data bên ngoài — review permissions trước khi allow cho toàn team.

## 5.15 External Resources & Further Reading

Tổng hợp tài liệu tham khảo cho Claude Code documentation workflow. Bảng dưới xếp theo thứ tự ưu tiên đọc — từ essential đến niche.

### Official Documentation

| Resource | Mô tả | Khi nào đọc |
|----------|-------|-------------|
| [Claude Code Docs](https://code.claude.com/docs/en/) | Tài liệu chính thức đầy đủ | Đọc đầu tiên — reference cho mọi feature |
| [Best Practices](https://code.claude.com/docs/en/best-practices) | CLAUDE.md design, verification, cost | Sau khi setup xong, trước khi bắt đầu project |
| [Extend Claude Code](https://code.claude.com/docs/en/extending) | Skills vs hooks vs MCP comparison | Khi cần chọn mechanism mở rộng |
| [Claude Code Changelog](https://code.claude.com/docs/en/changelog) | Feature mới, breaking changes | Mỗi tuần — features thay đổi nhanh |

### Project References

| Resource | Đường dẫn |
|----------|-----------|
| Claude Code Setup Cheat Sheet | [reference/claude-code-setup.md](../reference/claude-code-setup.md) |
| Model Specs & Pricing | [reference/model-specs.md](../reference/model-specs.md) |
| Skills List | [reference/skills-list.md](../reference/skills-list.md) |
| Config Architecture (6 lớp) | [reference/config-architecture.md](../reference/config-architecture.md) |

### Related Modules

| Module | Liên quan | Khi nào đọc |
|--------|-----------|-------------|
| [Cowork Setup](03-cowork-setup.md) | So sánh Claude Desktop vs Claude Code | Khi cần quyết định dùng tool nào cho tác vụ cụ thể |
| [Doc Workflows](01-doc-workflows.md) | Documentation patterns, SOP templates | Khi cần template cho tác vụ documentation lặp lại |

### Community & Blog

- [Mintlify Blog — Claude Code for Docs](https://mintlify.com/blog) — Kinh nghiệm thực tế dùng CC viết documentation, bao gồm bài học "trust but verify"
- [Claude Code GitHub Issues](https://github.com/anthropics/claude-code/issues) — Bug reports, feature requests, community workarounds

[Nguồn: Claude Code Docs]

---

← [Cowork Workflows](04-cowork-workflows.md) | [Tổng quan](../base/00-overview.md) | [Custom Style →](06-custom-style.md)
