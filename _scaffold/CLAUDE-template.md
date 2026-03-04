# CLAUDE.md — {{project_name}}

## Project context
{{project_description}}
- **Version:** xem file `VERSION` (SSOT)
- **Phase:** {{current_phase}}
- **Đối tượng:** {{target_audience}}
- **Architecture:** 2-tier — {{content_folder}}/ (content) + .claude/ (infra)

## Folder structure
```
{{project_root}}/
├── {{content_folder}}/         {{content_folder_description}}
├── .claude/                    Infrastructure
│   ├── CLAUDE.md               Folder Instructions (file này)
│   ├── SETUP.md                Onboarding cho maintainer mới
│   ├── settings.json           Project automation (hooks, permissions)
│   ├── commands/               Slash commands (/start, /checkpoint...)
│   └── skills/                 Auto-activate + on-demand skills
├── project-state.md            Project overview
└── VERSION                     SSOT cho version number
```

## Language rules
- **Ngôn ngữ chính:** {{language_main}}
- **Thuật ngữ kỹ thuật:** giữ tiếng Anh — KHÔNG Việt hóa
- **Placeholders:** `{{variable}}`
- {{source_marker_conventions}}

## Writing standards
- **Heading hierarchy:** `#` title → `##` section → `###` subsection — KHÔNG skip level
- **Code blocks:** luôn kèm language tag (```python, ```yaml, ```bash...)
- **Cross-links:** dùng relative paths (`../{{content_folder}}/file.md#section`)
- **File naming:** {{naming_conventions}}

## Icon & Emoji Rules
- **ALLOWED** (chỉ trong bảng và status markers): ⚠️ ✅ ❌ 🔴 🟡 🟢 🔵
- **BANNED:** Mọi emoji/icon khác
- **Prose warnings/tips/notes:** dùng Obsidian callout syntax
  - `> [!WARNING]` thay cho ⚠️ trong đoạn văn
  - `> [!TIP]` thay cho tips
  - `> [!NOTE]` thay cho ghi chú
  - `> [!IMPORTANT]` thay cho nội dung quan trọng

## Rules — PHẢI tuân thủ
1. **Git-first backup:** Chạy `/checkpoint` trước khi edit lớn. File `.bak` không nên tạo — trừ khi không có Git access.
2. **Check version:** khi edit module → đọc `VERSION` trước
3. **Version bump:** sửa `VERSION` trước — module headers tự reflect, KHÔNG sửa thủ công từng file
4. **No destructive git:** KHÔNG force push, reset --hard, hoặc xóa branch mà không hỏi user
5. **project-state.md:** update sau milestone lớn (version bump, structural changes)
6. {{additional_rules}}

## Git workflow
- **Branch naming:** `feat/<topic>`, `fix/<topic>`, `docs/<topic>`
- **Commit message:** {{commit_language}}, ví dụ: `Thêm cross-link module 03 → config`
- **Main branch:** `{{main_branch}}` — luôn tạo PR thay vì push trực tiếp
- **Không commit:** `.bak` files, `.env`, credentials

## Token optimization
- **Default model:** Sonnet — dùng cho hầu hết tác vụ (edit, search, review)
- **Switch Opus khi:** architectural decisions, complex refactoring, multi-file analysis
- **Giảm token:** đọc file có `offset`/`limit` khi file > 500 dòng
- **Skill thay vì prompt dài:** dùng skill có sẵn thay vì viết lại instructions mỗi lần

## Available skills
*Project skills (`.claude/skills/`):*

| Skill | Trigger |
|-------|---------|
| {{skill_1}} | {{trigger_1}} |
| {{skill_2}} | {{trigger_2}} |

## Available commands
*(`.claude/commands/`)*

| Command | Trigger |
|---------|---------|
| `/start` | Đầu mỗi session |
| `/checkpoint` | Quick commit |
| {{command_3}} | {{trigger_3}} |

## Deliverable status (quick ref)
| Range | Status |
|-------|--------|
| {{deliverable_range_1}} | {{status_1}} |
| {{deliverable_range_2}} | {{status_2}} |

## Khi nào update file này
- Thêm skill mới → update bảng Available skills
- Thay đổi folder structure → update Folder structure section
- Thay đổi conventions → update Language rules / Writing standards

---
<!-- HƯỚNG DẪN CUSTOMIZE (xóa section này sau khi điền xong)

Thay các {{placeholder}} sau:

{{project_name}}
  → Tên project ngắn gọn, ví dụ: "Documentation Standard", "API Integration Guide"

{{project_description}}
  → 1-2 câu mô tả project là gì và để làm gì.

{{current_phase}}
  → Ví dụ: "Discovery", "Development", "Internal Review"

{{target_audience}}
  → Ai dùng output, ví dụ: "Kỹ sư tự động hóa, R&D tại Phenikaa-X"

{{content_folder}} / {{content_folder_description}}
  → Tên folder content chính (guide/, docs/) + mô tả ngắn ("13 module files + reference/")

{{project_root}}
  → Tên thư mục gốc project

{{language_main}}
  → Ví dụ: "Tiếng Việt"

{{source_marker_conventions}}
  → Ví dụ: "[Nguồn: ...] cho official, [Ứng dụng Kỹ thuật] cho applied examples"
  → Hoặc xóa nếu project không cần

{{naming_conventions}}
  → Ví dụ: "lowercase, dấu gạch ngang, prefix số thứ tự (01-, 02-...)"

{{additional_rules}}
  → Rules đặc thù của project, ví dụ: "Pre-publish verify: check support.claude.com trước khi document features"

{{commit_language}}
  → Ví dụ: "tiếng Việt ngắn gọn" hoặc "English, imperative mood"

{{main_branch}}
  → Ví dụ: "master" hoặc "main"

{{skill_1..2}} / {{trigger_1..2}}
  → Liệt kê skills hiện có. Nếu chưa có: xóa dòng và ghi "Chưa có — thêm khi cần"

{{command_3}} / {{trigger_3}}
  → Thêm commands ngoài /start và /checkpoint. Hoặc xóa dòng nếu chỉ dùng 2 commands mặc định.

{{deliverable_range_1..2}} / {{status_1..2}}
  → Ví dụ: "Module 00–09" / "v1.0 base — 🟢"

Sau khi điền xong → xóa toàn bộ section comment này.
-->
