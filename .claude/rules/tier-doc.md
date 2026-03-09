---
paths:
  - "guide/doc/**/*.md"
---

# Doc Tier Writing Rules

## Audience
- Kỹ sư làm Technical Writing, Documentation, Cowork workflows
- Giả định đã đọc base/ — KHÔNG lặp lại kiến thức nền tảng

## Content scope
- Workflows, templates, recipes cho documentation tasks
- Cowork setup và workflows
- Custom Style configuration chi tiết
- KHÔNG chứa developer/coding content → cross-link sang dev/

## Format
- Recipes/workflows: numbered steps rõ ràng
- Templates: dùng code blocks với placeholder `{{variable}}`
- Prompt examples: XML format cho structured, `[]` cho markers

## Cross-links
- Luôn reference base/ cho kiến thức nền: `../base/03-prompt-engineering.md`
- Dùng relative paths
- KHÔNG duplicate content từ base/ — chỉ cross-link và build on top
