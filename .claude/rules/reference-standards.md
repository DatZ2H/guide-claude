---
paths:
  - "guide/reference/**"
---

# Reference Standards — Guide Claude Project

Rules bổ sung cho files trong guide/reference/. Load cùng writing-standards.md.

## Reference File Rules

- Reference files là tra cứu nhanh — ưu tiên dạng bảng, danh sách hơn đoạn văn dài
- Mỗi entry phải self-contained — reader không cần đọc module khác để hiểu
- Link ngược đến module liên quan: `Xem chi tiết: [Module X](../guide/XX-name.md#section)`
- Giữ format nhất quán trong cùng 1 file (nếu bảng thì toàn bảng, nếu list thì toàn list)

## Skills List Specific

- Mỗi skill entry CẦN: tên, mô tả ngắn, trigger keywords, trust level
- Phân nhóm rõ: Pre-built / Official Standalone / Official Plugins / Community / Project
- Community skills: ghi nguồn repo + disclaimer

## Config Architecture Specific

- Ưu tiên file structure visual (tree diagram)
- Ghi rõ precedence order khi có config overlap
- Mỗi config key: kiểu dữ liệu, default, ví dụ
