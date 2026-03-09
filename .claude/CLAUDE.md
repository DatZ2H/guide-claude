# CLAUDE.md — Guide Claude Project

## Project context
Dự án "Claude Guide cho Kỹ sư Phenikaa-X" — bộ tài liệu 3-tier hướng dẫn sử dụng Claude AI.
- **Version:** xem file `VERSION` (SSOT)
- **Phase:** v9.0 stable — infrastructure hardening
- **Đối tượng:** Kỹ sư tự động hóa, R&D, Robotics tại Phenikaa-X
- **Architecture:** 3-tier — guide/base + guide/doc + guide/dev + guide/reference + .claude/ (infra)

## Folder structure
```
guide/
├── base/               8 modules (00→07) — ai cũng cần
├── doc/                6 modules (01→06) — Technical Writing audience
├── dev/                6 modules (01→06) — Developer audience
└── reference/          config-architecture, model-specs, skills-list, ...
machine-readable/       llms.txt (machine-readable index)
.claude/                CLAUDE.md, SETUP.md, settings.json, settings.local.json
.claude/rules/          writing-standards, reference-standards, scaffold-standards, tier-base, tier-doc, tier-dev
.claude/hooks/          format-check.py (PostToolUse), link-check.py (standalone)
.claude/skills/         session-start/, version-bump/, cross-ref-checker/, module-review/, doc-standard-enforcer/, source-audit/, upgrade-guide/, nav-update/
.claude/commands/       start, checkpoint, validate-doc, review-module, weekly-review (5 files)
_scaffold/              Starter templates (project-instructions/, global-instructions/, skill-templates/, examples/, checklists/)
project-state.md        Project overview (cho người đọc)
VERSION                 SSOT cho version number
```

## Language rules
- **Ngôn ngữ chính:** Tiếng Việt
- **Thuật ngữ kỹ thuật:** giữ tiếng Anh — KHÔNG Việt hóa (AMR, ROS, SLAM, Lidar, skill, hook, prompt...)
- **Placeholders:** `{{variable}}`
- **Source markers:**
  - `[Nguồn: ...]` — official documentation
  - `[Ứng dụng Kỹ thuật]` — applied examples
  - `[Cập nhật MM/YYYY]` — time-sensitive content
- **Thinking features:** `Extended thinking` = UI toggle (Settings > Search and tools). `Adaptive Thinking` = API feature (`thinking: {type: "adaptive"}`). KHÔNG dùng hoán đổi.

## Writing standards
- **Heading hierarchy:** `#` title → `##` section → `###` subsection — KHÔNG skip level
- **Code blocks:** luôn kèm language tag (```python, ```yaml, ```bash...)
- **Cross-links:** dùng relative paths (`../base/04-context-management.md#section`)
- **File naming:** lowercase, dấu gạch ngang, prefix số thứ tự (01-, 02-...)
- **Module header:** Module 00 có version link `[VERSION](../VERSION)` (SSOT); modules 01–10 không bắt buộc — KHÔNG hardcode version

## Icon & Emoji Rules
- **ALLOWED** (chỉ trong bảng và status markers): ⚠️ ✅ ❌ 🔴 🟡 🟢 🔵
- **BANNED:** Mọi emoji/icon khác — bao gồm 💡 🚀 😊 🎯 ✨ 📌 🔥 👉 📝 💪 🤔 ⭐ 🏗️ 📊 🛠️
- **Prose warnings/tips/notes:** dùng Obsidian callout syntax
  - `> [!WARNING]` thay cho ⚠️ trong đoạn văn
  - `> [!TIP]` thay cho 💡
  - `> [!NOTE]` thay cho 📌
  - `> [!IMPORTANT]` thay cho 🎯
- Rule áp dụng cho **cả** content trong `guide/` **và** output Claude tạo ra
- Nếu output chứa emoji ngoài allowlist → remove trước khi trả lời

## Rules — PHẢI tuân thủ
1. **Git-first backup:** Chạy `/checkpoint` trước khi bắt đầu edit module lớn. File `.bak` không nên tạo (đã thêm vào `.gitignore`) — trừ khi làm việc offline không có Git access.
2. **Check version:** khi edit module → đọc `VERSION` trước
3. **Version bump:** sửa `VERSION` trước — module headers tự reflect, KHÔNG sửa thủ công từng file
4. **No destructive git:** KHÔNG force push, reset --hard, hoặc xóa branch mà không hỏi user
5. **project-state.md:** update sau milestone lớn (version bump, structural changes)
6. **Pre-publish verify:** trước khi document Memory/plan availability hoặc feature defaults, verify tại support.claude.com — features thay đổi thường xuyên

## Git workflow
- **Branch naming:** `feat/<topic>`, `fix/<topic>`, `docs/<topic>`
- **Commit message:** tiếng Việt ngắn gọn, ví dụ: `Thêm cross-link module 03 → config-architecture`
- **Main branch:** `master` — luôn tạo PR thay vì push trực tiếp
- **Không commit:** `.bak` files

## Token optimization
- **Default model:** Sonnet — dùng cho hầu hết tác vụ (edit, search, review)
- **Switch Opus khi:** architectural decisions, complex refactoring, multi-file analysis
- **Giảm token:** đọc file có `offset`/`limit` khi file > 500 dòng
- **Skill thay vì prompt dài:** dùng skill có sẵn thay vì viết lại instructions mỗi lần

## Available skills
*Project skills (`.claude/skills/`):*

| Skill | Trigger |
|-------|---------|
| `/session-start` | Bắt đầu session mới, "tiếp tục", "còn lại gì" |
| `/version-bump` | "bump version", "lên version", "release vX.X" |
| `/doc-standard-enforcer` | Manual deep review content — "review format", "kiểm tra standards" |
| `/cross-ref-checker` | Kiểm tra cross-references trong module |
| `/module-review` | Deep review một module (underlying skill cho `/review-module`) |
| `/source-audit` | Scan source markers theo 3-tier standard — "source audit", "kiểm tra sources" |
| `/upgrade-guide` | Scan stale data, broken refs, dependency issues — "health check", "scan project" |
| `/nav-update` | Auto-update prev/next nav links — "update nav", "fix navigation" |

*Global built-in (không phải project skill):*

| Skill | Note |
|-------|------|
| `/simplify` | Review code quality — available toàn Claude Code |

## Available commands
*(`.claude/commands/`)*

| Command | Trigger |
|---------|---------|
| `/start` | Đầu mỗi session |
| `/checkpoint` | Quick commit |
| `/validate-doc` | Kiểm tra module — argument: số module (vd `03`) |
| `/review-module` | Deep review module — argument: số module (vd `06`) |
| `/weekly-review` | Review hàng tuần |

## Automation infrastructure
- **Rules (auto-load):** `.claude/rules/writing-standards.md` loads khi edit `guide/**/*.md`
- **PostToolUse hook:** `format-check.py` kiểm tra heading hierarchy + code block tags + source markers sau mỗi Edit/Write
- **Standalone check:** `python3 .claude/hooks/link-check.py` scan cross-links + anchor targets (chạy trước checkpoint)
- **Source verification:** 3-tier standard — Tier 1 (Anthropic official), Tier 2 (verified repos), Tier 3 (community + disclaimer)

## Module status (quick ref)
| Tier | Files | Status |
|------|-------|--------|
| base/ | 00→07 (8 files) | v9.0 — reviewed + polished 🟢 |
| doc/ | 01→06 (6 files) | v9.0 — reviewed + polished 🟢 |
| dev/ | 01→06 (6 files) | v9.0 — complete content 🟢 |
| reference/ | 12 files | config-architecture, model-specs, skills-list, skills-guide, workflow-patterns, quick-templates, claude-code-setup, ecosystem-overview, cheatsheet-base/doc/dev, prompt-format-guide 🟢 |

## Khi nào update file này
- Thêm skill mới → update bảng Available skills
- Thay đổi folder structure → update Folder structure section
- Thay đổi conventions → update Language rules / Writing standards
