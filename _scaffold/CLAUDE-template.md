# Folder Instructions — {{project_name}}

## Project overview
{{project_description}}

## Folder structure
- {{content_folder}}/ — {{content_folder_description}}
- .claude/skills/ — {{skills_description}}
- .claude/commands/ — slash commands (/start, /checkpoint, v.v.)
- .claude/SETUP.md — maintainer guide (skills, commands, conventions)
- .claude/settings.json — project automation settings (hooks, permissions)
- project-state.md — context transfer document (briefing cho Project Chat khi cần)
- VERSION — single source of truth cho version number

## Conventions
- {{language_conventions}}
- {{naming_conventions}}
- {{source_marker_conventions}}

## Rules
- {{specific_rules}}
- KHÔNG sửa {{protected_files}} mà không tạo backup (`.bak`) trước
- Khi edit: đọc `VERSION` để biết version hiện tại
- Khi bump version: sửa `VERSION` trước — headers tự reflect, không cần sửa thủ công

---
<!-- HƯỚNG DẪN CUSTOMIZE (xóa section này sau khi điền xong)

Thay các {{placeholder}} sau:

{{project_name}}
  → Tên project ngắn gọn, ví dụ: "Documentation Standard", "API Integration Guide"

{{project_description}}
  → 1-2 câu mô tả project là gì và để làm gì.
  → Ví dụ: "Đây là dự án xây dựng bộ chuẩn tài liệu cho toàn công ty — rules + templates + glossary."

{{content_folder}}
  → Tên folder chứa content chính, ví dụ: guide/, docs/, content/

{{content_folder_description}}
  → Mô tả ngắn nội dung folder, ví dụ: "11 module files + reference/"

{{skills_description}}
  → Liệt kê skills có trong .claude/skills/, ví dụ: "session-start, version-bump"
  → Nếu chưa có skill nào: "Chưa có — thêm khi cần"

{{language_conventions}}
  → Quy tắc ngôn ngữ, ví dụ: "Language: Tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh"

{{naming_conventions}}
  → Quy tắc đặt tên file, ví dụ: "File naming: lowercase, dấu gạch ngang, có số thứ tự (01-, 02-...)"

{{source_marker_conventions}}
  → Quy tắc đánh dấu nguồn, ví dụ: "[Nguồn: ...] cho official, [Ví dụ] cho applied examples"
  → Hoặc xóa dòng này nếu project không cần source markers

{{specific_rules}}
  → Các rules đặc thù của project này. Ví dụ:
  → "KHÔNG publish module chưa qua review"
  → "Mỗi module phải có mục Checklist ở cuối"

{{protected_files}}
  → Files/folders cần bảo vệ khỏi edit không có backup, ví dụ: "files trong guide/", "docs/"

Sau khi điền xong → xóa toàn bộ section comment này trước khi lưu.
-->
