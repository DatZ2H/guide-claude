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

<!-- TODO (S13): Bổ sung advanced Custom Style patterns, multi-style workflows -->
