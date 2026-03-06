---
paths:
  - "_scaffold/**"
---

# Scaffold Standards — Guide Claude Project

Rules cho files trong _scaffold/ — starter templates cho dự án mới.

## Template Rules

- Templates phải generic — KHÔNG chứa Phenikaa-X specific content
- Dùng `{{placeholder}}` cho mọi giá trị cần customize
- Comments giải thích mục đích từng section: `<!-- Giải thích: ... -->`
- Mỗi template file có header comment block ghi rõ: purpose, khi nào dùng, cách customize

## Quality Gate

- Template chỉ ship nếu đã verified qua Base Toolkit trust criteria
- Hooks/skills trong template phải thuộc trust level "Anthropic Official" hoặc "Custom (verified)"
- KHÔNG include community tools chưa qua verification

## Tier Organization

- `templates/base/` — components dùng cho MỌI dự án (start, checkpoint, session-start, SessionStart hook)
- `templates/doc-project/` — thêm doc-specific tools (validate-doc, doc-standard, format-check hook)
- `templates/dev-project/` — thêm dev-specific tools (code-review, simplify)
- Mỗi tier kế thừa từ base — KHÔNG duplicate base components

## Examples

- `examples/` chứa config thực tế đã hoạt động — KHÔNG phải template
- Ghi rõ nguồn gốc: "Trích từ dự án Guide Claude v[X]" hoặc tương tự
- Examples phải reflect cấu trúc hiện tại của dự án nguồn
