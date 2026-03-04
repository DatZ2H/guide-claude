# Module 07: Template Library

**Thời gian đọc:** 15 phút (tra cứu) | **Mức độ:** Mọi level
**Cập nhật:** 2026-03-01 | Models: xem [specs](reference/model-specs.md)

---

Module này tập trung **tất cả 22 templates** vào một nơi duy nhất. Các module khác tham chiếu đến đây bằng mã **T-XX**.

**Cách sử dụng:**

1. Tìm template phù hợp qua **Bảng Index** bên dưới
2. Copy template
3. Thay `{{placeholder}}` bằng giá trị thực tế
4. Paste vào Claude

---

## Bảng Index tra cứu nhanh

| Mã | Tên Template | Category | Dùng khi |
|----|-------------|----------|----------|
| **T-01** | Tóm tắt tài liệu | Quick Start | Tóm tắt document đính kèm |
| **T-02** | Giải thích Error | Quick Start | Phân tích error log |
| **T-03** | Viết Email báo cáo | Quick Start | Email tiến độ project |
| **T-04** | Tạo Checklist | Quick Start | Checklist vận hành/kiểm tra |
| **T-05** | So sánh Giải pháp | Quick Start | Compare options, ra quyết định |
| **T-06** | User Manual Section | Technical Docs | Viết section cho user manual |
| **T-07** | Technical Specification | Technical Docs | Tạo technical spec document |
| **T-08** | Error Analysis | Troubleshooting | Phân tích lỗi có cấu trúc |
| **T-09** | Diagnostic Guide | Troubleshooting | Tạo hướng dẫn chẩn đoán lỗi |
| **T-10** | Code Review Request | Code Review | Review code có structured output |
| **T-11** | Standard Operating Procedure | SOP & Procedures | Tạo SOP hoàn chỉnh |
| **T-12** | Incident Report | Reports & Analysis | Báo cáo sự cố + RCA |
| **T-13** | Handover Summary | Workflow | Tóm tắt conversation để chuyển tiếp |
| **T-14** | Context Extraction | Workflow | Trích xuất 1 topic từ conversation dài |
| **T-15** | Chain Prompt | Workflow | Prompt chain nhiều bước |
| **T-16** | Tạo file Word | File Creation | Tạo .docx professional |
| **T-17** | Tạo file Excel | File Creation | Tạo .xlsx với formatting |
| **T-18** | Tạo file PowerPoint | File Creation | Tạo .pptx presentation |
| **T-19** | Task Decomposition Planner | Workflow | Lên kế hoạch tách task trước chain prompt |
| **T-20** | In-Progress Review Checklist | Workflow | Checklist review giữa các bước theo loại output |
| **T-21** | Multi-file Consistency Check | Workflow | Kiểm tra consistency sau khi sửa nhiều files |
| **T-22** | Cowork Task Plan | Cowork | Prompt Package cho Cowork task phức tạp |

---

## 7.1 Quick Start Templates (T-01 đến T-05)

Năm templates cơ bản dùng ngay không cần tùy chỉnh nhiều. Phù hợp cho người mới bắt đầu.

### T-01: Tóm tắt tài liệu

```xml
<task>
Tóm tắt tài liệu kỹ thuật đính kèm.
</task>

<requirements>
- Độ dài: Tối đa 500 từ
- Cấu trúc:
  1. Tổng quan (2-3 câu)
  2. Điểm chính (bullet points)
  3. Hạn chế/Lưu ý (nếu có)
  4. Đề xuất hành động tiếp theo
</requirements>

<input_data>
{{paste_noi_dung_tai_lieu_hoac_dinh_kem_file}}
</input_data>
```

### T-02: Giải thích Error

```xml
<task>
Phân tích error log sau và đề xuất cách khắc phục.
</task>

<context>
- Hệ thống: {{ten_he_thong}}
- Môi trường: {{moi_truong}}
</context>

<error_log>
{{paste_error_log}}
</error_log>

<requirements>
Trả lời theo cấu trúc:
1. **Nguyên nhân có thể:** (liệt kê theo xác suất từ cao đến thấp)
2. **Bước kiểm tra:** (numbered steps)
3. **Cách khắc phục:** (cho từng nguyên nhân)
4. **Phòng ngừa:** (nếu có)
</requirements>
```

### T-03: Viết Email báo cáo

```xml
<task>
Viết email báo cáo tiến độ project.
</task>

<context>
- Người gửi: {{ten_ban}} | Người nhận: {{ten_nguoi_nhan}} ({{chuc_vu}})
- Project: {{ten_project}} | Giai đoạn: {{giai_doan}}
</context>

<content_to_include>
- Tiến độ hoàn thành: {{phan_tram}}%
- Công việc đã hoàn thành: {{liet_ke}}
- Công việc đang thực hiện: {{liet_ke}}
- Vấn đề/Rủi ro: {{liet_ke_neu_co}}
- Kế hoạch tuần tới: {{liet_ke}}
</content_to_include>

<requirements>
- Tone: Professional, ngắn gọn
- Độ dài: Tối đa 200 từ
- Format: Email chuẩn với Subject, Body
</requirements>
```

### T-04: Tạo Checklist

```xml
<task>
Tạo checklist kiểm tra trước khi vận hành {{ten_thiet_bi}}.
</task>

<context>
- Thiết bị: {{ten_thiet_bi}}
- Mục đích: {{muc_dich_van_hanh}}
- Người thực hiện: {{vai_tro}}
</context>

<requirements>
- Format: Checklist với checkbox [ ]
- Nhóm theo categories (Hardware, Software, Safety)
- Mỗi item có criteria pass/fail rõ ràng
- Tổng thời gian kiểm tra: không quá {{so_phut}} phút
</requirements>
```

### T-05: So sánh Giải pháp

```xml
<task>
So sánh 2 giải pháp sau và đề xuất lựa chọn.
</task>

<options>
**Option A:** {{mo_ta_option_A}}
**Option B:** {{mo_ta_option_B}}
</options>

<evaluation_criteria>
- {{criteria_1}}
- {{criteria_2}}
- {{criteria_3}}
- {{criteria_4}}
</evaluation_criteria>

<requirements>
- Format: Bảng so sánh + Phân tích
- Kết luận: Đề xuất option với lý do
- Đề cập trade-offs của mỗi option
</requirements>
```

---

## 7.2 Technical Documentation Templates (T-06, T-07)

### T-06: User Manual Section

```xml
<role>
Technical Writer chuyên viết tài liệu cho robot công nghiệp.
</role>

<task>
Viết section "{{section_name}}" cho User Manual của {{product_name}}.
</task>

<context>
- Sản phẩm: {{product_name}} ({{brief_description}})
- Audience: {{target_audience}}
- Technical level: {{level}}
</context>

<section_requirements>
- Subsections cần include: {{list_subsections}}
- Độ dài: {{word_count}} words
</section_requirements>

<style_guide>
- Ngôn ngữ: Tiếng Việt, thuật ngữ kỹ thuật giữ tiếng Anh
- Mỗi procedure có: Purpose, Prerequisites, Steps, Expected result
- Include: CẢNH BÁO cho safety, LƯU Ý cho tips
</style_guide>
```

### T-07: Technical Specification

```xml
<role>
Systems Engineer chuyên viết technical specifications.
</role>

<task>
Tạo Technical Specification cho {{system_component}}.
</task>

<context>
- System: {{system_name}}
- Component: {{component_name}}
- Purpose: {{component_purpose}}
- Interfaces with: {{related_systems}}
</context>

<spec_requirements>
Sections bắt buộc:
1. Overview
2. Functional Requirements
3. Technical Requirements (Performance, Interfaces, Environmental)
4. Constraints
5. Dependencies
6. Acceptance Criteria
</spec_requirements>

<output_format>
- Tables cho specifications
- Clear numbering (REQ-001, REQ-002...)
- Bullet points cho requirements
</output_format>
```

---

## 7.3 Troubleshooting Templates (T-08, T-09)

### T-08: Error Analysis

```xml
<role>
Senior Robotics Engineer với 10 năm kinh nghiệm troubleshooting AMR.
</role>

<task>
Phân tích error sau và đề xuất solutions.
</task>

<system_info>
- System: {{system_name}}
- Software version: {{version}}
- Environment: {{environment}}
- Last known good state: {{last_good_state}}
</system_info>

<error_details>
<error_message>{{error_message}}</error_message>
<error_log>{{relevant_logs}}</error_log>
<symptoms>{{observed_symptoms}}</symptoms>
</error_details>

<analysis_instructions>
Phân tích step-by-step:
1. Error interpretation -- Error message nghĩa là gì?
2. Possible causes -- Liệt kê theo xác suất
3. Diagnostic steps -- Cách verify từng cause
4. Solutions -- Cho từng cause
5. Prevention -- Cách tránh trong tương lai
</analysis_instructions>

<output_format>
## Error Analysis Report
### 1. Error Summary
### 2. Possible Causes (bảng: #, Cause, Probability, Evidence)
### 3. Diagnostic Steps (numbered, có expected result)
### 4. Solutions (bảng: Cause, Solution, Effort, Risk)
### 5. Prevention
</output_format>
```

### T-09: Diagnostic Guide

```xml
<role>
Technical Support Engineer chuyên tạo diagnostic guides.
</role>

<task>
Tạo Diagnostic Guide cho issue: {{issue_type}}
</task>

<context>
- System: {{system_name}}
- Issue category: {{category}}
- Common symptoms: {{symptoms}}
- Target user: {{who_will_use}}
</context>

<guide_requirements>
Structure:
1. Symptom identification (checklist)
2. Quick checks (< 5 min, IF...THEN format)
3. Detailed diagnostics (flowchart hoặc decision tree)
4. Resolution steps (numbered)
5. Escalation criteria
</guide_requirements>
```

---

## 7.4 Code Review Template (T-10)

### T-10: Code Review Request

```xml
<role>
Senior {{language}} Engineer với kinh nghiệm {{domain}}.
</role>

<task>
Review code sau và provide feedback.
</task>

<code_context>
- Language: {{language}}
- Framework: {{framework}}
- Purpose: {{code_purpose}}
</code_context>

<code language="{{language}}">
{{PASTE_CODE_HERE}}
</code>

<review_criteria>
1. Correctness: Logic errors, bugs
2. Performance: Efficiency, resource usage
3. Readability: Naming, structure, comments
4. Maintainability: Modularity, DRY
5. Best Practices: {{framework}} conventions
6. Error Handling: Edge cases, exceptions
</review_criteria>

<output_format>
## Summary: [Approve/Request Changes/Reject]
## CRITICAL (Must Fix) -- bảng: Line, Issue, Suggested Fix
## WARNING (Should Fix) -- bảng: Line, Issue, Suggested Fix
## OK (Nice to Fix) -- bảng: Line, Issue, Suggested Fix
## Positive Aspects
## Recommendations
</output_format>
```

---

## 7.5 SOP Template (T-11)

### T-11: Standard Operating Procedure

```xml
<role>
Technical Writer chuyên viết SOPs cho môi trường sản xuất.
</role>

<task>
Tạo SOP cho: {{procedure_name}}
</task>

<sop_context>
- Thiết bị/System: {{equipment}}
- Phòng ban: {{department}}
- Người thực hiện: {{performer_role}}
- Tần suất: {{frequency}}
- Thời gian ước tính: {{estimated_time}}
</sop_context>

<procedure_details>
{{description_or_notes}}
</procedure_details>

<sop_template>
# SOP: {{procedure_name}}
**Document ID:** SOP-{{id}} | **Version:** {{version}}
**Effective Date:** {{date}} | **Review Date:** {{review_date}}

## 1. Mục đích (Purpose)
## 2. Phạm vi (Scope) -- áp dụng/không áp dụng
## 3. Trách nhiệm (Responsibilities) -- bảng: Vai trò, Trách nhiệm
## 4. Định nghĩa & Thuật ngữ -- bảng
## 5. Thiết bị & Vật liệu -- checklist
## 6. An toàn (Safety Precautions) -- CẢNH BÁO
## 7. Quy trình (Procedure) -- 7.1 Chuẩn bị, 7.2 Thực hiện, 7.3 Kết thúc
   Mỗi step có: Action, Expected result, Time
## 8. Xử lý sự cố -- bảng: Vấn đề, Nguyên nhân, Giải pháp
## 9. Tài liệu liên quan
## 10. Lịch sử thay đổi -- bảng: Version, Date, Changes, Author
</sop_template>
```

---

## 7.6 Reports & Analysis Template (T-12)

### T-12: Incident Report

```xml
<role>
Quality Engineer chuyên viết incident reports.
</role>

<task>
Tạo Incident Report cho sự cố: {{incident_summary}}
</task>

<incident_info>
- Date/Time: {{datetime}}
- Location: {{location}}
- System affected: {{system}}
- Severity: {{severity}}
</incident_info>

<incident_details>
What happened: {{description}}
Impact: {{impact}}
Immediate actions taken: {{actions_taken}}
</incident_details>

<report_template>
# Incident Report -- INC-{{id}}
## 1. Incident Summary -- bảng metadata
## 2. Description -- chi tiết sự cố
## 3. Impact Assessment -- bảng: Impact Area, Description, Severity
## 4. Timeline of Events -- bảng: Time, Event
## 5. Root Cause Analysis
   5.1 Immediate Cause
   5.2 Contributing Factors
   5.3 Root Cause
## 6. Corrective Actions -- bảng: Action, Owner, Due Date, Status
## 7. Preventive Actions -- bảng: Action, Owner, Due Date
## 8. Lessons Learned
## 9. Approvals -- bảng: Role, Name, Date
</report_template>
```

---

## 7.7 Workflow Templates (T-13, T-14, T-15)

### T-13: Handover Summary

**Dùng khi:** Conversation đạt 40-50+ messages, cần chuyển sang conversation mới.

```xml
<task>
Tóm tắt conversation hiện tại để handover sang conversation mới.
</task>

<context>
- Project: {{ten_project_hoac_topic}}
- Mục đích: Chuẩn bị context cho conversation tiếp theo
</context>

<summarize_instructions>
Tóm tắt theo cấu trúc:
1. **Topic chính:** (1 câu)
2. **Đã thảo luận:** (tối đa 5 key points, mỗi point 1-2 câu)
3. **Quyết định đã đưa ra:** (decision + rationale)
4. **Outputs đã tạo:** (files, code, documents nếu có)
5. **Vấn đề tồn đọng:** (issues chưa resolve)
6. **Next steps:** (action items, thứ tự ưu tiên)
7. **Technical details quan trọng:** (configs, parameters đã thống nhất)
</summarize_instructions>

<output_format>
Format để copy trực tiếp vào conversation mới.
Markdown với headings rõ ràng.
Chỉ output summary, không giải thích.
</output_format>
```

### T-14: Context Extraction

**Dùng khi:** Conversation có nhiều topics, chỉ cần context về 1 topic cụ thể.

```xml
<task>
Trích xuất context liên quan đến "{{specific_topic}}" từ conversation này.
</task>

<extraction_focus>
**Chỉ extract thông tin về:** {{specific_topic}}
**Bỏ qua:** Discussions không liên quan, small talk, thông tin đã outdated
</extraction_focus>

<output_requirements>
1. Output paste trực tiếp được vào conversation mới
2. Đủ context để tiếp tục task mà không cần conversation cũ
3. Giữ nguyên technical details (numbers, configs, code snippets)
4. Không dư thừa thông tin không liên quan
</output_requirements>
```

### T-15: Chain Prompt

**Dùng khi:** Task phức tạp cần chia thành nhiều bước.

**Step 1:**

```xml
<chain_info>
Step: 1 of {{total_steps}}
Purpose: {{step_purpose}}
</chain_info>

<task>
{{step_1_task}}
</task>

<output_for_next_step>
Format output để dễ sử dụng trong step tiếp theo.
</output_for_next_step>
```

**Step N (lặp lại):**

```xml
<chain_info>
Step: {{n}} of {{total_steps}}
</chain_info>

<input_from_previous>
{{output_tu_step_truoc}}
</input_from_previous>

<task>
{{step_n_task}}
</task>
```

**Workflow:** Chạy Step 1 > Copy output > Paste vào input Step 2 > Lặp lại.
Tip: Với chain ≥ 3 bước phức tạp, dùng T-19 (Task Decomposition Planner) để map scope và dependencies trước khi bắt đầu — xem mục 7.8.

---

## 7.8 Advanced Workflow Templates (T-19, T-20, T-21, T-22)

Bốn templates này dành cho workflow phức tạp nhiều bước và nhiều files — mở rộng từ T-13/T-14/T-15 cho các use cases nâng cao hơn khi scope lớn, dependencies nhiều, hoặc cần kiểm soát chất lượng chặt chẽ giữa các bước.

---

### T-19: Task Decomposition Planner

**Dùng khi:** Trước khi bắt đầu chain prompt ≥ 3 bước — để map scope, dependencies, và review checkpoints.

```xml
<task>
Giúp tôi lên kế hoạch tách task sau thành chain prompt hợp lý.
</task>

<task_description>
{{mo_ta_task_tong_the_can_lam}}
</task_description>

<output_desired>
{{mo_ta_output_cuoi_cung_files_documents_artifacts_cu_the}}
</output_desired>

<constraints>
- Môi trường: {{Chat / Cowork}}
- Thời gian: {{uoc_luong}}
- Files liên quan: {{liet_ke_neu_co}}
</constraints>

<planning_instructions>
Tạo Task Map với:
1. Số steps tối thiểu cần thiết (không tách thừa)
2. Với mỗi step:
   - Mục tiêu step (1 câu)
   - Input cần có (từ step trước hoặc từ tôi)
   - Output sẽ tạo ra
   - Review checkpoint: kiểm tra gì trước khi sang step tiếp
3. Dependencies: step nào phải xong trước step nào
4. Risk: step nào có rủi ro cao nhất, tại sao
</planning_instructions>

<output_format>
Bảng Markdown + dependency notes.
Sau bảng: 1 đoạn nhận xét ngắn về approach.
</output_format>
```

---

### T-20: In-Progress Review Checklist

**Dùng khi:** Sau mỗi bước trong chain prompt hoặc Cowork task — trước khi tiếp tục bước tiếp theo.

```xml
<task>
Review output vừa tạo trước khi tôi tiếp tục bước tiếp theo.
</task>

<output_type>
{{Document/Report | Restructured file | Data/Table | Config suggestion | Multi-file edit}}
</output_type>

<step_context>
- Đây là bước: {{so}} / {{tong_so_buoc}}
- Mục tiêu bước này: {{mo_ta}}
- Output vừa tạo: {{mo_ta_ngan}}
</step_context>

<review_instructions>
Kiểm tra output theo các tiêu chí sau (trả lời PASS / WARN / FAIL cho mỗi tiêu chí):
1. Completeness: Output có đủ nội dung theo yêu cầu bước này không?
2. Accuracy: Có thông tin nào bạn không chắc chắn không? Đánh dấu.
3. Consistency: Format và terminology có nhất quán không?
4. Ready for next step: Output có đủ để làm input cho bước tiếp theo không?

Sau đó đưa ra một trong 3 quyết định:
- CONTINUE: Tất cả PASS → sẵn sàng bước tiếp
- FIX THEN CONTINUE: Có WARN → liệt kê cần sửa gì, sau đó tiếp tục
- RESTART THIS STEP: Có FAIL → giải thích tại sao cần làm lại bước này
</review_instructions>
```

---

### T-21: Multi-file Consistency Check

**Dùng khi:** Sau khi sửa xong một nhóm files — kiểm tra consistency toàn bộ.

Dùng ở 3 thời điểm: trước khi sửa (impact analysis), sau khi sửa (cascade update), sau khi hoàn thành (verification).

**Phần 1: Impact Analysis** — dùng TRƯỚC khi sửa

```xml
<task>
Impact analysis trước khi tôi sửa file/nội dung.
</task>

<planned_change>
File sẽ sửa: {{ten_file}}
Nội dung sẽ thay đổi: {{mo_ta_thay_doi_vi_du_section_10.7_doi_thanh_10.8}}
</planned_change>

<instructions>
Scan toàn bộ thư mục. Liệt kê:
1. Files nào có reference đến {{noi_dung_se_thay_doi}}
2. Với mỗi file: reference cụ thể ở đâu (section, dòng, context)
3. Ước lượng effort update mỗi file: Thấp / Trung bình / Cao
Chưa sửa gì — chỉ report.
</instructions>
```

**Phần 2: Cascade Update** — dùng SAU khi sửa

```xml
<task>
Cascade update sau khi tôi đã sửa file.
</task>

<completed_change>
File đã sửa: {{ten_file}}
Thay đổi: {{noi_dung_cu}} → {{noi_dung_moi}}
</completed_change>

<instructions>
Scan toàn bộ thư mục. Tìm và update tất cả chỗ còn reference đến {{noi_dung_cu}}.
Với mỗi chỗ tìm được: sửa ngay, sau đó báo cáo đã sửa gì ở file nào.
</instructions>
```

**Phần 3: Final Verification** — dùng sau khi hoàn thành tất cả

```xml
<task>
Verification check sau khi hoàn thành tất cả edits.
</task>

<scope>
Files đã sửa trong session này: {{danh_sach}}
</scope>

<check_instructions>
Kiểm tra toàn bộ thư mục:
1. Cross-references: tất cả "xem [file/section]" còn valid không?
2. Terminology: {{term_A}}, {{term_B}} có nhất quán không?
3. Version/date: headers đã update ở tất cả files đã sửa chưa?
4. Index: README/master list có phản ánh đúng state hiện tại không?
Report: file nào cần fix, cụ thể là gì.
</check_instructions>
```

---

### T-22: Cowork Task Plan (Prompt Package)

**Dùng khi:** Lên kế hoạch cho Cowork project phức tạp (≥ 4 files hoặc ≥ 2 sessions).

**Cách dùng:** Điền vào template này trong Chat hoặc text editor TRƯỚC khi mở Cowork.

```markdown
# Cowork Task Plan — {{Ten_Project}}

**Ngày:** {{YYYY-MM-DD}}
**Tổng số tasks:** {{N}}
**Backup:** {{da_backup_chua_Git_commit_hash_hoac_backup_folder}}

## File Inventory

| File | Hành động | Dependency |
|------|-----------|------------|
| {{file_A}} | Sửa | Không có |
| {{file_B}} | Tạo mới | Cần file A xong trước |
| {{file_C}} | Chỉ đọc | — |

## Task 1: {{Ten_task}}

**Dependency:** {{None / Task_X_phai_xong}}
**Files sẽ sửa:** {{danh_sach}}
**Files tham khảo:** {{danh_sach}}

**Prompt:**
{{viet_prompt_day_du_o_day_copy_paste_thang_vao_Cowork}}

**Validation sau task này:**
- [ ] {{dieu_kien_1}}
- [ ] {{dieu_kien_2}}

---

## Task 2: {{Ten_task}}

**Dependency:** Task 1 phải complete và validated
**Input:** {{handover_file_hoac_mo_ta}}

**Prompt:**
{{viet_prompt_day_du_o_day}}

**Validation sau task này:**
- [ ] {{dieu_kien_1}}
- [ ] {{dieu_kien_2}}
```

---

## 7.9 File Creation Templates (T-16, T-17, T-18)

### T-16: Tạo file Word (.docx)

```
Tạo file Word (.docx) cho {{loai_tai_lieu}}:

Thông tin:
- {{noi_dung_chinh}}

Format:
- Header: {{thong_tin_header}}
- Table of contents
- Professional formatting với heading styles
- Bảng summary ở trang đầu
- Page numbers ở footer
- Font: Times New Roman hoặc Arial

Lưu với tên: {{ten_file}}.docx
```

**Lưu ý:** Cần bật "Code execution and file creation" trong Settings > Capabilities.

### T-17: Tạo file Excel (.xlsx)

```
Tạo file Excel (.xlsx) cho {{muc_dich}}:

Columns:
- {{column_1}}: {{kieu_du_lieu}}
- {{column_2}}: {{kieu_du_lieu}}
- {{column_3}}: {{kieu_du_lieu}}

Thêm:
- Conditional formatting: {{quy_tac_mau}}
- Filter on all columns
- Summary sheet với dashboard
- Formulas: {{cong_thuc_can_thiet}}

Lưu với tên: {{ten_file}}.xlsx
```

### T-18: Tạo file PowerPoint (.pptx)

```
Tạo file PowerPoint (.pptx) cho {{muc_dich_presentation}}.

Nội dung {{so_slides}} slides:
1. {{slide_1_title}}: {{noi_dung}}
2. {{slide_2_title}}: {{noi_dung}}
...

Style: clean, professional, ít text trên mỗi slide, dùng diagrams khi có thể.
Màu chủ đạo: {{mau_sac}}

Lưu với tên: {{ten_file}}.pptx
```

---

## Cách tùy chỉnh Templates

Mọi template đều có thể mở rộng bằng cách thêm các module tùy chọn (xem Module 03, mục 3.4):

| Cần thêm | Module XML | Ví dụ |
|----------|-----------|-------|
| Ví dụ mẫu | `<examples>` | Thêm 1-2 ví dụ output mong muốn |
| Kiểm soát chất lượng | `<quality_requirements>` | Yêu cầu đánh dấu [FACT] / [INFERENCE] |
| Kiểm soát độ dài | `<length_control>` | Giới hạn word count |
| Quy trình step-by-step | `<step_by_step>` | Yêu cầu reasoning từng bước |
| Xử lý edge cases | `<edge_cases>` | Định nghĩa cách xử lý trường hợp đặc biệt |

**Ví dụ:** Thêm quality control vào T-08 (Error Analysis):

```xml
<!-- Thêm sau </output_format> của T-08 -->
<quality_requirements>
- Đánh dấu [FACT] cho thông tin từ log/data
- Đánh dấu [INFERENCE] cho suy luận của bạn
- Nếu không chắc chắn, nói rõ và đề xuất cách verify
</quality_requirements>
```

---

**Tiếp theo:**

- Module 03: Prompt Engineering -- hiểu sâu 6 nguyên tắc và 7 kỹ thuật đằng sau các templates
- Module 05: Workflow Recipes -- quy trình hoàn chỉnh sử dụng các templates
