---
name: source-audit
description: >
  Scan guide/ files cho source markers theo 3-tier standard. Trigger khi user nói
  "source audit", "kiểm tra sources", "scan sources", "audit markers",
  hoặc cuối session để verify compliance. Output: danh sách sections thiếu markers,
  markers cần update, và phân loại theo mức độ ưu tiên.
---

# Source Audit — Guide Claude Project

Skill này scan tất cả module files trong guide/ để kiểm tra source markers theo 3-tier source verification standard.

## Trigger

Kích hoạt khi user:
- Nói "source audit", "kiểm tra sources", "scan sources", "audit markers"
- Cuối session content editing (best practice)
- Trước version bump

## 3-Tier Source Standard

### Tier 1 — Official (bắt buộc cho core features)

Markers hợp lệ:
- `[Nguồn: Claude Code Docs]` — từ code.claude.com/docs
- `[Nguồn: Anthropic API Docs]` — từ docs.anthropic.com
- `[Nguồn: Anthropic Help]` — từ support.anthropic.com hoặc support.claude.com
- `[Nguồn: Anthropic Blog]` — từ anthropic.com/blog hoặc anthropic.com/news

### Tier 2 — Verified (best practices, patterns)

Markers hợp lệ:
- `[Nguồn: Anthropic GitHub]` — từ github.com/anthropics/*
- `[Nguồn: Write the Docs]` — từ writethedocs.org
- `[Nguồn: ...]` — tên tài liệu/repo cụ thể

### Tier 3 — Community (cần disclaimer)

Markers hợp lệ:
- `[Nguồn: Community — URL]` — community repos
- `[Ứng dụng Kỹ thuật]` — project experience, applied examples
- `[Ghi chú: pattern từ thực tế, không phải official]` — non-official patterns

### Time-sensitive

- `[Cập nhật MM/YYYY]` — bắt buộc cho thông tin có thể thay đổi (model names, pricing, feature availability, defaults)

## Quy trình

### Buoc 1 — Scan files

List tất cả `.md` files trong `guide/` và `guide/reference/` (skip `.bak`).

### Buoc 2 — Cho mỗi file, kiểm tra

**A. Sections có source markers:**
- Grep `[Nguồn:`, `[Ứng dụng Kỹ thuật]`, `[Cập nhật`, `[Ghi chú:`
- Map markers vào sections (`##` headings)

**B. Sections THIẾU markers:**
- Sections mô tả features/behavior nhưng không có marker → flag
- NGOẠI LỆ: changelog entries, table of contents, navigation sections — KHÔNG cần marker

**C. Markers cần review:**
- `[Cập nhật MM/YYYY]` quá 6 tháng → flag "potentially stale"
- Tier 3 markers thiếu disclaimer → flag
- Markers không theo format chuẩn → flag

### Buoc 3 — Output report

Format:

```
## Source Audit — [ngày]

### Scan: [số files] files, [số sections] sections

### 🔴 Missing Markers (sections mô tả features nhưng thiếu source)
- [file] > [section heading] — [mô tả content] → cần [tier gợi ý]

### 🟡 Stale Markers (cần verify hoặc update)
- [file:line] — [Cập nhật MM/YYYY] — đã [X] tháng → verify

### 🟢 Format Issues (nhỏ, sửa nhanh)
- [file:line] — [mô tả vấn đề] → [gợi ý fix]

### ✅ PASS
[Patterns đã clean]

**Tổng: X missing, Y stale, Z format issues**
```

### Buoc 4 — Hỏi action

Sau khi output report, hỏi: "Anh muốn sửa ngay (tôi fix từng item) hay export checklist?"

## Rules

- KHÔNG tự ý sửa file — chỉ report
- Changelog entries là historical — KHÔNG flag thiếu marker
- Table of contents, navigation, index sections — KHÔNG cần marker
- Nếu không tìm thấy issues → output "All checks PASS"
- Priority: Missing (core features) > Stale > Format
