---
name: upgrade-guide
description: Scan Guide Claude project for stale data, broken references, and dependency issues. Use when planning updates or checking project health. Trigger khi user nói "upgrade scan", "health check", "kiểm tra stale data", "scan project", hoặc trước khi bắt đầu update cycle.
user-invocable: true
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
---

Current version: !cat VERSION

# Upgrade Guide Scanner — Guide Claude Project

Skill này quét toàn bộ hoặc một phần project để phát hiện stale data, broken references, và dependency issues trước khi update.

## Trigger

Kích hoạt khi user:
- Nói "upgrade scan", "health check", "kiểm tra stale", "scan project"
- Chuẩn bị bắt đầu update cycle lớn
- Sau khi nhiều modules thay đổi và muốn kiểm tra consistency

## Input

`$ARGUMENTS` — một trong hai dạng:
- Module number (vd `03`, `12`) — scan module đó + các files trong `depends-on` của nó
- `all` — scan toàn bộ: guide/base/ (8 files) + guide/doc/ (6 files) + guide/dev/ (6 files) + guide/reference/

Nếu không có argument → hỏi user: "Scan module cụ thể (số module) hay toàn bộ project (all)?"

## Quy trình

### Bước 1 — Xác định scope

Version đã inject ở trên — không cần đọc lại.

Xây dựng danh sách files cần scan:
- Nếu `all`: list toàn bộ `guide/base/*.md` + `guide/doc/*.md` + `guide/dev/*.md` + `guide/reference/*.md`
- Nếu path cụ thể (vd `base/03`, `dev/01`): tìm file match `guide/{tier}/{number}-*.md`, parse `depends-on: [...]`
- Nếu tier (vd `base`, `doc`, `dev`): scan toàn bộ tier đó

Ghi nhớ: today's date từ context (`currentDate`). Tháng stale threshold = 3 tháng trước hôm nay.

### Bước 2 — Scan từng file

Với mỗi file trong danh sách, thực hiện 5 checks:

#### Check A — Stale Content Markers

Tìm pattern `[Cập nhật MM/YYYY]` trong body text (không phải trong code blocks).

Với mỗi marker tìm thấy:
- Parse tháng/năm từ marker
- So sánh với ngưỡng stale (today - 3 tháng)
- Nếu cũ hơn ngưỡng → flag với age tính theo tháng

Cũng check header `**Cập nhật:** YYYY-MM-DD` — flag nếu >6 tháng (module-level staleness).

#### Check B — Cross-links

Tìm tất cả Markdown links dạng `[text](path)` trong file.

Với mỗi link:
- Bỏ qua external URLs (bắt đầu bằng `http://` hoặc `https://`)
- Bỏ qua anchor-only links (`#section`)
- Với relative paths: resolve từ vị trí file hiện tại, kiểm tra file target có tồn tại không
- Nếu không tồn tại → flag là broken

#### Check C — Dependency Warnings

Tìm dòng `depends-on: [...]` trong header của file.

Với mỗi item trong danh sách:
- Item dạng `reference/model-specs` → check `guide/reference/model-specs.md` tồn tại
- Item dạng `base/04-context-management` → check `guide/base/04-*.md` tồn tại
- Item dạng `doc/03-cowork-setup` → check `guide/doc/03-*.md` tồn tại
- Item dạng `dev/01-claude-code-setup` → check `guide/dev/01-*.md` tồn tại
- Nếu không tồn tại → flag là broken dependency

Cũng check dòng `impacts: [...]` tương tự.

#### Check D — Volatile Data

Scan body text (không phải code blocks) cho các pattern:

| Pattern | Mô tả |
|---------|-------|
| `claude-3[-\w]+` | Model IDs thế hệ cũ |
| `\$[0-9].*token` | Hardcoded pricing |
| `[0-9]+K tokens?` | Hardcoded context window sizes |
| `\b(200K\|100K\|128K)\b` | Specific context numbers |

Với mỗi match → flag là "Volatile data — verify còn current".

> [!NOTE]
> Volatile data không chắc là sai — chỉ cần xác nhận lại. Ưu tiên thấp hơn broken refs.

#### Check E — Emoji Compliance

Scan toàn bộ file content (kể cả code blocks) cho banned emoji list:

`💡 🚀 😊 🎯 ✨ 📌 🔥 👉 📝 💪 🤔 ⭐ 🏗️ 📊 🛠️`

Với mỗi match → flag dòng số + ký tự vi phạm.

### Bước 3 — Output report

Format cố định:

```
## Upgrade Report — {{scope}}
**Version:** {{version}} | **Date:** {{today}} | **Stale threshold:** >3 tháng

### Stale Content
| File | Marker | Age | Recommendation |
|------|--------|-----|----------------|
| guide/03-prompt.md:45 | [Cập nhật 06/2025] | 9 tháng | Update hoặc xóa marker |

_(Không có issues)_ — nếu clean

### Broken References
| File | Line | Link | Status |
|------|------|------|--------|
| guide/05-workflow.md:102 | 102 | ../reference/model-specs.md | ❌ File not found |

_(Không có issues)_ — nếu clean

### Dependency Warnings
| File | Issue |
|------|-------|
| guide/07-template.md | depends-on: `09-missing-module` — file không tồn tại |

_(Không có issues)_ — nếu clean

### Volatile Data
| File | Line | Pattern | Recommendation |
|------|------|---------|----------------|
| guide/01-setup.md:88 | 88 | "claude-3-5-sonnet" | Verify còn current |

_(Không có issues)_ — nếu clean

### Emoji Violations
| File | Line | Violation |
|------|------|-----------|
| guide/02-models.md:15 | 15 | 💡 (banned) |

_(Không có issues)_ — nếu clean

### Summary
**{{N}} files scanned. {{Y}} issues found.**

| Category | Count |
|----------|-------|
| Stale content | X |
| Broken references | X |
| Dependency warnings | X |
| Volatile data | X |
| Emoji violations | X |
```

### Bước 4 — Hỏi action

Sau khi output report:

Nếu có issues: "Anh muốn fix ngay (tôi fix từng item theo thứ tự ưu tiên) hay export checklist ra file để làm sau?"

Nếu không có issues: "✅ Project health check PASS — không tìm thấy issues trong scope `{{scope}}`."

## Ưu tiên xử lý

Khi user yêu cầu fix:
1. Broken References (❌ file not found) — fix ngay, ảnh hưởng navigation
2. Broken Dependencies — fix ngay, ảnh hưởng skill logic
3. Emoji Violations — fix nhanh
4. Stale Content — flag để author xem xét, không tự sửa content
5. Volatile Data — chỉ verify, không tự sửa

## Rules

- KHÔNG tự ý sửa content — chỉ report, trừ khi user confirm "fix ngay"
- Changelog entries là historical — KHÔNG flag stale markers trong changelog sections
- Code blocks: KHÔNG flag emoji hoặc volatile data bên trong ` ``` ` blocks (là examples)
- Nếu file không tồn tại khi scan → log là "File not found — skip" trong Summary
- Dùng line numbers chính xác khi flag issue
- Nếu scope `all` và có >20 issues → group by file, không list từng dòng riêng lẻ
