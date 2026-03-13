# Brainstorm — 2026-03-10 (Sessions 1-3)

> Ghi lại ý tưởng và phương hướng của Đạt qua 3 sessions brainstorm.

---

## 1. Bối cảnh — Tại sao có dự án này

- Bắt đầu tiếp cận AI từ zero — quá nhiều thông tin tiếng Anh, không biết bắt đầu từ đâu
- Xây Guide Claude ban đầu cho bản thân: tra cứu tiếng Việt, copy-paste workflows
- Sau đó nhận ra nhiều người xung quanh cũng cần — muốn chia sẻ
- Thực tế: mọi người ngại đọc tài liệu dài
- Giá trị thực nằm ở **công cụ hỗ trợ** (configs, profiles, skills) hơn là prose

### Thực tế hàng ngày

- Hầu hết thời gian: **làm việc với DOC** (documentation)
- Các hoạt động chính: brainstorming, capture kiến thức, đặt SOT đầu tiên, xây quy trình làm việc với Claude Code
- Nhìn thấy tiềm năng: Claude = đồng nghiệp, giảm khối lượng, scale hiệu suất
- Mục tiêu sau: dùng thành tựu đã xây → áp dụng cho anh em team khác
- Vai trò giống **BA** — cầu nối giữa AI capability và nhu cầu team

---

## 2. Vision tổng thể

### Mục tiêu cuối cùng

Số hóa kiến thức, quy trình, tiêu chuẩn → AI có đủ context → trợ thủ đắc lực → scale cho team/công ty.

### Triết lý

> Chia nhỏ thành đơn vị nhỏ nhất, xây trên nền chân lý đã xác thực → kế thừa, compose, scale.

### Nguyên tắc

- **Đứng trên vai người khổng lồ** — tận dụng SOT uy tín, không tự sáng tạo khi đã có cái tốt
- Nhưng phải **phù hợp**, không gượng ép
- Ưu tiên: Claude built-in → best practices cộng đồng → framework có tên
- Dần dần **tạo SOT riêng** cho PNX / team / cá nhân
- Kiểm soát chất lượng chặt — hạn chế hiệu ứng cánh bướm (sai nhỏ → lệch lớn)

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

## 3. Painpoints thực tế

### Vòng xoáy khi làm việc với AI

```
Chưa rõ mình muốn gì
  → Diễn đạt chưa rõ cho AI
    → AI trả lời nghe hay nhưng không đúng ý
      → Nghi ngờ, thêm rules/standards để kiểm soát
        → Quá nhiều nội dung, AI bỏ qua
          → Kết quả vẫn chưa ưng
            → Cảm giác "không kiểm soát được AI"
```

### Vòng lặp "build rồi rebuild"

```
Có ý tưởng → làm phần nhỏ với Claude → xong, thấy ổn
  → nhìn lại bức tranh lớn → không khớp
    → đập đi xây lại → lặp lại
```

Lịch sử rebuild Guide Claude:
- v1→v7: xây content, không xác định rõ hướng từ đầu → phình to, khó kiểm soát
- v7→v9: tái cấu trúc 3-tier (33 sessions, 5 phases)
- Đang cân nhắc v10: đổi kiến trúc lần nữa

**Sai lầm lớn nhất:** lần đầu không xác định rõ từ đầu → mọi thứ sau phải tái cấu trúc.

### Painpoints cụ thể

| Vấn đề | Biểu hiện |
|---------|----------|
| Chưa rõ mục tiêu trước khi làm | Lan man, cầu toàn, không biết "thế nào là done" |
| Diễn đạt chưa chính xác | Khả năng ngữ văn hạn chế, AI hiểu khác ý |
| Không biết kết quả đúng hay sai | Nghi ngờ output AI, dựa vào standards nhờ AI đánh giá nhưng chưa hiệu quả |
| Context bị trôi qua sessions | AI bị lạc đề, mất hướng khi session dài hoặc sang session mới |
| Nội dung quá nhiều | Rules/standards dài → AI bỏ qua, không hiệu quả |
| Memory management chưa tốt | Chưa biết quản lý memory đủ tốt |
| Chuyển session không nhất quán | Mỗi lần chuyển session làm 1 kiểu, không có quy trình chuẩn |
| Chọn SOT khó | Trăm ngàn framework — chọn sai từ đầu thì mọi thứ lệch |
| Bị cuốn theo updates | Chạy theo cập nhật trên mạng, thiếu tiêu chí lọc nội tại |
| Không biết cách đúng với Claude | Mỗi lần làm việc thấy 1 kiểu khác nhau |

### Scaffold thất bại — nguyên nhân gốc

- Scaffold thiết kế cho người **đã biết cách** — không giúp người bắt đầu từ zero
- Giống đưa xe đạp cho người chưa biết giữ thăng bằng
- Khi mang sang AMR-T800: gượng gạo, không hiệu quả vì thiếu guided journey

---

## 4. Hệ thống mong muốn — 4 phần

| Phần | Vai trò | Đặc điểm |
|------|---------|----------|
| **Knowledge** | Kiến thức nền, SSOT | Stable concepts, feature specs — update 1 chỗ |
| **Guide** | Sách tham khảo chuẩn tiếng Việt | Gọn, dễ tra, ví dụ thực tế, đáng tin |
| **Công cụ** | Framework thực hành | Configs, profiles, skills, hooks — hỗ trợ từ zero |
| **Ví dụ thực tế** | Trích từ dự án + profile thực | AMR-T800, Guide Claude — minh họa trực quan |

---

## 5. Nhận định quan trọng

- **Guide Claude là dự án pilot**, không phải sản phẩm cuối — đang dùng để học cách làm việc với AI, thử nghiệm quy trình, xây tools reuse
- **AMR-T800 Hub không phải dự án điển hình** — loại khỏi scope brainstorm
- Painpoints team (AMR-T800) trùng painpoints cá nhân → methodology xây cho bản thân có thể áp dụng cho team
- Bản chất công việc: **chuyển hóa kiến thức** (Tìm hiểu → Chọn lọc → Đóng gói → Chuyển giao) — đang kẹt ở Chọn lọc + Đóng gói

---

## 6. Đánh giá v9.1

### Còn giá trị cao (~60%)

- Prompt engineering, Evaluation framework, Anti-patterns, Doc workflows
- Infrastructure (.claude/) — skills, hooks, rules đã hardened

### Cần restructure

- Context management, tools & features — trộn lẫn knowledge và hướng dẫn
- Dev workflows — chưa kết nối với thực hành

### Giá trị thấp

- Feature specs rải rác — stale, trùng lặp
- Một số reference files chỉ dịch lại official docs
- Scaffold hiện tại — cần thiết kế lại

### Kết luận

Content phần lớn vẫn dùng được, nhưng **kiến trúc** (3-tier theo audience) không phù hợp với vision mới (4-part theo chức năng).

---

## 7. Đánh giá .claude hiện tại

### Đã tốt: kiểm soát chất lượng tài liệu

- 7 rules auto-load, hook format-check.py, 9 skills, `/start` orientation

### Thiếu: kiểm soát chất lượng tư duy

| Có (format/output) | Thiếu (thinking/direction) |
|---|---|
| Heading hierarchy đúng | "Cái này có khớp bức tranh lớn không?" |
| Link không broken | "Nên làm cái này hay không?" |
| Source có marker | "Mục tiêu session này nằm ở đâu trong tổng thể?" |
| Format check auto | Handoff context chuẩn giữa sessions |

### Vấn đề cụ thể

- Global CLAUDE.md gần như trống — chỉ emoji rules, không có methodology
- Không có bức tranh tổng thể dưới dạng Claude đọc được
- Không có handoff protocol cho brainstorm sessions
- Không có "thinking check" — chỉ có "format check"

---

> [!NOTE]
> Đây là tài liệu brainstorm — không phải kế hoạch thực thi.
