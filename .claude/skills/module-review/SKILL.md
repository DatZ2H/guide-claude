---
name: module-review
description: Checklist review một module trong Guide Claude project theo 5 tiêu chí chất lượng. Trigger khi user nói "review module X", "kiểm tra module", "đánh giá chất lượng module", hoặc trước khi bump version. Output: review report với điểm số và action items.
user-invocable: true
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
---

# Module Review Workflow — Guide Claude Project

Skill này cung cấp structured review cho từng module, đảm bảo chất lượng nhất quán trước khi release.

## Trigger

Kích hoạt khi user:
- Nói "review module [số/tên]", "đánh giá module", "kiểm tra chất lượng"
- Chuẩn bị bump version (chạy cho từng module thay đổi)
- Hoàn thành viết/sửa một module và muốn QA

## Quy trình

### Bước 1 — Xác định module

Hỏi user module nào cần review (nếu chưa rõ). Đọc file `guide/{base,doc,dev}/[XX]-[tên].md` đầy đủ.

Cũng đọc:
- `VERSION` — version hiện tại
- `git log --oneline -10` — xem có changes nào ảnh hưởng module này không

### Bước 2 — Đánh giá theo 5 tiêu chí

#### 1. Accuracy (Chính xác)
- Thông tin về Claude features có đúng không? (models, context window, tính năng)
- Source markers `[Nguồn: ...]` có đầy đủ cho claims quan trọng không?
- Có thông tin nào có thể đã outdated không?
- Flag: thông tin không có source mà nên có

#### 2. Consistency (Nhất quán)
- Terminology nhất quán trong module (ví dụ: "Cowork" không lẫn với "Claude Desktop Cowork mode")
- Version references: không hardcode, dùng link `VERSION` hoặc "xem VERSION"
- Format conventions: `[Nguồn: ...]`, `[Ứng dụng Kỹ thuật]`, `[Cập nhật MM/YYYY]` dùng đúng
- Language: tiếng Việt + thuật ngữ kỹ thuật tiếng Anh

#### 3. Completeness (Đầy đủ)
- Module có đủ nội dung theo mục lục trong 00-overview.md không?
- Có section nào có `[TBD]` hoặc placeholder chưa fill không?
- Cross-references đến modules khác có đủ không?

#### 4. Clarity (Rõ ràng)
- Có đoạn nào quá dài (>5 câu liên tục) không có break không?
- Examples và ví dụ thực tế có đủ không (tối thiểu 1 ví dụ Phenikaa-X context)?
- Có thuật ngữ introduce lần đầu mà chưa giải thích không?

#### 5. Actionability (Có thể áp dụng ngay)
- Prompts và templates có thể copy-paste không (đủ `{{placeholder}}` rõ ràng)?
- Kỹ sư mới có thể follow instructions không cần context thêm không?
- Có "anti-patterns" hoặc "CẢNH BÁO" khi cần không?

### Bước 3 — Output review report

Format cố định (thống nhất với `/review-module` command — hệ thống /10):

```
## Review: [filename] ([size]KB)

**Score: [tổng]/10**

| Tiêu chí | Điểm | Ghi chú |
|----------|-------|---------|
| Accuracy | 0-2 | [nhận xét ngắn] |
| Consistency | 0-2 | [nhận xét ngắn] |
| Completeness | 0-2 | [nhận xét ngắn] |
| Clarity | 0-2 | [nhận xét ngắn] |
| Actionability | 0-2 | [nhận xét ngắn] |

### Strengths
- [2-3 điểm mạnh]

### Issues
- L[line]: [mô tả cụ thể]

### Suggestions
- [2-3 đề xuất cải thiện, ưu tiên theo impact]
```

Quy ước điểm: 0 = thiếu/sai nghiêm trọng, 1 = có nhưng cần cải thiện, 2 = tốt.

### Bước 4 — Hỏi action

"Anh muốn tôi fix ngay các 'Must fix' items không?"

## Rules

- Đánh giá khách quan — không nói "tốt" chung chung mà phải chỉ ra cụ thể
- Score phải reflect thực tế — KHÔNG cho điểm cao vô căn cứ
- Nếu module quá dài (>40KB), chia làm 2 lần đọc: nửa đầu và nửa sau
- Không sửa file trực tiếp trong bước review — chỉ report
- Phân biệt "sai" (accuracy issue) vs "có thể cải thiện" (clarity issue)
- Issues PHẢI có line reference cụ thể
- Suggestions phải actionable — "thêm ví dụ X vào section Y", không phải "cải thiện ví dụ"
- Tổng output tối đa 30 dòng
