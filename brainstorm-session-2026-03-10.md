# Brainstorm Session — 2026-03-10

> Handoff document — capture toàn bộ bức tranh và vấn đề từ session brainstorm.
> Dùng để tiếp tục trao đổi ở session sau mà không mất context.
> **Cập nhật lần cuối:** Session 3 (2026-03-10)

---

## 1. Bối cảnh — Tại sao có dự án này

- **Đạt** bắt đầu tiếp cận AI từ zero — quá nhiều thông tin, hầu hết tiếng Anh, không biết bắt đầu từ đâu
- Xây Guide Claude ban đầu cho **bản thân**: tra cứu tiếng Việt, copy-paste workflows, xử lý công việc lặp nhanh hơn
- Sau đó nhận ra nhiều người xung quanh cũng cần — muốn chia sẻ, giúp tiếp cận AI dễ hơn
- Nhưng thực tế: **mọi người ngại đọc tài liệu dài**
- Nhận ra giá trị thực nằm ở **công cụ hỗ trợ** (configs, profiles, skills) hơn là prose

### Thực tế hàng ngày (Session 3)
- Hầu hết thời gian hiện tại: **làm việc với DOC** (documentation)
- Các hoạt động chính: brainstorming, capture kiến thức, đặt SOT đầu tiên, xây quy trình làm việc với Claude Code
- Nhìn thấy tiềm năng AI: Claude = đồng nghiệp, giảm khối lượng, scale hiệu suất
- Mục tiêu sau: dùng thành tựu đã xây → áp dụng cho anh em team khác (có thể ở nhóm chuyên môn khác)
- Vai trò giống **BA** — cầu nối giữa AI capability và nhu cầu team (không thiên kiến vào label này)

---

## 2. Vision tổng thể

### Mục tiêu cuối cùng
Số hóa kiến thức, quy trình, tiêu chuẩn → AI có đủ context → trợ thủ đắc lực → scale cho team/công ty.

### Triết lý xây dựng
> Chia nhỏ thành đơn vị nhỏ nhất, xây trên nền chân lý đã xác thực → kế thừa, compose, scale.

### Nguyên tắc bổ sung (Session 2)
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

### 3.2. Vòng lặp "build rồi rebuild"
```
Có ý tưởng → làm phần nhỏ với Claude → xong, thấy ổn
  → nhìn lại bức tranh lớn → không khớp
    → đập đi xây lại → lặp lại
```

Lịch sử rebuild Guide Claude:
- v1→v7: xây content, không xác định rõ hướng từ đầu → phình to, khó kiểm soát
- v7→v9: tái cấu trúc 3-tier (33 sessions, 5 phases)
- Đang cân nhắc v10: đổi kiến trúc lần nữa (3-tier → 4-part)

**Đạt xác nhận:** sai lầm lớn nhất là lần đầu — không xác định rõ từ đầu, dẫn đến mọi thứ sau phải tái cấu trúc.

### 3.3. Painpoints cụ thể
| Vấn đề | Biểu hiện |
|---------|----------|
| Chưa rõ mục tiêu trước khi làm | Lan man, cầu toàn, không biết "thế nào là done" |
| Diễn đạt chưa chính xác | Khả năng ngữ văn hạn chế, AI hiểu khác ý |
| Không biết kết quả đúng hay sai | Nghi ngờ output AI, dựa vào standards/best practices nhờ AI đánh giá nhưng chưa hiệu quả |
| Context bị trôi qua sessions | AI bị lạc đề, mất hướng khi session dài hoặc sang session mới |
| Nội dung quá nhiều | Rules/standards dài → AI bỏ qua, không hiệu quả |
| Memory management chưa tốt | Chưa biết quản lý memory đủ tốt |
| Chuyển session không nhất quán | Mỗi lần chuyển session làm 1 kiểu, không có quy trình chuẩn |
| Chọn SOT khó khi chưa có kinh nghiệm | Trăm ngàn framework — chọn sai từ đầu thì mọi thứ lệch |
| Bị cuốn theo official/community updates | Chạy theo cập nhật trên mạng, thiếu tiêu chí lọc nội tại |
| Không biết làm thế nào cho đúng với Claude | Mỗi lần làm việc thấy 1 việc khác nhau |

### 3.4. Scaffold thất bại — nguyên nhân gốc
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
- Đạt đang dùng nó để học cách làm việc với AI
- Thử nghiệm quy trình xây dựng knowledge base
- Xây tools/infra có thể reuse cho các domain khác

### AMR-T800 Hub — không phải dự án điển hình
- Đã tạo skeleton nhưng Đạt xác nhận đây không phải dự án điển hình
- Có thể loại bỏ khỏi scope brainstorm này

### Painpoints AMR-T800 team trùng khớp painpoints cá nhân
| AMR-T800 (team) | Đạt + Claude (cá nhân) |
|---|---|
| No Product Definition — chưa rõ T800 "là gì, làm gì" | Chưa rõ mục tiêu trước khi làm |
| Information Silos — mỗi nhóm tự hiểu khác | Context trôi qua sessions |
| No Quality Process — không ai test | Không biết kết quả đúng hay sai |
| Knowledge Gap — thiếu kiến thức | Chưa đủ kinh nghiệm chọn SOT |

→ Methodology xây cho bản thân có thể áp dụng được cho team — vì gốc vấn đề giống nhau.

### Bản chất công việc thực tế của Đạt (Session 3)
Bỏ qua labels — anh đang làm **chuyển hóa kiến thức**:

```
Tìm hiểu → Chọn lọc → Đóng gói → Chuyển giao
  (đọc, nghiên cứu)  (giữ gì, bỏ gì)  (doc, tool)  (cho team)
```

Đang kẹt ở **Chọn lọc + Đóng gói** — thiếu tiêu chí đánh giá và feedback loop.

---

## 7. Đánh giá .claude hiện tại (Session 2)

### Đã tốt: kiểm soát chất lượng tài liệu
- 7 rules auto-load theo context
- Hook format-check.py sau mỗi Edit/Write
- 9 skills cho document maintenance
- `/start` và `/session-start` cho orientation

### Thiếu hoàn toàn: kiểm soát chất lượng tư duy

| Có (format/output) | Thiếu (thinking/direction) |
|---|---|
| Heading hierarchy đúng | "Cái này có khớp bức tranh lớn không?" |
| Link không broken | "Nên làm cái này hay không?" |
| Source có marker | "Mục tiêu session này nằm ở đâu trong tổng thể?" |
| Format check auto | Handoff context chuẩn giữa sessions |

### Vấn đề cụ thể
- **Global CLAUDE.md gần như trống** — chỉ có emoji rules, không có workflow/methodology instructions
- **Không có bức tranh tổng thể** dưới dạng văn bản mà Claude đọc được mỗi session
- **Không có handoff protocol** cho brainstorm sessions
- **Không có "thinking check"** — chỉ có "format check"

### Pattern nguy hiểm: optimize công cụ thay vì giải quyết gốc
1. Lần 1: Xây content → phình to
2. Lần 2: Restructure 3-tier → kiến trúc vẫn chưa đúng vision
3. Lần 3: Infrastructure hardening → vẫn gặp vòng lặp rebuild
4. Lần 4 (nếu tiếp tục optimize Claude Code setup) → nguy cơ lặp lại

---

## 8. Phản biện các đề xuất (Session 3 — critical analysis)

### 8.1. Phản biện "North Star document"
- Nếu Đạt biết viết gì vào North Star → đã không gặp vấn đề
- Nếu Claude giúp viết → có thể tạo ra thứ "nghe hay nhưng không đúng ý" (đúng pattern painpoint)
- **Lời khuyên vòng tròn:** "giải quyết vấn đề bằng cách giải quyết vấn đề"

### 8.2. Phản biện "4 thói quen"
- 4 thói quen IS a framework — vừa được nghĩ ra trong session, chưa ai kiểm chứng
- Đang làm đúng cái khuyên đừng làm: tạo thứ mới thay vì dùng thứ đã có
- Chưa có bằng chứng hoạt động

### 8.3. Phản biện "sổ bài học"
- Giả định anh biết mình đã học gì — nhưng painpoint cốt lõi là không biết đúng/sai cho đến nhiều tuần sau
- Ghi sớm → có thể ghi sai. Ghi muộn → quên chi tiết
- Ví dụ: "scaffold thất bại" — thật sự scaffold kém, hay cách thiết kế scaffold kém? Hai kết luận rất khác

### 8.4. Claude có thể là một phần của vấn đề
- Claude mỗi session khác nhau — đồng ý và mở rộng theo hướng khác tùy cách diễn đạt
- Anh diễn đạt hơi khác → Claude đề xuất khác → kết quả không nhất quán
- Không rõ bao nhiêu sự "không nhất quán" là do anh, bao nhiêu do Claude

### 8.5. Thêm structure = thêm gánh nặng
- Painpoint: "rules/standards dài → AI bỏ qua"
- Thêm North Star + sổ bài học + inbox + handoff protocol = THÊM content cho Claude xử lý
- Có thể làm vấn đề tệ hơn

### 8.6. "Người khổng lồ" có thể chưa tồn tại
- Bài toán cụ thể: "1 kỹ sư robotics VN + Claude = số hóa kiến thức cho team nhỏ"
- Gần như không ai đã giải và chia sẻ giải pháp cho bài toán này
- Các framework knowledge management (Diátaxis, DACI, Zettelkasten...) thiết kế cho context khác
- Anh có thể đang ở **vùng chưa có đường mòn**

### 8.7. Vấn đề tự tham chiếu (self-referential)
- Dùng Claude để xây quy trình làm việc với Claude
- Dùng documentation để xây quy trình documentation
- Brainstorm về cách brainstorm
- Mỗi lần học → cái cũ cần cập nhật → vòng lặp ở tầng meta
- **Đây là bản chất, không phải bug** — câu hỏi đúng không phải "làm sao để xong" mà "làm sao để cái chưa xong vẫn có giá trị"

### 8.8. Thiếu feedback loop — có thể là nguyên nhân gốc sâu nhất
```
Build → xong → không ai dùng (chưa share cho team)
  → Không có feedback từ người dùng thật
    → Không biết cái nào hoạt động
      → Dùng tiêu chuẩn bên ngoài (official, community) thay cho feedback thật
        → Tiêu chuẩn bên ngoài không khớp context → rebuild
```

### 8.9. Session brainstorm này có phải vòng lặp?
- 3 sessions brainstorm về methodology mà chưa thử áp dụng gì
- Paralysis by analysis — phân tích nhiều, cảm giác tiến bộ, nhưng chưa thay đổi gì thực tế
- Cần cảnh giác: đến lúc nào thì dừng phân tích và bắt đầu thử?

---

## 9. 3 mâu thuẫn cốt lõi chưa giải quyết (Session 3)

### Mâu thuẫn 1: Hoàn thiện trước vs cần feedback để hoàn thiện
- Muốn: xây xong đàng hoàng → mới cho team dùng
- Thực tế: không có feedback từ team → không biết "đàng hoàng" trông thế nào
- Build trong chân không → tiêu chuẩn đánh giá chỉ từ bên ngoài hoặc từ chính mình

### Mâu thuẫn 2: Muốn ổn định vs bản chất thay đổi liên tục
- Muốn: SOT ổn định, quy trình lặp lại, kết quả nhất quán
- Thực tế: AI thay đổi nhanh, kiến thức đang phát triển, yêu cầu team sẽ khác đi
- Càng cố ổn định → càng phải rebuild khi thực tế thay đổi

### Mâu thuẫn 3: Đứng trên vai người khổng lồ vs bài toán chưa có ai giải
- Muốn: tận dụng framework, best practices đã kiểm chứng
- Thực tế: bài toán cụ thể này gần như chưa có giải pháp đóng gói sẵn
- "Người khổng lồ" có thể chưa tồn tại cho trường hợp này

---

## 10. Câu hỏi cần trả lời — Session tiếp theo

### Câu hỏi hiểu thực tế (chưa được trả lời)
1. Khi mở Claude lên, điều đầu tiên anh thường nói/làm là gì?
2. Khi nào anh cảm thấy session hiệu quả? Có session nào nhớ là "hôm đó làm tốt"?
3. "Mỗi lần khác nhau" — cụ thể khác ở đâu? Ví dụ 2-3 lần?
4. Đã bao giờ cho ai dùng thử kết quả chưa? Phản hồi thế nào?
5. Bao nhiêu thời gian thực tế mỗi tuần cho việc này?

### Câu hỏi chiến lược (cần phân tích tiếp)
6. Rebuild có thật sự xấu — hay vấn đề là rebuild quá đắt? Nếu rebuild rẻ thì sao?
7. "Đúng" cho anh nghĩa là gì — theo official, hay theo context cụ thể?
8. Khi nào thì dừng phân tích và bắt đầu thử?
9. Có thể lấy feedback sớm từ 1-2 người thay vì chờ hoàn thiện?

---

> [!NOTE]
> Đây là tài liệu brainstorm — không phải kế hoạch thực thi.
> Mọi quyết định cần confirm trước khi triển khai.
> **Session tiếp theo:** đọc file này, brainstorm tiếp từ mục 10.
