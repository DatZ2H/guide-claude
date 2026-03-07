---
description: Rules for dev tier content (guide/dev/**)
globs: guide/dev/**/*.md
---

# Dev Tier Writing Rules

## Audience
- Developer, DevOps, kỹ sư automation — quen CLI và code
- Giả định đã đọc base/ — KHÔNG lặp lại kiến thức nền tảng

## Content scope
- Claude Code CLI: setup, commands, configuration
- VS Code extension integration
- Agents, automation, CI/CD pipelines
- Plugins ecosystem
- Dev workflows (git, testing, code review)
- KHÔNG chứa documentation/Cowork content → cross-link sang doc/

## Format
- CLI commands: code blocks với `bash` language tag
- Config files: code blocks với `json` hoặc `yaml` tag
- Workflow steps: numbered, có command examples
- Feature verification: luôn note source (`[Nguồn: Claude Code Docs]`)

## Source verification
- Features phải verify tại code.claude.com/docs trước khi viết
- Claude Code thay đổi nhanh — luôn kèm `[Cập nhật MM/YYYY]`

## Module structure template

Mỗi dev/ module PHẢI theo structure sau:

```markdown
# [Title]

**Thời gian đọc:** X phút | **Mức độ:** Intermediate-Advanced
**Cập nhật:** YYYY-MM-DD | Models: xem [specs](../reference/model-specs.md)

---
depends-on: [base/XX-name, ...]
impacts: [...]
---

[1-2 câu intro — module này viết gì, ai cần đọc]

[Nguồn: Claude Code Docs] [Cập nhật MM/YYYY]

---

## [Section headings — content]

---

← [Prev](prev-file.md) | [Tổng quan](../base/00-overview.md) | [Next →](next-file.md)
```

Rules:
- Header metadata: giữ format giống base/ modules (thời gian đọc, mức độ, cập nhật, models)
- `depends-on` / `impacts`: bắt buộc — dùng 3-tier paths (base/XX, doc/XX, dev/XX, reference/XX)
- Navigation links: giữ nguyên từ placeholder — chỉ update nếu sai
- Target length: 200-500 dòng per module (nếu dài hơn → split sections hoặc cross-link)

## Cross-links
- Reference base/ cho concepts: `../base/04-context-management.md`
- Dùng relative paths
- KHÔNG duplicate content từ base/ — chỉ cross-link và extend
