# CLAUDE.md — Guide Claude Project

## Project context
Dự án "Claude Guide cho Kỹ sư Phenikaa-X" — bộ tài liệu 12 modules hướng dẫn sử dụng Claude AI.
- **Version:** xem file `VERSION` (SSOT)
- **Phase:** Internal Review — v5.0 cho team Phenikaa-X dùng thử
- **Đối tượng:** Kỹ sư tự động hóa, R&D, Robotics tại Phenikaa-X
- **Architecture:** 2-tier — guide/ (content) + .claude/ (infra)

## Folder structure
```
guide/                  12 module files (00→11) + reference/
guide/reference/        config-architecture.md, skills-list.md
machine-readable/       llms.txt (machine-readable index theo convention Florian Bruniaux)
.claude/                CLAUDE.md, SETUP.md, settings.json, settings.local.json
.claude/skills/         session-start/, version-bump/, cross-ref-checker/, module-review/, doc-standard-enforcer/
.claude/commands/       start, checkpoint, validate-doc, review-module, weekly-review (5 files)
_scaffold/              Starter templates (project-instructions/, global-instructions/, skill-templates/)
project-state.md        Project overview (cho người đọc)
VERSION                 SSOT cho version number
```

## Language rules
- **Ngôn ngữ chính:** Tiếng Việt
- **Thuật ngữ kỹ thuật:** giữ tiếng Anh — KHÔNG Việt hóa (AMR, ROS, SLAM, Lidar, skill, hook, prompt...)
- **Placeholders:** `{{variable}}`
- **Source markers:**
  - `[Nguồn: ...]` — official documentation
  - `[Ứng dụng Kỹ thuật]` — applied examples
  - `[Cập nhật MM/YYYY]` — time-sensitive content
- **Thinking features:** `Extended thinking` = UI toggle (Settings > Search and tools). `Adaptive Thinking` = API feature (`thinking: {type: "adaptive"}`). KHÔNG dùng hoán đổi.

## Writing standards
- **Heading hierarchy:** `#` title → `##` section → `###` subsection — KHÔNG skip level
- **Code blocks:** luôn kèm language tag (```python, ```yaml, ```bash...)
- **Cross-links:** dùng relative paths (`../guide/04-context-management.md#section`)
- **File naming:** lowercase, dấu gạch ngang, prefix số thứ tự (01-, 02-...)
- **Module header:** Module 00 có version link `[VERSION](../VERSION)` (SSOT); modules 01–10 không bắt buộc — KHÔNG hardcode version

## Rules — PHẢI tuân thủ
1. **Git-first backup:** Chạy `/checkpoint` trước khi bắt đầu edit module lớn. File `.bak` không nên tạo (đã thêm vào `.gitignore`) — trừ khi làm việc offline không có Git access.
2. **Check version:** khi edit module → đọc `VERSION` trước
3. **Version bump:** sửa `VERSION` trước — module headers tự reflect, KHÔNG sửa thủ công từng file
4. **No destructive git:** KHÔNG force push, reset --hard, hoặc xóa branch mà không hỏi user
5. **project-state.md:** update sau milestone lớn (version bump, structural changes)
6. **Pre-publish verify:** trước khi document Memory/plan availability hoặc feature defaults, verify tại support.claude.com — features thay đổi thường xuyên

## Git workflow
- **Branch naming:** `feat/<topic>`, `fix/<topic>`, `docs/<topic>`
- **Commit message:** tiếng Việt ngắn gọn, ví dụ: `Thêm cross-link module 03 → config-architecture`
- **Main branch:** `master` — luôn tạo PR thay vì push trực tiếp
- **Không commit:** `.bak` files

## Token optimization
- **Default model:** Sonnet — dùng cho hầu hết tác vụ (edit, search, review)
- **Switch Opus khi:** architectural decisions, complex refactoring, multi-file analysis
- **Giảm token:** đọc file có `offset`/`limit` khi file > 500 dòng
- **Skill thay vì prompt dài:** dùng skill có sẵn thay vì viết lại instructions mỗi lần

## Available skills
*Project skills (`.claude/skills/`):*

| Skill | Trigger |
|-------|---------|
| `/session-start` | Bắt đầu session mới, "tiếp tục", "còn lại gì" |
| `/version-bump` | "bump version", "lên version", "release vX.X" |
| `/doc-standard-enforcer` | Edit module, thêm content trong `guide/` |
| `/cross-ref-checker` | Kiểm tra cross-references trong module |
| `/module-review` | Deep review một module (underlying skill cho `/review-module`) |

*Global built-in (không phải project skill):*

| Skill | Note |
|-------|------|
| `/simplify` | Review code quality — available toàn Claude Code |

## Available commands
*(`.claude/commands/`)*

| Command | Trigger |
|---------|---------|
| `/start` | Đầu mỗi session |
| `/checkpoint` | Quick commit |
| `/validate-doc` | Kiểm tra module — argument: số module (vd `03`) |
| `/review-module` | Deep review module — argument: số module (vd `06`) |
| `/weekly-review` | Review hàng tuần |

## Module status (quick ref)
| Range | Status |
|-------|--------|
| 00–09 | v4.2 base + v5.0 currency sweep — 🟢 |
| 10 | Refactored v5.0 — Scheduled Tasks, Security, Troubleshooting 🟢 |
| 11 | New v5.0 — 12 workflow templates 🔵 |
| reference/ | config-architecture 🟢, skills-list Updated v5.0 🟢 |

## Khi nào update file này
- Thêm skill mới → update bảng Available skills
- Thay đổi folder structure → update Folder structure section
- Thay đổi conventions → update Language rules / Writing standards
