# CLAUDE.md — Guide Claude Project

<!-- Snapshot v8.5 — xem .claude/CLAUDE.md trong repo gốc cho version mới nhất -->

## Project context
Dự án "Claude Guide cho Kỹ sư Phenikaa-X" — bộ tài liệu 3-tier hướng dẫn sử dụng Claude AI.
- **Version:** xem file `VERSION` (SSOT)
- **Phase:** Upgrade v7.0 → v9.0 (xem `upgrade-plan-v8.md`)
- **Đối tượng:** Kỹ sư tự động hóa, R&D, Robotics tại Phenikaa-X
- **Architecture:** 3-tier — guide/base + guide/doc + guide/dev + guide/reference + .claude/ (infra)

## Folder structure
```
guide/
├── base/               8 modules (00→07) — ai cũng cần
├── doc/                6 modules (01→06) — Technical Writing audience
├── dev/                6 modules (01→06) — Developer audience
└── reference/          config-architecture, model-specs, skills-list, ...
.claude/                CLAUDE.md, settings.json, rules/, hooks/, skills/, commands/
_scaffold/              Starter templates + examples + checklists
VERSION                 SSOT cho version number
```

## Language rules
- **Ngôn ngữ chính:** Tiếng Việt
- **Thuật ngữ kỹ thuật:** giữ tiếng Anh — KHÔNG Việt hóa
- **Placeholders:** `{{variable}}`
- **Source markers:** `[Nguồn: ...]`, `[Ứng dụng Kỹ thuật]`, `[Cập nhật MM/YYYY]`

## Writing standards
- **Heading hierarchy:** `#` → `##` → `###` — KHÔNG skip level
- **Code blocks:** luôn kèm language tag
- **Cross-links:** relative paths (`../base/04-context-management.md#section`)

## Rules — PHẢI tuân thủ
1. **Git-first backup:** `/checkpoint` trước edit lớn
2. **Check version:** đọc `VERSION` trước khi edit module
3. **Version bump:** sửa `VERSION` trước — KHÔNG hardcode
4. **No destructive git:** KHÔNG force push, reset --hard
5. **project-state.md:** update sau milestone lớn

## Git workflow
- **Branch naming:** `feat/<topic>`, `fix/<topic>`, `docs/<topic>`
- **Commit message:** tiếng Việt ngắn gọn
- **Main branch:** `master` — luôn tạo PR

## Available commands
| Command | Trigger |
|---------|---------|
| `/start` | Đầu mỗi session |
| `/checkpoint` | Quick commit |
| `/validate-doc` | Kiểm tra module |
| `/review-module` | Deep review module |
| `/weekly-review` | Review hàng tuần |

## Automation infrastructure
- **Rules (auto-load):** 6 files trong `.claude/rules/` — load theo path
- **PostToolUse hook:** `format-check.py` — heading hierarchy + code block tags
- **Standalone check:** `link-check.py` — cross-links
- **Source verification:** 3-tier standard (Anthropic official → verified repos → community + disclaimer)
