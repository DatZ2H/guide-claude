# Project Overview — Claude Guide cho Kỹ sư Phenikaa-X

Version: xem `VERSION` (hiện tại: 5.1) | Updated: 2026-03-04

## Phase

Internal Review — v5.0 cho team Phenikaa-X dùng thử. Mục tiêu: 12 modules hoàn chỉnh cho kỹ sư Phenikaa-X (tự động hóa, R&D, Robotics).

## Trạng thái modules

| Module | File | Score | Status |
|--------|------|:-----:|--------|
| 00 | guide/00-overview.md | 8.8 🟢 | Sprint-patched v4.2 |
| 01 | guide/01-quick-start.md | 8.3 🟢 | Sprint-patched v4.2 |
| 02 | guide/02-setup-personalization.md | 8.0 🟢 | Sprint-patched v4.2 |
| 03 | guide/03-prompt-engineering.md | 8.8 🟢 | Sprint-patched v4.2 |
| 04 | guide/04-context-management.md | 8.0 🟢 | Sprint-patched v4.2 |
| 05 | guide/05-workflow-recipes.md | 7.8 🟡 | Updated v5.0 — thêm 2 Cowork recipes |
| 06 | guide/06-tools-features.md | 8.3 🟢 | Updated v5.0 — Sonnet 4.6 default |
| 07 | guide/07-template-library.md | 8.8 🟢 | Sprint-patched v4.2 |
| 08 | guide/08-mistakes-fixes.md | 8.0 🟢 | Sprint-patched v4.2 |
| 09 | guide/09-evaluation-framework.md | 8.8 🟢 | Sprint-patched v4.2 |
| 10 | guide/10-claude-desktop-cowork.md | TBD 🟡 | Refactored v5.0 — Scheduled Tasks, Security, Troubleshooting |
| 11 | guide/11-cowork-workflows.md | TBD 🔵 | New v5.0 — 12 workflow templates |
| ref | guide/reference/config-architecture.md | 8.0 🟢 | Sprint-patched v4.2 |
| ref | guide/reference/skills-list.md | 7.5 🟡 | Updated v5.0 — enterprise plugins |

> v5.0 released for internal review. Modules 10+11: scored after review cycle.

## Cấu trúc thư mục

```
Guide Claude/
├── README.md
├── VERSION                         SSOT cho version number
├── project-state.md                File này — project overview
│
├── guide/                          Content (12 modules + reference/)
│   ├── 00-overview.md → 11-cowork-workflows.md
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
