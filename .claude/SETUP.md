# Project Setup — Guide Claude

Tài liệu này dành cho **maintainer mới** hoặc khi setup lại môi trường làm việc.
Đây là danh sách những gì project này cần để hoạt động đúng.

---

## Skills đang dùng (Project-level)

8 skills trong `.claude/skills/` — active khi làm việc trong folder này:

| Skill | Trigger phrase | Mục đích |
|-------|----------------|---------|
| `session-start` | "bắt đầu", "tiếp tục", "còn lại gì" | Đọc git history, orientation 5 dòng, gợi ý next action |
| `version-bump` | "bump version", "release vX.X" | Cập nhật VERSION → changelog → project-state đúng thứ tự |
| `cross-ref-checker` | "kiểm tra cross-references" | Tìm stale file paths, broken cross-links trong guide/ |
| `module-review` | "review module X", "đánh giá chất lượng" | Checklist 5 tiêu chí: accuracy, consistency, completeness, clarity, actionability |
| `doc-standard-enforcer` | "review format", "kiểm tra standards" | Manual deep review content — 6 checks chất lượng |
| `source-audit` | "source audit", "kiểm tra sources" | Scan source markers theo 3-tier standard |
| `upgrade-guide` | "health check", "scan project" | Scan stale data, broken refs, dependency issues |
| `nav-update` | "update nav", "fix navigation" | Auto-update prev/next navigation links |

Skills nằm trong `.claude/skills/[tên-skill]/SKILL.md` — xem từng file để biết chi tiết workflow.

---

## Commands đang dùng (Project-level)

5 commands trong `.claude/commands/` — gọi bằng slash command:

| Command | Trigger | Mục đích |
|---------|---------|---------|
| `/start` | Đầu mỗi session | Orientation: version, branch, git status, last commit |
| `/checkpoint` | Sau khi hoàn thành task | Quick commit với staged files, format message tự động |
| `/validate-doc` | `/validate-doc 03` | Validate 1 module: code block tags, heading hierarchy, VERSION link |
| `/review-module` | `/review-module 06` | Deep review module: accuracy, consistency, completeness, clarity |
| `/weekly-review` | Đầu tuần | 5-bước review: git log, module health, issues, priorities, checkpoint |

Commands nằm trong `.claude/commands/[tên].md` — xem từng file để biết chi tiết workflow.

---

## Global Instructions cần có

**File:** `~/.claude/CLAUDE.md` (user-level, không nằm trong project folder)

Project này được develop với Global Instructions sau. Nếu maintainer mới setup máy:

1. Copy template từ `_scaffold/global-instructions/global-CLAUDE-phenikaa-x.md`
2. Thay `{{placeholder}}` bằng thông tin của bạn
3. Lưu tại `~/.claude/CLAUDE.md`

Không có Global Instructions vẫn hoạt động được, nhưng Claude sẽ mất các rules về language, file operations, và response behavior.

---

## Plugins cần cài

**Hiện tại:** Không cần plugin đặc biệt cho project này.

Pre-built skills (docx, xlsx, pptx, pdf) đã có sẵn — không cần cài thêm.

Nếu muốn nâng cao workflow, xem `guide/reference/skills-list.md` để chọn.

---

## Folder Instructions

**File:** `.claude/CLAUDE.md` (file này đã có trong repo)

Đọc file này để biết project structure, conventions, memory protocol, và rules.
Claude đọc file này tự động khi bắt đầu Cowork session trong folder này.

---

## Checklist cho maintainer mới

- [ ] Đọc `project-state.md` để nắm trạng thái dự án
- [ ] Đọc `git log --oneline -20` để xem recent changes
- [ ] Setup Global CLAUDE.md nếu chưa có (xem mục Global Instructions trên)
- [ ] Test skill `session-start`: gõ "bắt đầu" → Claude phải báo orientation
- [ ] Đọc `VERSION` để biết version hiện tại

---

## Liên kết nhanh

- Project overview: `project-state.md`
- Module listing + learning paths: `guide/base/00-overview.md`
- Cấu hình architecture: `guide/reference/config-architecture.md`
- Danh sách skills hệ thống: `guide/reference/skills-list.md`
- Templates: `_scaffold/`
