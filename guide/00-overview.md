# Claude Guide cho Kỹ sư Phenikaa-X

**Version:** xem [VERSION](../VERSION) | **Cập nhật:** 2026-03-02
**Claude models:** Opus 4.6 / Sonnet 4.6 / Haiku 4.5

---

## Giới thiệu

Tài liệu này hướng dẫn sử dụng Claude AI hiệu quả cho công việc kỹ thuật hàng ngày -- từ viết prompt cơ bản đến quản lý context trong conversation dài, từ tạo tài liệu chuyên nghiệp đến phân tích lỗi hệ thống.

**Đối tượng chính:** Kỹ sư tự động hóa, R&D, Robotics tại Phenikaa-X (AMR, ROS, SLAM, Lidar).

**Đối tượng mở rộng:** Bất kỳ kỹ sư kỹ thuật nào muốn sử dụng Claude hiệu quả.

---

## Cấu trúc 12 Modules

| Module | Tên | Mô tả | Mức độ |
|--------|-----|-------|--------|
| **00** | Overview (file này) | Mục lục, learning paths, conventions | -- |
| **01** | Quick Start | Bắt đầu với Claude trong 15 phút | Beginner |
| **02** | Setup & Personalization | Projects, Styles, Memory, MCP | Beginner-Intermediate |
| **03** | Prompt Engineering | 6 nguyên tắc, 7 kỹ thuật, Module System | Intermediate |
| **04** | Context Management | Context Window, Drift, Handover | Intermediate |
| **05** | Workflow Recipes | 14 quy trình copy-paste | Intermediate |
| **06** | Tools & Features | Cheat sheet tính năng Claude | Beginner-Intermediate |
| **07** | Template Library | 22 templates T-01 đến T-22 | Mọi level |
| **08** | Mistakes & Fixes | 6 nhóm lỗi phổ biến và cách sửa | Beginner-Intermediate |
| **09** | Evaluation Framework | Đánh giá chất lượng output | Intermediate |
| **10** | Claude Desktop & Cowork | Cowork mode, Folder Instructions, Scheduled Tasks | Beginner-Intermediate |
| **11** | Cowork Workflows Library | 12 workflows copy-paste cho Cowork | Intermediate |

---

## 3 Learning Paths

### Path A: Người mới bắt đầu (1-2 giờ)

Chưa từng dùng Claude hoặc mới dùng vài lần.

```
01 Quick Start (15 phút)
    |
02 Setup & Personalization (20 phút)
    |
07 Template Library (tra cứu khi cần)
    |
08 Mistakes & Fixes (15 phút)
```

**Kết quả:** Biết cách dùng Claude cơ bản, đã setup workspace, có templates sẵn sàng dùng.

> **Nếu dùng Claude Desktop:** Thêm Module 10 (Claude Desktop & Cowork) sau Module 02.

### Path B: Người muốn nâng cao (2-3 giờ)

Đã dùng Claude, muốn hiệu quả hơn.

```
03 Prompt Engineering (25 phút)
   → đặc biệt mục 3.5 (Task Decomposition) cho workflow nhiều bước
    |
04 Context Management (15 phút)
    |
05 Workflow Recipes (25 phút)
    |
09 Evaluation Framework (10 phút)
```

**Kết quả:** Viết prompt chuyên nghiệp, quản lý conversation dài, có quy trình cho từng loại task.

### Path C: Tra cứu nhanh (khi cần)

Đã nắm cơ bản, cần tìm thông tin cụ thể.

```
06 Tools & Features -- tra cứu tính năng
07 Template Library -- tìm template phù hợp
08 Mistakes & Fixes -- khi gặp vấn đề
```

---

## Conventions trong tài liệu

### Nguồn trích dẫn

| Marker | Nghĩa |
|--------|-------|
| [Nguồn: Anthropic Docs] + URL | Thông tin từ tài liệu chính thức Anthropic |
| [Ứng dụng Kỹ thuật] | Ví dụ ứng dụng nguyên tắc chính thức vào bối cảnh Phenikaa-X |
| [Cập nhật MM/YYYY] | Thông tin mới hoặc thay đổi so với version trước |

### Format

- **Tiếng Việt** là ngôn ngữ chính, thuật ngữ kỹ thuật giữ **tiếng Anh**
- `{{variable_name}}` -- placeholder cần thay bằng giá trị thực
- XML tags trong code blocks -- copy-paste vào Claude
- Mermaid diagrams -- flowcharts và decision trees (hiển thị tốt trên các Markdown viewers hỗ trợ)
- Tables -- so sánh, tra cứu nhanh

### Ký hiệu trạng thái

- BAD/GOOD -- so sánh prompt kém vs tốt
- CẢNH BÁO -- thông tin safety quan trọng
- LƯU Ý -- tips và best practices

---

## Thông tin cập nhật

### Version 5.0 (03/2026)

- Thêm Module 11: Cowork Workflows Library — 12 workflows copy-paste cho AMR engineering (SOP từ notes, batch review, báo cáo tuần, Word↔Markdown, glossary enforcement, training materials, extract data PDF, tổ chức folder, release notes, meeting prep, incident report, diff report)
- Refactor Module 10: thêm §10.5 Scheduled Tasks, §10.14 Desktop Commander & Cross-session Memory, §10.15 Customize Tab, §10.17 Security Best Practices, §10.18 Troubleshooting — mở rộng từ 13 lên 18 sections
- Currency sweep Modules 05, 06, reference/skills-list: cập nhật model names (Sonnet 4.6 / Opus 4.6), enterprise plugins, skills mới
- Thêm `machine-readable/llms.txt` — machine-readable index theo convention Florian Bruniaux cho AI crawlers
- Update CLAUDE.md và project-state.md: phản ánh v5.0 scope, 12 modules, 2-tier architecture
- Cross-ref fixes: Module 00 thêm Module 11 vào table và file tree, Module 10 "Tiếp theo" section thêm link Module 11
- Bump version từ 4.2

### Version 4.2 (03/2026)

- Fix 12 Medium issues Sprint 3 (M-01, M-04, M-06–M-08, M-11, M-13, M-14, M-16–M-18): guide/05, guide/07, guide/08, guide/10, ref/skills-list
- Fix 12 accuracy/terminology issues Sprint 2 (8H + 4M): guide/00, guide/01, guide/03, guide/06, guide/08, guide/10, ref/skills-list
- Audit cycle hoàn tất: 24/25 issues resolved (9 Critical + 14 High + 12 Medium) — overall health 7.2 → 8.3/10
- Update CLAUDE.md: sửa module status, thêm Thinking terminology rule (Extended thinking ≠ Adaptive Thinking), cập nhật folder structure, skills/commands list
- Xóa `.claude/worktrees/` orphan artifact, dọn `_scaffold/memory-starter/` deprecated folder
- Sửa stale references: ET/AT terminology, Extended thinking UI setting vs API feature, deprecated session-state.md references
- Thêm deprecation notes cho config-architecture.md (session-state template)
- Bump version từ 4.1

### Version 4.1 (03/2026)

- Thêm `guide/reference/config-architecture.md` — single source of truth cho 6 lớp cấu hình Claude (Profile Preferences → Global CLAUDE.md → Project Instructions → Project Knowledge → Folder Instructions → Skills)
- Thêm `_scaffold/project-instructions/` — 4 templates cho claude.ai Project Instructions (basic, tech-doc, troubleshooting, code-review) + README hướng dẫn chọn template
- Thêm `_scaffold/global-instructions/global-CLAUDE-phenikaa-x.md` — template Global CLAUDE.md cho Cowork
- Thêm `_scaffold/skill-templates/SKILL-template/SKILL-template.md` — folder-format skill template (thay thế file đơn cũ)
- Thêm `.claude/SETUP.md` — project manifest: skills trigger phrases, global instructions, plugins checklist cho maintainer mới
- Update Module 10: thêm §10.4.1 so sánh Folder Instructions vs Project Instructions (bảng 8 tiêu chí + decision tree)
- Update Module 10: thêm §10.6.7 tạo Project-level Skill, §10.6.8 Plugins workflow, §10.6.9 Configuration Lifecycle
- Update Module 02: thêm cross-link → `_scaffold/project-instructions/` + `config-architecture.md`
- Sửa path `skills-list.md` → `guide/reference/skills-list.md` trong Module 10 (§10.6.2)
- Deprecate `_scaffold/skill-templates/SKILL-template.md` → moved to `.bak`
- Deprecate `_memory/` folder và xóa `_scaffold/memory-starter/` — chuyển từ 3-tier (`guide/` + `.claude/` + `_memory/`) sang 2-tier (`guide/` + `.claude/`)
- Fix 12 accuracy/terminology issues (Sprint 2): guide/06 §6.1 §6.3, guide/02 §2.4, guide/08, guide/10, guide/01, ref/config-architecture, ref/skills-list, _scaffold/CLAUDE-template
- Bump version từ 4.0

### Version 4.0 (03/2026)

- Restructure sang 3-tier architecture: `guide/` + `.claude/` + `_memory/`
- Reframe Two-Layer Knowledge: bỏ mandatory sync protocol → Cowork-primary workflow + `project-state.md` là context transfer document
- Recipe 5.11: bỏ bước 7 (Sync mandatory) → optional context transfer
- Tạo 4 project-level skills trong `.claude/skills/`
- `_memory/` giảm từ 4 files → 2 files (session-state + decisions-log)
- Thêm VERSION file làm SSOT cho version number
- Tạo `_scaffold/` — bộ starter templates cho project Cowork mới (README, CLAUDE-template, project-state-template, memory-starter, skill-templates)
- Thêm mục 10.8.3: `_scaffold/` Starter Template
- Bump version từ 3.5

**Migration notes (từ v3.5 → v4.0):**

| Thay đổi | v3.5 | v4.0 |
|----------|------|------|
| Skills folder | `_project-setup/` | `.claude/skills/` — cập nhật CLAUDE.md nếu đang dùng path cũ |
| `_memory/` | 4 files (handoff, todo, context-map, decisions-log) | 2 files — bỏ `handoff.md`, `todo.md`, `context-map.md`; consolidate vào `session-state.md` |
| `project-state.md` vai trò | Sync target bắt buộc (weekly + trigger) | Briefing document on-demand — paste vào Project Chat khi cần, không sync định kỳ |
| Recipe 5.11 bước 7 | "Sync mandatory" | Bỏ bước này — context transfer là optional, chạy khi cần |
| Tạo project mới | Setup thủ công từ đầu | Copy `_scaffold/`, customize `{{placeholder}}`, done |

### Version 3.5 (03/2026)

- Thêm section 4.9: Two-Layer Knowledge Model — giải quyết desync giữa Project Knowledge (static) và Cowork folder (living files)
- Thêm section 10.8.2: project-state.md — Context Transfer Document (prompt export, hướng dẫn update khi cần)
- Update Recipe 5.11: thêm bước 7 (Update optional) vào Hybrid Workflow (6 giai đoạn → 7 giai đoạn)
- Update section 2.2: thêm hướng dẫn Two-Layer Knowledge cho Project Knowledge
- Tạo `project-state.md` — context transfer document giữa Project và Cowork
- Khởi tạo `_memory/` folder đầy đủ (context-map, decisions-log, handoff, todo)
- Bump version từ 3.4

### Version 3.4 (03/2026)

Bổ sung nội dung 6 gaps trong workflow nhiều bước và quản lý files:

- Thêm mục 3.5: Task Decomposition — framework quyết định khi nào tách task, 5 tiêu chí, anti-patterns
- Thêm mục 4.8: Output Quality Degradation — giải thích cơ chế, ngưỡng thực tế, 3 workaround patterns
- Thêm mục 9.6: In-Progress Review — checklist review theo 5 loại output, risk-based approach
- Thêm Module 08 Nhóm 6: Lỗi lan truyền workflow — error propagation, prevention patterns, recovery framework
- Thêm Module 10 mục 10.9: Pre-task Planning — scope analysis, Prompt Package pattern, case study
- Mở rộng Module 10 mục 10.7: thêm File Recovery subsection
- Thêm Recipe 5.12, 5.13, 5.14 vào Module 05
- Thêm T-19, T-20, T-21, T-22 vào Module 07 (tổng: 22 templates)
- Re-number Module 10: Task Lifecycle 10.9 → 10.10
- Mở rộng section 10.6: Plugins & Skills — taxonomy (Type × Trust), skills khuyến nghị, an toàn & governance
- Restructure skills-list.md theo phân loại Type × Trust
- Update section 6.14: tách rõ Skills / Plugins / MCP Connectors
- Cập nhật cross-references toàn bộ Guide
- Bump version từ 3.3

### Version 3.3 (03/2026)

- Thêm section 4.7: Context Engineering & External Memory — framework 4 thao tác (WRITE/SELECT/COMPRESS/ISOLATE), RAG awareness cho Projects, `_memory/` folder pattern
- Thêm Recipe 5.11: Hybrid Workflow — quy trình kết hợp Chat + Project + Cowork cho dự án dài
- Mở rộng section 10.8: bảng phân chia công việc 3 công cụ (thay vì 2)
- Thêm section 10.8.1: External Memory pattern `_memory/` folder cho Cowork
- Cross-references giữa Module 04, 05, 10 cho workflow mới
- Bump version từ 3.2

### Version 3.2 (02/2026)

- Sửa context window: cả Opus 4.6 và Sonnet 4.6 đều hỗ trợ 1M tokens beta (Modules 01, 04, 06, 10)
- Thêm Module 10 vào bảng "Tiếp theo" trong Module 01
- Thêm mention Claude Desktop/Cowork trong Module 01
- Tách ai-setup-guide.md thành 3 files trong `_project-setup/`
- Thêm cowork-setup-guide.md — hướng dẫn cấu hình Cowork cho project
- Thêm Cowork Session Checklist vào starter-prompts.md
- Xóa ai-setup-guide.md.bak
- Bump version từ 3.1

### Version 3.1 (02/2026)

- Thêm Module 10: Claude Desktop & Cowork (Cowork mode, Global/Folder Instructions, Scheduled Tasks, Plugins, Safety)
- Thêm cross-references từ Module 02 và 06 sang Module 10
- Cập nhật cấu trúc từ 10 lên 11 modules

### Version 3.0 Merged (02/2026)

Tài liệu này là kết quả merge từ 2 nguồn:

- **Sổ Tay Prompt Engineering cho Kỹ sư Phenikaa-X v2.1 LTS** -- chuyên sâu về prompt engineering, Module System, templates, evaluation framework
- **Claude Guide** (7 modules) -- tiếp cận thực tế, workflow recipes, tools coverage, mistakes & fixes

Các thay đổi so với cả hai nguồn:

- Cập nhật model mới: Claude Opus 4.6, Sonnet 4.6 (1M context beta), Haiku 4.5
- Extended thinking (UI toggle) có trên Opus 4.6 và Sonnet 4.6 — bật trong "Search and tools"
- Prefill Response đã deprecated từ Claude 4.6 -- loại bỏ khỏi tài liệu
- Thêm MCP Connectors mở rộng (Notion, Jira, v.v.)
- Context Awareness -- tính năng mới cho Opus 4.6 và Sonnet 4.6
- Thêm 3 templates mới: T-16 (Word), T-17 (Excel), T-18 (PowerPoint)

### Kiểm tra thông tin mới

Thông tin về Claude thay đổi nhanh. Luôn kiểm tra nguồn chính thức:

| Nguồn | URL | Nội dung |
|-------|-----|---------|
| Anthropic Docs | https://docs.anthropic.com | API docs, model specs, prompting guides |
| Anthropic Help Center | https://support.anthropic.com | Claude.ai features, troubleshooting |
| Anthropic News | https://www.anthropic.com/news | Announcements, new features |
| Models Overview | https://docs.anthropic.com/en/docs/about-claude/models/overview | Model specs mới nhất |

---

## Files trong bộ tài liệu

> **Cấu trúc dự án đầy đủ:** xem tại root `README.md`.

```
Guide Claude/
├── guide/                        ← 11 module files
│   ├── 00-overview.md            (file này) Mục lục, learning paths, conventions
│   ├── 01-quick-start.md         Quick Start 15 phút
│   ├── 02-setup-personalization.md   Setup & Personalization
│   ├── 03-prompt-engineering.md  Prompt Engineering (6 nguyên tắc, 7 kỹ thuật)
│   ├── 04-context-management.md  Context Management
│   ├── 05-workflow-recipes.md    Workflow Recipes (14 recipes)
│   ├── 06-tools-features.md      Tools & Features Cheat Sheet
│   ├── 07-template-library.md    Template Library (T-01 đến T-22)
│   ├── 08-mistakes-fixes.md      Mistakes & Fixes (6 nhóm lỗi)
│   ├── 09-evaluation-framework.md    Evaluation Framework
│   ├── 10-claude-desktop-cowork.md   Claude Desktop & Cowork
│   ├── 11-cowork-workflows.md    Cowork Workflows Library (12 workflows)
│   └── reference/                Tài liệu tham chiếu bổ sung
│
├── .claude/                      ← Infrastructure (cho tác giả)
│   ├── CLAUDE.md                 Folder Instructions — Project context & rules
│   ├── settings.json             Hooks (SessionStart)
│   ├── commands/                 Slash commands (/start, /checkpoint...)
│   └── skills/                   Skills on-demand cho documentation workflow
│
├── _scaffold/                    ← Starter templates cho project Cowork mới
│   ├── README-scaffold.md        Hướng dẫn setup
│   ├── CLAUDE-template.md        Template Folder Instructions
│   ├── project-state-template.md Template context transfer doc
│   ├── VERSION                   Giá trị khởi đầu "1.0"
│   ├── skill-templates/          Template tạo skill mới (tham khảo)
│   ├── project-instructions/     Templates cho claude.ai Project Instructions
│   └── global-instructions/      Template Global CLAUDE.md cho Cowork
│
├── project-state.md              ← Project overview (cho người đọc)
└── VERSION                       ← Version number (single source of truth)
```

---

**Bắt đầu:** Nếu bạn mới, đọc Module 01. Nếu đã quen Claude, đọc Module 03.
