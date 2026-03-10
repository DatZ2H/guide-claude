# Cheatsheet — Base Tier

**Cập nhật:** 2026-03-07 | Quick-reference card cho guide/base/ (Modules 00–07)

[Nguồn: Tổng hợp từ guide/base/] [Cập nhật 03/2026]

> [!TIP]
> Cheatsheet này là bảng tra cứu nhanh — mỗi mục link về module gốc để đọc chi tiết.

---

## 1. Prompt Engineering — Công thức & Patterns

### 1.1 Công thức C-T-R

```text
C = Context   (tình huống, đối tượng, bối cảnh)
T = Task      (hành động cụ thể cần làm)
R = Requirements (format, độ dài, tone, ràng buộc)
```

Xem chi tiết: [base/03 — Prompt Engineering](../base/03-prompt-engineering.md#32-sáu-nguyên-tắc-cốt-lõi)

### 1.2 XML Module System — 13 tags

| Tag | Mục đích | Bắt buộc? |
|-----|---------|:---------:|
| `<role>` | Chuyên môn cụ thể | — |
| `<task>` | Hành động cần thực hiện | ✅ |
| `<context>` | Bối cảnh, thông tin nền | ✅ |
| `<requirements>` | Ràng buộc output (format, độ dài) | — |
| `<output_format>` | Cấu trúc mong muốn (JSON, bảng...) | — |
| `<examples>` | Input/output mẫu (multishot) | — |
| `<constraints>` | Điều KHÔNG được làm | — |
| `<thinking_instructions>` | Hướng dẫn suy luận | — |
| `<quality_requirements>` | Tiêu chuẩn chính xác | — |
| `<tone>` | Giọng điệu / phong cách | — |
| `<input_data>` | Dữ liệu cần xử lý | — |
| `<evaluation_criteria>` | Tiêu chí đánh giá / so sánh | — |
| `<chain_info>` | Context cho multi-prompt | — |

Xem chi tiết: [base/03 — 13-Module System](../base/03-prompt-engineering.md#34-module-system-nâng-cao-advanced)

### 1.3 Six Core Principles

| # | Nguyên tắc | Ghi nhớ |
|---|-----------|---------|
| 1 | Be Clear & Specific | Giả sử Claude chưa biết context của bạn |
| 2 | Use Examples | 3–5 examples tốt hơn 1000 từ giải thích |
| 3 | Chain of Thought | Hướng dẫn suy luận cho bài toán phức tạp |
| 4 | Iterative Refinement | Kỳ vọng cải thiện, không cần hoàn hảo lần 1 |
| 5 | Leverage Knowledge | Không giải thích CS cơ bản — focus vấn đề cụ thể |
| 6 | Assign Role | "Senior Technical Writer" > "writer" |

### 1.4 Task Decomposition — Khi nào tách prompt?

| Output dự kiến | Rủi ro | Hành động |
|---------------|--------|-----------|
| < 800 từ | Thấp | 1 prompt đủ |
| 800–1500 từ | TB | Theo dõi chất lượng, cân nhắc tách |
| 1500–3000 từ | Cao | Dùng Outline-First pattern |
| > 3000 từ | Rất cao | Bắt buộc tách, 1–2 section/prompt |

**Outline-First pattern:** Tạo outline trước → Review → Viết từng section → Review tổng thể.

Xem chi tiết: [base/03 — Task Decomposition](../base/03-prompt-engineering.md#35-task-decomposition-khi-nào-và-cách-tách-task-advanced)

### 1.5 Prompt theo loại task

| Loại task | Modules XML cần dùng |
|----------|---------------------|
| Content Creation | role + task + context + requirements + output_format |
| Document Analysis | task + context + input_data + quality_requirements |
| Data Analysis | task + context + input_data + requirements |
| Brainstorming | task + context + constraints + evaluation_criteria |
| Quality Control | task + context + quality_requirements + input_data |
| Code Review | role + task + context + input_data + output_format + constraints |
| SOP Generation | role + task + context + requirements + output_format + constraints |

### 1.6 Variable naming

```text
Đúng:   {{machine_id}}, {{error_log}}, {{sensor_data}}
Sai:    {{Machine Id}}, {{errorLog}}, {{SensorData}}
```

---

## 2. Context Management

### 2.1 Token specs

| Model | Context window | Tương đương |
|-------|:--------------:|------------|
| Opus / Sonnet 4.6 | 200K (1M beta) | ~500–700 trang |
| Sonnet 4.5 | 200K | ~500–700 trang |
| Haiku 4.5 | 200K | ~500–700 trang |

**Quy đổi:** 1 token ~ 4 ký tự Anh | 1–2 ký tự Việt | Code tốn token hơn prose.

### 2.2 Conversation length — Khi nào hành động?

| Messages | Trạng thái | Hành động |
|:--------:|-----------|-----------|
| 1–30 | Tối ưu | Tiếp tục bình thường |
| 31–50 | Theo dõi | Quan sát dấu hiệu drift |
| 51–70 | Cảnh báo | Dùng Context Refresh |
| > 70 | Handover | Tạo conversation mới |

### 2.3 Context Drift — 5 dấu hiệu

1. Claude hỏi lại thông tin đã cung cấp
2. Câu trả lời mâu thuẫn nhau
3. Format thay đổi bất ngờ (bullets → numbers)
4. Claude quên ràng buộc đã đặt
5. Fixate vào 1 giải pháp duy nhất

### 2.4 Context Refresh template

```xml
<context_refresh>
**Mục tiêu chính:** {{goal}}
**Đã hoàn thành:** {{completed_items}}
**Quyết định đã chốt:** {{decisions}}
**Ràng buộc:** {{constraints}}
**Task hiện tại:** {{current_task}}
</context_refresh>
```

### 2.5 Handover — 3 kiểu

| Kiểu | Khi nào | Cách làm |
|------|---------|----------|
| Simple | Chuyển chủ đề mới | 2–3 câu tóm tắt |
| Full | Cùng chủ đề, chat dài | Dùng Template T-13 |
| Selective | Trích 1 subtopic | Dùng Template T-14 |

### 2.6 Session Lifecycle — 3 surfaces

| | Claude.ai Chat | Cowork | Claude Code |
|--|---------------|--------|-------------|
| **Init** | Memory + Project Instructions | Folder Instructions (CLAUDE.md) | SessionStart hook + git log |
| **Work** | 30+ msg = watch drift | File system = memory | /checkpoint = git commit |
| **Manage** | Context Refresh / Handover | Tạo task mới khi xong | /compact khi cần |
| **Persist** | Memory auto-update | Files + git history | CLAUDE.md + Git |

Xem chi tiết: [base/04 — Context Management](../base/04-context-management.md)

---

## 3. Model Selection

| Câu hỏi | Model |
|---------|-------|
| Task đơn giản (Q&A, format, brainstorm)? | **Sonnet 4.6** |
| Suy luận phức tạp (debug, kiến trúc, code review)? | **Opus 4.6** |
| Cần nhanh, task đơn giản? | **Haiku 4.5** |

Xem chi tiết: [base/05 — Tools & Features](../base/05-tools-features.md)

---

## 4. Tools — Khi nào dùng gì?

| Tool | Dùng khi | Token cost |
|------|---------|:----------:|
| Extended Thinking | Debug phức tạp, phân tích multi-system | Cao |
| Web Search | Thông tin hiện tại, fact verification | TB |
| Research | Deep dive, nhiều nguồn | Cao |
| File Upload | Phân tích tài liệu cụ thể | TB |
| File Creation | Tạo Word/Excel/PPT/PDF | TB |
| Artifacts | Code, diagrams, components | TB |
| MCP Connectors | Truy cập dịch vụ bên ngoài | TB |

**Extended Thinking tips:**
- Tự động chain-of-thought khi bật — KHÔNG cần thêm "think step-by-step"
- Dùng cho: debugging, analysis, comparison, multi-system review
- Bỏ qua cho: Q&A, formatting, brainstorm đơn giản

### 4 Preset Styles

| Style | Use case | Tone |
|-------|---------|------|
| Normal | Mặc định, cân bằng | Professional |
| Concise | Q&A, tra cứu | Direct, ngắn |
| Explanatory | Học tập, onboarding | Educational |
| Formal | Docs khách hàng, báo cáo | Authoritative |

Xem chi tiết: [base/05 — Tools & Features](../base/05-tools-features.md)

---

## 5. File Handling

### 5.1 Upload limits

| Loại | Formats | Max size |
|------|---------|:--------:|
| Documents | PDF, DOCX, TXT, MD, HTML | 30MB |
| Code | PY, JS, JSON, YAML, XML | 30MB |
| Images | PNG, JPG, WEBP, GIF | 30MB |
| Data | CSV, XLSX | 30MB |

Max 20 files/lần upload.

### 5.2 Phương thức tối ưu

| Tình huống | Cách tốt nhất |
|-----------|--------------|
| Code < 50 dòng | Paste trực tiếp |
| Error log < 100 dòng | Paste trực tiếp |
| Full source file | Upload file |
| Tài liệu có format | Upload file |
| Dùng lại nhiều lần | Project Knowledge |

Xem chi tiết: [base/01 — Quick Start](../base/01-quick-start.md)

---

## 6. Common Mistakes — 7 nhóm lỗi

| # | Nhóm lỗi | Ví dụ | Fix nhanh |
|---|----------|-------|----------|
| 1 | Prompt mơ hồ | "Viết cái gì đó về robots" | Thêm scope, audience, format |
| 2 | Kỳ vọng sai | Nghĩ Claude nhớ qua chats | Dùng Projects, Handover |
| 3 | Quản lý chat kém | 80 messages, 3 chủ đề | Context Refresh, chat mới |
| 4 | Dùng tool sai | Extended thinking cho Q&A | Chọn tool phù hợp |
| 5 | Giới hạn model | Hallucination, sycophancy | quality_requirements, Self-check |
| 6 | Lỗi lan truyền | Outline sai → SOP sai → review sai | Validate mỗi bước |
| 7 | Claude Code specific | Kitchen sink, correcting loop | Xem [dev/04](../dev/04-agents-automation.md) |

### Chống hallucination

```xml
<quality_requirements>
- [FACT] chỉ cho thông tin đã xác minh
- [INFERENCE] cho suy luận
- [CẦN VERIFY] cho thông tin chưa chắc
- Nói "Tôi không biết" nếu không chắc
</quality_requirements>
```

### Recovery — Khi lỗi xảy ra

| Tình huống | Hành động |
|-----------|-----------|
| Lỗi chỉ ở bước N | Fix in-place |
| Lỗi từ bước M (M < N) | Rollback về M, chạy lại |
| > 2 bước bị ảnh hưởng | Rollback toàn bộ, bắt đầu lại |

Xem chi tiết: [base/06 — Mistakes & Fixes](../base/06-mistakes-fixes.md)

---

## 7. Evaluation — 4 tiêu chí chấm điểm

| Tiêu chí | 1 — Kém | 2 — Chấp nhận | 3 — Tốt |
|---------|---------|-------------|---------|
| **Accuracy** | Sai, hallucination | Đúng nhưng thiếu | Chính xác, có nguồn |
| **Relevance** | Lạc đề | Trả lời + thừa | Đúng trọng tâm |
| **Clarity** | Khó hiểu | Hiểu được, cần đọc lại | Rõ ràng, dễ scan |
| **Actionability** | Không biết bước tiếp | Có hướng, bước mơ hồ | Bước rõ, copy-paste được |

**Tổng điểm:** 8–12 = Dùng được | 5–7 = Cần iterate | 4 = Viết lại

### Khi điểm thấp — Thêm gì vào prompt?

| Tiêu chí yếu | Thêm vào prompt |
|-------------|----------------|
| Accuracy | `<quality_requirements>` + yêu cầu trích nguồn |
| Relevance | Thu hẹp scope + `<constraints>` |
| Clarity | `<output_format>` + examples |
| Actionability | Bước cụ thể + expected results |

### Error severity

| Mức | Hành động |
|-----|-----------|
| **CRITICAL** | Dừng ngay, fix (mất dữ liệu, sai nghĩa, vượt scope) |
| **WARN** | Ghi nhận, fix sau (format, tone drift) |
| **OK** | Tiếp tục (synonym, ±20% độ dài, thứ tự nhỏ) |

Xem chi tiết: [base/07 — Evaluation Framework](../base/07-evaluation.md)

---

## 8. Setup nhanh — Personalization layers

```text
Layer 1: Profile Preferences    (account-wide)
Layer 2: Project Instructions   (project-level)
Layer 3: Styles                 (tone/format)
Layer 4: Memory                 (cross-conversation)
```

**Ưu tiên:** Project Instructions > Profile Preferences > Memory

**Project naming:** `[Team]-[Purpose]-[Version]` — VD: `RnD-TroubleshootingSLAM-v1`

**Project Knowledge — Tổ chức folder:**

```text
References/     — Datasheets, specs, APIs
Standards/      — Coding, naming, style guidelines
Templates/      — Document templates
Context/        — Project-specific info
```

Xem chi tiết: [base/02 — Setup & Personalization](../base/02-setup.md)

---

## Cross-references

- **Quick Start 15 phút:** [base/01](../base/01-quick-start.md)
- **Setup chi tiết:** [base/02](../base/02-setup.md)
- **Prompt Engineering đầy đủ:** [base/03](../base/03-prompt-engineering.md)
- **Context Management:** [base/04](../base/04-context-management.md)
- **Tools & Features:** [base/05](../base/05-tools-features.md)
- **Mistakes & Fixes:** [base/06](../base/06-mistakes-fixes.md)
- **Evaluation Framework:** [base/07](../base/07-evaluation.md)
- **Cheatsheet Doc tier:** [cheatsheet-doc.md](cheatsheet-doc.md)
- **Model specs:** [model-specs.md](model-specs.md)
- **Config architecture:** [config-architecture.md](config-architecture.md)
