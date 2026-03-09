---
name: nav-update
description: Auto-update prev/next navigation links trong guide/ files. Trigger khi user nói "update nav", "fix navigation", "nav-update", hoặc sau khi thêm/xóa/rename module. Output danh sách files updated + verification.
user-invocable: true
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
  - Edit
---

# Nav Update — Guide Claude Project

Skill này scan guide/{base,doc,dev}/ và auto-update prev/next navigation links ở cuối mỗi module file.

## Trigger

Kích hoạt khi user:
- Nói "update nav", "fix navigation", "nav-update"
- Sau khi thêm, xóa, hoặc rename module file
- Trước khi bump version (verify navigation)

## Navigation Format

### Pattern chung

```markdown
← [Prev Title](prev-file.md) | [Tổng quan](overview-path) | [Next Title →](next-file.md)
```

### Rules theo tier

| Tier | Overview path | First file | Last file |
|------|--------------|------------|-----------|
| base/ | `00-overview.md` | Không có ← prev (00 là root) | Không có next → |
| doc/ | `../base/00-overview.md` | Không có ← prev | Không có next → |
| dev/ | `../base/00-overview.md` | Không có ← prev | Không có next → |

### Đặc biệt: base/00-overview.md

```markdown
[Tổng quan](00-overview.md) | [Quick Start →](01-quick-start.md)
```

(Không có ← vì 00 là root)

## Quy trình

### Bước 1 — Scan files

List `.md` files trong guide/base/, guide/doc/, guide/dev/ (sorted by filename).
Bỏ qua guide/reference/ (không có nav links).

### Bước 2 — Xác định thứ tự

Mỗi tier: sort files theo prefix số (00, 01, 02...).
Xây ordered list: `[{file, title, prev, next}]`.

Title lấy từ heading `#` đầu tiên trong file. Nếu title quá dài, dùng short name:
- Lấy phần sau số prefix, bỏ `.md`, title-case
- Ví dụ: `04-context-management.md` → "Context Management"

### Bước 3 — Generate nav lines

Với mỗi file:
1. Đọc file, tìm nav line hiện tại (pattern: dòng chứa `[Tổng quan]` + `←` hoặc `→`)
2. Generate nav line mới theo rules
3. So sánh: nếu khác → update

### Bước 4 — Apply updates

Dùng Edit tool để replace nav line cũ bằng mới.
Nếu file chưa có nav line → append ở cuối (sau `---` separator).

### Bước 5 — Report

Output format:

```
## Nav Update — [ngày]

Updated: X files
Unchanged: Y files
Missing nav (added): Z files

### Changes:
- base/03-prompt-engineering.md: updated prev link
- dev/01-claude-code-setup.md: added nav line

### Verification:
- Total nav links: N
- All targets exist: YES/NO
```

## Rules

- KHÔNG sửa content — chỉ nav line ở cuối file
- Nav line phải là dòng cuối cùng (hoặc cuối cùng trước blank line)
- Separator `---` trước nav line nếu chưa có
- reference/ files KHÔNG có nav links — skip
- Luôn verify target files tồn tại sau khi update
