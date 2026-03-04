# Claude Code Setup & Reference cho Documentation

[Cập nhật 03/2026]

Cheat sheet cho Claude Code trong documentation workflow. Tổ chức theo workflow — tra cứu theo tình huống đang làm.

## 1. Quick Setup

Cài đặt và chạy session đầu tiên.

### Yêu cầu

| Yêu cầu | Chi tiết |
|----------|----------|
| OS | macOS, Linux, Windows (WSL2 hoặc native) |
| Node.js | v18 trở lên |
| Git | Khuyến nghị — nhiều tính năng cần git repo |

### Cài đặt

```bash
npm install -g @anthropic-ai/claude-code
claude --version          # verify
claude                    # lần đầu → mở browser để xác thực
/init                     # tạo CLAUDE.md starter
```

### Checklist sau cài đặt

```text
□ Tùy chỉnh CLAUDE.md cho project (xem template ở Section 5)
□ Tạo .claude/settings.json — cấu hình permissions
□ Tạo slash commands nếu cần (xem Section 5)
□ Test: chạy session, verify Claude đọc đúng CLAUDE.md
```

[Nguồn: Claude Code Docs — Installation]

## 2. Workflow hàng ngày

Quy trình làm việc mỗi ngày với documentation project.

### Bắt đầu session

```text
/start
```

Đọc version hiện tại, git status, 5 commits gần nhất. Chạy mỗi khi mở Claude Code.

### Edit module

```text
/checkpoint                    # backup trước khi edit
# ... edit content ...
/validate-doc <số_module>      # kiểm tra sau khi edit
```

Khi edit file trong `guide/`, skill `doc-standard-enforcer` tự kích hoạt — enforce heading hierarchy, language tags, cross-links.

### Quick commit

```text
/checkpoint
```

Commit nhanh các thay đổi hiện tại. Dùng trước và sau mỗi block công việc.

> [!TIP]
> Mặc định dùng Sonnet. Chuyển `/model opus` khi cần architectural decisions hoặc multi-file analysis, rồi `/model sonnet` khi xong.

## 3. Workflow review

Kiểm tra chất lượng module và tổng thể project.

### Review một module

```text
/review-module <số_module>
```

Deep review theo scoring rubric — heading hierarchy, code blocks, cross-links, source markers, nội dung. Output: điểm + danh sách issues.

### Validate nhanh

```text
/validate-doc <số_module>
```

Kiểm tra nhẹ hơn `/review-module` — chỉ check writing standards, không scoring.

### Review hàng tuần

```text
/weekly-review
```

Review tổng thể project: tiến độ, issues tích lũy, next actions. Chạy cuối tuần hoặc cuối sprint.

## 4. Workflow release

Quy trình bump version và release.

### Bump version

```text
/version-bump
```

Thực hiện tuần tự: cập nhật file `VERSION` (SSOT) → thêm changelog entry vào `00-overview.md` → update `project-state.md`. Luôn confirm version number trước khi chạy.

### Quy trình release đầy đủ

```text
1. /weekly-review              # review tổng thể trước release
2. /review-module <số>         # review từng module cần thiết
3. /version-bump               # bump version
4. /checkpoint                 # commit changes
5. Tạo PR → master             # merge khi ready
```

## 5. Cấu hình project

Reference cho các thành phần cấu hình. Đọc khi setup hoặc cần tra cứu.

### CLAUDE.md — Project Instructions

File tự động load vào context mỗi session. Khai báo conventions, rules, và project context.

**Vị trí và scope:**

| Vị trí | Scope | Shared |
|--------|-------|--------|
| `~/.claude/CLAUDE.md` | Mọi project | Không |
| `./CLAUDE.md` hoặc `./.claude/CLAUDE.md` | Project hiện tại | Có (commit vào git) |
| `./.claude/CLAUDE.local.md` | Cá nhân, project này | Không (gitignored) |
| Thư mục con chứa `CLAUDE.md` | Load khi làm việc trong thư mục đó | Có |

**Include vs Exclude:**

| Include (nên có) | Exclude (không nên có) |
|------------------|------------------------|
| Bash commands Claude không đoán được | Thứ Claude đã biết từ code |
| Writing/coding style khác default | Conventions chuẩn của ngôn ngữ |
| Test/build commands cụ thể | API documentation chi tiết (link thay thế) |
| Branch naming, commit conventions | Thông tin thay đổi thường xuyên |
| Project-specific decisions | Giải thích dài / tutorials |
| Gotchas, non-obvious behaviors | Mô tả từng file trong codebase |

[Nguồn: Claude Code Docs — Best Practices]

> [!TIP]
> Giữ CLAUDE.md dưới 200 dòng. Nếu dài hơn → chuyển reference content sang Skills.

**Template cho Documentation Project:**

```markdown
# CLAUDE.md — {{project_name}}

## Project context
{{mô tả project, đối tượng, phase hiện tại}}

## Folder structure
{{liệt kê cấu trúc chính}}

## Language rules
- Ngôn ngữ chính: {{ngôn ngữ}}
- Thuật ngữ kỹ thuật: giữ tiếng Anh
- Placeholders: {{variable}}

## Writing standards
- Heading hierarchy: # title → ## section → ### subsection — KHÔNG skip level
- Code blocks luôn có language tag
- Cross-links dùng relative paths

## Rules — PHẢI tuân thủ
1. Backup trước khi sửa file content
2. Commit message {{ngôn ngữ}}, ngắn gọn
3. KHÔNG tự ý xóa file mà không hỏi
```

### Slash Commands vs Skills

| | Slash Commands | Skills |
|--|----------------|--------|
| Vị trí | `.claude/commands/` | `.claude/skills/` |
| Kích hoạt | Gọi thủ công: `/tên` | Tự động khi context khớp |
| Tạo mới | Thêm file `.md`, dùng `$ARGUMENTS` cho tham số | Thêm thư mục chứa instruction file |

**Commands trong project này:**

```text
.claude/commands/
├── start.md            # /start
├── checkpoint.md       # /checkpoint
├── validate-doc.md     # /validate-doc <số>
├── review-module.md    # /review-module <số>
└── weekly-review.md    # /weekly-review
```

**Skills trong project này:**

```text
.claude/skills/
├── session-start/          # Trigger: bắt đầu session
├── version-bump/           # Trigger: "bump version", "lên version"
├── doc-standard-enforcer/  # Trigger: edit file trong guide/
├── cross-ref-checker/      # Trigger: kiểm tra cross-references
└── module-review/          # Trigger: deep review module
```

Danh sách đầy đủ skills (official, community, internal): xem [skills-list.md](skills-list.md).

Chi tiết kiến trúc 6 lớp cấu hình: xem [config-architecture.md](config-architecture.md).

## 6. Quick Reference

### Tình huống → Lệnh

| Đang cần... | Chạy |
|--------------|------|
| Bắt đầu session | `/start` |
| Backup trước khi edit | `/checkpoint` |
| Kiểm tra module sau edit | `/validate-doc <số>` |
| Review sâu một module | `/review-module <số>` |
| Review tổng thể project | `/weekly-review` |
| Release version mới | `/version-bump` |
| Tác vụ phức tạp | `/model opus` → làm → `/model sonnet` |

### Liên kết

| Tài liệu | Đường dẫn |
|-----------|-----------|
| Kiến trúc cấu hình (6 lớp) | [config-architecture.md](config-architecture.md) |
| Danh sách skills & plugins | [skills-list.md](skills-list.md) |
| Claude Code Docs (official) | https://docs.anthropic.com/en/docs/claude-code/ |
| Claude Code Best Practices | https://docs.anthropic.com/en/docs/claude-code/best-practices |
