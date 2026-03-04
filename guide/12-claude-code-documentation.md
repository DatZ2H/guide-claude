# Module 12: Claude Code cho Documentation & Technical Writing

**Thời gian đọc:** 35 phút | **Mức độ:** Intermediate
**Cập nhật:** 2026-03-04 | Models: xem [specs](reference/model-specs.md)

---

Module này hướng dẫn sử dụng Claude Code — CLI agent chạy trong terminal — cho documentation và technical writing workflow. Nếu bạn không viết code, đây vẫn là công cụ mạnh cho quản lý tài liệu có Git, batch editing, và quality assurance tự động.

> [!NOTE]
> Module này focus vào **non-coding documentation workflow**. Nếu bạn dùng Claude Code để viết code, tham khảo official docs tại https://code.claude.com/docs.
> Nếu bạn chỉ cần tạo/sửa file đơn lẻ mà không cần Git → xem [Module 10: Cowork](10-claude-desktop-cowork.md).

**Config & Commands reference:** [Claude Code Setup](reference/claude-code-setup.md)

[Nguồn: Claude Code Docs]

---

## 12.1 Claude Code là gì — cho Non-coders

Claude Code là CLI agent chạy trong terminal, dùng chung kiến trúc với Claude Desktop (Cowork) nhưng được thiết kế cho môi trường có Git và file system access rộng hơn. Điểm khác biệt cốt lõi: thay vì chat qua UI, bạn làm việc trong terminal với workflow tự động hóa và batch operations. Section này giải thích khi nào dùng Claude Code thay vì Cowork hoặc claude.ai — đặc biệt cho các kỹ sư documentation không viết code.

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

```
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

## 12.2 Cài đặt & First Session

Hướng dẫn cài đặt Claude Code qua npm, verify bằng `claude --version`, và khởi tạo first session trong thư mục dự án. Lệnh `/init` tạo `CLAUDE.md` mẫu — bước nên làm ngay với project mới. Section này đi kèm checklist nhanh để xác nhận môi trường sẵn sàng.

Xem thêm: [Claude Code Setup — Quick Setup Checklist](reference/claude-code-setup.md#quick-setup-checklist).

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
> Windows: Claude Code chạy native trên PowerShell/CMD hoặc qua WSL2. Nếu dùng WSL2, đặt project files trong WSL filesystem (không phải `/mnt/c/`) để tránh latency khi đọc nhiều file.

### First Session Walkthrough

Sau khi `claude` khởi động và xác thực thành công:

**Bước 1 — Khởi tạo project:**

```text
/init
```

Lệnh này tạo `CLAUDE.md` mẫu trong thư mục hiện tại. Mở file và điền thông tin project (xem template tại [CLAUDE.md Reference](reference/claude-code-setup.md#claudemd-reference)).

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

Xem thêm: [Claude Code Setup — Quick Setup Checklist](reference/claude-code-setup.md#quick-setup-checklist).

## 12.3 Cấu hình 4 lớp (User → Project → Local → Managed)

Claude Code có hệ thống cấu hình 4 lớp theo thứ tự ưu tiên tăng dần: **User** (`~/.claude/CLAUDE.md`) → **Project** (`CLAUDE.md` tại root) → **Local** (`.claude/CLAUDE.md`, không commit) → **Managed** (enterprise policy). Mỗi lớp kế thừa và override lớp dưới. Section này giải thích cách cấu hình từng lớp cho documentation project — language rules, writing standards, emoji policy — và khi nào dùng `.claude/rules/` thay vì CLAUDE.md chính.

Xem thêm: [Claude Code Setup — CLAUDE.md Reference](reference/claude-code-setup.md#claudemd-reference).

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

Xem thêm: [Claude Code Setup — CLAUDE.md Reference](reference/claude-code-setup.md#claudemd-reference).

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

## 12.4 Plan Mode — Explore → Plan → Execute → Commit

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

## 12.5 Slash Commands & Custom Commands

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

## 12.6 Skills cho Documentation

Skills là agent chuyên biệt được gọi từ main session để thực hiện tác vụ có quy trình cố định. Phân biệt hai loại: **invocable** (user trigger thủ công) và **reference** (Claude tự load context). Section này hướng dẫn tạo custom skill cho documentation workflow, giải thích `disable-model-invocation`, và phân tích cost/benefit. Ví dụ thực tế: `doc-standard-enforcer` từ project này.

Xem thêm: [Skills List](reference/skills-list.md).

[Nguồn: Claude Code Docs — Skills]

### Skills Ecosystem

Skills phân loại theo hai trục — Type × Trust:

| | Official | Community |
|--|----------|-----------|
| **Pre-built** | docx, xlsx, pptx, pdf | — |
| **Standalone** | doc-coauthoring, internal-comms | docs-review, obsidian-markdown, mermaidjs-v11... |
| **Plugin** | productivity, product-management | — |

Pre-built Skills tự kích hoạt — không cần cài. Standalone Skills cần thêm thư mục vào `.claude/skills/` (project-level) hoặc cài qua `npx @skill-hub/cli install`. Community skills chưa có badge `[Approved PX]` cần đọc SKILL.md và test kỹ trước khi dùng. Xem đầy đủ: [Skills List](reference/skills-list.md).

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

## 12.7 Subagents cho Review & Research

Subagents là Claude instance độc lập chạy song song hoặc tuần tự với main session, cấu hình qua `.claude/agents/`. Pattern hữu ích nhất cho documentation: **Writer/Reviewer** — main session viết, subagent review theo checklist độc lập không bị bias từ writing context. Section này giải thích khi nào dùng subagent thay vì main session, và cách cấu hình `.claude/agents/` template.

[Nguồn: Claude Code Docs — Sub-agents]

### Concept

Subagent là Claude instance chạy trong isolated context — không chia sẻ conversation history với main session. Main session gửi task, subagent thực hiện rồi trả summary. Điểm mấu chốt: subagent không bị bias bởi context trước đó, nên phù hợp cho review độc lập.

```
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

## 12.8 Session Management

Các lệnh quản lý session: `/clear` (reset context, giữ file), `/rewind` (undo về checkpoint trước), `/rename` (đặt tên để resume sau), `/compact` (tóm tắt context dài). Flag CLI: `--continue` resume session gần nhất, `--resume <id>` resume session cụ thể. Section này cũng đề cập hai failure pattern phổ biến — kitchen sink và over-correction — cùng cách tránh.

Xem thêm: [Claude Code Setup — Essential Commands](reference/claude-code-setup.md#essential-commands).

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

Xem thêm: [Claude Code Setup — Essential Commands](reference/claude-code-setup.md#essential-commands).

## 12.9 Git Integration cho Documentation

Claude Code tích hợp Git natively: tạo branch, commit, đọc git history trong session. Section này hướng dẫn thiết lập Git workflow cho documentation project — branch naming convention, commit message format, pre-commit hooks để validate trước khi commit. Trình bày `SessionStart` hook: chạy tự động khi mở session, hiển thị git status và nhắc checkpoint.

[Nguồn: Claude Code Docs — Git Integration]

[Full content sẽ viết ở S17/S18]

## 12.10 Verification & Quality Assurance

Pattern hiệu quả nhất trong documentation QA là cung cấp cho Claude checklist kiểm tra output của chính nó — thay vì chỉ yêu cầu "viết tốt". Section này trình bày `/validate-doc` (heading hierarchy, language tags, cross-links, emoji policy), `cross-ref-checker` skill (phát hiện broken links), và nguyên tắc thiết kế checklist có tiêu chí pass/fail rõ ràng.

[Full content sẽ viết ở S17/S18]

## 12.11 Permissions & Safety

Claude Code có hệ thống permissions granular: cho phép hoặc deny từng tool (read, write, bash, git) theo scope session hoặc project. Lệnh `/permissions` hiển thị và chỉnh sửa permissions hiện tại. Section này hướng dẫn cấu hình permissions tối giản cho documentation workflow (thường không cần bash rộng), và giải thích sandbox mode — dry-run trước khi approve execute.

Xem thêm: [Claude Code Setup — Permission Templates](reference/claude-code-setup.md#permission-templates).

[Nguồn: Claude Code Docs — Permissions]

[Full content sẽ viết ở S17/S18]

## 12.12 Token Optimization & Cost

Model selection là đòn bẩy lớn nhất cho cost: Haiku cho tác vụ đơn giản (format check, batch rename), Sonnet cho editing và review thông thường, Opus chỉ khi cần phân tích kiến trúc phức tạp. `/compact` tóm tắt context dài để giảm token trong session nhiều file. Section này còn đề cập `offset`/`limit` khi đọc file lớn, và `effort` level để điều chỉnh thinking depth.

Xem thêm: [Model Specs & Pricing](reference/model-specs.md).

[Nguồn: Claude Code Docs — Token Usage]

[Full content sẽ viết ở S17/S18]

## 12.13 Batch & Automation

Claude Code hỗ trợ non-interactive mode qua `claude -p "prompt"` — cho phép pipe input/output, tích hợp CI pipeline, và fan-out pattern (nhiều instance song song). Section này trình bày các use case documentation: validate docs trong PR check, auto-generate changelog từ git diff, batch format nhiều file. Bao gồm ví dụ tích hợp GitHub Actions.

[Nguồn: Claude Code Docs — CLI Usage]

[Full content sẽ viết ở S17/S18]

## 12.14 Plugins & MCP cho Documentation

MCP (Model Context Protocol) cho phép Claude Code kết nối external services qua standardized interface. Lệnh `claude mcp add` thêm plugin từ marketplace hoặc custom server. Section này điểm qua các plugin có ích cho documentation: GitHub (đọc issues, tạo PR comment), Notion (sync markdown ↔ Notion), và hướng dẫn approve permissions cho từng plugin.

[Nguồn: Claude Code Docs — MCP]

[Full content sẽ viết ở S17/S18]

## 12.15 External Resources & Further Reading

Tổng hợp tài liệu tham khảo và community resources cho Claude Code documentation workflow. Ưu tiên đọc: official docs, changelog để track feature mới, community patterns cho documentation-specific use cases.

- [Claude Code Official Docs](https://code.claude.com/docs)
- [Claude Code Setup Cheat Sheet](reference/claude-code-setup.md)
- [Model Specs & Pricing](reference/model-specs.md)
- [Skills List](reference/skills-list.md)
- [Config Architecture](reference/config-architecture.md)

[Full content sẽ viết ở S17/S18]
