# Folder Instructions — Claude Guide Project

## Project overview
Đây là dự án "Claude Guide cho Kỹ sư Phenikaa-X" — bộ tài liệu 11 modules hướng dẫn sử dụng Claude AI.

## Folder structure
- guide/ — 11 module files (00-overview đến 10-claude-desktop-cowork) + reference/
- guide/reference/ — config-architecture.md, skills-list.md
- .claude/ — CLAUDE.md (Folder Instructions), SETUP.md (project manifest), skills/
- .claude/skills/ — 4 project-level skills: session-start, cross-ref-checker, module-review, version-bump
- _scaffold/ — starter templates (project-instructions/, global-instructions/, skill-templates/, memory-starter/)
- _memory/ — session-state.md + decisions-log.md
- project-state.md — context transfer document (briefing cho Project Chat khi cần)
- VERSION — single source of truth cho version number

## Conventions
- Language: Tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh
- Source markers: [Nguồn: ...] cho official, [Ứng dụng Kỹ thuật] cho applied examples
- File naming: lowercase, dấu gạch ngang, có số thứ tự module (01-, 02-...)

## Memory protocol
- Đầu session: đọc _memory/session-state.md và _memory/decisions-log.md
- Khi quyết định quan trọng: append vào _memory/decisions-log.md
- Cuối session: update _memory/session-state.md

## Rules
- KHÔNG sửa file trong guide/ mà không tạo backup (.bak) trước
- Khi edit module: đọc VERSION để biết version hiện tại
- Khi bump version: sửa VERSION trước — module headers tự reflect qua link `[VERSION](../VERSION)`, không cần sửa thủ công
