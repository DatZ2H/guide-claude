# Prompt Format Guide

**Loại tài liệu:** Reference | **Audience:** Tất cả kỹ sư
**Cập nhật:** 2026-03-07

---
depends-on: [base/03-prompt-engineering]
impacts: [doc/02-template-library, base/06-mistakes-fixes]
---

Hướng dẫn chi tiết 3 loại format dùng trong prompt Claude: XML tags, bracket markers, và placeholders. Module này bổ sung cho [Prompt Engineering](../base/03-prompt-engineering.md) — cung cấp tra cứu nhanh và examples theo tier.

[Nguồn: Anthropic Docs - Prompting Best Practices] [Cập nhật 03/2026]

---

## Tổng quan 3 Format

| Format | Cú pháp | Mục đích | Khi nào dùng |
|--------|---------|----------|-------------|
| XML tags | `<tag>...</tag>` | Cấu trúc prompt phức tạp, tách rõ sections | Prompt > 3 yếu tố, cần Claude phân biệt instruction vs content |
| Bracket markers | `[Label]` | Prompt đơn giản, metadata labels, quality markers | Prompt C-T-R nhanh, đánh dấu mức tin cậy |
| Placeholders | `{{variable_name}}` | Giá trị cần thay thế mỗi lần dùng | Templates tái sử dụng, bất kỳ format nào |

> [!IMPORTANT] **Quy tắc vàng:** Không trộn XML tags và bracket markers trong cùng một prompt. Chọn 1 format và dùng nhất quán. Placeholders `{{}}` dùng được trong cả hai format.

---

## XML Tags — Chi tiết

XML tags giúp Claude phân biệt rõ các phần trong prompt, giảm nhầm lẫn giữa instruction và content. Đây là format chính thức được Anthropic khuyến nghị cho structured prompts.

[Nguồn: Anthropic Docs - Use XML tags]

### Danh sách tags chuẩn

| Tag | Mục đích | Bắt buộc? |
|-----|----------|-----------|
| `<task>` | Mô tả nhiệm vụ | Core |
| `<context>` | Bối cảnh, thông tin nền | Core |
| `<role>` | Vai trò/expertise của Claude | Khuyến nghị |
| `<requirements>` | Yêu cầu format, độ dài, ngôn ngữ | Tùy chọn |
| `<output_format>` | Cấu trúc output mong muốn | Tùy chọn |
| `<examples>` | Ví dụ input-output mẫu | Tùy chọn |
| `<constraints>` | Ràng buộc, giới hạn | Tùy chọn |
| `<input_data>` | Dữ liệu đầu vào (logs, data) | Tùy chọn |
| `<thinking_instructions>` | Hướng dẫn quá trình suy luận | Tùy chọn |
| `<quality_requirements>` | Yêu cầu độ chính xác | Tùy chọn |
| `<tone>` | Giọng điệu, phong cách | Tùy chọn |
| `<evaluation_criteria>` | Tiêu chí đánh giá | Tùy chọn |
| `<chain_info>` | Thông tin chuỗi prompt | Tùy chọn |
| `<documents>` | Chứa nhiều tài liệu | Tùy chọn |

### Quy tắc đặt tên

- **Lowercase + underscore:** `<task_description>`, `<input_data>` (không phải `<TaskDescription>`)
- **Mô tả rõ ràng:** tên tag phản ánh nội dung bên trong
- **Nhất quán:** dùng cùng tag name xuyên suốt project
- **Nesting hợp lý:** dùng khi content có hierarchy tự nhiên

```xml
<!-- Nesting example cho multiple documents -->
<documents>
  <document index="1">
    <source>report_q1.pdf</source>
    <document_content>
      {{REPORT_Q1}}
    </document_content>
  </document>
  <document index="2">
    <source>report_q2.pdf</source>
    <document_content>
      {{REPORT_Q2}}
    </document_content>
  </document>
</documents>
```

### Khi nào dùng XML

| Dùng XML | Không cần XML |
|----------|---------------|
| Prompt > 3 yếu tố (role + task + context + data + ...) | Câu hỏi đơn giản 1-2 câu |
| Có data đầu vào cần tách khỏi instructions | Prompt C-T-R ngắn gọn |
| Cần few-shot examples | Chat hàng ngày |
| Output cần theo template cụ thể | Brainstorming tự do |
| Prompt dùng lại nhiều lần (template) | Hỏi kiến thức chung |

### Template copy-paste

```xml
<role>
{{vai_tro_chuyen_mon}}
</role>

<task>
{{mo_ta_nhiem_vu}}
</task>

<context>
- Hệ thống: {{ten_he_thong}}
- Audience: {{doi_tuong}}
- Mục đích: {{muc_dich}}
</context>

<requirements>
- Format: {{format_mong_muon}}
- Độ dài: {{gioi_han}}
- Ngôn ngữ: {{yeu_cau_ngon_ngu}}
</requirements>
```

---

## Bracket Markers — Chi tiết

Bracket markers `[Label]` dùng cho prompt đơn giản và metadata labels. Hai use cases chính:

### Use case 1: Prompt C-T-R nhanh

Dùng `[Context]`, `[Task]`, `[Requirements]` để cấu trúc prompt ngắn mà không cần XML:

```text
[Context]
SOP Pre-operation Check cho AMR-Fleet tại nhà máy Phenikaa-X.
Audience: Kỹ thuật viên bảo trì Level 2.

[Task]
Viết SOP Pre-operation Check theo format chuẩn công ty.

[Requirements]
- Numbered steps + Pass/Fail criteria
- Tối đa 2 trang
- Tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh
```

### Use case 2: Quality markers trong output

Yêu cầu Claude đánh dấu mức tin cậy cho từng claim:

| Marker | Ý nghĩa | Khi nào dùng |
|--------|---------|-------------|
| `[FACT]` | Thông tin factual đã verify | Dữ liệu chính xác |
| `[INFERENCE]` | Suy luận từ dữ liệu | Phân tích, đánh giá |
| `[CẦN VERIFY]` | Chưa chắc chắn | Thông tin cần kiểm tra thêm |

**Ví dụ prompt:**

```text
Phân tích error log này. Đánh dấu mỗi claim:
- [FACT] cho thông tin trực tiếp từ log
- [INFERENCE] cho suy luận của bạn
- [CẦN VERIFY] cho thông tin cần kiểm tra thêm

{{error_log}}
```

### Brackets trong bộ tài liệu này

Bộ tài liệu Guide Claude dùng brackets cho source citations:

| Marker | Ý nghĩa |
|--------|---------|
| `[Nguồn: ...]` | Tài liệu chính thức (Tier 1-2) |
| `[Ứng dụng Kỹ thuật]` | Ví dụ ứng dụng từ Phenikaa-X |
| `[Cập nhật MM/YYYY]` | Thông tin time-sensitive |
| `[Ghi chú: ...]` | Pattern non-official (Tier 3) |

---

## Placeholders — Chi tiết

Placeholders `{{variable_name}}` đánh dấu giá trị cần thay thế mỗi lần sử dụng. Dùng được trong cả XML tags và bracket markers.

### Quy tắc đặt tên

- **Lowercase + underscore:** `{{machine_id}}`, `{{error_log}}`
- **Mô tả rõ:** `{{sensor_data}}` thay vì `{{data}}`
- **Không dùng space:** `{{machine_id}}` không phải `{{machine id}}`

### Placeholders phổ biến theo tier

**Base (mọi kỹ sư):**

| Placeholder | Mô tả |
|-------------|--------|
| `{{machine_id}}` | ID robot/thiết bị |
| `{{error_log}}` | Log lỗi cần phân tích |
| `{{sensor_data}}` | Dữ liệu sensor |
| `{{document_content}}` | Nội dung tài liệu cần xử lý |

**Doc (Technical Writing):**

| Placeholder | Mô tả |
|-------------|--------|
| `{{template_type}}` | Loại template (SOP, spec, manual) |
| `{{audience_level}}` | Mức độ audience (beginner, intermediate, expert) |
| `{{style_name}}` | Tên Custom Style đang dùng |
| `{{review_criteria}}` | Tiêu chí review tài liệu |

**Dev (Developer):**

| Placeholder | Mô tả |
|-------------|--------|
| `{{file_path}}` | Đường dẫn file cần xử lý |
| `{{test_command}}` | Lệnh chạy test |
| `{{branch_name}}` | Tên git branch |
| `{{agent_config}}` | Cấu hình agent YAML |

---

## Ví dụ theo Tier

### Base — Debug AMR (XML)

```xml
<role>
Senior ROS Engineer với kinh nghiệm AMR diagnostics.
</role>

<task>
Phân tích error log và đề xuất root cause + fix.
</task>

<context>
- Robot: {{machine_id}}
- Firmware: {{firmware_version}}
- Vấn đề: Localization failure sau khi rotate nhanh
</context>

<input_data>
{{error_log}}
</input_data>

<quality_requirements>
- Đánh dấu [FACT] / [INFERENCE] / [CẦN VERIFY] cho mỗi claim
- Nếu không chắc chắn, nói rõ thay vì đoán
</quality_requirements>
```

### Doc — Review SOP (Brackets)

```text
[Context]
Review SOP-042 "Quy trình bảo trì hàng tuần AMR-Fleet".
Audience: Kỹ thuật viên Level 2. Chuẩn: IEC 82079-1.

[Task]
Đánh giá SOP theo 4 tiêu chí: completeness, clarity, safety compliance, actionability.

[Requirements]
- Output dạng bảng: Tiêu chí | Score (1-5) | Issues | Fix đề xuất
- Ưu tiên CRITICAL issues trước
```

### Dev — Agent Config (XML + Placeholders)

```xml
<task>
Tạo custom agent configuration cho {{project_name}}.
</task>

<context>
- Project type: {{project_type}}
- Cần agents cho: code review, testing, documentation
- Permission mode: default
</context>

<requirements>
- Output: YAML frontmatter format cho .claude/agents/
- Mỗi agent: name, description, tools, model
- Include example usage commands
</requirements>
```

---

## Chọn Format — Decision Table

| Tiêu chí | Brackets `[...]` | XML `<...>` |
|----------|:-:|:-:|
| Prompt < 5 dòng | ✅ | |
| Prompt > 3 yếu tố | | ✅ |
| Có data đầu vào lớn | | ✅ |
| Cần few-shot examples | | ✅ |
| Chat/hỏi nhanh hàng ngày | ✅ | |
| Template tái sử dụng | | ✅ |
| Quality markers trong output | ✅ | |
| Multiple documents | | ✅ |

**Quy tắc ngón tay cái:** Dùng brackets cho prompt nhanh. Chuyển sang XML khi prompt bắt đầu phức tạp (> 3 yếu tố hoặc có data đầu vào).

---

## Anti-patterns

| Anti-pattern | Vấn đề | Fix |
|-------------|--------|-----|
| Trộn XML và brackets trong 1 prompt | Claude bối rối, output không nhất quán | Chọn 1 format, dùng nhất quán |
| Tag names không rõ nghĩa (`<a>`, `<data1>`) | Claude phải đoán nội dung | Dùng tên mô tả: `<error_log>`, `<review_criteria>` |
| Placeholder không lowercase (`{{MachineName}}`) | Không nhất quán với convention | `{{machine_name}}` — lowercase + underscore |
| XML quá sâu (> 3 cấp nesting) | Phức tạp không cần thiết | Flatten hoặc tách thành prompts riêng |
| Dùng XML cho prompt 1 câu | Overhead không cần thiết | Hỏi trực tiếp, không cần tags |

---

**Xem thêm:**

- [Prompt Engineering](../base/03-prompt-engineering.md) — 6 nguyên tắc + 7 kỹ thuật + Module System
- [Template Library](../doc/02-template-library.md) — Templates doc-specific
- [Quick Templates](quick-templates.md) — Templates tra cứu nhanh
- [Cheatsheet Base](cheatsheet-base.md) — Prompt patterns tóm tắt
