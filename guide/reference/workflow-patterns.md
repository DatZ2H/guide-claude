# Workflow Patterns — Reference

**Cập nhật:** 2026-03-07

Tài liệu tham khảo cho các workflow patterns dùng với Claude: external memory, project scaffolding, và context transfer.

[Nguồn: Claude Code Docs — Memory] [Cập nhật 03/2026]

---

## External Memory — Pattern `_memory/` folder

> **DEPRECATED (03/2026):** Pattern `_memory/` folder đã deprecated. Git history thay thế hoàn toàn — ít overhead, không cần maintain thêm files. Dùng `.claude/CLAUDE.md` + `git log` + SessionStart hook thay thế.

Nội dung bên dưới giữ lại làm tham khảo cho ai đã dùng pattern này.

<details>
<summary>Chi tiết _memory/ pattern (deprecated)</summary>

Cowork không có memory giữa tasks. Pattern `_memory/` folder biến file system thành bộ nhớ có cấu trúc.

**Cấu trúc:**

```text
project-folder/
├── _memory/
│   ├── session-state.md     ← Trạng thái session hiện tại
│   └── decisions-log.md     ← Quyết định + lý do (tích lũy)
├── (project files)
└── ...
```

**Thay thế hiện tại:**

| Cũ (`_memory/`) | Mới (Git-based) |
|-----------------|-----------------|
| `session-state.md` | `git log --oneline -10` + SessionStart hook |
| `decisions-log.md` | Commit messages có rationale + CLAUDE.md |

</details>

**Xem thêm:** [Context Management, mục 4.7](../base/04-context-management.md#47-context-engineering-quản-lý-context-có-chiến-lược) — External Memory trong context engineering.

---

## `_scaffold/` — Starter Template cho Project Mới

Thay vì thiết lập `project-state.md`, `.claude/CLAUDE.md`, và `VERSION` từ đầu cho mỗi dự án mới, **Guide Claude project cung cấp `_scaffold/`** — bộ template đã được chuẩn hóa theo 3-tier architecture (base/doc/dev).

**Cấu trúc `_scaffold/`:**

```text
_scaffold/
├── README-scaffold.md           Hướng dẫn setup từng bước
├── CLAUDE-template.md           Template cho .claude/CLAUDE.md
├── project-state-template.md    Template cho project-state.md
├── VERSION                      Giá trị khởi đầu "1.0"
│
├── skill-templates/             Template tạo skill mới (tham khảo — KHÔNG copy)
│   └── SKILL-template/          ← mỗi skill là folder
│       └── SKILL-template.md    Mẫu SKILL.md đầy đủ
│
├── project-instructions/        Templates cho claude.ai Project Instructions (tham khảo)
│   ├── README.md
│   ├── template-basic.md
│   ├── template-troubleshooting.md
│   ├── template-tech-doc.md
│   └── template-code-review.md
│
└── global-instructions/         Template cho Global CLAUDE.md (tham khảo)
    └── global-CLAUDE-phenikaa-x.md
```

**Cách dùng:** Copy `_scaffold/` vào thư mục dự án mới, rename và customize theo README-scaffold.md. Toàn bộ setup hoàn tất trong 5-10 phút.

> Xem `_scaffold/README-scaffold.md` để biết checklist đầy đủ và phân biệt folder nào copy vào project, folder nào chỉ để tham khảo.
