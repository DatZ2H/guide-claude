# Rule Template — Tạo rule file mới

## Khi nào tạo rule?

**Rule** = instructions auto-load khi Claude đọc/edit file matching path pattern.

| Dùng Rule khi | Dùng CLAUDE.md khi | Dùng Skill khi |
|---|---|---|
| Standards áp dụng cho folder/file cụ thể | Rules áp dụng toàn project | Workflow phức tạp, nhiều bước |
| Giảm context window (chỉ load khi cần) | Luôn cần load | Cần user trigger hoặc auto-detect |
| Ví dụ: writing style cho docs/ | Ví dụ: git workflow, version rules | Ví dụ: version-bump, module-review |

## Template

Tạo file `.claude/rules/{{rule_name}}.md` với nội dung:

```markdown
---
paths:
  - {{path_pattern_1}}
  - {{path_pattern_2}}
---

# {{Rule Title}}

{{Mô tả ngắn rule này enforce gì.}}

## {{Category 1}}

- Rule 1
- Rule 2

## {{Category 2}}

- Rule 3
- Rule 4
```

## Frontmatter spec

```yaml
---
paths:
  - docs/**/*.md        # Glob pattern — match files trong docs/
  - src/api/**          # Match mọi file trong src/api/
---
```

- **`paths`** là field duy nhất trong rule frontmatter
- Dùng glob patterns (giống `.gitignore`)
- Rule trigger khi Claude **đọc** file matching pattern (Read tool)
- Nhiều paths = OR logic (match bất kỳ pattern nào)

## Gotchas

- Rule chỉ trigger on **Read**, không trigger on Write/Edit
- Nếu `paths` sai format → rule **silent fail** (không load, không báo lỗi)
- Dùng unquoted paths hoặc standard YAML array — tránh complex quoting
- Không có `allowed-tools`, `description`, hay `!command` trong rule frontmatter (khác với skill)
- File rule PHẢI ở `.claude/rules/` — không nested thêm subfolder

## Ví dụ thực tế

### Rule cho documentation folder

```markdown
---
paths:
  - docs/**/*.md
---

# Documentation Standards

## Heading

- Heading hierarchy: # → ## → ### — KHÔNG skip level
- Mỗi file bắt đầu bằng # title duy nhất

## Code blocks

- Luôn kèm language tag
- Inline code cho tên hàm, biến, file paths
```

### Rule cho scaffold/template folder

```markdown
---
paths:
  - _scaffold/**
---

# Scaffold Standards

- Templates phải generic — KHÔNG chứa project-specific content
- Dùng `{{placeholder}}` cho mọi giá trị cần customize
- Examples phải reflect cấu trúc hiện tại của project nguồn
```

## Checklist sau khi tạo rule

- [ ] File đặt trong `.claude/rules/`
- [ ] Frontmatter `paths:` đúng glob pattern
- [ ] Test: mở file matching pattern → verify Claude mention rule content
- [ ] Update CLAUDE.md nếu cần (Automation infrastructure section)
