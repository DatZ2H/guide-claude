# Brainstorm Session — 2026-03-10

> Handoff document — capture toàn bộ bức tranh và vấn đề từ session brainstorm.
> Dùng để tiếp tục trao đổi ở session sau mà không mất context.

---

## 1. Bối cảnh — Tại sao có dự án này

- **Đạt** bắt đầu tiếp cận AI từ zero — quá nhiều thông tin, hầu hết tiếng Anh, không biết bắt đầu từ đâu
- Xây Guide Claude ban đầu cho **bản thân**: tra cứu tiếng Việt, copy-paste workflows, xử lý công việc lặp nhanh hơn
- Sau đó nhận ra nhiều người xung quanh cũng cần — muốn chia sẻ, giúp tiếp cận AI dễ hơn
- Nhưng thực tế: **mọi người ngại đọc tài liệu dài**
- Nhận ra giá trị thực nằm ở **công cụ hỗ trợ** (configs, profiles, skills) hơn là prose

---

## 2. Vision tổng thể

### Mục tiêu cuối cùng
Số hóa kiến thức, quy trình, tiêu chuẩn → AI có đủ context → trợ thủ đắc lực → scale cho team/công ty.

### Triết lý xây dựng
> Chia nhỏ thành đơn vị nhỏ nhất, xây trên nền chân lý đã xác thực → kế thừa, compose, scale.

### Phạm vi không chỉ Guide Claude
```
Kiến thức cần số hóa:
├── Cách làm việc với AI           ← Guide Claude (đang làm)
├── Quy trình viết tài liệu       ← Cần xây
├── Tiêu chuẩn kỹ thuật nội bộ    ← Cần xây
├── Quy trình thiết kế             ← Cần xây
├── Kinh nghiệm đúc kết           ← Cần xây
├── Tips, tricks, best practices   ← Cần xây
└── Onboarding cho người mới       ← Cần xây
```

### Đảm bảo xuyên suốt
- Kết quả đồng nhất (không mỗi lần một kiểu)
- Dễ tiếp cận (không cần chuyên gia AI)
- Dễ bảo trì (tách knowledge, update 1 chỗ)
- AI như đồng nghiệp (config context sẵn)

### Scale path
```
Cá nhân (Đạt) → Team (Solution, Software) → Công ty (PNX) → Chia sẻ
```

---

## 3. Painpoints thực tế (từ chính Đạt)

### 3.1. Vòng xoáy khi làm việc với AI
```
Chưa rõ mình muốn gì
  → Diễn đạt chưa rõ cho AI
    → AI trả lời nghe hay nhưng không đúng ý
      → Nghi ngờ, thêm rules/standards để kiểm soát
        → Quá nhiều nội dung, AI bỏ qua
          → Kết quả vẫn chưa ưng
            → Cảm giác "không kiểm soát được AI"
```

### 3.2. Painpoints cụ thể
| Vấn đề | Biểu hiện |
|---------|----------|
| Chưa rõ mục tiêu trước khi làm | Lan man, cầu toàn, không biết "thế nào là done" |
| Diễn đạt chưa chính xác | Khả năng ngữ văn hạn chế, AI hiểu khác ý |
| Không biết kết quả đúng hay sai | Nghi ngờ output AI, dựa vào standards/best practices nhờ AI đánh giá nhưng chưa hiệu quả |
| Context bị trôi qua sessions | AI bị lạc đề, mất hướng khi session dài hoặc sang session mới |
| Nội dung quá nhiều | Rules/standards dài → AI bỏ qua, không hiệu quả |
| Memory management chưa tốt | Chưa biết quản lý memory đủ tốt |

### 3.3. Scaffold thất bại — nguyên nhân gốc
- Scaffold thiết kế cho người **đã biết cách** — không giúp được người bắt đầu từ zero
- Giống đưa xe đạp cho người chưa biết giữ thăng bằng
- Khi mang sang AMR-T800: gượng gạo, không hiệu quả vì thiếu guided journey từ ý tưởng → triển khai

---

## 4. Phân tích v9.1 — cái gì giữ, cái gì không

### Còn giá trị cao (~60% content)
- Prompt engineering (base/03) — nguyên lý stable
- Evaluation framework (base/07) — framework ổn định
- Anti-patterns (base/06) — bài học thực tế
- Doc workflows (doc/) — quy trình viết tài liệu
- Infrastructure (.claude/) — skills, hooks, rules đã hardened

### Cần restructure
- Context management, tools & features — trộn lẫn knowledge và hướng dẫn
- Dev workflows — chưa kết nối với thực hành

### Giá trị thấp
- Feature specs rải rác 6 files — stale, trùng lặp
- Một số reference files chỉ dịch lại official docs
- Scaffold hiện tại — cần thiết kế lại

### Kết luận
Content phần lớn vẫn dùng được, nhưng **kiến trúc** (3-tier theo audience) không phù hợp với vision mới (4-part theo chức năng).

---

## 5. Hệ thống mong muốn — 4 phần

| Phần | Vai trò | Đặc điểm |
|------|---------|----------|
| **Knowledge** | Kiến thức nền, SSOT | Stable concepts, feature specs — update 1 chỗ |
| **Guide** | Sách tham khảo chuẩn tiếng Việt | Gọn, dễ tra, ví dụ thực tế, đáng tin |
| **Công cụ** | Framework thực hành | Configs, profiles, skills, hooks — hỗ trợ từ zero |
| **Ví dụ thực tế** | Trích từ dự án + profile thực | AMR-T800, Guide Claude — minh họa trực quan |

---

## 6. Phát hiện quan trọng nhất

### Guide Claude là dự án pilot, không phải sản phẩm cuối
- Anh đang dùng nó để học cách làm việc với AI
- Thử nghiệm quy trình xây dựng knowledge base
- Xây tools/infra có thể reuse cho các domain khác

### Vấn đề cần giải quyết TRƯỚC TIÊN
Không phải "v10 có bao nhiêu files" mà là:

> **Xây dựng một methodology giúp Đạt + AI cùng nhau biến kiến thức rời rạc thành tài liệu/công cụ chuẩn — bắt đầu từ zero, cho ra kết quả nhất quán, kiểm soát được.**

Methodology này là **nền móng chung** cho mọi thứ: Guide Claude, tiêu chuẩn kỹ thuật, onboarding, v.v.

### Vấn đề chưa giải — cần brainstorm tiếp
- Methodology đó cụ thể gồm những gì?
- Làm thế nào để AI giúp hoàn thành khi chính anh chưa biết cách?
- Bắt đầu từ đâu khi mọi thứ đều cần?

---

## 7. Session tiếp theo cần làm gì

1. **Brainstorm methodology** — quy trình "từ kiến thức rời → sản phẩm chuẩn" với AI
2. **Thử áp dụng** methodology đó vào 1 phần nhỏ cụ thể (ví dụ: 1 module guide, hoặc 1 tiêu chuẩn kỹ thuật)
3. **Đánh giá kết quả** — methodology có giải quyết được vòng xoáy painpoints không?
4. **Rồi mới** quay lại thiết kế kiến trúc v10

---

> [!NOTE]
> Đây là tài liệu brainstorm — không phải kế hoạch thực thi.
> Mọi quyết định cần confirm trước khi triển khai.
