# Custom Style Reference

**Mức độ:** Intermediate | **Audience:** Technical Writing, Documentation
**Cập nhật:** 2026-03-07

---
depends-on: [base/02-setup]
impacts: []
---

Hướng dẫn chi tiết cách tạo và quản lý Custom Styles trong Claude.ai. Kiến thức nền tảng về 4 preset styles: xem [Setup & Personalization, mục 2.3](../base/02-setup.md#23-styles----tùy-chỉnh-cách-claude-trả-lời).

---

## Tạo Custom Style

Bạn có thể tạo Custom Style bằng 2 cách:

**Cách 1: Upload writing sample.** Cung cấp 1-2 văn bản mẫu thể hiện phong cách bạn muốn. Claude sẽ học và bắt chước tone, structure, vocabulary.

**Cách 2: Viết instructions trực tiếp.** Mô tả cách bạn muốn Claude respond.

---

## Custom Style Templates cho Phenikaa-X

### Technical Documentation Style

[Ứng dụng Kỹ thuật]

```text
Name: Phenikaa-X Technical

Instructions:
- Ngôn ngữ: Tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh
- Tone: Professional, direct, actionable
- Không dùng filler phrases ("như bạn biết", "điều quan trọng là")
- Format:
  - Headings rõ ràng
  - Numbered steps cho procedures
  - CẢNH BÁO và LƯU Ý cho safety/tips
  - Code blocks cho commands
- Độ dài: Vừa đủ, không thừa
- Khi không chắc chắn: nói rõ, đề xuất cách verify
```

### Internal Communication Style

[Ứng dụng Kỹ thuật]

```text
Name: Phenikaa-X Internal

Instructions:
- Ngôn ngữ: Tiếng Việt, thân thiện nhưng chuyên nghiệp
- Tone: Collaborative, supportive
- Format:
  - Summary ở đầu (TL;DR)
  - Bullet points cho action items
  - Deadline rõ ràng
  - Tag người chịu trách nhiệm
- Độ dài: Ngắn gọn, tối đa 1 trang
```

---

## Khi nào dùng Style nào

| Tình huống | Style khuyến nghị |
|-----------|-------------------|
| Debug session hàng ngày | Normal hoặc Concise |
| Viết tài liệu cho khách hàng | Formal hoặc Custom "Technical" |
| Hỏi đáp nhanh về ROS commands | Concise |
| Brainstorming giải pháp | Explanatory |
| Email nội bộ | Custom "Internal Communication" |
| Training materials | Explanatory |

4 preset styles (Normal, Concise, Explanatory, Formal) và cách chọn: xem [Setup & Personalization, mục 2.3](../base/02-setup.md#23-styles----tùy-chỉnh-cách-claude-trả-lời).

---

## Multi-Style Workflow

[Ứng dụng Kỹ thuật]

Trong thực tế, một dự án documentation thường cần nhiều styles khác nhau cho từng loại output. Cách quản lý:

**1. Tạo 2-3 Custom Styles cho team:**
- "Technical" — cho SOP, specs, procedures
- "Internal" — cho email, báo cáo nội bộ, meeting notes
- "Client-facing" — cho tài liệu gửi khách hàng

**2. Chuyển style theo task, không theo ngày:**
- Bắt đầu task → chọn style phù hợp với output type
- Không cần maintain 1 style xuyên suốt session

**3. Kết hợp Style + Project Instructions:**
- Style kiểm soát **tone và format** (cách Claude viết)
- Project Instructions kiểm soát **content và scope** (Claude viết gì)
- Hai thứ bổ sung nhau, không thay thế
