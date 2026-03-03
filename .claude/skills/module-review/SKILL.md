---
name: module-review
description: Checklist review một module trong Guide Claude project theo 5 tiêu chí chất lượng. Trigger khi user nói "review module X", "kiểm tra module", "đánh giá chất lượng module", hoặc trước khi bump version. Output: review report với điểm số và action items.
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

Hỏi user module nào cần review (nếu chưa rõ). Đọc file `guide/[XX]-[tên].md` đầy đủ.

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

Format cố định:

```
## Module Review — [XX] [Tên Module] — [ngày]

### Tóm tắt
- Điểm tổng: [X/5] tiêu chí PASS
- Trạng thái: ✅ Ready to release | ⚠️ Minor fixes needed | 🔴 Major issues

### Kết quả từng tiêu chí

| Tiêu chí | Kết quả | Ghi chú |
|----------|---------|---------|
| Accuracy | ✅/⚠️/🔴 | [nhận xét ngắn] |
| Consistency | ✅/⚠️/🔴 | [nhận xét ngắn] |
| Completeness | ✅/⚠️/🔴 | [nhận xét ngắn] |
| Clarity | ✅/⚠️/🔴 | [nhận xét ngắn] |
| Actionability | ✅/⚠️/🔴 | [nhận xét ngắn] |

### Action Items

**Must fix (trước release):**
1. [file:dòng] — [vấn đề] → [fix cụ thể]

**Should fix (sprint này):**
1. [file:dòng] — [vấn đề] → [gợi ý]

**Nice to have:**
1. [gợi ý cải thiện]
```

### Bước 4 — Hỏi action

"Anh muốn tôi fix ngay các 'Must fix' items không?"

## Rules

- Đánh giá khách quan — không nói "tốt" chung chung mà phải chỉ ra cụ thể
- Nếu module quá dài (>40KB), chia làm 2 lần đọc: nửa đầu và nửa sau
- Không sửa file trực tiếp trong bước review — chỉ report
- Phân biệt "sai" (accuracy issue) vs "có thể cải thiện" (clarity issue)
- Luôn ghi rõ dòng số khi flag issue cụ thể
