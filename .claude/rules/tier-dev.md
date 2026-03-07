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

## Cross-links
- Reference base/ cho concepts: `../base/04-context-management.md`
- Dùng relative paths
- KHÔNG duplicate content từ base/ — chỉ cross-link và extend
