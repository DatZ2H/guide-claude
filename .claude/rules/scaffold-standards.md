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

## Folder Organization

- `project-instructions/` — templates cho claude.ai Project Instructions (4 loại: basic, code-review, tech-doc, troubleshooting)
- `global-instructions/` — template Global CLAUDE.md
- `skill-templates/` — template tạo skill mới (folder structure + SKILL.md)
- `examples/` — config thực tế đã hoạt động (guide-claude, dev-example) — KHÔNG phải template
- `checklists/` — workflow checklists (new-project, daily-workflow)

## Examples

- `examples/` chứa config thực tế đã hoạt động — KHÔNG phải template
- Ghi rõ nguồn gốc: "Trích từ dự án Guide Claude v[X]" hoặc tương tự
- Examples phải reflect cấu trúc hiện tại của dự án nguồn
