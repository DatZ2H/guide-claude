# Claude Guide cho Kỹ sư Phenikaa-X

Bộ tài liệu 3-tier hướng dẫn sử dụng Claude AI hiệu quả cho công việc kỹ thuật — từ prompt engineering đến workflow automation.

**Version:** xem file `VERSION`

**Đối tượng:** Kỹ sư tự động hóa, R&D, Robotics tại Phenikaa-X

## Cấu trúc dự án

| Thư mục | Nội dung | Dành cho |
|---------|---------|----------|
| `guide/base/` | 8 modules nền tảng — ai cũng cần | Tất cả kỹ sư |
| `guide/doc/` | 6 modules Technical Writing & Cowork | Doc authors |
| `guide/dev/` | 6 modules Developer & Automation | Developers |
| `guide/reference/` | 12 files tra cứu nhanh (cheatsheets, specs, templates) | Tất cả |
| `.claude/` | Folder Instructions + Skills + Hooks | Claude (runtime) |
| `_scaffold/` | Templates để clone cho project mới | Authors (reuse) |
| `machine-readable/` | llms.txt — machine-readable index cho AI | AI tools |

## Bắt đầu đọc

> Mở `guide/base/00-overview.md` để xem mục lục, learning paths, và conventions.

## Cho tác giả / maintainers

- `project-state.md` — trạng thái dự án, dùng sync với Project chat
- `VERSION` — single source of truth cho version number
- `upgrade-plan-v8.md` — plan chi tiết upgrade v7.0 → v9.0 (completed)
- `.claude/SETUP.md` — onboarding cho maintainer mới
