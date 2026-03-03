---
name: {{skill_name}}
description: {{one_line_description_with_trigger_context}}
---

# {{Skill Title}}

## Trigger

Kích hoạt khi user:
- Nói "{{trigger_phrase_1}}"
- Nói "{{trigger_phrase_2}}"
- {{trigger_condition_3}}

## Pre-conditions

Trước khi chạy, Claude kiểm tra:
- {{required_input_1}} có tồn tại không
- {{required_input_2}} có sẵn không

Nếu thiếu → hỏi user trước khi tiếp tục.

## Quy trình

### Bước 1 — {{step_1_name}}

{{step_1_description_chi_tiet_claude_lam_gi}}

### Bước 2 — {{step_2_name}}

{{step_2_description}}

### Bước 3 — {{step_3_name}}

{{step_3_description}}

## Output

{{describe_output_format_and_content}}

## Rules

- KHÔNG thực hiện nếu thiếu {{critical_input}} — hỏi user trước
- {{rule_2}}
- {{rule_3}}

---
<!-- HƯỚNG DẪN TẠO SKILL MỚI (xóa section này sau khi điền xong)

CẤU TRÚC FILE (quan trọng):
  Skill PHẢI là một FOLDER, không phải file đơn.
  Đúng:  .claude/skills/your-skill-name/SKILL.md
  Sai:   .claude/skills/your-skill-name.md

  Sau khi dùng template này:
  1. Tạo folder: .claude/skills/{{skill_name}}/
  2. Copy file này vào folder: .claude/skills/{{skill_name}}/SKILL.md
  3. Điền {{placeholders}} và xóa phần hướng dẫn này

Thay các {{placeholder}} sau:

{{skill_name}}
  → Tên kebab-case, ví dụ: "session-start", "module-review", "version-bump"
  → Dùng tên này làm tên folder

{{one_line_description_with_trigger_context}}
  → ĐÂY LÀ PHẦN QUAN TRỌNG NHẤT — quyết định Claude có nhận ra skill không
  → Phải bao gồm CẢ HAI: "làm gì" VÀ "khi nào trigger"
  → Kém:  "Review tài liệu kỹ thuật"
  → Tốt:  "Review tài liệu kỹ thuật theo 5 tiêu chí chất lượng. Trigger khi user nói
           'review module X', 'kiểm tra chất lượng', hoặc trước khi release."

{{Skill Title}}
  → Tiêu đề đầy đủ cho phần đọc của người, ví dụ: "Module Review Workflow"

{{trigger_phrase_1..2}}
  → Câu/từ user hay nói để gọi skill, ví dụ: "review module", "bump version"

{{trigger_condition_3}}
  → Tình huống khác (không chỉ phrase), ví dụ: "Chuẩn bị bump version"

{{required_input_1..2}}
  → Những gì phải có trước khi skill chạy, ví dụ: "_memory/session-state.md"

{{step_1..3_name}}
  → Tên ngắn cho bước, ví dụ: "Đọc context", "Phân tích", "Output report"

{{step_1..3_description}}
  → Mô tả chi tiết Claude làm gì trong bước này — càng cụ thể càng tốt

{{describe_output_format_and_content}}
  → Output trông như thế nào? File? Message? Format cụ thể?
  → Ví dụ: "Báo cáo markdown với 3 sections: Summary, Issues, Recommendations"

{{critical_input}}
  → Input bắt buộc phải có — thiếu thì không chạy

{{rule_2..3}}
  → Constraints quan trọng, ví dụ: "KHÔNG sửa file — chỉ report"
  → "Luôn confirm với user trước khi overwrite file"

SAU KHI ĐIỀN XONG:
- Xóa toàn bộ section comment này
- Thêm skill vào .claude/CLAUDE.md:
  ## Skills
  - `{{skill_name}}` — {{one_line_description}}
- Test: mở Cowork session mới → gõ trigger phrase → verify Claude activate đúng
-->
