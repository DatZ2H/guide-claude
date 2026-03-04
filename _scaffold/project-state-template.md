# Project State — {{project_name}}
Version: {{version}} | Last updated: {{date}}

## Phase hiện tại
- **Phase:** {{current_phase}}
- **Mục tiêu:** {{project_goal}}
- **Đối tượng:** {{target_audience}}

## Trạng thái deliverables

| Deliverable | File/Folder | Trạng thái | Ghi chú |
|-------------|-------------|------------|---------|
| {{deliverable_1}} | {{file_path_1}} | {{status_1}} | {{note_1}} |
| {{deliverable_2}} | {{file_path_2}} | {{status_2}} | {{note_2}} |
| {{deliverable_3}} | {{file_path_3}} | {{status_3}} | {{note_3}} |

## Cấu trúc thư mục

```
{{project_root}}/
├── README.md
├── VERSION
├── project-state.md
│
├── {{content_folder}}/          Tầng A — Content
│   └── {{content_structure}}
│
└── .claude/                     Tầng B — Infrastructure
    ├── CLAUDE.md
    ├── SETUP.md
    ├── settings.json
    ├── commands/
    └── skills/
```

## Quyết định gần nhất

| Ngày | Quyết định | Rationale |
|------|-----------|-----------|
| {{date}} | Khởi tạo project với 2-tier architecture | Phân tách content vs infrastructure |
| {{date}} | {{decision_2}} | {{rationale_2}} |
| {{date}} | {{decision_3}} | {{rationale_3}} |

> Decisions cũ hơn 30 ngày: xem `git log`.

## Conventions
- {{language_convention}}
- `{{variable}}` = placeholder
- {{other_conventions}}

## Khi nào update project-state.md

File này là **project overview** — tổng quan cho người đọc và Claude.

Update khi:
- Sau milestone lớn (version bump, hoàn thành deliverable)
- Khi cấu trúc thư mục hoặc decisions thay đổi đáng kể
- Trước khi onboard thành viên mới vào project

---
<!-- HƯỚNG DẪN CUSTOMIZE (xóa section này sau khi điền xong)

Thay các {{placeholder}} sau:

{{project_name}}        → Tên đầy đủ của project
{{version}}             → Version hiện tại, ví dụ: 1.0
{{date}}                → Ngày hôm nay (YYYY-MM-DD)
{{current_phase}}       → Ví dụ: "Discovery", "Development", "Review", "Production"
{{project_goal}}        → Mục tiêu cuối cùng của project trong 1 câu
{{target_audience}}     → Ai sẽ dùng output của project này
{{deliverable_1..3}}    → Tên các deliverable chính (module, doc, template...)
{{file_path_1..3}}      → Đường dẫn file tương ứng
{{status_1..3}}         → "Draft", "In Progress", "Done", "Blocked"...
{{note_1..3}}           → Ghi chú ngắn, hoặc để trống
{{project_root}}        → Tên thư mục gốc của project
{{content_folder}}      → Tên folder content chính (guide/, docs/, content/...)
{{content_structure}}   → Liệt kê các files/folders chính trong content folder
{{decision_2..3}}       → Các quyết định kiến trúc/hướng đi ban đầu
{{rationale_2..3}}      → Lý do đằng sau quyết định
{{language_convention}} → Ví dụ: "Tiếng Việt chính, thuật ngữ kỹ thuật giữ tiếng Anh"
{{other_conventions}}   → Các conventions khác (markers, naming, format...)

Sau khi điền xong → xóa toàn bộ section comment này trước khi lưu.
-->
