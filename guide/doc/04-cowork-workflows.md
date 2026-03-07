# 12 Cowork Workflow Templates

**Thời gian đọc:** 30 phút | **Mức độ:** Intermediate | **Audience:** Technical Writing, Documentation
**Cập nhật:** 2026-03-07 | Models: xem [specs](../reference/model-specs.md)

---
depends-on: [reference/model-specs, doc/03-cowork-setup, doc/01-doc-workflows, doc/02-template-library, base/07-evaluation]
impacts: [doc/03-cowork-setup]
---

[Nguồn: Anthropic Help Center - Get started with Cowork] [Cập nhật 03/2026]

Module này cung cấp workflows copy-paste sẵn sàng dùng cho Cowork — chế độ làm việc trực tiếp trên file system của Claude Desktop. Mỗi workflow bao gồm: mục tiêu, setup, prompt template, và tips thực tế.

**Khác với [Doc Workflows](01-doc-workflows.md)** (general recipes dùng trên mọi interface), workflows ở đây khai thác file system access đặc trưng của Cowork: đọc nhiều file cùng lúc, tạo output trực tiếp vào thư mục, và thao tác batch mà không cần bạn copy-paste từng bước.

> [!IMPORTANT] Cowork cần plan Pro, Max, Team, hoặc Enterprise. Xem hướng dẫn setup tại [Cowork Setup](03-cowork-setup.md).

---

## 4.1 Viết SOP từ notes có sẵn

[Ứng dụng Kỹ thuật]

Khi có tài liệu thô rải rác (meeting notes, draft, reference docs), workflow này gom lại và tạo SOP hoàn chỉnh — thay vì phải tự tổng hợp thủ công.

**Khi nào dùng:** Cần tạo SOP từ tài liệu đã có nhưng chưa được format, hoặc cần chuẩn hóa quy trình đang tồn tại dưới dạng notes.

**Input:** Folder chứa meeting notes, draft documents, reference specs, và bất kỳ tài liệu liên quan nào.

**Output:** SOP hoàn chỉnh dạng `.md` hoặc `.docx`, có numbering, safety notes, và approval section.

**Setup:**
- Tạo folder `sop-input/` chứa tất cả tài liệu nguồn
- Nếu có SOP template chuẩn của công ty, đặt vào folder và đặt tên `_template.md` hoặc `_template.docx`
- Folder Instructions (nếu dùng): ghi rõ tên công ty, ngôn ngữ output mong muốn

**Prompt:**

```text
Đọc tất cả tài liệu trong folder này. Tổng hợp và tạo SOP cho quy trình "{{ten_quy_trinh}}".

Thông tin về SOP:
- Đối tượng thực hiện: {{vi_du_ky_thuat_vien_van_hanh_AMR}}
- Scope: {{pham_vi_ap_dung}}
- Tần suất thực hiện: {{vi_du_moi_ca_lam_viec}}

Cấu trúc SOP cần có:
1. Mục đích và phạm vi áp dụng
2. Định nghĩa và viết tắt
3. Thiết bị và vật tư cần thiết
4. Các bước thực hiện (có numbering rõ ràng)
5. Safety warnings (đánh dấu ⚠️ cho mọi bước có rủi ro)
6. Xử lý sự cố thường gặp
7. Approval và revision history (để trống, điền sau)

{{neu_co_template}}: Giữ format của file `_template.*` trong folder.
{{neu_khong_co_template}}: Dùng Markdown với heading hierarchy chuẩn.

Lưu file output là `SOP-{{ten_viet_tat}}-v1.0.md` trong cùng folder.
```

**Expected output:** File SOP hoàn chỉnh, có thể đem đi review ngay. Claude tổng hợp tất cả tài liệu nguồn, giải quyết mâu thuẫn giữa các tài liệu bằng cách chú thích `[Mâu thuẫn: file A nói X, file B nói Y — cần confirm]`.

**Tips:**
- Nếu Claude gặp thông tin mâu thuẫn giữa các tài liệu, yêu cầu nó đánh dấu `[CONFLICT]` thay vì tự quyết định — để bạn resolve sau.
- Với SOP dài >20 bước, thêm dòng "Tạo checklist tóm tắt riêng trong file `SOP-{{ten_viet_tat}}-checklist.md`" vào prompt.
- Sau khi Claude tạo SOP, chạy lại với prompt: "Review SOP vừa tạo. Liệt kê các bước thiếu hoặc không rõ ràng theo quan điểm của người mới bắt đầu."

**Ví dụ:** Viết Style Guide cho team documentation. Folder `sop-input/` chứa: email thread thảo luận conventions, 2 tài liệu mẫu "viết đúng" của senior writer, và draft naming convention từ team lead. `{{ten_quy_trinh}}` = "Viết và xuất bản tài liệu kỹ thuật". Claude đọc 3 nguồn, phát hiện mâu thuẫn: email nói "dùng Title Case cho headings", tài liệu mẫu lại dùng Sentence case → đánh dấu `[CONFLICT]`. Output: `SOP-doc-style-guide-v1.0.md` gồm 8 sections: Scope → Heading Rules → Terminology → Tone & Voice → Code Block Standards → Image Guidelines → Review Checklist → Revision History.

> [!NOTE] **AMR Context**
> Áp dụng workflow này cho viết SOP vận hành AMR.
> Thay: `{{ten_quy_trinh}}` = "Vận hành AMR tại trạm sạc", input folder chứa meeting notes buổi training + draft checklist operator + spec sheet pin AMR-500.

> [!TIP] **Model:** Sonnet 4.6 cho tổng hợp tài liệu từ nhiều nguồn — cân bằng chất lượng và tốc độ. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

> [!TIP] **Skill:** `/doc-standard-enforcer` — enforce writing standards cho SOP output trước khi finalize.

---

## 4.2 Batch review tài liệu kỹ thuật

[Ứng dụng Kỹ thuật]

Thay vì mở từng file và review riêng lẻ, workflow này cho Claude đọc toàn bộ folder và tạo một báo cáo review tổng hợp.

**Khi nào dùng:** Cần review nhiều tài liệu (5–20 files) trước deadline, hoặc cần standardize chất lượng documentation của cả team.

**Input:** Folder chứa 5–10 tài liệu cần review (`.docx`, `.md`, `.pdf`, `.txt`).

**Output:** Report tổng hợp: đánh giá từng tài liệu theo rubric, action items cụ thể, priority ranking.

**Setup:**
- Chuẩn bị rubric review hoặc dùng framework từ [Evaluation Framework](../base/07-evaluation.md)
- Nếu có style guide, đặt vào folder với tên `_style-guide.*`
- Tạo file `_review-criteria.md` trong folder nếu có tiêu chí đặc thù

**Prompt:**

```text
Review tất cả tài liệu trong folder này (bỏ qua file bắt đầu bằng `_`).

Tiêu chí review:
- **Completeness:** Tài liệu có đủ thông tin để người dùng mới thực hiện không?
- **Accuracy:** Có thông tin mâu thuẫn hoặc đã lỗi thời không?
- **Clarity:** Ngôn ngữ có rõ ràng, tránh mơ hồ không?
- **Format:** Có tuân theo {{ten_standard_hoac_style_guide}} không?
- **{{tieu_chi_bo_sung}}:** {{mo_ta}}

Cho mỗi tài liệu, trả về:
- Tên file
- Điểm tổng thể (1–5) với lý do ngắn gọn
- Top 3 issues quan trọng nhất
- Recommended actions cụ thể (không chung chung)

Cuối báo cáo:
- Xếp hạng tài liệu từ "cần sửa gấp nhất" đến "tốt nhất"
- Action items tổng hợp theo owner (nếu biết)

Lưu báo cáo là `review-report-{{YYYY-MM-DD}}.md` trong folder.
```

**Expected output:** File `review-report-*.md` gồm bảng đánh giá từng tài liệu, danh sách issues có priority, và action items sắp xếp theo urgency.

**Tips:**
- Giới hạn 10 file/batch để Claude review kỹ — nếu có nhiều hơn, tạo sub-batch và merge reports sau.
- Thêm dòng "Với issues liên quan đến accuracy, trích dẫn câu/đoạn cụ thể cần verify" để report có thể action ngay.
- Nếu review theo góc độ người dùng cuối: "Đọc mỗi tài liệu như một {{ky_thuat_vien_moi}} lần đầu tiếp xúc. Liệt kê những điểm gây bối rối."

**Ví dụ:** Review 6 SOP drafts của team documentation trước deadline xuất bản. Folder chứa 6 file `.md` + `_style-guide.md`. `{{ten_standard_hoac_style_guide}}` = "Documentation Style Guide v2.0". Claude review 6 files, phát hiện: SOP-003 và SOP-005 dùng thuật ngữ khác nhau cho cùng một bước ("submit for review" vs "gửi review" — inconsistency Anh-Việt), SOP-001 thiếu section "Revision History". Report xếp hạng SOP-004 là "cần sửa gấp" vì thiếu 3 steps quan trọng trong quy trình approval. Action items nhóm theo owner: 4 items cho Writer A, 2 items cho Editor B.

> [!NOTE] **AMR Context**
> Áp dụng workflow này cho batch review SOP vận hành AMR.
> Thay: folder chứa 8 SOP files + `_style-guide.md` = "AMR Documentation Standard". Focus thêm tiêu chí: safety warnings đầy đủ, emergency stop procedure có trong mọi SOP.

> [!TIP] **Model:** Sonnet 4.6 cho batch review — xử lý nhiều files mà không cần deep reasoning. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## 4.3 Tạo báo cáo tuần từ log files

[Ứng dụng Kỹ thuật]

Tổng hợp log thô (test logs, deployment logs, issue reports) thành báo cáo tuần có cấu trúc — không cần đọc từng log thủ công.

**Khi nào dùng:** Cuối tuần cần nộp báo cáo, hoặc cần track tiến độ dự án từ scattered log files.

**Input:** Folder chứa log files của tuần: test logs, deployment logs, error reports, daily standup notes.

**Output:** Báo cáo tuần format chuẩn (Markdown hoặc Word), sẵn sàng gửi cho manager hoặc khách hàng.

**Setup:**
- Tạo folder `weekly-logs/` với sub-folders theo ngày hoặc loại log
- Nếu có template báo cáo chuẩn, đặt vào folder với tên `_report-template.*`
- Tùy chọn: tạo `_report-config.md` định nghĩa format, recipient, và KPIs cần report

**Prompt:**

```text
Đọc tất cả log files và notes trong folder này. Tạo báo cáo tuần cho tuần {{YYYY-WXX}} ({{date_start}} đến {{date_end}}).

Audience: {{vi_du_manager_ky_thuat_hoac_khach_hang}}
Tone: {{professional_concise_hoac_detailed}}

Cấu trúc báo cáo:

## Executive Summary
3–5 bullet points quan trọng nhất của tuần.

## Công việc hoàn thành
Nhóm theo category (deployment, testing, maintenance, etc.)
Với mỗi item: task name, status, brief outcome.

## Issues & Resolutions
Mọi issue xuất hiện trong tuần + cách giải quyết.
Issue chưa resolved: ghi rõ status và next action.

## Metrics (nếu có trong logs)
{{cac_KPI_can_track}}: extract và present dạng table.

## Kế hoạch tuần tới
Extract từ action items trong logs.

{{neu_co_template}}: Follow format của `_report-template.*`.

Lưu output là `weekly-report-{{YYYY-WXX}}.md`.
```

**Expected output:** Báo cáo hoàn chỉnh, Claude tự aggregate số liệu từ logs, highlight issues nổi bật, và extract action items.

**Tips:**
- Đặt tên log files theo pattern `YYYY-MM-DD-*.log` để Claude sắp xếp chronologically chính xác hơn.
- Để báo cáo phù hợp audience: với technical audience, giữ error codes và stack traces; với management/khách hàng, thêm "Translate technical issues sang business impact khi report."
- Để chạy đều đặn mỗi tuần: pin folder `weekly-logs/` trong Cowork sidebar và lưu prompt vào file `_weekly-prompt.md` — mỗi thứ Sáu chỉ cần mở Cowork, paste prompt, xong trong <1 phút.

**Ví dụ:** Tạo báo cáo tuần cho documentation team. Folder `weekly-logs/` chứa: task tracker export (ai viết gì, status), review notes từ 3 reviewers, và daily standup notes. `{{vi_du_manager_ky_thuat_hoac_khach_hang}}` = "Documentation Manager". Claude tổng hợp: 5 SOP hoàn thành draft, 2 đang review (1 có 8 comments chưa resolve), 1 blocked vì thiếu input từ engineering. Executive summary nêu đúng 3 highlights. Metrics: 8/12 docs on track, 2 at risk, 2 delayed. Report gửi được ngay cho Manager mà không cần edit thêm.

> [!NOTE] **AMR Context**
> Áp dụng workflow này cho weekly AMR deployment report.
> Thay: `{{vi_du_manager_ky_thuat_hoac_khach_hang}}` = "Project Manager", folder chứa deployment logs (3 AMR units) + maintenance tickets + daily standup notes. Thêm KPIs: uptime %, navigation errors, charging cycles.

> [!TIP] **Model:** Sonnet 4.6 cho tổng hợp log — task thường ngày, không cần deep reasoning. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## 4.4 Chuyển đổi Word ↔ Markdown batch

[Ứng dụng Kỹ thuật]

Migrate cả folder tài liệu Word sang Markdown (hoặc ngược lại) mà vẫn giữ nguyên structure: headings, tables, code blocks, lists.

**Khi nào dùng:** Migrate documentation sang Obsidian, Notion, hoặc Git-based wiki. Hoặc cần convert Markdown sang Word để gửi cho stakeholders quen file Office.

**Input:** Folder chứa `.docx` files (để convert sang `.md`) hoặc `.md` files (để convert sang `.docx`).

**Output:** Files đã convert trong sub-folder `converted/`, giữ nguyên tên file chỉ đổi extension.

**Setup:**
- Kiểm tra Cowork có access vào folder đích
- Tạo folder `converted/` trước (hoặc yêu cầu Claude tạo)
- Nếu convert sang Word: cần có Word template để giữ font/style chuẩn — đặt vào folder với tên `_word-template.dotx`

**Prompt:**

```text
Convert tất cả file {{.docx / .md}} trong folder này sang {{.md / .docx}}.

Yêu cầu khi convert:
- Giữ nguyên heading hierarchy (H1→H2→H3)
- Convert tables sang {{Markdown table syntax / Word table}}
- Code blocks: {{giữ nguyên formatting, thêm language tag nếu biết}}
- Images: {{ghi placeholder [IMAGE: tên file] nếu không embed được}}
- Links: {{giữ nguyên link text và URL}}
- Footnotes: {{convert sang inline notes hoặc endnotes}}

{{neu_convert_sang_docx}}: Dùng template `_word-template.dotx` nếu có trong folder.

Sau khi convert xong từng file, tạo file `conversion-report.md` liệt kê:
- Files converted thành công
- Files có vấn đề (với mô tả cụ thể)
- Elements không convert được (tables phức tạp, special formatting, etc.)

Lưu tất cả output vào sub-folder `converted/`.
```

**Expected output:** Folder `converted/` chứa tất cả files đã convert + `conversion-report.md` cho biết điều gì cần manual review.

**Tips:**
- Tables phức tạp (merged cells, nested) thường cần manual review — conversion report sẽ flag những cases này.
- Với batch lớn (>20 files), thêm "Convert lần lượt từng file và report sau mỗi file" để track progress và dừng nếu có error.
- Sau khi convert xong, spot-check bằng cách mở `conversion-report.md` — focus vào files được flag "có vấn đề" trước.

**Ví dụ:** Migrate documentation wiki của team từ SharePoint Word docs sang Git-based MkDocs. Folder `docs-word/` chứa 18 file `.docx` từ nhiều contributors. Claude convert 16/18 thành công, 2 bị flag: `api-guide.docx` có merged-cell tables cần redraw thủ công, `architecture-overview.docx` chứa embedded Visio diagram (lưu placeholder `[IMAGE: architecture-diagram]`). Conversion report mapping rõ: 16 files sẵn sàng vào `docs/` của MkDocs repo, 2 files cần manual pass.

> [!NOTE] **AMR Context**
> Áp dụng workflow này cho migrate tài liệu AMR sang Obsidian vault.
> Thay: 15 SOP `.docx` từ 3 engineers. 13/15 convert thành công, 2 bị flag: SOP có merged-cell table cần redraw, SOP chứa embedded Excel chart (lưu placeholder). 15 Markdown files sẵn sàng import vào Obsidian.

> [!TIP] **Model:** Sonnet 4.6 cho batch convert — format mapping, không cần reasoning sâu. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## 4.5 Kiểm tra thuật ngữ nhất quán (Glossary Enforcement)

[Ứng dụng Kỹ thuật]

Scan toàn bộ folder documentation để tìm inconsistencies trong cách dùng thuật ngữ, so với một glossary chuẩn.

**Khi nào dùng:** Trước khi publish documentation, hoặc khi nhiều người cùng viết và thuật ngữ không nhất quán giữa các tài liệu.

**Input:** Folder chứa tài liệu cần scan + file `glossary.md` (hoặc `glossary.xlsx`) định nghĩa thuật ngữ chuẩn.

**Output:** Report liệt kê inconsistencies theo từng thuật ngữ, với file và line reference cụ thể.

**Setup:**
- Chuẩn bị file glossary với format rõ ràng: "Thuật ngữ chuẩn | Các biến thể KHÔNG dùng | Định nghĩa"
- Đặt glossary vào folder với tên bắt đầu bằng `_` để Claude biết đây là reference file, không phải file cần scan
- Folder Instructions nên note: "File `_glossary.*` là reference, không review nó"

**Prompt:**

```text
Đọc file `{{_glossary.md hoặc _glossary.xlsx}}` để lấy danh sách thuật ngữ chuẩn.

Sau đó scan tất cả file còn lại trong folder (bỏ qua files bắt đầu bằng `_`).

Với mỗi thuật ngữ trong glossary:
1. Tìm tất cả biến thể không chuẩn (synonyms, abbreviations, typos)
2. Liệt kê theo format: `[File] [Dòng hoặc Section]: Tìm thấy "{{bien_the_khong_chuan}}" → Nên dùng "{{thuat_ngu_chuan}}"`

Tạo report với 2 phần:

### Phần 1: Inconsistencies theo thuật ngữ
Nhóm findings theo từng thuật ngữ trong glossary.
Chỉ list những thuật ngữ CÓ inconsistency — bỏ qua thuật ngữ consistent.

### Phần 2: Inconsistencies theo file
Nhóm lại theo file để dễ sửa.
Cho mỗi file: số lượng issues, danh sách sửa cụ thể.

### Summary
- Tổng số files scan
- Tổng số inconsistencies tìm được
- Top 3 thuật ngữ bị dùng sai nhiều nhất

Lưu report là `glossary-check-{{YYYY-MM-DD}}.md`.
```

**Expected output:** Report có thể action ngay — biết chính xác file nào, vị trí nào cần sửa thuật ngữ gì.

**Tips:**
- Glossary nên có column "Cũng chấp nhận" cho các thuật ngữ synonyms hợp lệ — tránh false positives.
- Sau khi nhận report, yêu cầu tiếp: "Dựa trên report này, tạo file `find-replace-commands.md` liệt kê các lệnh Find & Replace để fix tự động trong VS Code hoặc Word."
- Chạy glossary check định kỳ (monthly) trước khi có documentation release mới.

**Ví dụ:** Scan bộ tài liệu kỹ thuật 20 files theo style guide glossary — 30 thuật ngữ. Tìm 52 inconsistencies: "API endpoint" vs "API route" vs "endpoint" (3 cách gọi cho cùng concept) xuất hiện trong 11/20 files; "user guide" vs "user manual" vs "hướng dẫn người dùng" là top issue (8 variations). Report nhóm theo file: Writer A cần fix 18 chỗ, Writer B cần fix 24 chỗ. Dùng tiếp tip "tạo find-replace-commands.md" → fix hàng loạt trong VS Code.

> [!NOTE] **AMR Context**
> Áp dụng workflow này cho scan documentation AMR theo AMR glossary.
> Thay: glossary 45 thuật ngữ AMR chuẩn, scan 23 files, tìm 67 inconsistencies: "autonomous mobile robot" viết 5 cách; "charging station" vs "docking station" vs "trạm sạc" xuất hiện trong 12/23 files. Report nhóm theo file.

> [!TIP] **Model:** Sonnet 4.6 cho glossary scan — text comparison task, không cần deep reasoning. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## 4.6 Tạo training materials từ technical docs

[Ứng dụng Kỹ thuật]

Chuyển technical spec hoặc architecture doc thành training material phù hợp cho audience mới — không cần redesign từ đầu.

**Khi nào dùng:** Onboard kỹ thuật viên mới, tạo training cho khách hàng, hoặc khi cần trình bày technical content cho non-technical audience.

**Input:** Technical spec, architecture doc, hoặc internal documentation (`.md`, `.docx`, `.pdf`).

**Output:** Slide outline (`.md`) hoặc training guide (`.md`) có structure phù hợp với audience mới — sẵn sàng import vào PowerPoint hoặc dùng trực tiếp.

**Setup:**
- Xác định rõ audience: background của họ, điều họ cần biết, điều họ KHÔNG cần biết
- Đặt technical docs vào folder, có thể kèm `_audience-notes.md` mô tả audience profile

**Prompt:**

```text
Đọc tất cả tài liệu kỹ thuật trong folder này.

Tạo {{training guide .md / slide outline .md}} cho audience sau:
- Họ là: {{vi_du_ky_thuat_vien_moi_chua_co_background_ve_AMR}}
- Họ cần biết: {{vi_du_van_hanh_co_ban_va_xu_ly_su_co_thuong_gap}}
- Họ KHÔNG cần biết: {{vi_du_chi_tiet_thuat_toan_navigation_hoac_hardware_specs}}
- Thời gian training: {{vi_du_4_gio_hoac_2_buoi_x_2_gio}}

Nguyên tắc khi đơn giản hóa:
- Thay technical jargon bằng ngôn ngữ dễ hiểu (giải thích thuật ngữ khi lần đầu xuất hiện)
- Thêm analogies hoặc ví dụ thực tế khi cần
- Mỗi concept quan trọng: 1 "Key takeaway" rõ ràng
- Hands-on exercises: thêm ít nhất 1 exercise sau mỗi major section

{{neu_tao_slide_outline}}:
Mỗi slide gồm: tiêu đề, bullet points chính (max 5), speaker notes.
Ước tính thời gian cho mỗi section.
Lưu là `slide-outline-{{ten_chu_de}}-v1.0.md`.

{{neu_tao_training_guide}}:
Thêm "Check your understanding" questions cuối mỗi chapter.
Lưu là `training-guide-{{ten_chu_de}}-v1.0.md`.
```

**Expected output:** Training material dạng Markdown, đã calibrate cho audience cụ thể. Slide outline sẵn sàng import vào PowerPoint; training guide dùng được trực tiếp hoặc convert sang PDF.

**Tips:**
- Sau khi tạo xong, test bằng cách yêu cầu: "Giả sử bạn là {{audience_profile}}, đọc training guide này và liệt kê 5 điểm bạn vẫn chưa hiểu rõ."
- Sau khi có `slide-outline.md`, import vào PowerPoint bằng cách dùng Outline View (View → Outline) hoặc dùng add-in như Copilot/Beautiful.ai để auto-generate slides từ text.
- Thêm "Quiz cuối khóa" vào prompt để Claude tự tạo assessment questions từ nội dung training.

**Ví dụ:** Tạo onboarding guide cho technical writer mới từ Style Guide + SOP publishing workflow nội bộ. Input: Style Guide 15 trang (dành cho senior writers) + 3 SOP quy trình. Audience: biết viết nhưng chưa quen quy trình nội bộ. Output: Training Guide 4 chương (Toolchain → Style Rules → Publishing Workflow → Review Process), mỗi chương có "Check your understanding" 3 câu hỏi. Style Guide gốc dùng jargon "canonical source" → Training Guide giải thích bằng ngôn ngữ thực tế.

> [!NOTE] **AMR Context**
> Áp dụng workflow này cho tạo onboarding deck về AMR navigation.
> Thay: input là architecture doc 40 trang về SLAM và path planning. Audience là kỹ thuật viên cơ khí, không có background software. Output: slide outline 25 slides (AMR là gì → Navigation ở mức cao → Vận hành thực tế). "SLAM" giải thích bằng analogy "người đi trong phòng tối, vừa đi vừa vẽ bản đồ". Speaker notes gợi ý demo thực tế sau slide 15.

> [!TIP] **Model:** Sonnet 4.6 cho tạo training materials — restructure và simplify nội dung. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## 4.7 Extract data từ PDF/images batch

[Ứng dụng Kỹ thuật]

Đọc hàng loạt scan documents, receipts, hoặc forms và tổng hợp data vào một Excel file — thay cho việc nhập tay từng cái.

**Khi nào dùng:** Cần digitize stack documents giấy đã scan, extract data từ standardized forms, hoặc aggregate thông tin từ nhiều reports PDF.

**Input:** Folder chứa `.pdf`, `.png`, `.jpg` — scan của forms, reports, receipts.

**Output:** CSV file (`.csv`) tổng hợp data từ tất cả documents, một row per document — sẵn sàng import vào Excel hoặc Google Sheets.

**Setup:**
- Đảm bảo scan quality đủ tốt (300 DPI minimum cho text thường)
- Tạo file `_extraction-fields.md` liệt kê chính xác các fields cần extract
- Đặt tên files nguồn có ý nghĩa (vd: `2026-01-15-report-AMR001.pdf`) để tracking dễ hơn

**Prompt:**

```text
Extract data từ tất cả files {{.pdf / .png / .jpg}} trong folder này.

Fields cần extract (theo thứ tự columns trong Excel):
{{vi_du_danh_sach_cot}}:
- Document ID (tên file không có extension)
- Date (format: YYYY-MM-DD)
- {{ten_truong_1}} — tìm tại: {{vi_tri_tren_form_hoac_label}}
- {{ten_truong_2}} — tìm tại: {{vi_tri_tren_form_hoac_label}}
- [thêm fields...]
- Notes (bất kỳ thông tin bất thường hoặc không đọc được)

Quy tắc extraction:
- Nếu field không tìm thấy: ghi "N/A"
- Nếu không đọc được (poor scan quality): ghi "UNREADABLE"
- Nếu có nhiều giá trị trong một field: liệt kê cách nhau bằng dấu ";"
- Số: giữ nguyên format (không convert đơn vị)

Tạo 2 CSV files:
- `extracted-data-{{YYYY-MM-DD}}.csv` — data table chính (một row per document)
- `extracted-errors-{{YYYY-MM-DD}}.csv` — error log: documents có issues (UNREADABLE fields, missing data)

Cuối prompt: report summary — bao nhiêu documents processed, bao nhiêu có issues.
```

**Expected output:** 2 CSV files — data table chính và error log. Import vào Excel để filter/analysis; mở error log để biết documents nào cần manual review.

> [!WARNING] Accuracy cao với fields riêng lẻ trên scans chất lượng tốt. Line-item extraction từ bảng (tables) kém chính xác hơn đáng kể — luôn verify thủ công với loại data này trước khi dùng.

**Tips:**
- Chia batch thành nhóm 20 files để Claude xử lý ổn định hơn, merge Excel sheets sau.
- Với forms có layout chuẩn (tất cả cùng template), thêm "Đây là standardized form — layout giống nhau trong tất cả files" để tăng accuracy.
- Sau khi nhận Excel, chạy quick sanity check: "Xem sheet Error log và phân loại errors: OCR issues, blank fields, hay form khác template?"

**Ví dụ:** Extract thông tin từ 30 vendor quote forms PDF để tổng hợp procurement comparison. Mỗi form gồm: vendor name, quote date, line items (product, unit price, quantity, delivery time), payment terms. Claude extract 28/30 thành công, 2 vào error log (1 corrupt, 1 scan quá mờ để đọc số). Import CSV vào Excel → pivot table so sánh giá theo vendor, filter theo delivery time ≤ 30 ngày — tiết kiệm 4 giờ nhập tay thủ công.

> [!NOTE] **AMR Context**
> Áp dụng workflow này cho extract thông tin từ AMR test reports.
> Thay: 20 test report PDF, mỗi report gồm test date, AMR serial number, 7 test scenarios (pass/fail), tester name. 18/20 thành công, 2 vào error log (1 corrupt, 1 scan mờ). Import CSV để filter theo AMR serial hoặc scenario và phân tích pass rate trend.

> [!TIP] **Model:** Sonnet 4.6 cho data extraction — structured task từ scan documents. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## 4.8 Tổ chức folder dự án

[Ứng dụng Kỹ thuật]

Dọn dẹp folder lộn xộn: đặt naming convention, tạo structure chuẩn, và generate summary report — không cần xem từng file thủ công.

**Khi nào dùng:** Folder dự án nhiều người contribute, tích lũy nhiều năm, không có naming convention; hoặc cần chuẩn hóa trước khi bàn giao.

**Input:** Folder lộn xộn với mixed file types, tên không nhất quán, không có cấu trúc rõ ràng.

**Output:** Folder đã organize với structure chuẩn, files renamed, và summary report giải thích những gì đã thay đổi.

**Setup:**
- **Luôn backup trước** — Cowork sẽ move/rename files thực sự
- Tạo file `_organize-rules.md` chỉ định naming convention và folder structure mong muốn (nếu có)
- Nếu không có quy tắc riêng, Claude sẽ propose structure dựa trên content scan

**Prompt:**

```text
Phân tích cấu trúc folder này và tổ chức lại theo best practices.

Bước 1 — Scan và đề xuất (CHƯA thay đổi gì):
- Liệt kê tất cả files theo loại và topic
- Đề xuất folder structure mới
- Đề xuất naming convention
- Liệt kê files có thể duplicate hoặc outdated

Dừng và đợi confirmation trước khi bước 2.

{{sau_khi_confirm}}

Bước 2 — Thực hiện:
- Tạo folder structure đã đề xuất (hoặc đã điều chỉnh)
- Move files vào đúng folder
- Rename files theo naming convention: {{vi_du_YYYY-MM-DD_[category]_[description]}}
- Với files cũ/duplicate: move vào `_archive/` thay vì xóa

Bước 3 — Report:
Tạo `reorganization-report.md` gồm:
- Before/after folder structure (dạng tree)
- Danh sách tất cả files đã rename với mapping cũ → mới
- Files đã archive với lý do
- Files không chắc chắn (cần review thủ công)
```

**Expected output:** Folder clean với structure nhất quán. Report cho phép undo thủ công nếu cần (mapping cũ → mới được ghi rõ).

**Tips:**
- Dùng Bước 1 (đề xuất trước) là critical — xem qua trước khi cho Claude thực thi. Files bị rename không thể auto-undo.
- Move vào `_archive/` thay vì xóa — xóa chỉ sau khi đã verify không cần.
- Thêm "Đừng rename files đang open hoặc locked" nếu folder đang được dùng bởi người khác.

**Ví dụ:** Dọn folder documentation project (150+ files, 3 writers, 2 năm). Bước 1 — Claude scan phát hiện 18 duplicates, 30+ files tên `draft-final`/`v2-final`/`FINAL_USE_THIS`, không có naming convention. Đề xuất structure: `published/`, `drafts/`, `templates/`, `archive/`. Sau khi team confirm, Bước 2 — 150 files phân loại, 35 files vào archive, naming convention `YYYY-MM-DD_[doc-type]_[name].md` áp dụng thống nhất. Reorganization report mapping 115 files đã rename → mọi người biết ngay file cũ nằm ở đâu.

> [!NOTE] **AMR Context**
> Áp dụng workflow này cho dọn folder dự án AMR.
> Thay: folder AMR-500 (200+ files, 3 engineers). Bước 1 phát hiện 23 duplicates, 40+ files tên `final`/`final_v2`/`final_FINAL`, đề xuất structure `docs/`, `specs/`, `test-results/`, `archive/`. Bước 2: 200 files phân loại, 45 files vào archive, naming convention chuẩn hóa.

> [!TIP] **Model:** Sonnet 4.6 cho folder organization — scan và categorize files, không cần reasoning phức tạp. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## 4.9 Tạo release notes từ git history

[Ứng dụng Kỹ thuật]

Chuyển git log và changed files thành release notes readable cho stakeholders không có technical background.

**Khi nào dùng:** Chuẩn bị release mới, cần communicate changes cho khách hàng hoặc management, hoặc cần changelog cho documentation.

**Input:** Git log export (`.txt`) + danh sách changed files, và optionally PR descriptions hoặc ticket summaries.

**Output:** Release notes có cấu trúc — phù hợp cho stakeholders (non-technical) và internal team (technical).

**Setup:**
- Export git log: `git log v3.1..v3.2 --pretty=format:"%h %s %an %ad" > git-log.txt`
- Export changed files: `git diff v3.1..v3.2 --name-only > changed-files.txt`
- Đặt cả hai file vào folder làm việc
- Tùy chọn: thêm `_release-context.md` với business context (feature goals, known issues, migration notes)

**Prompt:**

```text
Đọc file `git-log.txt` và `changed-files.txt` trong folder này.

Tạo release notes cho version {{ten_version}} ({{date_release}}).

**Phần 1 — Release Notes cho Stakeholders** (non-technical)
Audience: {{vi_du_project_manager_khach_hang}}
- Tone: professional, plain language, không có commit hashes hay file paths
- Nhóm changes theo impact: "New features", "Improvements", "Bug fixes"
- Với mỗi item: mô tả benefit cho người dùng (không phải mô tả code change)
- Thêm "Breaking changes" section nếu có

**Phần 2 — Changelog kỹ thuật** (internal)
Audience: developers, QA team
- Format: Keep a Changelog standard
- Liệt kê đầy đủ với commit references
- Nhóm: Added / Changed / Deprecated / Removed / Fixed / Security

**Phần 3 — Migration guide** (nếu có breaking changes)
- Từng bước user cần làm để upgrade
- Known issues và workarounds

Lưu output là `RELEASE-NOTES-{{version}}.md`.
```

**Expected output:** Hai-tier release notes — stakeholder-friendly summary ở phần 1, technical changelog đầy đủ ở phần 2.

**Tips:**
- Commit messages viết tốt (conventional commits: `feat:`, `fix:`, `docs:`) giúp Claude categorize chính xác hơn. Nếu commits messy, thêm context trong `_release-context.md`.
- Sau khi nhận output, yêu cầu: "Phần stakeholder notes có dùng technical terms nào không? Nếu có, replace bằng ngôn ngữ business."
- Với releases lớn, yêu cầu Claude tạo thêm "one-liner summary" (1 câu) phù hợp cho email announcement.

**Ví dụ:** Release notes cho documentation toolchain update v2.1 — Vale linter + MkDocs upgrade + 5 custom validation rules mới. Git log 31 commits từ 2 contributors. Claude phân loại: 5 new rules (features), 8 config improvements, 11 bug fixes, 7 refactoring (không mention cho stakeholders). Stakeholder section: "Validation chạy nhanh hơn 40%", "Thêm check tự động cho broken links". Technical changelog 31 entries theo Keep a Changelog. One-liner email announcement: "Vale v2.1 ra mắt — validation nhanh hơn 40%, thêm 5 rules mới."

> [!NOTE] **AMR Context**
> Áp dụng workflow này cho release notes AMR firmware.
> Thay: git log 47 commits từ 4 developers. 8 new features, 12 improvements, 19 bug fixes, 8 refactoring (không mention cho stakeholders). Stakeholder section focus vào "tránh obstacle nhanh hơn 30%" và "giảm thời gian charge scheduling". Technical changelog 47 entries theo Keep a Changelog.

> [!TIP] **Model:** Sonnet 4.6 cho release notes — categorize và rephrase commits. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## 4.10 Meeting prep — tổng hợp context trước cuộc họp

[Ứng dụng Kỹ thuật]

Tổng hợp tất cả background information thành một briefing ngắn gọn trước meeting — thay vì đọc lại email và notes cũ.

**Khi nào dùng:** Trước meeting quan trọng (client review, sprint planning, technical design review), cần nắm context nhanh từ nhiều nguồn.

**Input:** Folder chứa previous meeting notes, project docs, email threads (export dạng `.txt`), action items từ lần trước.

**Output:** Briefing document 1–2 trang: context, key decisions đã có, open items, suggested agenda.

**Setup:**
- Tạo folder `meeting-prep/{{ten_meeting}}/`
- Đặt vào đó: meeting notes cũ, email exports, relevant specs, action items tracker
- Tên files nên có date prefix để Claude hiểu chronology

**Prompt:**

```text
Đọc tất cả tài liệu trong folder này. Tạo briefing cho meeting "{{ten_meeting}}" vào {{ngay_gio}}.

Participants: {{danh_sach_nguoi_tham_gia_va_vai_tro}}
Duration: {{vi_du_60_phut}}
Meeting goal: {{vi_du_review_deployment_plan_va_confirm_go_live_date}}

Briefing cần có:

### Background (5 phút đọc)
- Project status hiện tại — 3–5 bullets
- Key decisions đã được confirm (không cần rediscuss)
- Changes quan trọng kể từ meeting trước

### Open Items cần resolve trong meeting này
Cho mỗi item:
- Item: mô tả ngắn
- Context: tại sao chưa resolve được
- Options (nếu đã có): các hướng giải quyết đang xem xét
- Owner: ai cần đưa ra decision

### Action items từ meeting trước — Status update
Liệt kê action items của meeting trước và status hiện tại.

### Suggested Agenda ({{thoi_gian_meeting}} phút)
Timeline cụ thể cho meeting, dựa trên open items ưu tiên.

### Thông tin cần confirm trước meeting
Những gì bạn nên verify/chuẩn bị trước khi vào meeting.

Lưu briefing là `briefing-{{YYYY-MM-DD}}-{{ten_meeting_viet_tat}}.md`.
```

**Expected output:** Briefing document ngắn gọn, ai đọc 5 phút cũng nắm được full context. Agenda suggest giúp meeting có structure từ đầu.

**Tips:**
- Export email threads sang `.txt` (Gmail: Print → Save as PDF → extract text; Outlook: Save as `.msg` rồi yêu cầu Claude đọc). Format không quan trọng — Claude handle được.
- Sau khi nhận briefing, forward cho participants: "Đây là briefing cho meeting ngày X, vui lòng đọc trước." Giảm thời gian catch-up trong meeting.
- Với recurring meetings (weekly sync), tạo template folder và reuse cấu trúc — chỉ cần thêm materials mới mỗi tuần.

**Ví dụ:** Prep cho quarterly documentation review meeting với product team. Folder chứa: 3 meeting notes từ Q1–Q3, action items tracker, documentation coverage report, 2 email threads về scope changes. Briefing: Background nêu 8/12 modules đã updated, 4 modules cần rework vì product thay đổi spec. Open Items: 3 decisions cần product team confirm (scope Module 09, timeline API docs, reviewer assignment). Suggested Agenda 45 phút: 10 phút status → 25 phút open items → 10 phút next steps. Team vào meeting với full context, không cần 15 phút catch-up.

> [!NOTE] **AMR Context**
> Áp dụng workflow này cho prep weekly sync với khách hàng về AMR deployment.
> Thay: folder chứa 3 meeting notes, 2 email threads (issues escalation), Gantt PDF, action items tracker. Briefing: 2 milestones đã pass, 1 delay (AMR-003 firmware), 3 open items cần decision. Suggested Agenda 60 phút: 10 phút status → 30 phút open items → 15 phút Q&A → 5 phút next steps.

> [!TIP] **Model:** Sonnet 4.6 cho meeting prep — tổng hợp và cấu trúc thông tin. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## 4.11 Incident report từ raw data

[Ứng dụng Kỹ thuật]

Tạo incident report chuyên nghiệp từ raw data lộn xộn (error logs, screenshots, timeline notes) — đúng format và đủ thông tin để submit.

**Khi nào dùng:** Sau khi xảy ra incident (system failure, safety event, deployment issue), cần document đúng quy trình.

**Input:** Folder chứa error logs, screenshots (nếu Claude có vision access), timeline notes, và bất kỳ raw data liên quan đến incident.

**Output:** Incident report đầy đủ: root cause analysis, impact assessment, resolution steps, và prevention measures.

**Setup:**
- Gom tất cả raw data vào folder `incident-{{YYYY-MM-DD}}-{{mo_ta_ngan}}/`
- Tạo `_incident-timeline.md` ghi thô timeline (giờ:phút, sự kiện) — không cần format đẹp
- Nếu có incident report template của công ty/khách hàng, đặt vào folder với tên `_template.*`

**Prompt:**

```text
Đọc tất cả tài liệu và logs trong folder này.

Tạo incident report cho incident: "{{mo_ta_ngan_incident}}" xảy ra lúc {{thoi_diem}}.

Incident Report Structure:

### 1. Incident Summary
- Incident ID: {{INC-YYYY-MMDD-XXX}}
- Severity: {{Critical / High / Medium / Low}} — đề xuất dựa trên impact
- Status: {{Resolved / In Progress}}
- Duration: {{thoi_gian_tu_phat_hien_den_resolved}}

### 2. Timeline
Reconstruct timeline đầy đủ từ logs và notes.
Format: `[HH:MM] Event description (Source: filename)`

### 3. Root Cause Analysis
- Immediate cause (gì đã trigger incident)
- Contributing factors (điều kiện cho phép incident xảy ra)
- Root cause (lý do sâu xa nhất)

### 4. Impact Assessment
- Systems/processes affected
- Duration of impact
- Users/operations affected
- Estimated impact (nếu có data để ước lượng)

### 5. Resolution
- Actions taken (với timestamp từ timeline)
- Resolution confirmation

### 6. Prevention Measures
- Immediate actions (trong 1 tuần)
- Long-term improvements (trong 1 tháng)
- Process changes recommended

{{neu_co_template}}: Điền vào template `_template.*` thay vì format trên.

Lưu là `incident-report-{{INC-ID}}.md`.
```

**Expected output:** Incident report hoàn chỉnh, có thể submit ngay hoặc sau minimal editing. Timeline được reconstruct từ logs, root cause được phân tích đầy đủ.

**Tips:**
- Nếu timeline không rõ ràng, yêu cầu Claude "Chỉ reconstruct timeline từ timestamps trong logs — đánh dấu [ESTIMATED] cho events không có timestamp rõ ràng."
- Root cause analysis: thêm "Dùng 5-Whys technique để phân tích root cause" vào prompt nếu muốn analysis sâu hơn.
- Sau khi tạo report, review kỹ phần Prevention Measures — đây là phần quan trọng nhất nhưng Claude có thể đề xuất chung chung. Hỏi thêm: "Với mỗi prevention measure, ai là owner và deadline cụ thể?"

**Ví dụ:** Incident report cho documentation portal outage — MkDocs build failure khiến knowledge base phục vụ nội dung stale trong 6 giờ. Folder chứa: build logs, deployment pipeline output, notes của on-call engineer. Claude reconstruct timeline 15 events từ 09:12 đến 15:47. Root cause: dependency conflict giữa Vale plugin mới và MkDocs version hiện tại, không được test trên staging trước khi deploy. Impact: 120 users truy cập tài liệu cũ, 3 support tickets sai hướng. Prevention: thêm staging validation step + pin dependency versions trong pipeline.

> [!NOTE] **AMR Context**
> Áp dụng workflow này cho AMR collision incident report.
> Thay: folder chứa navigation error log (500 dòng), camera footage timestamps, maintenance log, voice memo của operator. Claude reconstruct timeline 23 events từ 14:15 đến 14:47. Root cause: obstacle detection threshold thay đổi trong maintenance ca sáng nhưng không logged vào change management. Prevention: mandatory change log step trong maintenance SOP + alert khi safety parameters thay đổi.

> [!TIP] **Model:** Sonnet 4.6 cho incident report thông thường. Chuyển Opus 4.6 khi logs phức tạp, nhiều hệ thống tương tác cần phân tích root cause sâu. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## 4.12 So sánh documents (Diff report)

[Ứng dụng Kỹ thuật]

So sánh 2 phiên bản của cùng một tài liệu và tạo diff report rõ ràng — highlight changes theo loại (addition, deletion, modification) và đánh giá impact.

**Khi nào dùng:** Review SOP trước khi approve, track changes giữa document versions, hoặc so sánh kết quả trước/sau khi edit.

**Input:** 2 files của cùng tài liệu — version cũ và version mới (bất kỳ format nào: `.docx`, `.md`, `.txt`, `.pdf`).

**Output:** Diff report với changes được categorize, highlighted, và đánh giá impact level.

**Setup:**
- Đặt tên file rõ ràng: `document-v1.md` và `document-v2.md` (hoặc dùng date: `document-2026-01.md` vs `document-2026-03.md`)
- Nếu chỉ muốn diff một section cụ thể, note trong `_diff-scope.md`

**Prompt:**

```text
So sánh file `{{ten_file_cu}}` (version cũ) với `{{ten_file_moi}}` (version mới).

Tạo diff report với cấu trúc:

### Summary
- Tổng số changes: [số additions, deletions, modifications]
- Sections bị thay đổi nhiều nhất
- Overall assessment: minor revision / major revision / structural overhaul

### Changes theo loại

**Additions** (nội dung mới trong version mới):
- [Section/Heading] — Nội dung được thêm
- Impact: {{vi_du_thong_tin_moi_co_the_anh_huong_gi}}

**Deletions** (nội dung có trong version cũ, không còn trong version mới):
- [Section/Heading] — Nội dung bị xóa
- Lý do xóa (nếu suy ra được từ context)

**Modifications** (nội dung được sửa đổi):
- [Section/Heading] — Thay đổi cụ thể (format: "Cũ: ... → Mới: ...")
- Impact: significance của thay đổi

**Formatting/Structure changes** (nếu có):

### Risk Assessment
Liệt kê changes có thể gây impact tiêu cực nếu không verify:
- Changes mâu thuẫn với tài liệu khác
- Thông tin bị xóa mà có thể vẫn cần
- Changes chưa rõ lý do

### Recommendation
Approve / Request revision / Needs discussion — với lý do ngắn gọn.

Lưu report là `diff-report-{{ten_file}}-v1-vs-v2.md`.
```

**Expected output:** Diff report actionable — reviewer biết chính xác cần check gì, không cần đọc cả hai documents.

**Tips:**
- Thêm "Ignore changes về formatting và whitespace — chỉ report content changes" nếu muốn focus vào nội dung.
- Với SOP diff trước approval: "Đặc biệt chú ý changes trong Safety warnings và critical procedures — flag bất kỳ thay đổi nào trong những sections này dù nhỏ."
- Nếu muốn side-by-side view: "Với mỗi modification, tạo table 2 cột: Cũ | Mới" — dễ đọc hơn cho reviewers không quen format diff.

**Ví dụ:** So sánh User Guide v1 vs v2 trước khi publish — v2 được viết lại sau product update. Diff phát hiện: v2 thêm 3 sections mới (onboarding flow mới, API v2 endpoints, FAQ), sửa 8 screenshots không còn match UI, xóa "Legacy Import" section (flag risk — cần verify nếu users vẫn cần tính năng này). Overall: major revision. Recommendation: "Approve với condition — confirm Legacy Import section có thể xóa trước khi publish."

> [!NOTE] **AMR Context**
> Áp dụng workflow này cho so sánh SOP AMR trước khi approval.
> Thay: SOP-charging-v1.md (12 bước) vs SOP-charging-v2.md (14 bước). Diff phát hiện: v2 thêm 2 bước safety check, sửa thứ tự bước 7 và 8, xóa warning note ở bước 10 (flag risk — cần verify lý do xóa trước khi approve).

> [!TIP] **Model:** Sonnet 4.6 cho diff report — text comparison, không cần reasoning phức tạp. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## Tổng kết — Chọn workflow phù hợp

Bảng dưới giúp chọn workflow nhanh theo loại task:

| Task | Workflow | Thời gian ước tính |
|------|----------|--------------------|
| Viết tài liệu mới từ notes | 4.1 Viết SOP | 10–20 phút |
| Review nhiều tài liệu cùng lúc | 4.2 Batch review | 5–10 phút |
| Báo cáo tuần từ logs | 4.3 Báo cáo tuần | 5–10 phút |
| Migrate Word ↔ Markdown | 4.4 Convert batch | 5–15 phút |
| Kiểm tra thuật ngữ | 4.5 Glossary check | 10–15 phút |
| Tạo training material | 4.6 Training materials | 15–30 phút |
| Digitize scan documents | 4.7 Extract data | 10–20 phút |
| Dọn folder dự án | 4.8 Tổ chức folder | 15–30 phút |
| Release notes từ git | 4.9 Release notes | 5–10 phút |
| Prep trước meeting | 4.10 Meeting prep | 5–10 phút |
| Viết incident report | 4.11 Incident report | 10–20 phút |
| So sánh 2 versions | 4.12 Diff report | 5–10 phút |

---

**Modules liên quan:**
- [Doc Workflows](01-doc-workflows.md) — General recipes cho mọi interface
- [Template Library](02-template-library.md) — Doc-specific templates
- [Evaluation Framework](../base/07-evaluation.md) — Rubric dùng trong 4.2
- [Cowork Setup](03-cowork-setup.md) — Setup và cấu hình Cowork

---

← [Cowork Setup](03-cowork-setup.md) | [Tổng quan](../base/00-overview.md) | [Claude Code Doc →](05-claude-code-doc.md)
