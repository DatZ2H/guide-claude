# New Project Checklist

Step-by-step từ zero đến working `.claude/` infrastructure.

---

## Phase 1: Khởi tạo (5-10 phút)

### 1.1 Tạo project folder và git

- [ ] Tạo folder project
- [ ] `git init` + commit đầu tiên
- [ ] Tạo `VERSION` file (bắt đầu từ `1.0`)

### 1.2 Tạo `.claude/CLAUDE.md`

- [ ] Copy `CLAUDE-template.md` từ `_scaffold/` → `.claude/CLAUDE.md`
- [ ] Điền tất cả `{{placeholder}}`:
  - `{{project_name}}` — tên project
  - `{{project_description}}` — 1-2 câu mô tả
  - `{{target_audience}}` — ai dùng output
  - `{{architecture_tier}}` — "2-tier" (default) hoặc "3-tier" (nhiều audience)
  - `{{content_folder}}` — folder content chính (docs/, guide/, src/...)
  - `{{language_main}}` — ngôn ngữ chính
  - `{{main_branch}}` — master hoặc main
- [ ] Xóa section comment hướng dẫn customize ở cuối file
- [ ] Verify: không còn `{{placeholder}}` nào

### 1.3 Tạo commands cơ bản

- [ ] Tạo `.claude/commands/start.md` — copy từ `examples/dev-example/commands/start.md`
- [ ] Tạo `.claude/commands/checkpoint.md` — copy từ `examples/dev-example/commands/checkpoint.md`
- [ ] Customize commit message format nếu cần (English vs tiếng Việt)

### 1.4 Tạo `settings.json` với SessionStart hook

- [ ] Tạo `.claude/settings.json`:
```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "v=$(cat VERSION 2>/dev/null || echo '?'); n=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' '); echo \"Project v${v}. ${n} files modified since last commit.\""
          }
        ]
      }
    ]
  }
}
```

---

## Phase 2: Verify (2-3 phút)

- [ ] Mở Claude Code trong project folder
- [ ] Verify SessionStart hook hiển thị version + file count
- [ ] Chạy `/start` — verify output đúng format
- [ ] Test `/checkpoint` — verify đề xuất commit message

---

## Phase 3: Mở rộng (khi cần)

### Hooks (khuyến nghị khi team > 1 người)

- [ ] Thêm PostToolUse hook cho format checking:
  ```json
  {
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{
        "type": "command",
        "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/your-lint-script.py\"",
        "timeout": 10,
        "statusMessage": "Checking format..."
      }]
    }]
  }
  ```
- [ ] Thêm PreToolUse hook cho safety gates (tùy chọn):
  ```json
  {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "echo 'review command before execution'",
        "timeout": 5
      }]
    }]
  }
  ```

> [!TIP]
> Trước khi build hook/rule mới, kiểm tra `_scaffold/` và `.claude/` xem đã có pattern tương tự chưa.

### Rules (khi có standards cho folder cụ thể)

- [ ] Tạo `.claude/rules/` folder
- [ ] Thêm rule files theo path patterns (xem `_scaffold/skill-templates/rule-template.md`):
  ```
  rules/
  └── writing-standards.md    → docs/**/*.md
  ```
- [ ] Nội dung rule: heading hierarchy, code block tags, naming conventions

### Skills (khi có workflow lặp lại)

- [ ] Tạo `.claude/skills/your-skill/SKILL.md`
- [ ] Copy structure từ `_scaffold/skill-templates/SKILL-template/`
- [ ] Thêm vào bảng Available skills trong CLAUDE.md
- [ ] Khi thêm rules/hooks/skills → quay lại CLAUDE.md điền `{{rules_description}}`, `{{hooks_description}}`, `{{skills_count}}`

### Planning workflow (cho projects có multi-phase work)

- [ ] Tạo auto memory directory (Claude tự tạo khi dùng MEMORY.md)
- [ ] Tạo plan file trong memory: `{memory-dir}/{plan-name}.md`
- [ ] Cập nhật MEMORY.md với link tới plan file
- [ ] (Tùy chọn) Tạo `/plan` skill — xem `_scaffold/skill-templates/` cho template

### project-state.md (cho projects có phases)

- [ ] Copy `project-state-template.md` từ `_scaffold/`
- [ ] Điền project overview, phase, decisions

---

## Quick verification checklist

Sau khi setup xong, verify tất cả:

- [ ] `claude` command chạy được trong project folder
- [ ] SessionStart hook hiển thị thông tin
- [ ] `/start` output đúng format
- [ ] `/checkpoint` đề xuất commit message
- [ ] CLAUDE.md không còn `{{placeholder}}`
- [ ] `.gitignore` có `.claude/settings.local.json` (nếu dùng local settings)
