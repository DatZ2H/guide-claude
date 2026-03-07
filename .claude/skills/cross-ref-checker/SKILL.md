---
name: cross-ref-checker
description: Scan toàn bộ guide/ folder tìm stale cross-references trong Guide Claude project. Trigger khi user nói "kiểm tra cross-references", "tìm stale references", "scan references", "cross-ref sweep", hoặc trước khi bump version. Output: danh sách items cần fix, phân loại theo mức độ ưu tiên.
---

# Cross-Reference Checker — Guide Claude Project

Skill này scan tất cả module files (base/, doc/, dev/, reference/) để tìm references đã lỗi thời sau restructure hoặc version changes.

## Trigger

Kích hoạt khi user:
- Nói "kiểm tra cross-references", "scan references", "cross-ref sweep"
- Chuẩn bị bump version (chạy trước version-bump)
- Sau khi restructure folders hoặc rename files

## Patterns cần tìm

### Nhóm 1 — File paths lỗi thời (Critical)
- `outputs/` hoặc `_project-setup/` → phải là `guide/` hoặc `.claude/`
- `00-README.md` → phải là `00-overview.md`
- `_memory/` → đã deprecated, xóa references
- Old flat paths `guide/XX-*.md` (vd `guide/03-prompt-engineering.md`) → phải là `guide/base/03-*.md`, `guide/doc/XX-*.md`, hoặc `guide/dev/XX-*.md`
- `M00`, `M01`, ..., `M12` references → phải là `base/XX`, `doc/XX`, `dev/XX`

### Nhóm 2 — Version references (High)
- Hardcoded `**Version:** X.X` trong module headers → phải link về `VERSION` file
- Version numbers trong body text nếu không phải changelog → kiểm tra có đúng không

### Nhóm 3 — Internal links (Medium)
- `[[wikilink]]` hoặc `[text](path)` trỏ đến file không tồn tại trong guide/
- Module-to-module references kiểu "xem Module X, mục Y.Z" → verify heading vẫn tồn tại

### Nhóm 4 — _memory/ references (Low — chỉ trong body, không phải changelog)
- Bất kỳ nơi nào còn reference đến `_memory/` → đã deprecated, cần xóa hoặc update

## Quy trình

### Bước 1 — Đọc danh sách files
List toàn bộ `.md` files trong `guide/base/`, `guide/doc/`, `guide/dev/`, `guide/reference/`.

### Bước 2 — Scan từng pattern
Với mỗi pattern trong 4 nhóm trên: grep/search trong tất cả module .md files (không scan .bak).

### Bước 3 — Output checklist

Format output:

```
## Cross-Reference Check — [ngày]

### 🔴 Critical (cần sửa trước khi release)
- [file:dòng] — [mô tả vấn đề] → [gợi ý fix]

### 🟡 High (nên sửa trong sprint này)
- [file:dòng] — [mô tả vấn đề] → [gợi ý fix]

### 🟢 Medium / Low (có thể để sau)
- [file:dòng] — [mô tả vấn đề] → [gợi ý fix]

### ✅ PASS — Không tìm thấy issues
[Pattern nào đã clean]

**Tổng: X critical, Y high, Z medium/low**
```

### Bước 4 — Hỏi action

Sau khi output checklist, hỏi: "Anh muốn sửa ngay (tôi fix từng item) hay export checklist ra file để làm sau?"

## Rules

- KHÔNG tự ý sửa file — chỉ report
- Phân biệt rõ "intentional mention" (giải thích tại sao bỏ) vs "stale reference" (vẫn hướng dẫn dùng pattern cũ)
- Changelog entries là historical — KHÔNG flag là stale
- Nếu không tìm thấy issues → output "✅ All checks PASS" và confirm sẵn sàng version bump
