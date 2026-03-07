# Doc Template Library

**Thời gian đọc:** 15 phút (tra cứu) | **Mức độ:** Mọi level
**Cập nhật:** 2026-03-07 | Models: xem [specs](../reference/model-specs.md)

---
depends-on: [reference/model-specs, base/03-prompt-engineering, doc/01-doc-workflows]
impacts: [base/03-prompt-engineering, doc/01-doc-workflows, base/06-mistakes-fixes, doc/04-cowork-workflows]
---

Templates chuyên sâu cho documentation tasks — Technical Docs, Troubleshooting, SOP, Reports, và Workflows. Copy template, thay `{{placeholder}}`, paste vào Claude.

> [!NOTE] Giả định đã đọc [base/](../base/). Templates cơ bản (T-01~T-05) nằm ở [Quick Start Templates](../reference/quick-templates.md).

[Ứng dụng Kỹ thuật]

---

## Bảng Index tra cứu nhanh

| Mã | Tên Template | Category | Dùng khi |
|----|-------------|----------|----------|
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

## 2.1 Technical Documentation Templates (T-06, T-07)

[Ứng dụng Kỹ thuật]

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

**Ví dụ — AMR PNX-100 User Manual, section "Emergency Stop":**

Placeholder values: section_name: Emergency Stop Procedures | product_name: AMR PNX-100 | audience: Warehouse operators | technical level: Non-technical | subsections: Types of E-Stop, Trigger conditions, Recovery procedure.

> [!NOTE] **AMR Context** — Viết section "Emergency Stop Procedures" cho AMR PNX-100 User Manual. Audience: warehouse operator không có background ROS — dùng ngôn ngữ đơn giản, nhiều hình minh họa.

> [!TIP] **Model:** Sonnet 4.6 — Structured technical writing. Dùng Opus nếu section phức tạp liên quan nhiều subsystem tương tác. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

> [!TIP] **Skill:** `/doc-standard-enforcer` — Enforce writing standards trước khi finalize section.

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

**Ví dụ — Technical Spec cho AMR Navigation Module:**

Placeholder values: system_component: Navigation & Localization Module | system_name: PNX AMR Fleet v3 | component_purpose: Autonomous navigation trong môi trường semi-structured | interfaces_with: Sensor fusion module, Fleet Management System, Safety controller.

> [!NOTE] **AMR Context** — Spec cho SLAM module: localization accuracy ≤ 5 cm, max replan latency ≤ 200 ms, environmental constraints (dynamic obstacles, narrow aisles), interfaces với sensor array và safety controller.

> [!TIP] **Model:** Opus 4.6 — Complex system specs với nhiều cross-functional requirements cần reasoning sâu về constraints và acceptance criteria. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## 2.2 Troubleshooting Templates (T-08, T-09)

[Ứng dụng Kỹ thuật]

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

**Ví dụ — AMR mất định vị sau firmware update:**

Placeholder values: System: PNX AMR Fleet v3.2.0 | Error: `NavigationException: Failed to find a valid plan. Tolerance: 0.5` | Last known good state: AMR hoạt động bình thường trên firmware v3.1.2, map đã load thành công.

> [!NOTE] **AMR Context** — Phân tích `LIDAR_TIMEOUT` error trên AMR sau firmware update — output của template này trở thành input cho Incident Report (T-12).

> [!TIP] **Model:** Sonnet 4.6 — Structured error analysis với log patterns. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

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

**Ví dụ — guide cho kỹ thuật viên mới xử lý localization failure:**

Placeholder values: issue_type: AMR mất định vị giữa hành trình | system_name: PNX AMR v3 | common_symptoms: AMR dừng đột ngột, đèn báo lỗi đỏ, Fleet Manager hiển thị "Localization Lost" | target_user: Field technician không có ROS background.

> [!NOTE] **AMR Context** — Diagnostic Guide "AMR dừng giữa hành trình không rõ nguyên nhân": tích hợp vào AMR Maintenance Manual, section Troubleshooting — dùng được bởi kỹ thuật viên warehouse không cần training ROS.

> [!TIP] **Model:** Sonnet 4.6 — Structured guide writing với decision tree. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

> [!TIP] **Skill:** `/doc-standard-enforcer` — Kiểm tra writing standards trước khi tích hợp vào maintenance manual.

---

## 2.3 Code Review Template (T-10)

[Ứng dụng Kỹ thuật]

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

**Ví dụ — review Python ROS2 navigation node:**

Placeholder values: language: Python | domain: ROS2 Navigation | code_purpose: Custom cost function cho global planner — ưu tiên tránh zone nguy hiểm trong warehouse.

> [!NOTE] **AMR Context** — Review Python node xử lý sensor fusion data trước khi merge vào main branch. Kết quả review được document hóa thành code review record cho audit trail.

> [!TIP] **Model:** Sonnet 4.6 — Standard code review. Dùng Opus cho review kiến trúc phức tạp hoặc safety-critical code. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## 2.4 SOP Template (T-11)

[Ứng dụng Kỹ thuật]

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

**Ví dụ — SOP thay pin AMR:**

Placeholder values: procedure_name: AMR Battery Replacement | equipment: PNX AMR-100, Docking Station DS-200, Battery Pack BP-48V | department: Maintenance Team | frequency: Mỗi 8 giờ vận hành hoặc khi SoC < 15% | estimated_time: 10 phút.

> [!NOTE] **AMR Context** — SOP cho AMR firmware update procedure: bao gồm backup config, update sequence, validation test, và rollback plan nếu update thất bại.

> [!TIP] **Model:** Sonnet 4.6 — Structured procedural writing với format cố định. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

> [!TIP] **Skill:** `/doc-standard-enforcer` — Validate SOP format và safety warning conventions trước khi submit cho approval.

---

## 2.5 Reports & Analysis Template (T-12)

[Ứng dụng Kỹ thuật]

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

**Ví dụ — báo cáo sự cố AMR va chạm:**

Placeholder values: incident_summary: AMR va chạm với pallet di động tại Zone B | datetime: 2026-02-15 14:32 | location: Warehouse Zone B, Row 7 | system: PNX AMR Fleet #3 | severity: Medium | impact: Hàng hóa bị đổ, dừng hoạt động 45 phút.

> [!NOTE] **AMR Context** — Incident report sau khi AMR dừng khẩn cấp do obstacle detection failure — đầu vào cho monthly safety review và corrective action tracking (CAPA process).

> [!TIP] **Model:** Sonnet 4.6 — Structured report với format cố định, không cần reasoning phức tạp. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## 2.6 Workflow Templates (T-13, T-14, T-15)

[Ứng dụng Kỹ thuật]

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

**Ví dụ — handover sau session viết documentation:**

Placeholder values: project: AMR Fleet Documentation v5.0 — Module 07 Template Library | Đã thảo luận: cấu trúc 22 templates, pattern documentation context, AMR use cases | Next steps: validate-doc 07, cross-module review.

> [!NOTE] **AMR Context** — Handover sau session thiết kế AMR navigation parameters: carry đủ context (map version, tuning values, test results, open issues) sang conversation mới tiếp tục tuning.

> [!TIP] **Model:** Sonnet 4.6 — Summarization task không cần reasoning phức tạp. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

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

**Ví dụ — extract context về documentation decisions:**

Placeholder values: specific_topic: Navigation parameter tuning cho Warehouse Zone A | Bỏ qua: thảo luận về Zone B, hardware issues không liên quan.

> [!NOTE] **AMR Context** — Extract toàn bộ context liên quan đến SLAM config từ conversation dài về AMR deployment — để dùng riêng trong conversation viết technical spec.

> [!TIP] **Model:** Sonnet 4.6 — Extraction và filtering task. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

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
Tip: Với chain ≥ 3 bước phức tạp, dùng T-19 (Task Decomposition Planner) để map scope và dependencies trước khi bắt đầu — xem mục [2.7](#t-19-task-decomposition-planner).

**Ví dụ — chain 3 bước viết AMR Emergency Response Guide:**

Step 1: Extract incidents từ incident reports có sẵn → danh sách scenarios | Step 2: Draft procedures cho từng scenario theo SOP format (T-11) | Step 3: Format consistency check và cross-reference với User Manual.

> [!NOTE] **AMR Context** — Chain viết AMR Emergency Response Guide: (1) extract từ incident reports, (2) draft procedures theo T-11, (3) format và cross-reference với User Manual.

> [!TIP] **Model:** Sonnet 4.6 — Dùng nhất quán cho cả chain để tránh inconsistency giữa các steps. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## 2.7 Advanced Workflow Templates (T-19, T-20, T-21, T-22)

[Ứng dụng Kỹ thuật]

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

**Ví dụ — lên kế hoạch viết documentation package:**

Placeholder values: task_description: Viết complete documentation package cho AMR PNX-100 deployment | output_desired: User Manual (8 sections), 5 SOPs, Emergency Response Guide, 3 Quick Reference Cards | Môi trường: Cowork | Thời gian: 3 sessions | Files: existing technical spec, incident reports, maintenance logs.

> [!NOTE] **AMR Context** — Decompose task viết AMR Maintenance Manual (8 chapters) thành chain có dependencies rõ ràng và review checkpoints sau mỗi chapter nhóm — tránh viết sai thứ tự gây cascade edits.

> [!TIP] **Model:** Sonnet 4.6 — Planning và decomposition task. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

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

**Ví dụ — review draft SOP sau khi viết xong:**

Placeholder values: output_type: Document/Report | Đây là bước 2/4 | Mục tiêu: Draft SOP AMR Battery Replacement hoàn chỉnh | Output vừa tạo: 12 steps, chưa có safety warnings section.

> [!NOTE] **AMR Context** — Review bước draft Emergency Procedures trước khi sang bước validate với Safety Officer — đảm bảo tất cả CẢNH BÁO safety đã include và không có bước nào thiếu Expected Result.

> [!TIP] **Model:** Sonnet 4.6 — Checklist-based review với criteria rõ ràng. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

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

**Ví dụ — sau khi update firmware version trong docs:**

Phần 1 scenario: File sẽ sửa: `technical-spec.md` | Thay đổi: Firmware version "v3.1.2" → "v3.2.0" | Cần check: User Manual, SOP Firmware Update, SOP Battery, Quick Reference Cards, Incident Report template.

> [!NOTE] **AMR Context** — Sau khi update navigation parameter defaults trong Technical Spec, scan toàn bộ SOPs và diagnostic guides có reference đến parameters này để update cascade.

> [!TIP] **Model:** Sonnet 4.6 — Scan và update tasks. Dùng Opus nếu scope lớn (>10 files) và cần reasoning về semantic consistency. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

> [!TIP] **Skill:** `/cross-ref-checker` — Kiểm tra cross-references tự động trong module guide.

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

**Ví dụ — plan cho AMR Documentation Sprint:**

Placeholder values: Ten_Project: AMR PNX-100 Documentation Sprint | Tổng số tasks: 4 | File Inventory: technical-spec.md (sửa), user-manual.md (tạo mới), sop-battery.md (tạo mới), emergency-guide.md (tạo mới) | Backup: Git commit `abc1234` trước khi bắt đầu.

> [!NOTE] **AMR Context** — Lên plan cho session viết complete AMR documentation set trước commissioning: 4 tasks có dependencies, 2 sessions Cowork, checkpoint sau mỗi task.

> [!TIP] **Model:** Sonnet 4.6 — Planning task. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## 2.8 File Creation Templates (T-16, T-17, T-18)

[Nguồn: Anthropic Help Center - Code execution and file creation] [Cập nhật 03/2026]

### T-16: Tạo file Word (.docx)

```text
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

**Ví dụ — export Technical Spec sang Word:**

Placeholder values: loai_tai_lieu: Technical Specification | noi_dung_chinh: AMR PNX-100 Navigation Module Spec (output từ T-07) | ten_file: AMR-PNX100-NavSpec-v1.0.

> [!NOTE] **AMR Context** — Export Technical Spec (T-07) hoặc SOP (T-11) sang Word để gửi cho stakeholders không dùng Markdown — đặc biệt hữu ích khi submit tài liệu cho khách hàng.

> [!TIP] **Model:** Sonnet 4.6 — File generation task. Cần bật "Code execution and file creation" trong Settings > Capabilities. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

### T-17: Tạo file Excel (.xlsx)

```text
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

**Ví dụ — AMR Fleet Maintenance Tracker:**

Placeholder values: muc_dich: AMR Fleet Maintenance Schedule 2026 | Columns: AMR ID (text), Last Service Date (date), Next Service Date (date), Battery Cycles (number), Status (dropdown: OK/Due/Overdue), Technician (text) | Conditional formatting: đỏ nếu Next Service Date < today.

> [!NOTE] **AMR Context** — Tracking sheet cho battery cycle count và maintenance schedule của toàn bộ AMR fleet — export hàng tuần để dispatch team lên kế hoạch bảo trì.

> [!TIP] **Model:** Sonnet 4.6 — File generation task. Cần bật "Code execution and file creation" trong Settings > Capabilities. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

### T-18: Tạo file PowerPoint (.pptx)

```text
Tạo file PowerPoint (.pptx) cho {{muc_dich_presentation}}.

Nội dung {{so_slides}} slides:
1. {{slide_1_title}}: {{noi_dung}}
2. {{slide_2_title}}: {{noi_dung}}
...

Style: clean, professional, ít text trên mỗi slide, dùng diagrams khi có thể.
Màu chủ đạo: {{mau_sac}}

Lưu với tên: {{ten_file}}.pptx
```

**Ví dụ — AMR Deployment Progress Report:**

Placeholder values: muc_dich: Stakeholder briefing sau commissioning phase 1 | so_slides: 8 | Slides: (1) Executive Summary, (2) System Architecture, (3) Commissioning Status, (4) KPIs vs. Targets, (5) Issues & Mitigations, (6) Timeline Phase 2, (7) Budget Snapshot, (8) Q&A | Màu: xanh navy + trắng.

> [!NOTE] **AMR Context** — Presentation cho management review sau AMR fleet commissioning phase 1: show uptime, incident count, throughput improvement vs. manual.

> [!TIP] **Model:** Sonnet 4.6 — File generation task. Cần bật "Code execution and file creation" trong Settings > Capabilities. Xem [decision flowchart](../reference/model-specs.md#chọn-model)

---

## Cách tùy chỉnh Templates

Mọi template đều có thể mở rộng bằng cách thêm các module tùy chọn (xem [Prompt Engineering, mục 3.4](../base/03-prompt-engineering.md#34-module-system-nâng-cao-advanced)):

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

**Xem thêm:**

- [Prompt Engineering](../base/03-prompt-engineering.md) -- hiểu sâu 6 nguyên tắc và 7 kỹ thuật đằng sau các templates
- [Doc Workflows](01-doc-workflows.md) -- quy trình hoàn chỉnh sử dụng các templates
- [Quick Start Templates (T-01~T-05)](../reference/quick-templates.md) -- templates cơ bản dùng ngay

---

← [Doc Workflows](01-doc-workflows.md) | [Tổng quan](../base/00-overview.md) | [Cowork Setup →](03-cowork-setup.md)
