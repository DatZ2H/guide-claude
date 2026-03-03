# Scaffold — Tạo project Cowork mới

Bộ template này giúp khởi tạo nhanh một Cowork project theo 3-tier architecture chuẩn:
- **Tầng A** — Content (thư mục chính chứa nội dung)
- **Tầng B** — Infrastructure (`.claude/` — Folder Instructions + skills)
- **Tầng C** — Persistence (`_memory/` — session state + decisions log)

## Cách dùng

### Bước 1: Copy scaffold vào project mới
```
cp -r _scaffold/ /path/to/new-project/
```

### Bước 2: Rename và restructure
```
mv README-scaffold.md README.md
mkdir -p .claude/skills _memory
mv CLAUDE-template.md .claude/CLAUDE.md
mv project-state-template.md project-state.md
mv memory-starter/session-state.md _memory/session-state.md
mv memory-starter/decisions-log.md _memory/decisions-log.md
```

> **Lưu ý về skills:** KHÔNG copy `skill-templates/` vào project. Thư mục này là nguồn tham khảo —
> khi cần tạo skill mới, copy `skill-templates/SKILL-template/` vào `.claude/skills/your-skill-name/`
> rồi rename và customize. Xem hướng dẫn tạo skill tại Module 10, mục 10.6.7.

### Bước 3: Customize từng file
1. `.claude/CLAUDE.md` — thay toàn bộ `{{placeholder}}` bằng thông tin project thật
2. `project-state.md` — điền phase, structure, decisions ban đầu
3. `_memory/session-state.md` — điền date khởi tạo
4. `_memory/decisions-log.md` — điền decision đầu tiên (vì sao dùng kiến trúc này)
5. `VERSION` — giữ `1.0` hoặc chỉnh theo quy ước project

### Bước 4: Tạo content folder
Tạo thư mục chứa nội dung chính (ví dụ: `docs/`, `guide/`, `content/`) và bắt đầu làm việc.

## Checklist sau khi setup

- [ ] `.claude/CLAUDE.md` đã customize — không còn `{{placeholder}}` nào
- [ ] `_memory/session-state.md` có date và summary khởi tạo
- [ ] `_memory/decisions-log.md` có ít nhất 1 decision đầu tiên
- [ ] `VERSION` đúng (thường bắt đầu từ `1.0`)
- [ ] `project-state.md` có phase + folder structure thật của project
- [ ] Test: mở Cowork, Claude đọc Folder Instructions đúng (không báo lỗi file không tìm thấy)
- [ ] (Tùy chọn) Thêm skill files vào `.claude/skills/` nếu project cần on-demand workflows

## Cấu trúc scaffold này tạo ra

```
your-project/
├── README.md                    ← (file này, sau khi rename)
├── VERSION                      Single source of truth cho version
├── project-state.md             Context transfer document
│
├── your-content/                Tầng A — tạo thủ công
│
├── .claude/                     Tầng B — Infrastructure
│   ├── CLAUDE.md                Folder Instructions (từ CLAUDE-template.md)
│   └── skills/                  On-demand skill files
│       └── my-skill/            ← mỗi skill là một folder
│           └── SKILL.md         ← từ skill-templates/SKILL-template/SKILL-template.md
│
└── _memory/                     Tầng C — Persistence
    ├── session-state.md         Active tasks + last session
    └── decisions-log.md         Audit trail quyết định
```

## Thư mục tham khảo trong scaffold (KHÔNG copy vào project)

Các thư mục dưới đây là **nguồn templates** — xem và copy nội dung khi cần, không copy nguyên folder:

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
└── global-instructions/         Template cho Global CLAUDE.md (Cowork, user-level)
    └── global-CLAUDE-phenikaa-x.md
```

**Cách dùng project-instructions:** Khi tạo claude.ai Project mới → mở file template phù hợp → copy phần giữa `---COPY START---` và `---COPY END---` → paste vào Project Settings > Instructions.

**Cách dùng global-instructions:** Copy `global-CLAUDE-phenikaa-x.md` → customize `{{placeholder}}` → lưu tại `~/.claude/CLAUDE.md` trên máy của bạn.

## Lưu ý

- **Memory protocol:** Đầu mỗi Cowork session → Claude đọc `_memory/` trước khi làm việc. Ghi rõ trong `.claude/CLAUDE.md`.
- **Backup rule:** Không sửa file quan trọng mà không tạo `.bak` trước.
- **VERSION:** Mỗi milestone lớn → bump version trong file `VERSION`. Module headers tham chiếu về đây thay vì hardcode.
- **project-state.md:** Đây là briefing document — update trên Cowork, paste vào Project Chat khi cần brainstorm/planning với context đầy đủ.
