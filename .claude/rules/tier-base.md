---
paths:
  - "guide/base/**/*.md"
---

# Base Tier Writing Rules

## Audience
- Tất cả kỹ sư Phenikaa-X — không giả định kinh nghiệm AI trước đó
- Ngôn ngữ đơn giản, tránh jargon không cần thiết

## Content scope
- Kiến thức nền tảng — ai cũng cần biết
- KHÔNG chứa content chỉ dành cho Doc hoặc Dev audience
- Nếu content chỉ relevant cho 1 audience → cross-link sang doc/ hoặc dev/

## Format
- Examples phải universal (không doc-specific, không dev-specific)
- Khi có ví dụ audience-specific → dùng callout `> [!TIP] Xem thêm: [doc/XX](...)` hoặc `[dev/XX](...)`
- Code blocks: luôn có language tag

## Cross-links
- Link sang doc/ hoặc dev/ khi mention nội dung chuyên sâu
- Dùng relative paths: `../doc/01-doc-workflows.md`
- KHÔNG duplicate content từ doc/ hoặc dev/ — chỉ cross-link
