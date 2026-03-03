# Module 01: Quick Start -- Bắt đầu với Claude trong 15 phút

**Thời gian đọc:** 15 phút | **Mức độ:** Beginner
**Cập nhật:** 2026-02-28 | Claude Opus 4.6 / Sonnet 4.6

---

Module này giúp bạn bắt đầu sử dụng Claude ngay lập tức. Không cần XML tags, không cần kỹ thuật nâng cao. Chỉ cần đăng nhập và làm theo 4 bước.

**Yêu cầu:** Tài khoản Claude.ai (Free hoặc Pro). Nếu chưa có, đăng ký tại https://claude.ai.

---

## Bước 1: Đăng nhập và giao diện (2 phút)

1. Truy cập https://claude.ai
2. Đăng nhập bằng email hoặc Google account
3. Bạn sẽ thấy giao diện chính:

```
  Sidebar (trái)         Khu vực chat (giữa)
  - Projects             - Ô nhập tin nhắn
  - Conversations        - Nút gửi
  - Search               - Search and tools
```

**Thử ngay:** Gõ vào ô chat: "Xin chào, bạn có thể giúp gì cho tôi?" và nhấn Enter.

---

## Bước 2: Năm prompts đầu tiên (8 phút)

Thử 5 prompts sau để làm quen. Copy-paste trực tiếp, thay thông tin trong ngoặc vuông.

### Prompt 1: Hỏi đáp nhanh

```
Giải thích ngắn gọn [khái niệm kỹ thuật] là gì.
Tôi là kỹ sư, không cần giải thích quá cơ bản.
```

**Ví dụ:** "Giải thích ngắn gọn SLAM là gì. Tôi là kỹ sư, không cần giải thích quá cơ bản."

### Prompt 2: Phân tích error

```
Tôi gặp lỗi sau trên [hệ thống]:

[paste error message hoặc log]

Nguyên nhân có thể là gì và cách fix?
```

**Ví dụ:** "Tôi gặp lỗi sau trên ROS2: 'Transform timeout: Could not find a connection between odom and base_link'. Nguyên nhân có thể là gì và cách fix?"

### Prompt 3: Viết email

```
Viết email ngắn gọn báo cáo tiến độ project [tên project] cho [người nhận].
Tiến độ: [X]%. Vấn đề: [mô tả]. Kế hoạch tuần tới: [mô tả].
Tone professional, tiếng Việt.
```

### Prompt 4: Tạo checklist

```
Tạo checklist kiểm tra trước khi vận hành [thiết bị].
Chia theo nhóm: Hardware, Software, Safety.
Mỗi item có tiêu chí pass/fail rõ ràng.
```

### Prompt 5: So sánh giải pháp

```
So sánh [Option A] và [Option B] cho [mục đích].
Tiêu chí: chi phí, thời gian triển khai, độ tin cậy, khả năng mở rộng.
Đề xuất option nào tốt hơn và tại sao.
```

**Quan sát sau 5 prompts:**

- Claude trả lời bằng tiếng Việt nếu bạn hỏi tiếng Việt
- Claude giữ thuật ngữ kỹ thuật tiếng Anh (nếu bạn yêu cầu)
- Prompt càng rõ ràng, kết quả càng chính xác
- Bạn có thể tiếp tục hỏi trong cùng conversation để refine kết quả

---

## Bước 3: Upload file đầu tiên (3 phút)

Claude có thể đọc và phân tích files bạn upload.

**Cách upload:** Click biểu tượng clip (đính kèm) bên cạnh ô nhập tin nhắn, chọn file.

**Thử ngay với prompt này:**

```
[Upload một file tài liệu hoặc log]

Tóm tắt nội dung file này trong 5 bullet points.
Highlight những điểm quan trọng nhất.
```

**File types hỗ trợ:**

| Loại | Formats |
|------|---------|
| Tài liệu | PDF, DOCX, TXT, MD, HTML |
| Code | PY, JS, JSON, YAML, XML |
| Hình ảnh | PNG, JPG, WEBP, GIF |
| Data | CSV, XLSX |

**Giới hạn:** Tối đa 30MB mỗi file, 20 files mỗi conversation.

---

## Bước 4: Thiết lập nhanh cho công việc hàng ngày (2 phút)

Để Claude hiểu bạn hơn mỗi lần chat, thiết lập Profile Preferences:

1. Click avatar góc trái dưới > **Settings** > **Profile**
2. Chọn "Engineering" hoặc "Software Development"
3. Nhập vào ô Profile Preferences:

```
Ngôn ngữ: Tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh.
Tôi là kỹ sư làm việc với [lĩnh vực của bạn].
Trả lời ngắn gọn, actionable. Khi không chắc chắn, nói rõ.
```

Từ bây giờ, mọi conversation mới sẽ tự động áp dụng preferences này.

---

## Checkpoint: Tôi đã sẵn sàng chưa?

Hoàn thành checklist sau để xác nhận bạn đã nắm cơ bản:

- [ ] Đã đăng nhập Claude.ai thành công
- [ ] Đã gửi ít nhất 3 prompts và nhận response
- [ ] Đã upload ít nhất 1 file và Claude phân tích được
- [ ] Đã thiết lập Profile Preferences
- [ ] Hiểu rằng: prompt rõ ràng hơn = kết quả tốt hơn

**Nếu đã check hết:** Bạn sẵn sàng để đi sâu hơn.

**Nếu chưa check hết:** Quay lại bước chưa hoàn thành. Không cần vội -- mục tiêu là làm quen, không phải thành thạo ngay.

---

## 5 điều cần nhớ khi mới bắt đầu

**1. Claude không phải Google.** Đừng hỏi "AMR là gì?" -- hãy hỏi "Giải thích sự khác biệt giữa AMR và AGV cho người mới trong ngành logistics, kèm ví dụ thực tế."

**2. Càng rõ ràng, kết quả càng tốt.** Claude tuân thủ instructions rất chặt. Nếu bạn nói "viết đúng 3 câu", nó sẽ viết đúng 3 câu. Nếu bạn không nói, nó tự quyết. "Giúp tôi viết tài liệu" kém hơn "Viết SOP kiểm tra Lidar trước khi vận hành robot AMR, cho kỹ thuật viên bảo trì, format checklist."

**3. Đừng ngại yêu cầu lại (iterate).** Nếu kết quả chưa đúng ý, nói cụ thể điều gì chưa đúng. Thay vì "Làm lại đi" (Claude không biết sửa gì), hãy nói "Phần Safety cần chi tiết hơn, rút ngắn mỗi section còn 3 bullet points."

**4. Mỗi conversation là một context riêng.** Claude không nhớ gì giữa các cuộc hội thoại trừ khi bật Memory (Settings > Capabilities — có trên mọi plan). Nếu chuyển từ "debug Lidar" sang "viết SOP charging", hãy tạo conversation mới.

**5. Claude sẽ nói "tôi không biết".** Đây là điểm mạnh, không phải điểm yếu. Nếu Claude không chắc, nó sẽ nói thẳng thay vì bịa ra câu trả lời. Tuy nhiên, luôn verify thông tin quan trọng -- không AI nào hoàn hảo 100%.

---

## Tiếp theo nên đọc gì?

| Mục tiêu của bạn | Module khuyến nghị |
|-------------------|-------------------|
| Thiết lập Projects, Styles, Memory | Module 02: Setup & Personalization |
| Dùng Claude Desktop / Cowork mode | Module 10: Claude Desktop & Cowork |
| Học cách viết prompt hiệu quả | Module 03: Prompt Engineering |
| Cần template copy-paste ngay | Module 07: Template Library |
| Muốn quy trình hoàn chỉnh cho công việc | Module 05: Workflow Recipes |

---

**Lưu ý:** Module này chỉ bao gồm tính năng cơ bản nhất. Claude còn nhiều khả năng khác: tạo file Word/Excel/PowerPoint, research sâu, tạo diagrams, phân tích hình ảnh, và hơn thế nữa. Nếu bạn dùng **Claude Desktop**, xem thêm Module 10 về Cowork mode — cho phép Claude thao tác trực tiếp với file trên máy tính. Các module tiếp theo sẽ hướng dẫn chi tiết.
