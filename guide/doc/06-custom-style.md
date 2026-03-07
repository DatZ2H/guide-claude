# Custom Style Reference

**Mức độ:** Intermediate | **Audience:** Technical Writing, Documentation
**Cập nhật:** 2026-03-07

---
depends-on: [base/02-setup]
impacts: []
---

Hướng dẫn chi tiết cách tạo và quản lý Custom Styles trong Claude.ai. Kiến thức nền tảng về 4 preset styles: xem [Setup & Personalization, mục 2.3](../base/02-setup.md#23-styles----tùy-chỉnh-cách-claude-trả-lời).

[Nguồn: Anthropic Help Center - Custom Style] [Cập nhật 03/2026]

---

## Tạo Custom Style

Bạn có thể tạo Custom Style bằng 2 cách:

**Cách 1: Upload writing sample.** Cung cấp 1-2 văn bản mẫu thể hiện phong cách bạn muốn. Claude sẽ học và bắt chước tone, structure, vocabulary.

**Cách 2: Viết instructions trực tiếp.** Mô tả cách bạn muốn Claude respond.

> [!NOTE] Custom Style là tính năng của Claude.ai (Settings > Styles). Verify tính khả dụng tại support.anthropic.com nếu UI thay đổi.

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

---

## Advanced Patterns

### Style + Project Instructions Combo

[Ứng dụng Kỹ thuật]

Style và Project Instructions hoạt động ở hai lớp khác nhau. Kết hợp đúng cách giúp kiểm soát cả **cách viết** lẫn **viết gì** mà không cần prompt dài mỗi lần.

| Lớp | Kiểm soát | Ví dụ |
|-----|-----------|-------|
| **Style** | Tone, format, độ dài, ngôn ngữ | "Tiếng Việt, professional, numbered steps, không filler phrases" |
| **Project Instructions** | Scope, terminology, templates, standards | "SOP theo chuẩn IEC 82079-1, dùng glossary công ty, 10 sections chuẩn" |

**Cách setup:**

1. Vào Project → Project Instructions: thêm scope rules, terminology, templates chuẩn
2. Vào Settings → Styles: tạo Custom Style cho tone và format
3. Khi làm việc trong Project: chọn Style phù hợp — Project Instructions tự động áp dụng

**Ví dụ thực tế:**

```text
Project Instructions (Project "AMR Documentation"):
- Mọi SOP theo 10 sections chuẩn (Purpose, Scope, ..., Change Log)
- Glossary: AMR = Autonomous Mobile Robot, PLC = ...
- Safety warnings theo ANSI Z535: trước bước nguy hiểm, không sau
- Cross-reference format: "Xem SOP-XXX, Mục Y"

Style "Phenikaa-X Technical":
- Tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh
- Tone: Professional, direct, actionable
- Format: Numbered steps, headings rõ ràng
- Không filler phrases
```

Khi viết SOP trong Project này với Style "Technical", Claude tự động áp dụng cả hai lớp — bạn chỉ cần nói "Viết SOP bảo trì cho AMR-003" mà không cần lặp lại conventions.

### Per-task Style Switching

[Ứng dụng Kỹ thuật]

Trong cùng một session, bạn có thể chuyển style giữa các tasks mà không cần tạo conversation mới. Workflow:

```text
Task 1 — Viết SOP (Style: Technical)
  → Output: professional, numbered steps, formal

Chuyển Style → "Internal Communication"

Task 2 — Viết email thông báo SOP mới (Style: Internal)
  → Output: thân thiện, bullet points, ngắn gọn

Chuyển Style → "Client-facing"

Task 3 — Viết release note cho khách hàng (Style: Client-facing)
  → Output: polished, highlight benefits, không jargon nội bộ
```

**Cách chuyển:** Settings > Styles > chọn style khác. Claude áp dụng ngay từ message tiếp theo.

> [!TIP] Chuyển style phù hợp khi đổi loại output — không cần tạo conversation mới mỗi lần.

### Team Style Library

[Ứng dụng Kỹ thuật]

Khi team có nhiều người cùng viết tài liệu, chuẩn hóa styles giúp output nhất quán. Cách xây dựng:

**Bước 1: Xác định 3-4 output types chính của team.**

| Output type | Ví dụ | Style cần |
|-------------|-------|-----------|
| Technical docs | SOP, specs, manuals | Formal, structured, actionable |
| Internal comms | Email, Slack, meeting notes | Concise, friendly, clear action items |
| Client-facing | Release notes, proposals | Polished, benefit-focused, professional |
| Training | Guides, tutorials | Explanatory, step-by-step, supportive |

**Bước 2: Tạo Custom Style cho mỗi output type.** Upload 1-2 writing samples tốt nhất của team làm reference. Claude sẽ học tone, structure, vocabulary từ samples.

**Bước 3: Chia sẻ instructions dạng text.** Custom Styles hiện tại là per-account — chưa có tính năng share trực tiếp giữa accounts. Workaround: lưu style instructions vào shared doc (Notion, Confluence, hoặc file trong repo), mỗi thành viên copy vào account của mình.

> [!NOTE] Custom Styles là tính năng per-account trên Claude.ai. Kiểm tra tính khả dụng của team sharing tại support.anthropic.com nếu feature set thay đổi. [Cập nhật 03/2026]

### Style cho Claude Code (Cowork)

Khi dùng Claude trong Cowork (Projects), Style hoạt động song song với Project Instructions:

- **Project Instructions** = CLAUDE.md trong Claude Code — scope, rules, conventions
- **Style** = cách Claude trả lời — tone, format, độ dài

Nếu dự án cần output format rất cụ thể (ví dụ: mọi output phải theo Markdown, headings 3 cấp, code blocks có language tag), đặt rules đó vào Project Instructions thay vì Style. Style nên focus vào tone và communication preferences.

**Xem thêm:** [Prompt Format Guide](../reference/prompt-format-guide.md) — khi nào dùng XML tags vs brackets trong prompt, áp dụng cho mọi style.

---

← [Claude Code Doc](05-claude-code-doc.md) | [Tổng quan](../base/00-overview.md)
