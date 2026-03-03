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
├── .claude/                     Tầng B — Infrastructure
│   ├── CLAUDE.md
│   └── skills/
│
└── _memory/                     Tầng C — Persistence
    ├── session-state.md
    └── decisions-log.md
```

## Quyết định gần nhất

| Ngày | Quyết định | Rationale |
|------|-----------|-----------|
| {{date}} | Khởi tạo project với 3-tier architecture | Phân tách content vs infrastructure vs persistence |
| {{date}} | {{decision_2}} | {{rationale_2}} |
| {{date}} | {{decision_3}} | {{rationale_3}} |

## Conventions
- {{language_convention}}
- `{{variable}}` = placeholder
- {{other_conventions}}

## Khi nào update project-state.md

File này là **context transfer document** — update trên Cowork, paste vào Project Chat khi cần brainstorm/planning.

Update khi:
- Sau milestone lớn (version bump, hoàn thành deliverable)
- Trước khi brainstorm trên Project Chat (để có context mới nhất)
- Khi cấu trúc thư mục hoặc decisions thay đổi đáng kể

## Hướng dẫn cho Claude khi đọc file này

1. File này là **briefing document** — tổng quan dự án, paste vào Project Chat khi cần context cho brainstorm/planning.
2. Nội dung chi tiết nằm trong **Cowork folder**. Phần lớn công việc diễn ra trên Cowork (Cowork-primary workflow).
3. Nếu cần tham chiếu nội dung cụ thể, yêu cầu người dùng paste excerpt hoặc ghi chú "sẽ kiểm tra trên Cowork".
4. Ưu tiên **quyết định gần nhất** trong bảng trên hơn nội dung file nào nếu có mâu thuẫn.
5. Khi đề xuất thay đổi, output dưới dạng **prompt có thể chạy trên Cowork** — không giả định Claude đang đọc file thật.

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
