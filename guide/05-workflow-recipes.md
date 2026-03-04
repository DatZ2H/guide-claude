# Module 05: Workflow Recipes

**Thời gian đọc:** 25 phút | **Mức độ:** Intermediate
**Cập nhật:** 2026-03-01 | Models: xem [specs](reference/model-specs.md)

---

Module này không dạy lý thuyết -- nó cung cấp quy trình copy-paste cho từng loại công việc cụ thể. Mỗi recipe bao gồm: khi nào dùng, setup cần thiết, prompts cụ thể, và tips thực tế.

---

## 5.1 Recipe: Viết tài liệu từ đầu (Document Drafting)

**Khi nào dùng:** Cần viết tài liệu mới -- user guide, SOP, technical spec, training material.

**Setup:** Nên dùng trong Project đã có style guide và template uploaded. Style: Custom "Technical" hoặc Formal preset.

### Quy trình 4 bước

**Bước 1 -- Brief và Outline:**

```text
Tôi cần viết {{loai_tai_lieu}} cho {{san_pham_he_thong}}.

Background:
- {{mo_ta_ngan_san_pham}}
- {{phien_ban_release}}

Target audience: {{mo_ta_nguoi_doc}}

Mục tiêu: Sau khi đọc xong, người đọc có thể {{ket_qua_mong_doi}}.

Đề xuất outline chi tiết. Chỉ outline -- chưa viết nội dung.
Với mỗi section, note ngắn 1 dòng về nội dung chính.
```

**Bước 2 -- Review và điều chỉnh outline:**

```text
Điều chỉnh outline:
- {{them_bo_gop_tach_sections}}
- {{thay_doi_thu_tu_neu_can}}

Confirm outline cuối cùng trước khi viết.
```

**Bước 3 -- Viết từng section:**

```text
Viết section "{{ten_section}}" theo outline đã thống nhất.

Tuân thủ:
- {{quy_tac_viet_cu_the}}
- Nếu cần thông tin tôi chưa cung cấp, đánh dấu [TBD: mô tả thông tin cần]
  và tiếp tục viết phần còn lại.
```

**Bước 4 -- Review tổng thể:**

```text
Đọc lại toàn bộ tài liệu từ đầu đến cuối và kiểm tra:

1. Consistency: thuật ngữ, capitalization, format
2. Completeness: có thiếu step hay thông tin quan trọng nào không?
3. Flow: logic trình bày có smooth không?
4. Audience: ngôn ngữ có phù hợp target audience không?

Liệt kê mọi issue tìm được.
```

**Tip thực tế:** Ở bước 3, viết từng section riêng lẻ trong các messages khác nhau. Không nên yêu cầu Claude viết hết cả tài liệu 20-30 trang trong một message -- chất lượng sẽ giảm ở các phần cuối do context dài.

[Ứng dụng Kỹ thuật] Ví dụ: Viết User Guide cho AMR-500. Bước 1 brief — "Viết user guide cho robot tự hành AMR-500, vận hành trong nhà máy sản xuất linh kiện điện tử. Target audience: kỹ thuật viên vận hành, quen xe nâng thông thường, chưa có background lập trình. Sau khi đọc, người đọc có thể khởi động, vận hành cơ bản, và xử lý 5 lỗi thường gặp." Bước 2 điều chỉnh — tách riêng "Safety Procedures" thành section đầu tiên. Bước 3 — viết mỗi section trong 1 message riêng (Safety → Startup → Navigation Modes → Emergency Stop → Error Codes), không gộp cả guide vào 1 prompt.

---

## 5.2 Recipe: Review và cải thiện tài liệu (Document Review)

**Khi nào dùng:** Cần review tài liệu do đồng nghiệp viết, hoặc cải thiện tài liệu cũ.

**Setup:** Upload file tài liệu cần review (PDF, Word, hoặc paste text). Nếu có style guide: upload vào Project Knowledge.

### Review toàn diện

```text
[Upload file]

Review tài liệu này theo các tiêu chí sau.
Đánh giá theo thang: [Pass] / [Needs Improvement] / [Fail]

Tiêu chí:
1. ACCURACY -- Thông tin có chính xác, up-to-date không?
2. CLARITY -- Target audience ({{mo_ta_audience}}) có hiểu được không?
3. CONSISTENCY -- Thuật ngữ, format, tone có nhất quán không?
4. COMPLETENESS -- Có thiếu thông tin quan trọng nào không?
5. STRUCTURE -- Tổ chức logic có hợp lý không?
6. GRAMMAR & STYLE -- Ngữ pháp, chính tả, style có chuẩn không?

Output format:
Bảng tóm tắt assessment > Chi tiết từng issue > Overall recommendation.
```

### Review chuyên sâu cho procedures

```text
[Upload file hướng dẫn sử dụng]

Đóng vai {{persona_nguoi_dung}} đọc tài liệu này lần đầu.
"Đi qua" từng step trong procedures và kiểm tra:

- Có step nào bị thiếu giữa chừng không? (gap analysis)
- Có step nào giả định người đọc đã biết điều chưa được giải thích?
- Có thuật ngữ nào xuất hiện mà chưa được define?
- Expected results sau mỗi step có được nêu rõ không?
- Error cases có được đề cập không?

Liệt kê mọi vấn đề tìm được, sắp xếp theo thứ tự xuất hiện trong tài liệu.
```

**Ví dụ Phenikaa-X:** Review SOP vận hành AMR -- persona là "kỹ thuật viên mới, chưa từng dùng robot tự hành, quen với xe nâng thông thường".

---

## 5.3 Recipe: Troubleshooting có cấu trúc

**Khi nào dùng:** Debug lỗi hệ thống, phân tích log, xác định root cause.

**Setup:** Nên bật Extended thinking cho các case phức tạp (nhiều module liên quan). Upload log files trực tiếp.

### Prompt chuẩn

```xml
<role>
Senior Robotics Engineer chuyên troubleshooting hệ thống AMR.
</role>

<task>
Phân tích {{loai_data}} dưới đây và xác định root cause.
</task>

<context>
- Robot/Hệ thống: {{ten_he_thong}}
- Môi trường: {{mo_ta_moi_truong}}
- Vấn đề: {{mo_ta_van_de}}
- Thời gian xuất hiện: {{thoi_gian}}
- Đã thử: {{cac_buoc_da_thu}}
</context>

<input_data>
{{log_data_hoac_error_messages}}
</input_data>

<requirements>
- Xác định root cause chính (không chỉ liệt kê symptoms)
- Phân biệt rõ: nguyên nhân gốc vs. hệ quả
- Đề xuất solutions xếp theo mức ưu tiên
- Mỗi solution ghi rõ: thay đổi gì, ở đâu, risk level
</requirements>
```

### Khi nào bật Extended thinking

| Bật Extended thinking | Không cần |
|----------------------|-----------|
| Log có nhiều warning từ nhiều module | Lỗi đơn giản, error message rõ ràng |
| Cần phân biệt nguyên nhân gốc vs. hệ quả dây chuyền | Đã biết nguyên nhân, chỉ cần fix |
| Tương tác giữa nhiều subsystems | Lỗi nằm trong 1 module duy nhất |

---

## 5.4 Recipe: Chuẩn hóa thuật ngữ (Terminology Management)

**Khi nào dùng:** Tạo hoặc cập nhật glossary, đảm bảo team dùng thuật ngữ nhất quán.

### Tạo glossary từ tài liệu hiện có

```text
[Upload 3-5 tài liệu mẫu của team]

Phân tích các tài liệu đã upload và:

1. Trích xuất tất cả thuật ngữ kỹ thuật/chuyên ngành
2. Xác định các trường hợp cùng concept nhưng dùng từ khác nhau
   (ví dụ: "robot" vs "AMR" vs "mobile robot" vs "xe tự hành")
3. Đề xuất thuật ngữ chuẩn cho mỗi concept

Output dạng bảng:
| Thuật ngữ chuẩn | Định nghĩa | Viết tắt | Thuật ngữ cần tránh | Ghi chú |

Sắp xếp theo alphabet.
```

### Kiểm tra tính nhất quán

```text
[Upload file tài liệu + glossary]

So sánh tài liệu với glossary đã upload.
Tìm mọi trường hợp thuật ngữ trong tài liệu không khớp với glossary:
- Dùng thuật ngữ sai
- Dùng cách viết/viết hoa khác
- Dùng thuật ngữ chưa có trong glossary (cần bổ sung?)

Báo cáo dạng bảng với vị trí cụ thể (section + paragraph).
```

[Ứng dụng Kỹ thuật] Ví dụ: Team R&D dùng lẫn lộn "robot tự hành" / "AGV" / "AMR" / "xe tự hành" — cùng 1 concept, 4 cách gọi khác nhau trong SOP, maintenance manual, incident report, training material. Upload 4 tài liệu → Claude trích xuất glossary → chuẩn hóa: "AMR" là thuật ngữ chính thức; "AGV" chỉ dùng khi so sánh với công nghệ cũ (dây chuyền guided wire). Sau đó dùng prompt "Kiểm tra tính nhất quán" để scan và đánh dấu 23 chỗ cần fix trong 4 files.

---

## 5.5 Recipe: Tạo file chuyên nghiệp (Document Generation)

**Khi nào dùng:** Cần output là file thật (Word, Excel, PowerPoint) chứ không chỉ text.

### Tạo report Word

```text
Tạo file Word (.docx) cho {{loai_bao_cao}}:

Thông tin:
- {{noi_dung_chinh}}

Format:
- Header: tên công ty + tên dự án + ngày
- Table of contents
- Professional formatting với heading styles
- Bảng summary ở trang đầu
- Page numbers ở footer
```

### Tạo Excel tracking

```text
Tạo file Excel (.xlsx) cho {{muc_dich_tracking}}:

Columns:
- {{danh_sach_columns}}

Thêm:
- Conditional formatting: {{quy_tac_mau}}
- Filter on all columns
- Summary sheet với dashboard
```

### Tạo presentation

```text
Tạo file PowerPoint (.pptx) cho {{muc_dich_presentation}}.

Nội dung {{so_slides}} slides:
{{danh_sach_slides}}

Style: clean, professional, ít text trên mỗi slide, dùng diagrams khi có thể.
```

**Lưu ý:** Cần bật "Code execution and file creation" trong Settings > Capabilities để tạo file xlsx, docx.

---

## 5.6 Recipe: Research và tổng hợp

**Khi nào dùng:** Cần tìm hiểu thông tin trước khi viết hoặc ra quyết định.

### Research nhanh (Web Search)

```text
Tìm kiếm và tổng hợp thông tin về {{chu_de}}:

1. {{khia_canh_1}}
2. {{khia_canh_2}}
3. {{khia_canh_3}}

Với mỗi source, nêu rõ: tên, nguồn, và key takeaway.
Cuối cùng: đề xuất approach tốt nhất cho trường hợp cụ thể của tôi.
```

### Research

[Nguồn: Anthropic Help Center - Research]
URL: https://support.anthropic.com/en/articles/11088861

Khi cần research kỹ hơn -- competitive analysis, technology landscape, industry standards -- dùng Research. Claude tự động tìm kiếm nhiều nguồn, tổng hợp, và tạo báo cáo chi tiết.

```text
Sử dụng Research để nghiên cứu:
{{chu_de_can_research}}

Focus vào:
- {{khia_canh_1}}
- {{khia_canh_2}}
- {{khia_canh_3}}

Tạo báo cáo tổng hợp với citations.
```

| Aspect | Web Search | Research |
|--------|-----------|---------------|
| Depth | Quick lookup, 1-3 sources | Deep dive, multiple sources |
| Output | Direct answer | Report có citations |
| Thời gian | Nhanh (giây) | Lâu hơn (phút) |
| Dùng khi | Tra cứu nhanh, verify thông tin | Nghiên cứu sâu, tổng hợp đa nguồn |

**Cách bật:** Message input > Click "Search and tools" > Chọn "Web Search" hoặc "Research".

---

## 5.7 Recipe: Structured Output cho automation

[Nguồn: Anthropic Docs - Structured Outputs]
URL: https://docs.anthropic.com/en/docs/build-with-claude/structured-outputs

**Khi nào dùng:** Output cần parse tự động bởi script, dashboard, hoặc pipeline -- không phải người đọc.

### Prompt-based JSON (Claude.ai)

```xml
<task>
Phân tích {{loai_data}} và trả kết quả dưới dạng JSON.
</task>

<input_data>
{{data_input}}
</input_data>

<output_format>
Trả về CHỈ JSON, không markdown, không giải thích.
Theo đúng schema sau:

{
  "robot_id": "string",
  "timestamp": "string (ISO 8601)",
  "errors": [
    {
      "module": "string (lidar | slam | navigation | motor)",
      "severity": "string (critical | warning | info)",
      "message": "string",
      "suggested_fix": "string"
    }
  ],
  "root_cause": "string",
  "recommended_action": "string"
}
</output_format>
```

**Tip:** Thêm "Trả về CHỈ JSON, không markdown, không giải thích" để tránh Claude wrap output trong code block.

### Ứng dụng Phenikaa-X

[Ứng dụng Kỹ thuật]

| Use case | Lợi ích |
|----------|---------|
| Parse Lidar error logs tự động | Feed trực tiếp vào dashboard monitoring |
| Trích xuất thông số từ datasheet | Tự động so sánh specs giữa các sensor |
| Tạo incident report có cấu trúc | Đồng bộ format cho mọi incident |
| Đánh giá code review | Tích hợp vào CI/CD pipeline |

### Khi nào dùng

```mermaid
flowchart TD
    A["Can output tu Claude"] --> B{"Output se duoc\nxu ly tu dong?"}
    B -->|"Co — script/API doc"| C{"Dung API?"}
    B -->|"Khong — nguoi doc"| D["Dung prompt thuong\nKhong can JSON"]
    C -->|"Co"| E["Structured Outputs\nqua API — guaranteed"]
    C -->|"Khong — Claude.ai"| F["Prompt-based JSON\nvoi schema trong output_format"]
```

---

## 5.8 Recipe: Convert và migrate tài liệu

**Khi nào dùng:** Chuyển đổi format hoặc cấu trúc lại tài liệu cũ.

### Convert Word sang Markdown

```text
[Upload file Word]

Chuyển tài liệu Word này sang Markdown format:
- Giữ nguyên cấu trúc heading hierarchy
- Bảng > Markdown tables
- Hình ảnh > placeholder [Image: mô tả]
- Bold/italic > **bold** / *italic*
- Cross-references > [Section Name](#section-name)

Output: file Markdown hoàn chỉnh.
```

### Restructure tài liệu cũ

```text
[Upload file tài liệu cũ]

Tài liệu này được viết {{thoi_gian}} trước và cần cập nhật.

Hãy:
1. Phân tích cấu trúc hiện tại và chỉ ra vấn đề
2. Đề xuất cấu trúc mới phù hợp hơn
3. Đánh dấu nội dung nào:
   - [Keep] Giữ nguyên (còn chính xác)
   - [Review] Cần review (có thể đã outdated)
   - [Rewrite] Cần viết lại
   - [Add] Cần bổ sung (thiếu)

Chưa cần viết lại -- chỉ cần assessment và migration plan.
```

---

## 5.9 Recipe: Sử dụng MCP Connectors trong workflow

**Khi nào dùng:** Muốn Claude tương tác trực tiếp với tools bạn đang dùng -- không cần copy-paste qua lại.

### Connectors hữu ích

| Connector | Dùng để |
|-----------|---------|
| **Google Drive** | Đọc documents, spreadsheets trực tiếp |
| **Notion** | Tạo/update pages trong Notion workspace |
| **Slack** | Tìm kiếm conversations, context |
| **GitHub** | Truy cập repositories, review code |
| **Gmail** | Tham chiếu emails, draft responses |
| **Jira** | Xem và quản lý tickets |

### Workflow ví dụ

```text
Tôi cần tạo một trang Notion mới với nội dung:
- Title: "Documentation Standards v2.0"
- Sections: {{danh_sach_sections}}
- Bảng comparison giữa standard cũ và mới
```

**Setup:** Settings > Connected Apps > Connect service cần thiết.

**Lưu ý:** Mỗi connector tốn context tokens khi fetch data. Chỉ connect khi thực sự cần.

---

## 5.10 Document Lifecycle -- Workflow tổng hợp

Kết hợp các recipes thành quy trình hoàn chỉnh cho một tài liệu từ ý tưởng đến published.

```mermaid
flowchart TD
    A["PLAN\nRecipe 5.6 Research"] --> B["TEMPLATE\nRecipe 5.5 Generate template"]
    B --> C["DRAFT\nRecipe 5.1 Viet tung section"]
    C --> D["REVIEW\nRecipe 5.2 Review toan dien"]
    D --> E["TERMINOLOGY\nRecipe 5.4 Kiem tra thuat ngu"]
    E --> F{"Dat chat luong?"}
    F -->|"Chua"| G["Chinh sua theo feedback"]
    G --> D
    F -->|"Dat"| H["PUBLISH\nRecipe 5.5 Tao file cuoi"]
    H --> I["DISTRIBUTE\nRecipe 5.9 Push to Notion/tools"]
    I --> J["MAINTAIN\nRecipe 5.8 Update khi can"]
```

### Checklist cho mỗi giai đoạn

| Giai đoạn | Checklist |
|-----------|----------|
| **Plan** | Audience xác định? Scope rõ ràng? Research đủ? |
| **Draft** | Viết từng section? [TBD] markers cho info thiếu? |
| **Review** | 6 tiêu chí đều Pass? Procedures đi qua được? |
| **Terminology** | Khớp glossary? Thuật ngữ nhất quán? |
| **Publish** | Format đúng? Metadata đầy đủ? Version đúng? |
| **Maintain** | Review date đặt? Owner assigned? |

---

## 5.11 Recipe: Hybrid Workflow — Chat + Project + Cowork

[Cập nhật 03/2026]

**Khi nào dùng:** Dự án kéo dài nhiều ngày, cần cả brainstorm/research (thinking) lẫn tạo file/tổ chức thư mục (executing). Ví dụ: xây dựng bộ tài liệu chuẩn, tạo training package, viết technical specification.

**Setup cần thiết:**
- Claude.ai account với Projects enabled (Pro trở lên)
- Claude Desktop với Cowork
- Thư mục project đã có `.claude/CLAUDE.md` (xem Module 10, mục 10.13)
- Project Knowledge chỉ chứa `project-state.md` (xem Module 04, mục 4.9 — Two-Layer Knowledge)

**Triết lý:** Mỗi công cụ Claude có thế mạnh riêng — dùng đúng công cụ cho đúng giai đoạn, liên kết bằng files.

### Quy trình 6 giai đoạn (+ 1 update optional)

```mermaid
flowchart TD
    A["1. RESEARCH\nClaude.ai Chat\n+ Web Search"] --> B["2. PLAN\nClaude.ai Chat\nhoac Project"]
    B --> C["3. SETUP\nCowork\nTao cau truc folder"]
    C --> D["4. DRAFT\nProject hoac Cowork\nViet noi dung"]
    D --> E["5. REVIEW\nProject\nSo sanh voi references"]
    E --> F{"Dat\nchat luong?"}
    F -->|"Chua"| D
    F -->|"Dat"| G["6. FINALIZE\nCowork\nFormat + to chuc files"]
    G --> H["7. UPDATE (optional)\nCowork export\nproject-state.md\n> Upload vao PK khi can"]
```

### Chi tiết từng giai đoạn

| Giai đoạn | Công cụ | Tại sao công cụ này | Prompt mẫu |
|-----------|---------|---------------------|------------|
| **1. Research** | Claude.ai Chat (web search) | Memory cross-session giúp continuity; web search cho thông tin mới | "Tìm kiếm và tổng hợp best practices về {{chủ đề}}. Focus vào {{khía cạnh 1}}, {{khía cạnh 2}}." |
| **2. Plan** | Claude.ai Chat hoặc Project | Tương tác qua lại nhanh; Project giữ reference files | "Dựa trên research, đề xuất outline cho {{tài liệu}}. Mỗi section ghi mục đích + nội dung chính." |
| **3. Setup** | Cowork | Tạo folder structure + files trực tiếp | "Tạo cấu trúc thư mục theo outline đã thống nhất. Tạo file placeholder cho mỗi section." *(xem prompt chi tiết bên dưới)* |
| **4. Draft** | Project (iterate nội dung) hoặc Cowork (ghi file) | Project: Custom Instructions giữ tone nhất quán. Cowork: output thẳng vào file | "Viết section {{tên}} theo outline. Tuân thủ style guide trong Project Knowledge." |
| **5. Review** | Project | So sánh draft với glossary, style guide đã upload | "Review file {{tên}} theo 6 tiêu chí (Recipe 5.2). So sánh với glossary.md." |
| **6. Finalize** | Cowork | Batch operations: chuyển format, tổ chức, rename | "Chuyển tất cả file .md trong drafts/ sang .docx trong output/. Thêm header chuẩn." |
| **7. Update** *(optional)* | Cowork → Project Knowledge | Export trạng thái → upload khi cần briefing Project Chat | "Cập nhật project-state.md từ git log và file system hiện tại. Output sẵn sàng upload vào Project Knowledge." |

### Prompts chi tiết cho từng giai đoạn

**Giai đoạn 3 — Setup folder qua Cowork:**

```text
Đọc CLAUDE.md và git log --oneline -10 nếu có.

Tạo cấu trúc thư mục cho dự án "{{tên dự án}}":

{{mô tả cấu trúc — ví dụ:}}
- drafts/          — bản nháp đang viết
- output/          — file hoàn chỉnh
- references/      — tài liệu tham khảo
- templates/       — mẫu tài liệu
- .claude/         — Folder Instructions + skills

Tạo file placeholder (.md) cho mỗi section trong outline:
{{danh sách sections}}

Mỗi file placeholder chứa: heading, mục đích section (1 dòng), "[TBD]".

Sau khi tạo xong, commit với message mô tả cấu trúc đã tạo.
```

**Giai đoạn 4 — Draft nội dung qua Project Chat:**

```text
Viết section "{{tên section}}" cho {{tên tài liệu}}.

Tuân thủ:
- Style guide trong Project Knowledge
- Glossary trong Project Knowledge
- Outline đã thống nhất: {{paste outline hoặc reference file}}

Nếu cần thông tin chưa cung cấp, đánh dấu [TBD: mô tả] và tiếp tục.

Output: nội dung Markdown hoàn chỉnh cho section này.
```

*Sau khi review xong nội dung ở Project Chat → copy sang Cowork để ghi file, hoặc dùng Cowork trực tiếp nếu đã quen.*

**Chuyển context từ Chat/Project sang Cowork:**

Khi cần mang kết quả từ Chat/Project vào Cowork, tạo file trung gian:

```text
Tóm tắt kết quả research/decisions đã thảo luận thành format
có thể paste vào file. Cấu trúc:

1. Key findings (bullet points)
2. Decisions đã chốt (decision + rationale)
3. Outline/plan đã thống nhất
4. Constraints và requirements

Output: text sẵn sàng copy vào file .md
```

*Paste output vào file trong thư mục project (ví dụ: `references/research-summary.md`) → Cowork đọc được ở session sau.*

### Khi nào KHÔNG cần Hybrid Workflow

| Tình huống | Dùng gì thay thế |
|-----------|-------------------|
| Task xong trong 1 session, không cần file output | Chat thông thường |
| Chỉ cần tạo files, không cần research/iterate | Cowork alone |
| Task đơn giản, 1 file output | Chat + download hoặc Cowork |
| Team collaboration cần audit trail | Project alone (có chat history) |

### Tips thực tế

1. **Không cần dùng đủ 3 công cụ cho mọi task.** Hybrid Workflow là framework linh hoạt — bỏ qua giai đoạn không cần thiết.

2. **Sync context bằng files, không bằng memory.** Copy-paste kết quả quan trọng vào file trong thư mục project. Cowork đọc file, không đọc Chat/Project history.

3. **Dùng Two-Layer Knowledge khi files thay đổi thường xuyên qua Cowork** (xem Module 04, mục 4.9). Project Knowledge chỉ chứa `project-state.md` — không upload working documents sẽ bị stale.

4. **Update `project-state.md` khi cần** — sau milestone hoặc trước khi dùng Project Chat cho task mới. Không cần theo lịch cố định. Chi tiết: Module 10, mục 10.8.2.

---

## 5.12 Recipe: Task Planning trước khi chạy Chain Prompt

**Khi nào dùng:** Task cần chain ≥ 3 prompts, có dependency giữa các bước. Planning trước giúp xác định rõ thứ tự, input/output mỗi bước, và review checkpoint — thay vì chạy prompt rồi mới phát hiện thiếu context hoặc sai hướng.

### Bước 1 — Scope + Dependencies

Trả lời 3 câu hỏi trong 1 prompt trước khi bắt đầu chain:

```text
Tôi cần {{mô_tả_task_tổng_thể}}.

Trước khi bắt đầu, trả lời 3 câu hỏi:

1. Output cuối cùng mong muốn là gì?
   (Mô tả cụ thể: file gì, format gì, ai dùng, dùng để làm gì)

2. Files/artifacts nào sẽ được tạo hoặc sửa trong quá trình?
   (Liệt kê từng file, không gộp chung "các file liên quan")

3. Phần nào phụ thuộc phần nào?
   (Step A phải xong trước khi Step B bắt đầu?
    Hay Step B và C có thể song song?)
```

### Bước 2 — Tạo Task Map

Yêu cầu Claude tạo bảng task map từ câu trả lời ở bước 1:

```text
Dựa trên scope analysis trên, tạo bảng task map:

| Step | Mục tiêu | Input từ step trước | Output cần có | Review checkpoint |
|------|----------|---------------------|---------------|-------------------|

Mỗi step phải có stopping criteria rõ ràng — step này XONG khi nào?
Đánh dấu step nào cần review kỹ trước khi tiếp.
```

### Bước 3 — Validate plan trước khi chạy

Checklist 5 items trước khi bắt đầu chain:

```text
- [ ] Số steps hợp lý? (không quá nhỏ gộp nhiều việc, không quá lớn chia quá mịn)
- [ ] Dependency map đúng thứ tự? (step trước tạo đúng output step sau cần)
- [ ] Mỗi step có clear stopping criteria?
- [ ] Review checkpoint được định nghĩa? (biết check gì sau step nào)
- [ ] Biết bước nào cần backup trước khi thực hiện?
```

[Ứng dụng Kỹ thuật] Ví dụ: tạo báo cáo đánh giá hiệu suất AMR 3 tháng. Step 1: thu thập và chuẩn hóa data từ 3 nguồn (fleet management, maintenance log, incident report). Step 2: phân tích trends theo KPIs đã định nghĩa. Step 3: tạo bảng so sánh target vs actual. Step 4: viết executive summary + recommendations. Step 5: format thành report hoàn chỉnh. Review checkpoint sau Step 1 (data đủ chưa?) và Step 3 (số liệu khớp chưa?) trước khi viết narrative.

---

## 5.13 Recipe: Multi-file Editing Workflow

**Khi nào dùng:** Cần sửa nhiều files liên quan nhau — trong Cowork hoặc chain prompt dài. Rủi ro lớn nhất: sửa file A nhưng file B, C vẫn reference nội dung cũ của A.

### Giai đoạn 1 — Pre-edit: Impact Analysis

Trước khi sửa bất kỳ file nào, scan impact trước:

```text
Trước khi sửa {{tên file/section}}, scan toàn bộ thư mục và liệt kê:

1. Files nào có reference đến {{nội dung sẽ thay đổi}}
2. Với mỗi file: reference cụ thể ở đâu (section, dòng, nội dung)

Chưa sửa gì — chỉ report impact.
```

### Giai đoạn 2 — Edit: thực hiện sửa với explicit scope

Nguyên tắc: luôn list đầy đủ tên files sẽ sửa và khóa scope rõ ràng.

```text
Thực hiện thay đổi sau:
- File: {{tên file}}
- Thay đổi: {{mô tả cụ thể}}

Files sẽ sửa trong bước này:
1. {{file_1}}
2. {{file_2}}

KHÔNG chạm files khác ngoài danh sách này.
```

### Giai đoạn 3 — Post-edit: Cascade Update + Verification

Sau khi sửa xong, update tất cả references:

```text
Vừa sửa {{file A}}: {{mô tả thay đổi}}.

Scan toàn bộ thư mục, tìm tất cả chỗ reference đến {{nội dung cũ}}.
Liệt kê: [tên file] → [nội dung cần update].
Sau đó sửa từng chỗ.
```

Verification prompt cuối cùng:

```text
Chạy consistency check toàn bộ:
1. Cross-references còn valid không? (links, "xem mục X", "xem file Y")
2. Terminology nhất quán không? (cùng concept dùng cùng từ)
3. Version/date đã update ở tất cả files đã sửa chưa?
4. Index/README phản ánh đúng state hiện tại không?

Liệt kê mọi inconsistency tìm được.
```

[Ứng dụng Kỹ thuật] Ví dụ dùng chính Guide này: khi sửa section numbering ở Module 10 (10.7 → 10.8), cascade update cần chạy qua README.md, Module 02 (learning path references), Module 06 (cross-references), Module 08 (error references). Không chạy Impact Analysis trước → dễ bỏ sót reference ở Module 08.

**Cross-reference:** Template T-21 (Multi-file Consistency Check, Module 07) là phiên bản template của recipe này.

---

## 5.14 Recipe: Cowork Session Planning Checklist

**Khi nào dùng:** Trước khi mở Cowork cho task phức tạp (≥ 3 files hoặc ≥ 2 sessions). Planning 5–10 phút trước khi bắt đầu tiết kiệm 30+ phút sửa lỗi sau.

### Decision framework — chọn mức planning

```mermaid
flowchart TD
    A["Task can Cowork"] --> B{"Bao nhieu files?"}
    B -->|"1-2 files\nkhong dependency"| C["Lightweight\nMo Cowork go thang"]
    B -->|"3+ files"| D{"Co dependency\ngiua files?"}
    D -->|"Co, 1 session du"| E["Medium\n5-10 phut plan\nTra loi 4 cau hoi scope"]
    D -->|"Co, nhieu sessions"| F["Heavyweight\nPrompt Package day du\nTemplate task plan"]
```

### 4 câu hỏi scope analysis

Trả lời trước khi mở Cowork:

```text
- [ ] Output mong muốn là gì? (files cụ thể, format, nơi lưu)
- [ ] Files nào bị tạo mới / sửa / chỉ đọc?
- [ ] Task nào phải hoàn thành trước task nào?
- [ ] Backup plan là gì nếu output sai? (rollback thế nào?)
```

### Template prompt cho 1 Cowork task (heavyweight planning)

Dùng template này cho mỗi task trong chuỗi nhiều sessions:

```text
## Task {{số}} / {{tổng số tasks}}

Mục tiêu: {{1 câu mô tả kết quả mong đợi}}

Files sẽ sửa: {{danh sách đầy đủ}}
Files tham khảo (chỉ đọc): {{danh sách}}
Input từ task trước: {{handover file hoặc "none — task đầu tiên"}}

Output expected: {{mô tả cụ thể — file gì, nội dung gì, format gì}}
Stopping criteria: Task này xong khi {{điều kiện rõ ràng, verify được}}

KHÔNG làm: {{boundaries — files không được sửa, scope không được mở rộng}}
```

[Ứng dụng Kỹ thuật] Ví dụ: Guide update v3.3 → v3.4. Tại sao chia thành nhiều tasks thay vì 1 task duy nhất? Vì mỗi module là file riêng, cross-references giữa modules cần verify sau mỗi batch edit, và context window hữu hạn — nhồi tất cả thay đổi vào 1 session tăng rủi ro Claude quên instruction ở cuối. Thứ tự: sửa nội dung trước (Modules 03, 04, 08, 09, 05), update cross-references sau (Module 02, 07), cuối cùng update metadata (README, CHANGELOG).

**Cross-reference:** Template T-22 (Cowork Task Plan, Module 07). Module 10, mục 10.9 (Pre-task Planning) giải thích chi tiết hơn về planning cho Cowork sessions.

---

## 5.15 Recipe: Cowork Batch Processing

[Cập nhật 03/2026]

**Khi nào dùng:** Xử lý nhiều files cùng lúc trong Cowork — convert format hàng loạt, extract thông tin từ nhiều tài liệu, tổ chức lại cấu trúc thư mục lớn.

### Quy trình 4 bước

**Bước 1 — Chọn folder và scope:**

```text
Đọc danh sách files trong {{thư_mục}}:
- Liệt kê tất cả files có extension {{ext}}
- Tổng số: bao nhiêu files?
- Preview 3 files đầu để confirm format đúng trước khi chạy full batch.
```

**Bước 2 — Mô tả input/output:**

```text
Input: {{mô tả format hiện tại — ví dụ: file .docx, có heading Word styles}}
Output mong muốn: {{mô tả format đích — ví dụ: file .md, heading #/##/###}}
Quy tắc convert: {{quy tắc đặc thù — ví dụ: bảng Word → Markdown table, hình ảnh → [Image: tên file]}}
Đặt file output vào: {{thư mục đích}}
```

**Bước 3 — Review plan trước khi chạy:**

```text
Trước khi bắt đầu, liệt kê:
1. Số files sẽ xử lý
2. Files nào có thể gặp vấn đề (format không chuẩn, kích thước lớn)
3. Thứ tự xử lý nếu có dependency

Đề xuất batch size hợp lý.
Chưa chạy — chờ approve.
```

**Bước 4 — Approve và chạy batch:**

```text
OK, chạy batch convert theo plan đã thống nhất.
Sau mỗi {{N}} files, báo cáo trạng thái: đã xong X/total, lỗi nếu có.
```

### Prompt template: Batch convert Word → Markdown

```text
Trong thư mục {{input_folder}}, convert tất cả file .docx sang Markdown:

Quy tắc:
- Heading styles (H1→H3) → # / ## / ###
- Bold/Italic → **bold** / *italic*
- Tables → Markdown table
- Hình ảnh → [Image: {{tên file gốc}}]
- Footnotes → ghi chú ở cuối section

Output: lưu file .md vào {{output_folder}}, giữ tên file gốc.
Báo cáo khi hoàn thành: số thành công, số lỗi, danh sách file lỗi nếu có.
```

### Tips

- **Chia batch nếu > 20 files.** Xử lý quá nhiều cùng lúc tăng rủi ro lỗi giữa chừng và khó track kết quả.
- **Dùng Sonnet cho batch tasks.** Opus không cần thiết cho convert/extract — Sonnet nhanh hơn và tiết kiệm quota.
- **Preview 3 files trước khi chạy full batch.** Phát hiện vấn đề format sớm, tránh phải redo toàn bộ.
- **Backup thư mục input trước khi chạy** nếu script có thể ghi đè — dùng Git commit hoặc copy thủ công.

[Ứng dụng Kỹ thuật] Ví dụ: Convert 45 SOP Word docs sang Markdown để đưa vào knowledge base. Chia thành 3 batch (15 files/batch), preview batch đầu xác nhận heading styles đúng, chạy lần lượt. Phát hiện 3 files có hình ảnh embedded cần xử lý thủ công — tách riêng, không block batch còn lại.

---

## 5.16 Recipe: Cowork + Scheduled Tasks cho báo cáo định kỳ

[Cập nhật 03/2026]

**Khi nào dùng:** Cần tạo output tự động theo lịch định kỳ — weekly test report, monthly summary, daily log digest — không cần mở Cowork thủ công mỗi lần.

**Yêu cầu:** Claude Desktop với Cowork (Pro plan trở lên). Máy phải đang bật vào thời điểm scheduled task chạy.

### Quy trình 3 bước

**Bước 1 — Tạo prompt template:**

Viết prompt hoàn chỉnh với tất cả instructions. Scheduled task chạy prompt này tự động — không có người ở đó để clarify, nên prompt phải self-contained.

```text
[Scheduled task — chạy mỗi {{ngày}} lúc {{giờ}}]

Đọc files trong {{thư_mục_data}}:
- {{file_pattern_1}} — chứa {{loại_data_1}}
- {{file_pattern_2}} — chứa {{loại_data_2}}

Tổng hợp thành báo cáo tuần:
1. Tóm tắt executive: 3-5 điểm chính
2. Metrics so với tuần trước: {{danh_sách_KPI}}
3. Issues phát sinh: list với severity
4. Actions needed: ai cần làm gì trước {{deadline}}

Lưu báo cáo tại: {{output_folder}}/report-{{ngày}}.md
Format ngày: YYYY-MM-DD
```

**Bước 2 — Test manual trước khi schedule:**

```text
Chạy thử prompt báo cáo này một lần với data hiện tại.
Confirm: output format đúng, file được lưu đúng chỗ, không có lỗi.
```

**Bước 3 — Setup Scheduled Task trong Cowork:**

Trong Claude Desktop > Cowork > Scheduled Tasks:

1. Tạo task mới
2. Paste prompt template
3. Chọn schedule: Daily / Weekly / Monthly + thời điểm
4. Cron syntax nếu cần lịch phức tạp:

| Lịch | Cron syntax |
|------|-------------|
| Mỗi thứ Hai 8:00 AM | `0 8 * * 1` |
| Mỗi thứ Sáu 5:00 PM | `0 17 * * 5` |
| Ngày 1 hàng tháng 9:00 AM | `0 9 1 * *` |
| Mỗi ngày trong tuần 9:00 AM | `0 9 * * 1-5` |

### Prompt template: Weekly test report

```text
[Scheduled task — chạy mỗi thứ Sáu 5:00 PM]

Đọc tất cả file log trong tests/results/ từ tuần này (thứ Hai đến hôm nay).
File pattern: test-*.log

Tạo Weekly Test Report:

## Summary
- Tổng test cases: X passed / Y failed / Z skipped
- Pass rate: X%

## Failed Tests
| Test | Error | Module | Priority |
|------|-------|--------|----------|
[liệt kê từng test fail]

## Trends so tuần trước
[so sánh pass rate, module có nhiều fail nhất]

## Actions Needed
[issues cần fix trước release tiếp theo]

Lưu tại: reports/weekly/test-report-{{YYYY-MM-DD}}.md
```

### Tips

- **Máy phải đang bật.** Scheduled Tasks chạy trên máy local — không chạy được nếu máy tắt hoặc ngủ.
- **Cron syntax chuẩn 5 trường:** `phút giờ ngày_tháng tháng ngày_tuần`. Sai cú pháp → task không chạy.
- **Prompt phải self-contained.** Không dùng "như đã nói", "nhớ lần trước" — mỗi lần chạy là conversation mới.
- **Test manual ít nhất 1 lần** trước khi để chạy tự động. Kiểm tra: file được lưu đúng path, format đúng.
- **Đặt output vào folder có Git** để track lịch sử báo cáo theo thời gian.

[Ứng dụng Kỹ thuật] Ví dụ: Tự động tổng hợp SLAM performance log mỗi sáng thứ Hai. Prompt đọc slam-*.log từ tuần trước, tạo bảng so sánh localization accuracy, loop closure rate, và mapping drift theo ngày. Output file .md trong reports/weekly/ → commit tự động vào Git → team xem trên GitHub.

**Chi tiết Scheduled Tasks:** Xem Module 10, mục 10.5.

---

**Tiếp theo:**

- Module 07: Template Library -- tất cả templates copy-paste cho mọi tình huống
- Module 06: Tools & Features -- tra cứu nhanh tính năng Claude
- Module 10: Claude Desktop & Cowork -- cấu hình Cowork cho Hybrid Workflow
