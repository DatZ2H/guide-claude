# Example: Guide Claude Project

**Nguồn:** Trích từ dự án Guide Claude v9.0 — bộ tài liệu 3-tier hướng dẫn sử dụng Claude AI.

**Đặc điểm dự án:**
- Documentation project (Obsidian Vault)
- 3-tier architecture: base/ + doc/ + dev/ + reference/
- Tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh
- Git-based workflow với PR

---

## Cấu trúc `.claude/` thực tế

```
.claude/
├── CLAUDE.md               # Project instructions (~90 dòng nội dung)
├── SETUP.md                # Onboarding guide
├── settings.json           # Hooks config (SessionStart, PostToolUse)
├── settings.local.json     # Local overrides (không commit)
├── rules/                  # 7 rule files — auto-load theo path
│   ├── writing-standards.md    → guide/**/*.md
│   ├── reference-standards.md  → guide/reference/**
│   ├── scaffold-standards.md   → _scaffold/**
│   ├── tier-base.md            → guide/base/**
│   ├── tier-doc.md             → guide/doc/**
│   ├── tier-dev.md             → guide/dev/**
│   └── planning-standards.md   → project-state.md
├── hooks/                  # 2 hook scripts
│   ├── format-check.py     # PostToolUse — heading hierarchy + code block tags
│   └── link-check.py       # Standalone — cross-link verification
├── commands/               # 5 slash commands
│   ├── start.md            # /start — session orientation
│   ├── checkpoint.md       # /checkpoint — quick commit
│   ├── validate-doc.md     # /validate-doc [module] — format check
│   ├── review-module.md    # /review-module [module] — deep review
│   └── weekly-review.md    # /weekly-review — weekly status
└── skills/                 # 9 on-demand skills
    ├── session-start/
    ├── version-bump/
    ├── cross-ref-checker/
    ├── module-review/
    ├── doc-standard-enforcer/
    ├── source-audit/
    ├── upgrade-guide/
    ├── nav-update/
    └── plan/
```

## Các files mẫu trong thư mục này

| File | Mô tả |
|------|--------|
| `CLAUDE.md` | Project instructions — phiên bản rút gọn (key patterns) |
| `settings.json` | Hooks configuration thực tế |
| `commands/start.md` | Session orientation command |
| `commands/checkpoint.md` | Quick commit workflow |

## Patterns đáng chú ý

### 1. CLAUDE.md giữ dưới 200 dòng
Toàn bộ context được load mỗi conversation. Giữ ngắn gọn, chi tiết chuyển vào rules/ và skills/.

### 2. Rules phân theo tier
Thay vì 1 file rules lớn, dự án dùng 7 rule files nhỏ — mỗi file chỉ load khi edit đúng path. Tiết kiệm context window.

### 3. Hooks enforce tự động
`format-check.py` chạy sau mỗi Edit/Write — bắt lỗi heading hierarchy và code block tags ngay lập tức, không cần nhớ kiểm tra thủ công.

### 4. Commands vs Skills
- **Commands** (`/start`, `/checkpoint`): workflow ngắn, chạy nhanh, hay dùng
- **Skills** (`session-start`, `source-audit`): workflow phức tạp hơn, có trigger conditions, auto-activate khi phù hợp

### 5. VERSION file là SSOT
Một file `VERSION` duy nhất — modules reference về đây thay vì hardcode version.

### 6. Discovery Protocol
CLAUDE.md = project manifest (Claude đọc đầu tiên). MEMORY.md = personal registry (auto-load, chứa links tới plans). Mọi thứ Claude cần biết phải có hoặc được link từ 1 trong 2 file này.

### 7. Planning workflow xuyên session
Plans lưu trong auto memory directory, link từ MEMORY.md. `/start` tự scan plan status. `/plan` skill quản lý tạo/xem/update plans.

---

> [!NOTE]
> Files trong thư mục này là **snapshot tại v9.0**. Để xem config mới nhất, đọc trực tiếp `.claude/` trong repo gốc.
