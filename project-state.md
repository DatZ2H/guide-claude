# Project Overview — Claude Guide cho Kỹ sư Phenikaa-X

Version: xem `VERSION` (hiện tại: 7.0) | Updated: 2026-03-04

## Phase

v7.0 — Upgrade hoàn tất (2026-03-04). 9 quyết định D1-D9 đã triển khai qua 22 sessions. Sẵn sàng cho Internal Review tại Phenikaa-X.

## Trạng thái modules

| Module | File | Score | Status |
|--------|------|:-----:|--------|
| 00 | guide/00-overview.md | 🟢 | v7.0 — 13 modules, dependency tags, Learning Paths updated |
| 01 | guide/01-quick-start.md | 🟢 | v7.0 — Hybrid examples, AMR callouts, model hints |
| 02 | guide/02-setup-personalization.md | 🟢 | v7.0 — Hybrid examples, AMR callouts, model hints |
| 03 | guide/03-prompt-engineering.md | 🟢 | v7.0 — Full rewrite S11, 7 AMR callouts, 15 model hints |
| 04 | guide/04-context-management.md | 🟢 | v7.0 — Hybrid examples, AMR callouts, model hints |
| 05 | guide/05-workflow-recipes.md | 🟢 | v7.0 — Full rewrite S09/S10, 16 AMR callouts, 18 model hints |
| 06 | guide/06-tools-features.md | 🟢 | v7.0 — Hybrid examples, AMR callouts, model hints |
| 07 | guide/07-template-library.md | 🟢 | v7.0 — Full rewrite S12, 22 AMR callouts, 26 model hints |
| 08 | guide/08-mistakes-fixes.md | 🟢 | v7.0 — Full rewrite S11, 5 AMR callouts, 5 model hints |
| 09 | guide/09-evaluation-framework.md | 🟢 | v7.0 — Hybrid examples, AMR callouts, model hints |
| 10 | guide/10-claude-desktop-cowork.md | 🟢 | v7.0 — Refactored S19: 10.13 → intro + redirect to M12 |
| 11 | guide/11-cowork-workflows.md | 🟢 | v7.0 — Full rewrite S08/S10, 12 AMR callouts, 13 model hints |
| 12 | guide/12-claude-code-documentation.md | 🔵 | New v6.5/v7.0 — Claude Code Documentation, 1190 lines, 26 sections |
| ref | guide/reference/config-architecture.md | 🟢 | v7.0 — SSOT: 6 lớp cấu hình Claude |
| ref | guide/reference/model-specs.md | 🟢 | New v5.1 — Mermaid flowchart, 5 AMR examples, Feature table |
| ref | guide/reference/skills-list.md | 🟢 | v7.0 — Trust labels, Audience tags, [Approved PX], Skill-Recipe Mapping |
| ref | guide/reference/claude-code-setup.md | 🔵 | New v6.5 — CC cheat sheet, Workflow-first, 272 lines |

> v7.0 released 2026-03-04. Toàn bộ 22 sessions hoàn tất. 0 banned emoji, 0 stale anchors, 6 project skills operational.

## Cấu trúc thư mục

```
Guide Claude/
├── README.md
├── VERSION                         SSOT cho version number
├── project-state.md                File này — project overview
│
├── guide/                          Content (13 modules + reference/)
│   ├── 00-overview.md → 12-claude-code-documentation.md
│   └── reference/
│       ├── config-architecture.md  SSOT: 6 lớp cấu hình Claude
│       └── skills-list.md
│
├── machine-readable/               Machine-readable index
│   └── llms.txt                    Index theo convention Florian Bruniaux (CC BY-SA 4.0)
│
├── _scaffold/                      Starter templates cho project mới
│   ├── project-instructions/       4 templates cho claude.ai
│   ├── global-instructions/        Template Global CLAUDE.md
│   └── skill-templates/            Template tạo skill
│
└── .claude/                        Infrastructure (Claude config)
    ├── CLAUDE.md                   Folder Instructions
    ├── SETUP.md                    Onboarding cho maintainer mới
    ├── settings.json               Hooks (SessionStart)
    ├── commands/                    Slash commands (/start, /checkpoint, /weekly-review...)
    └── skills/                     Auto-activate + on-demand skills
```

## Quyết định gần nhất

| Ngày | Quyết định | Rationale |
|------|-----------|-----------|
| 2026-03-04 | D9: Claude Code cho Documentation — Option D Hybrid (Module 12 + reference/claude-code-setup.md) | Narrative guide + lookup cheat sheet cho kỹ sư dùng CC trong doc workflow |
| 2026-03-04 | D8 Emoji policy: Allowlist ⚠️ ✅ ❌ 🔴 🟡 🟢 🔵, Obsidian callouts cho prose | Nhất quán, không noise, dễ maintain |
| 2026-03-04 | D4 Hybrid examples: Doc context (primary) + AMR callout + model hint | Tăng relevance cho kỹ sư kỹ thuật mà không mất tính tổng quát |
| 2026-03-04 | D6 Centralize specs: reference/model-specs.md làm SSOT | Tránh stale data phân tán trong 13 modules |
| 2026-03-03 | Option B cho v5.0: refactor Module 10 + thêm Module 11 + machine-readable layer | Module 10 quá tải → tách setup/security; Module 11 = 12 workflow templates AMR |
| 2026-03-03 | Thêm machine-readable/llms.txt (convention Florian Bruniaux, CC BY-SA 4.0) | Cho phép AI tools index guide dễ hơn; chuẩn bị cho publish |
| 2026-03-03 | Bump v4.1 → v4.2: audit cycle closed (24/25 issues) | Ghi nhận 3 sprints fix, health 7.2→8.3/10 |
| 2026-03-03 | Audit cleanup Option A: giữ final-checkpoint + s7 + next-phase-plan | Lưu record + backlog; xóa s1–s6 đã consumed |
| 2026-03-03 | Deprecate `_memory/` — git history thay thế | Giảm complexity, bỏ persistence layer không cần thiết |
| 2026-03-02 | config-architecture.md làm SSOT cho 6 lớp cấu hình | Unified mental model, dễ cross-link |
| 2026-03-02 | Stable vs Dynamic split: concepts → modules; templates → _scaffold/ | Templates thay đổi nhanh → tách riêng |
| 2026-03-02 | 2-tier architecture: guide/ (content) + .claude/ (infra) | Phân tách content vs infrastructure |
| 2026-03-02 | VERSION file làm SSOT | Tránh hardcode version trong 11+ files |
| 2026-02-28 | Tiếng Việt + thuật ngữ kỹ thuật giữ tiếng Anh | Không Việt hóa AMR, ROS, SLAM, Lidar |

> Decisions cũ hơn 30 ngày: xem `git log`.

## Conventions

- Tiếng Việt chính, thuật ngữ kỹ thuật giữ tiếng Anh
- `{{variable}}` = placeholder
- Markers: `[Nguồn: ...]`, `[Ứng dụng Kỹ thuật]`, `[Cập nhật MM/YYYY]`
- Heading hierarchy: `#` title → `##` section → `###` subsection
- Code blocks luôn có language tag
