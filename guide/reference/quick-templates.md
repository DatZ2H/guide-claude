# Quick Start Templates (T-01 ~ T-05)

**Cập nhật:** 2026-03-07

Năm templates cơ bản dùng ngay không cần tùy chỉnh nhiều. Phù hợp cho người mới bắt đầu. Copy template, thay `{{placeholder}}`, paste vào Claude.

[Nguồn: Anthropic Docs - Prompting Best Practices]

---

## Bảng Index

| Mã | Tên Template | Dùng khi |
|----|-------------|----------|
| **T-01** | Tóm tắt tài liệu | Tóm tắt document đính kèm |
| **T-02** | Giải thích Error | Phân tích error log |
| **T-03** | Viết Email báo cáo | Email tiến độ project |
| **T-04** | Tạo Checklist | Checklist vận hành/kiểm tra |
| **T-05** | So sánh Giải pháp | Compare options, ra quyết định |

Templates chuyên sâu (T-06~T-22): xem [Doc Template Library](../doc/02-template-library.md).

---

## T-01: Tóm tắt tài liệu

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

**Ví dụ — tóm tắt Release Notes v3.2:**

```xml
<task>Tóm tắt Release Notes v3.2 đính kèm.</task>
<requirements>
- Độ dài: Tối đa 200 từ
- Cấu trúc:
  1. Tổng quan release (2 câu)
  2. Breaking changes (nếu có)
  3. Tính năng mới chính (tối đa 5 items)
  4. Action items cho team
</requirements>
<input_data>{{paste_release_notes_pdf}}</input_data>
```

> [!NOTE] **AMR Context** — Tóm tắt AMR Fleet Management User Manual v4.0 thành Quick Reference Card cho kỹ thuật viên triển khai.

> [!TIP] **Model:** Sonnet 4.6 — Đủ mạnh cho summarization. Xem [decision flowchart](model-specs.md#chọn-model)

---

## T-02: Giải thích Error

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

**Ví dụ — lỗi trong docs build pipeline:**

```xml
<context>
- Hệ thống: MkDocs documentation site
- Môi trường: GitHub Actions CI/CD
</context>
<error_log>
ERROR - Config value 'nav': The following pages exist in the docs directory,
but are not included in the "nav" configuration: 'guide/07-template-library.md'
</error_log>
```

> [!NOTE] **AMR Context** — Phân tích ROS Navigation Stack error khi AMR mất định vị: `[ERROR] [amcl]: Failed to transform initial pose in time`.

> [!TIP] **Model:** Sonnet 4.6 — Pattern matching và log analysis không cần Opus. Xem [decision flowchart](model-specs.md#chọn-model)

---

## T-03: Viết Email báo cáo

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

**Ví dụ — email báo cáo milestone documentation:**

Placeholder values: Người nhận: Lead Engineer | Project: AMR Fleet Documentation v5.0 | Giai đoạn: Internal Review | Tiến độ: 85% | Tuần tới: hoàn thiện Module 07–11.

> [!NOTE] **AMR Context** — Email báo cáo tiến độ hoàn thiện bộ tài liệu AMR trước đợt commissioning, gửi cho Project Manager và Safety Officer.

> [!TIP] **Model:** Sonnet 4.6 — Standard writing task. Xem [decision flowchart](model-specs.md#chọn-model)

---

## T-04: Tạo Checklist

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

**Ví dụ — checklist review tài liệu trước publish:**

```xml
<task>Tạo checklist kiểm tra tài liệu kỹ thuật trước khi publish.</task>
<context>
- Thiết bị: AMR Technical Documentation Package
- Mục đích: Pre-publish quality check
- Người thực hiện: Technical Writer / Reviewer
</context>
<requirements>
- Nhóm theo categories (Content, Format, Cross-references, Safety Warnings)
- Tổng thời gian kiểm tra: không quá 20 phút
</requirements>
```

> [!NOTE] **AMR Context** — Checklist kiểm tra AMR trước khi deploy vào warehouse: battery level, sensor calibration, emergency stop, network connectivity.

> [!TIP] **Model:** Sonnet 4.6 — Structured list generation. Xem [decision flowchart](model-specs.md#chọn-model)

---

## T-05: So sánh Giải pháp

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

**Ví dụ — so sánh documentation tools:**

Placeholder values: Option A: MkDocs + Material theme | Option B: Confluence | Criteria: Git integration, offline access, search quality, cost.

> [!NOTE] **AMR Context** — So sánh 2 thuật toán localization: AMCL vs. Cartographer cho AMR hoạt động trong warehouse bán động — để quyết định approach cho dự án.

> [!TIP] **Model:** Sonnet 4.6 — Comparison với criteria rõ ràng. Dùng Opus nếu quyết định có tác động kiến trúc lớn. Xem [decision flowchart](model-specs.md#chọn-model)
