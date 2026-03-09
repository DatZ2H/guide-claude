# Project Instructions Templates

Thư mục này chứa templates cho **claude.ai Project Instructions** — system prompt áp dụng cho tất cả conversations trong một Project.

> **Lưu ý về lớp cấu hình:** Project Instructions là lớp cấu hình cho claude.ai (web/app).
> Nếu bạn dùng **Claude Code** hoặc **Cowork**, xem `CLAUDE-template.md` thay thế (→ `.claude/CLAUDE.md`).
> Xem `guide/reference/config-architecture.md` để hiểu sự khác biệt giữa các lớp.

---

## Cách dùng

1. Mở claude.ai → Project cần cấu hình → Settings → Instructions
2. Chọn template phù hợp từ folder này
3. Copy phần giữa `---COPY START---` và `---COPY END---` → paste vào Instructions field
4. Thay tất cả `{{placeholder}}` bằng thông tin thật
5. Save

---

## Danh sách templates

| File | Dùng khi | Audience |
|------|----------|----------|
| `template-basic.md` | Bắt đầu từ đầu, chưa rõ dùng template nào | Mọi kỹ sư |
| `template-troubleshooting.md` | Project dành riêng cho debug/troubleshoot | Kỹ sư vận hành, R&D |
| `template-tech-doc.md` | Project viết tài liệu kỹ thuật | Technical Writer, Team Lead |
| `template-code-review.md` | Project review code ROS2/Python | Senior Engineer, Team Lead |

---

## Nguyên tắc viết Project Instructions tốt

**NÊN đặt vào đây:**
- Role của Claude trong project ("bạn là X tại Phenikaa-X")
- Context kỹ thuật cụ thể (tech stack, environment, audience)
- Output format rules
- Safety constraints

**KHÔNG đặt vào đây:**
- Tài liệu dài hơn 500 từ → dùng Project Knowledge
- Rules áp dụng tất cả projects → dùng Profile Preferences
- Workflow automation → không thể trong claude.ai Projects

**Giới hạn:** ~2,000–4,000 tokens. Nếu instructions quá dài, Claude có thể không follow hết phần cuối.

---

## Khi nào update template?

Templates này cần review khi:
- Claude thay đổi model hoặc capabilities lớn
- Tech stack của Phenikaa-X thay đổi (ROS version, sensor mới...)
- Team có feedback về template không fit workflow

Khi update template → **KHÔNG sửa guide modules** (base/02, doc/02...) trừ khi có thay đổi về khái niệm.
Templates và guide modules tách biệt để dễ maintain.
