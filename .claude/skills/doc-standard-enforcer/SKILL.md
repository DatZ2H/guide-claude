---
name: doc-standard-enforcer
description: >
  Auto-activate khi user tạo hoặc edit nội dung trong guide/. Trigger khi user nói
  "edit module", "viết section", "thêm content", "update guide", "sửa module",
  "thêm ví dụ", "viết thêm", hoặc bất kỳ yêu cầu nào tạo/chỉnh sửa file markdown
  trong thư mục guide/. Enforces writing standards cho Guide Claude project.
---

# Doc Standard Enforcer — Guide Claude Project

Skill này tự động áp dụng writing standards khi tạo hoặc edit nội dung trong `guide/`.

## Khi nào kích hoạt

Bất kỳ lúc nào user yêu cầu tạo mới hoặc chỉnh sửa nội dung trong `guide/**/*.md`.

## Rules — PHẢI tuân thủ khi viết/edit content

### Ngôn ngữ

- Viết tiếng Việt
- Giữ nguyên thuật ngữ kỹ thuật tiếng Anh — KHÔNG dịch (prompt, hook, skill, context window, token, API, AMR, ROS, SLAM, Lidar...)
- Dùng `{{variable}}` cho placeholders

### Heading hierarchy

- `#` — module title (chỉ 1 lần, dòng đầu tiên)
- `##` — section
- `###` — subsection
- KHÔNG skip level (VD: `##` → `####` là SAI)

### Cấu trúc section

- Mỗi `##` hoặc `###` bắt đầu bằng 1-2 câu context giải thích section này nói về gì trước khi đi vào chi tiết
- Tránh đoạn văn >5 câu liên tục — break bằng list, code block, hoặc sub-heading

### Code blocks

- Luôn có language tag: ```python, ```yaml, ```bash, ```markdown...
- KHÔNG dùng ``` không tag

### Cross-links

- Dùng relative path: `[tên](../guide/04-context-management.md#section-name)`
- KHÔNG dùng absolute path hoặc URL đến repo

### Source markers

- `[Nguồn: official docs URL hoặc tên tài liệu]` — cho thông tin từ documentation
- `[Ứng dụng Kỹ thuật]` — cho ví dụ applied từ Phenikaa-X context
- `[Cập nhật MM/YYYY]` — cho thông tin time-sensitive có thể thay đổi

### Version

- Module header dùng `[VERSION](../VERSION)` — KHÔNG hardcode số version

## Trước khi edit

1. Đọc `VERSION` để biết version hiện tại
2. Tạo backup `.bak` của file trước khi sửa
3. Đọc file cần edit đầy đủ trước khi bắt đầu

## Sau khi edit

Tự kiểm tra nhanh:
- Heading hierarchy có đúng không?
- Code blocks có language tag không?
- Relative links có trỏ đúng file tồn tại không?
- Có section nào thiếu câu context mở đầu không?
