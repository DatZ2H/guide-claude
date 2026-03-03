# CLAUDE.md — Guide Claude Project

## Project context
Dự án "Claude Guide cho Kỹ sư Phenikaa-X" — bộ tài liệu 11 modules hướng dẫn sử dụng Claude AI.
- **Version:** xem file `VERSION` (SSOT)
- **Phase:** Development — đang iterate, chưa publish
- **Đối tượng:** Kỹ sư tự động hóa, R&D, Robotics tại Phenikaa-X
- **Architecture:** 3-tier — guide/ (content) + .claude/ (infra) + _memory/ (persistence)

## Folder structure
```
guide/                  11 module files (00→10) + reference/
guide/reference/        config-architecture.md, skills-list.md
.claude/                CLAUDE.md, SETUP.md, skills/
_scaffold/              Starter templates (project-instructions/, global-instructions/, skill-templates/, memory-starter/)
_memory/                session-state.md + decisions-log.md
project-state.md        Context transfer document (briefing cho Project Chat)
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

## Writing standards
- **Heading hierarchy:** `#` title → `##` section → `###` subsection — KHÔNG skip level
- **Code blocks:** luôn kèm language tag (```python, ```yaml, ```bash...)
- **Cross-links:** dùng relative paths (`../guide/04-context-management.md#section`)
- **File naming:** lowercase, dấu gạch ngang, prefix số thứ tự (01-, 02-...)
- **Module header:** mỗi module có version link `[VERSION](../VERSION)` — KHÔNG hardcode version

## Memory protocol
- **Đầu session:** đọc `_memory/session-state.md` + `_memory/decisions-log.md`
- **Khi quyết định quan trọng:** append vào `_memory/decisions-log.md`
- **Cuối session:** update `_memory/session-state.md`

## Rules — PHẢI tuân thủ
1. **Backup trước khi sửa:** KHÔNG edit file trong `guide/` mà không tạo `.bak` trước
2. **Check version:** khi edit module → đọc `VERSION` trước
3. **Version bump:** sửa `VERSION` trước — module headers tự reflect, KHÔNG sửa thủ công từng file
4. **No destructive git:** KHÔNG force push, reset --hard, hoặc xóa branch mà không hỏi user
5. **project-state.md:** update sau milestone lớn hoặc trước khi brainstorm trên Project Chat

## Git workflow
- **Branch naming:** `feat/<topic>`, `fix/<topic>`, `docs/<topic>`
- **Commit message:** tiếng Việt ngắn gọn, ví dụ: `Thêm cross-link module 03 → config-architecture`
- **Main branch:** `main` — luôn tạo PR thay vì push trực tiếp
- **Không commit:** `.bak` files, `_memory/` (personal state)

## Token optimization
- **Default model:** Sonnet — dùng cho hầu hết tác vụ (edit, search, review)
- **Switch Opus khi:** architectural decisions, complex refactoring, multi-file analysis
- **Giảm token:** đọc file có `offset`/`limit` khi file > 500 dòng
- **Skill thay vì prompt dài:** dùng skill có sẵn thay vì viết lại instructions mỗi lần

## Available skills
| Skill | Trigger |
|-------|---------|
| `/session-start` | Bắt đầu session mới, "tiếp tục", "còn lại gì" |
| `/version-bump` | "bump version", "lên version", "release vX.X" |
| `/simplify` | Review code quality sau khi edit |

<!-- Placeholder: thêm skills mới ở đây -->

## Module status (quick ref)
| Range | Status |
|-------|--------|
| 00, 02, 04, 05, 10 | Draft v3.5–v4.0 (updated for 3-tier) |
| 01, 03, 06–09 | Draft v3.4 (chưa update) |
| reference/ | config-architecture (v4.0), skills-list |

## Khi nào update file này
- Thêm skill mới → update bảng Available skills
- Thay đổi folder structure → update Folder structure section
- Thay đổi conventions → update Language rules / Writing standards
