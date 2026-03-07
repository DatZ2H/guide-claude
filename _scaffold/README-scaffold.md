# Scaffold — Tạo project mới với Claude Code / Cowork

Bộ template này giúp khởi tạo nhanh một project theo 2-tier architecture chuẩn:
- **Tầng A** — Content (thư mục chính chứa nội dung)
- **Tầng B** — Infrastructure (`.claude/` — Folder Instructions + skills + commands)

Hoạt động với cả **Claude Code** (CLI) và **Cowork** (Desktop).

> [!TIP]
> Mới bắt đầu? Xem [checklists/new-project-checklist.md](checklists/new-project-checklist.md) để setup từng bước.
> Cần ví dụ thực tế? Xem [examples/](examples/) — có config từ dự án Guide Claude và một dev project mẫu.

## Cách dùng

### Bước 1: Copy scaffold vào project mới
```bash
cp -r _scaffold/ /path/to/new-project/
```

### Bước 2: Rename và restructure
```bash
mv README-scaffold.md README.md
mkdir -p .claude/skills .claude/commands
mv CLAUDE-template.md .claude/CLAUDE.md
mv project-state-template.md project-state.md
```

> **Lưu ý về skills:** KHÔNG copy `skill-templates/` vào project. Thư mục này là nguồn tham khảo —
> khi cần tạo skill mới, copy `skill-templates/SKILL-template/` vào `.claude/skills/your-skill-name/`
> rồi rename thành `SKILL.md` và customize. Xem hướng dẫn tại Module 10, mục 10.6.7.

### Bước 3: Customize từng file
1. `.claude/CLAUDE.md` — thay toàn bộ `{{placeholder}}` bằng thông tin project thật
2. `project-state.md` — điền phase, structure, decisions ban đầu
3. `VERSION` — giữ `1.0` hoặc chỉnh theo quy ước project

### Bước 4: Tạo infrastructure bổ sung (khuyến nghị)
```bash
# SETUP.md — onboarding cho maintainer mới
touch .claude/SETUP.md

# settings.json — hooks và permissions
echo '{}' > .claude/settings.json

# Commands cơ bản
touch .claude/commands/start.md
touch .claude/commands/checkpoint.md
```

### Bước 5: Tạo content folder
Tạo thư mục chứa nội dung chính (ví dụ: `docs/`, `guide/`, `content/`) và bắt đầu làm việc.

## Checklist sau khi setup

- [ ] `.claude/CLAUDE.md` đã customize — không còn `{{placeholder}}` nào
- [ ] `VERSION` đúng (thường bắt đầu từ `1.0`)
- [ ] `project-state.md` có phase + folder structure thật của project
- [ ] `.claude/commands/` có ít nhất `start.md` và `checkpoint.md`
- [ ] Test: mở Claude Code hoặc Cowork → Claude đọc Folder Instructions đúng
- [ ] (Tùy chọn) Thêm skill files vào `.claude/skills/` nếu project cần on-demand workflows

## Cấu trúc scaffold này tạo ra

```
your-project/
├── README.md                    ← (file này, sau khi rename)
├── VERSION                      SSOT cho version number
├── project-state.md             Project overview
│
├── your-content/                Tầng A — tạo thủ công
│
└── .claude/                     Tầng B — Infrastructure
    ├── CLAUDE.md                Folder Instructions (từ CLAUDE-template.md)
    ├── SETUP.md                 Onboarding guide
    ├── settings.json            Hooks, permissions
    ├── commands/                Slash commands
    │   ├── start.md             Session orientation
    │   └── checkpoint.md        Quick commit
    └── skills/                  On-demand skill files
        └── my-skill/            ← mỗi skill là một folder
            └── SKILL.md         ← từ skill-templates/SKILL-template/
```

## Thư mục tham khảo trong scaffold (KHÔNG copy vào project)

Các thư mục dưới đây là **nguồn templates và tham khảo** — xem và copy nội dung khi cần, không copy nguyên folder:

```
_scaffold/
│
├── project-instructions/        Templates cho claude.ai Project Instructions
│   ├── README.md                Hướng dẫn chọn template
│   ├── template-basic.md        Template cơ bản
│   ├── template-troubleshooting.md
│   ├── template-tech-doc.md
│   └── template-code-review.md
│
├── global-instructions/         Template cho Global CLAUDE.md (user-level)
│   └── global-CLAUDE-phenikaa-x.md
│
├── skill-templates/             Template tạo skill mới
│   └── SKILL-template/
│       └── SKILL-template.md
│
├── examples/                    Config thực tế đã hoạt động
│   ├── guide-claude/            Dự án Guide Claude (doc project, 3-tier)
│   │   ├── README.md            Overview + patterns đáng chú ý
│   │   ├── CLAUDE.md            Project instructions thực tế
│   │   ├── settings.json        Hooks config (SessionStart + PostToolUse)
│   │   └── commands/            start.md, checkpoint.md
│   └── dev-example/             Dev project mẫu (Python FastAPI)
│       ├── README.md            Overview + cách mở rộng
│       ├── CLAUDE.md            Minimal project instructions
│       ├── settings.json        SessionStart hook
│       └── commands/            start.md, checkpoint.md
│
└── checklists/                  Quy trình làm việc
    ├── new-project-checklist.md Step-by-step setup từ zero
    └── daily-workflow.md        Session start → work → checkpoint → handover
```

**Cách dùng project-instructions:** Khi tạo claude.ai Project mới → mở file template phù hợp → copy phần giữa `---COPY START---` và `---COPY END---` → paste vào Project Settings > Instructions.

**Cách dùng global-instructions:** Copy `global-CLAUDE-phenikaa-x.md` → customize `{{placeholder}}` → lưu tại `~/.claude/CLAUDE.md` trên máy.

**Cách dùng examples:** Đọc README trong mỗi example → xem patterns → copy files cần thiết vào project mới → customize.

**Cách dùng checklists:** Mở checklist phù hợp → follow từng bước → tick off khi xong.

## Lưu ý

- **Git-first backup:** Dùng `/checkpoint` hoặc `git commit` trước khi edit lớn. Không tạo file `.bak`.
- **VERSION:** Mỗi milestone lớn → bump version trong file `VERSION`. Module headers tham chiếu về đây thay vì hardcode.
- **project-state.md:** Đây là project overview — update sau milestone lớn (version bump, structural changes).
