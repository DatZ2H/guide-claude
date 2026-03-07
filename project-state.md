# Project Overview — Claude Guide cho Kỹ sư Phenikaa-X

Version: xem `VERSION` (hiện tại: 9.0) | Updated: 2026-03-07

## Phase

v7.0 → v9.0 Upgrade (bắt đầu 2026-03-06). Plan chi tiết: `upgrade-plan-v8.md`.
- S0 automation infrastructure: ✅ Done
- P1 Foundation (S1-S7): ✅ Done (v7.3) — cross-links, source markers, prompt format, Context Sync, 3-way matrix, M08 patterns
- P2 Structure (S8-S15): ✅ Done (v8.0) — tách guide/ thành base/doc/dev, cleanup, navigation
- P3 Dev Content (S16-S22): ✅ Done (v8.3) — viết mới 6 dev modules + ecosystem reference
- P4 Enhancement (S23-S28): ✅ Done (v8.5) — cheatsheets, _scaffold, skills guide, prompt format guide
- P5 Polish (S29-S33): ✅ Done (v9.0) — full audit, content review, navigation finalize, release

## Trạng thái modules

### base/ — Ai cũng cần

| Module | File | Status |
|--------|------|--------|
| 00 | base/00-overview.md | 🟢 v9.0 — 3-tier index, learning paths, dependency graph |
| 01 | base/01-quick-start.md | 🟢 v9.0 — Hybrid examples, AMR callouts |
| 02 | base/02-setup.md | 🟢 v9.0 — Setup cơ bản (Custom Style chi tiết → doc/06) |
| 03 | base/03-prompt-engineering.md | 🟢 v9.0 — Prompt format convention, XML/[]/{{}} standard |
| 04 | base/04-context-management.md | 🟢 v9.0 — Context Sync, Decision Matrix 3-way, Session Lifecycle, Task Lifecycle |
| 05 | base/05-tools-features.md | 🟢 v9.0 — Tools + Desktop + Planning patterns (merged M06+M10+M05) |
| 06 | base/06-mistakes-fixes.md | 🟢 v9.0 — 7 nhóm lỗi, CC anti-patterns extracted sang dev/04 |
| 07 | base/07-evaluation.md | 🟢 v9.0 — Framework universal, doc examples → callout |

### doc/ — Technical Writing audience

| Module | File | Status |
|--------|------|--------|
| 01 | doc/01-doc-workflows.md | 🟢 v9.0 — Doc recipes + Cowork recipes (từ M05) |
| 02 | doc/02-template-library.md | 🟢 v9.0 — Doc templates T-06~T-22 (từ M07) |
| 03 | doc/03-cowork-setup.md | 🟢 v9.0 — Cowork config + workflows (từ M10) |
| 04 | doc/04-cowork-workflows.md | 🟢 v9.0 — 12 Cowork workflows (từ M11) |
| 05 | doc/05-claude-code-doc.md | 🟢 v9.0 — CC cho documentation (từ M12) |
| 06 | doc/06-custom-style.md | 🟢 v9.0 — Custom Style reference + advanced patterns |

### dev/ — Developer audience

| Module | File | Status |
|--------|------|--------|
| 01 | dev/01-claude-code-setup.md | 🟢 v9.0 — CLI install, auth, CLAUDE.md, permissions, sandbox, settings |
| 02 | dev/02-cli-reference.md | 🟢 v9.0 — Commands, flags, slash commands, keyboard shortcuts |
| 03 | dev/03-ide-integration.md | 🟢 v9.0 — VS Code, JetBrains, Desktop, Remote Control, Web |
| 04 | dev/04-agents-automation.md | 🟢 v9.0 — Subagents, Agent Teams, CI/CD, headless mode |
| 05 | dev/05-plugins.md | 🟢 v9.0 — Discover, install, create plugins, MCP ecosystem |
| 06 | dev/06-dev-workflows.md | 🟢 v9.0 — Git, testing, code review, debugging, session management |

### reference/

| File | Status |
|------|--------|
| config-architecture.md | 🟢 SSOT: 6 lớp cấu hình Claude |
| model-specs.md | 🟢 Mermaid flowchart, 5 AMR examples |
| skills-list.md | 🟢 Trust labels, Audience tags |
| skills-guide.md | 🟢 Detailed skills & commands descriptions |
| claude-code-setup.md | 🟢 CC cheat sheet |
| workflow-patterns.md | 🟢 External Memory, _scaffold patterns (từ M10) |
| quick-templates.md | 🟢 Universal templates T-01~T-05 (từ M07) |
| ecosystem-overview.md | 🟢 Community tools, MCP servers, plugins, CI/CD |
| cheatsheet-base.md | 🟢 Quick-reference card Base tier |
| cheatsheet-doc.md | 🟢 Quick-reference card Doc tier |
| cheatsheet-dev.md | 🟢 Quick-reference card Dev tier |
| prompt-format-guide.md | 🟢 XML tags, brackets, placeholders — khi nào dùng gì |

> v9.0 released 2026-03-07. Upgrade v7.0 → v9.0 complete. 3-tier guide fully operational.

## Cấu trúc thư mục

```
Guide Claude/
├── README.md
├── VERSION                         SSOT cho version number
├── project-state.md                File này — project overview
│
├── guide/                          Content (3-tier + reference/)
│   ├── base/                       8 modules (00→07) — ai cũng cần
│   ├── doc/                        6 modules (01→06) — Technical Writing
│   ├── dev/                        6 modules (01→06) — Developer
│   └── reference/                  12 files — tra cứu
│
├── machine-readable/               Machine-readable index
│   └── llms.txt                    Index theo convention Florian Bruniaux (CC BY-SA 4.0)
│
├── _scaffold/                      Starter templates cho project mới
│   ├── project-instructions/       4 templates cho claude.ai
│   ├── global-instructions/        Template Global CLAUDE.md
│   ├── skill-templates/            Template tạo skill
│   ├── examples/                   guide-claude/, dev-example/
│   └── checklists/                 new-project, daily-workflow
│
└── .claude/                        Infrastructure (Claude config)
    ├── CLAUDE.md                   Folder Instructions
    ├── SETUP.md                    Onboarding cho maintainer mới
    ├── settings.json               Hooks (SessionStart, PostToolUse)
    ├── rules/                      6 rules (writing-standards, reference, scaffold, tier-base/doc/dev)
    ├── hooks/                      format-check.py, link-check.py
    ├── commands/                   Slash commands (/start, /checkpoint, /weekly-review...)
    └── skills/                     8 skills (session-start, version-bump, cross-ref-checker, module-review, doc-standard-enforcer, source-audit, upgrade-guide, nav-update)
```

## Quyết định gần nhất

| Ngày | Quyết định | Rationale |
|------|-----------|-----------|
| 2026-03-07 | v9.0 release — P5 Polish complete | 5 sessions: audit, base+ref review, doc+dev review, nav finalize, release |
| 2026-03-07 | P4 Enhancement complete (v8.5) — cheatsheets, _scaffold, skills guide | 6 sessions additive content |
| 2026-03-07 | P3 Dev Content complete (v8.3) — 6 dev modules + ecosystem ref | 7 sessions new content |
| 2026-03-07 | P2 Structure complete (v8.0) — 3-tier guide/base+doc+dev | 8+2 sessions, old files removed, navigation complete |
| 2026-03-07 | P1 Foundation complete (v7.3) — quality fixes | 7 sessions: links, sources, format, Context Sync, matrix, patterns |
| 2026-03-06 | S0: Automation infrastructure — rules, hooks, source-audit skill | QA framework 4 lớp cho upgrade v7→v9 |
| 2026-03-06 | Upgrade plan v7.0→v9.0 approved — 5 phases, ~36 work units | Tài liệu nền tảng, ưu tiên chất lượng |

> Decisions cũ hơn 30 ngày: xem `git log`.

## Conventions

- Tiếng Việt chính, thuật ngữ kỹ thuật giữ tiếng Anh
- `{{variable}}` = placeholder
- Markers: `[Nguồn: ...]`, `[Ứng dụng Kỹ thuật]`, `[Cập nhật MM/YYYY]`
- Heading hierarchy: `#` title → `##` section → `###` subsection
- Code blocks luôn có language tag
