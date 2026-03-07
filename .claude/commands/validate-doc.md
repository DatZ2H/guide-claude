Validate một module guide. Argument: $ARGUMENTS (tier/số như "base/03", "dev/01" hoặc full path như "guide/base/03-prompt-engineering.md").

**Bước 1 — Resolve file path:**
- Nếu $ARGUMENTS là `tier/số` (vd "base/03", "doc/01", "dev/04"): tìm file match `guide/{tier}/{số}-*.md`
- Nếu $ARGUMENTS chỉ là số (vd "03"): tìm trong tất cả tiers `guide/base/03-*.md`, `guide/doc/03-*.md`, `guide/dev/03-*.md` — nếu nhiều match → hỏi user chọn
- Nếu $ARGUMENTS là full path: dùng trực tiếp
- Nếu không tìm thấy file → báo lỗi và dừng

**Bước 2 — Đọc file và chạy 5 checks:**

**Check 1: Heading hierarchy**
- H1 (`#`) chỉ xuất hiện 1 lần (title)
- Không skip level: H1→H2→H3 OK, H1→H3 FAIL, H2→H4 FAIL
- Report: dòng nào vi phạm

**Check 2: Cross-links**
- Tìm tất cả relative links dạng `[...](../path)` hoặc `[...](./path)`
- Kiểm tra file target có tồn tại không (dùng Glob)
- Kiểm tra anchor `#section` nếu có — heading target có tồn tại trong file đích không
- Report: link nào broken

**Check 3: Code blocks**
- Tìm tất cả code fences ` ``` `
- Kiểm tra có language tag không (` ```python `, ` ```yaml `...)
- Cho phép ngoại lệ: code block trong blockquote hoặc plaintext output
- Report: dòng nào thiếu language tag

**Check 4: Source markers**
- `[Nguồn: ...]` — kiểm tra format đúng (có nội dung bên trong, không rỗng)
- `[Cập nhật MM/YYYY]` — kiểm tra format tháng/năm hợp lệ
- `[Ứng dụng Kỹ thuật]` — kiểm tra đúng chính tả
- Report: marker nào sai format

**Check 5: Version reference**
- Module 00 (base/00-overview.md) phải có link đến VERSION file (`../../VERSION` hoặc `../VERSION` tùy depth)
- Các modules khác (01-07, doc/*, dev/*): KHÔNG bắt buộc version link — chỉ check không hardcode version number trong header
- Report: nếu hardcode version (vd "v8.0" trong header metadata)

**Bước 3 — Output:**

Nếu không có issue:
```
✅ {filename} — Passed all checks
```

Nếu có issues, format mỗi issue một dòng:
```
{filename} — {N} issues found

[Headings]  L42: H4 after H2 (skipped H3)
[Links]     L87: broken link → ../06-tools-features.md#nonexistent
[Code]      L123: code fence without language tag
[Markers]   L201: [Cập nhật 13/2025] — invalid month
[Version]   L3: hardcoded "v4.1" in header
```

Rules:
- KHÔNG sửa file — chỉ report
- KHÔNG đọc file khác ngoài module target và các link targets
- Output tối đa 20 dòng — nếu quá nhiều issues thì group theo check type và show count
