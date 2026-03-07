# Cheatsheet — Doc Tier

**Cập nhật:** 2026-03-07 | Quick-reference card cho guide/doc/ (Modules 01–06)

[Nguồn: Tổng hợp từ guide/doc/] [Cập nhật 03/2026]

> [!TIP]
> Cheatsheet này là bảng tra cứu nhanh — mỗi mục link về module gốc để đọc chi tiết.

---

## 1. Doc Workflows — 12 Recipes

| # | Recipe | Bước chính | Link |
|---|--------|-----------|------|
| 1.1 | Viết tài liệu từ đầu | Brief → Outline → Viết section → Review | [doc/01](../doc/01-doc-workflows.md) |
| 1.2 | Review & cải thiện | 6 tiêu chí: Accuracy, Clarity, Consistency, Completeness, Structure, Grammar | [doc/01](../doc/01-doc-workflows.md) |
| 1.3 | Troubleshooting có cấu trúc | XML prompt: role + task + context + requirements | [doc/01](../doc/01-doc-workflows.md) |
| 1.4 | Chuẩn hóa thuật ngữ | Glossary file → enforcement scan | [doc/01](../doc/01-doc-workflows.md) |
| 1.5 | Tạo file chuyên nghiệp | Word / Excel / PowerPoint / PDF | [doc/01](../doc/01-doc-workflows.md) |
| 1.6 | Research & tổng hợp | Multi-source → structured report | [doc/01](../doc/01-doc-workflows.md) |
| 1.7 | Structured Output | JSON schema cho automation | [doc/01](../doc/01-doc-workflows.md) |
| 1.8 | Convert & migrate | Format chuyển đổi batch | [doc/01](../doc/01-doc-workflows.md) |
| 1.9 | MCP Connectors | Google Drive, Notion, Slack, GitHub, Jira | [doc/01](../doc/01-doc-workflows.md) |
| 1.10 | Document Lifecycle | Workflow tổng hợp end-to-end | [doc/01](../doc/01-doc-workflows.md) |
| 1.11 | Batch Processing | Scope → Input/Output → Plan → Execute | [doc/01](../doc/01-doc-workflows.md) |
| 1.12 | Scheduled Tasks | Cron syntax + self-contained prompts | [doc/01](../doc/01-doc-workflows.md) |

### Doc drafting — 4 bước

```text
1. Brief (XML prompt + placeholders)  → Claude tạo outline
2. Review outline                     → Approve / adjust
3. Viết từng section                  → 1-2 section/prompt
4. Review tổng thể (6 tiêu chí)      → Final edits
```

### Review rubric — 6 tiêu chí

| Tiêu chí | Kiểm tra |
|---------|----------|
| Accuracy | Thông tin đúng, có nguồn? |
| Clarity | Người mới hiểu không? |
| Consistency | Thuật ngữ, format nhất quán? |
| Completeness | Thiếu section nào không? |
| Structure | Heading hierarchy đúng? |
| Grammar & Style | Chính tả, tone phù hợp? |

Xem chi tiết: [doc/01 — Doc Workflows](../doc/01-doc-workflows.md)

---

## 2. Template Index — T-06 đến T-22

| Mã | Template | Category | Dùng khi |
|:---:|---------|---------|---------|
| T-06 | User Manual Section | Technical Docs | Viết section user manual |
| T-07 | Technical Specification | Technical Docs | Tạo technical spec |
| T-08 | Error Analysis | Troubleshooting | Phân tích lỗi có cấu trúc |
| T-09 | Diagnostic Guide | Troubleshooting | Hướng dẫn chẩn đoán lỗi |
| T-10 | Code Review Request | Code Review | Review code structured |
| T-11 | Standard Operating Procedure | SOP & Procedures | Tạo SOP hoàn chỉnh |
| T-12 | Incident Report | Reports & Analysis | Báo cáo sự cố + RCA |
| T-13 | Handover Summary | Workflow | Tóm tắt conversation chuyển tiếp |
| T-14 | Context Extraction | Workflow | Trích xuất 1 topic từ conversation |
| T-15 | Chain Prompt | Workflow | Prompt chain nhiều bước |
| T-16 | Tạo file Word | File Creation | Tạo .docx professional |
| T-17 | Tạo file Excel | File Creation | Tạo .xlsx có formatting |
| T-18 | Tạo file PowerPoint | File Creation | Tạo .pptx presentation |
| T-19 | Task Decomposition Planner | Workflow | Lên kế hoạch task phức tạp |
| T-20 | In-Progress Review Checklist | Workflow | Review output giữa các step |
| T-21 | Multi-file Consistency Check | Workflow | Verify consistency sau edits |
| T-22 | Cowork Task Plan | Cowork | Plan Cowork project phức tạp |

> [!NOTE]
> Templates T-01 đến T-05 (universal) nằm trong [reference/quick-templates.md](quick-templates.md)

### SOP template (T-11) — 10 sections

```text
1. Mục đích (Purpose)
2. Phạm vi (Scope)
3. Trách nhiệm (Responsibilities)
4. Định nghĩa & Thuật ngữ
5. Thiết bị & Vật liệu
6. An toàn (Safety Precautions)
7. Quy trình (7.1 Chuẩn bị → 7.2 Thực hiện → 7.3 Kết thúc)
8. Xử lý sự cố
9. Tài liệu liên quan
10. Lịch sử thay đổi
```

### Template customization — Thêm modules

| Cần thêm | Module XML |
|---------|-----------|
| Ví dụ mẫu | `<examples>` |
| Quality control | `<quality_requirements>` |
| Giới hạn độ dài | `<length_control>` |
| Step-by-step | `<step_by_step>` |
| Edge cases | `<edge_cases>` |

Xem chi tiết: [doc/02 — Template Library](../doc/02-template-library.md)

---

## 3. Cowork — Setup & Commands

### 3.1 Folder Instructions — Khi nào cần?

| Tình huống | Cần? |
|-----------|:----:|
| Project có naming convention riêng | ✅ |
| Thư mục cần context đặc thù | ✅ |
| Chia sẻ team — cần nhất quán | ✅ |
| Thư mục tạm, dùng 1 lần | ❌ |
| Task đơn giản, context đủ trong prompt | ❌ |

### 3.2 Instruction layers — Thứ tự ưu tiên

```text
Global Instructions    (mọi sessions)
  ↓ override by
Folder Instructions    (folder cụ thể)
  ↓ override by
Task Prompt            (task hiện tại)
```

### 3.3 Scheduled Tasks — Cron syntax

```text
0 8 * * 1        Mỗi thứ Hai 8:00 AM
0 17 * * 5       Mỗi thứ Sáu 5:00 PM
0 9 1 * *        Ngày 1 hàng tháng 9:00 AM
0 9 * * 1-5      Mỗi ngày trong tuần 9:00 AM
```

> [!NOTE]
> Scheduled tasks yêu cầu máy phải bật và prompts phải self-contained.

Xem chi tiết: [doc/03 — Cowork Setup](../doc/03-cowork-setup.md)

---

## 4. Cowork Workflows — 12 mẫu thực tế

| # | Workflow | Input | Output | Thời gian |
|---|---------|-------|--------|:---------:|
| 4.1 | SOP từ notes | Meeting notes + drafts | SOP `.md` | 10–20 min |
| 4.2 | Batch review tài liệu | 5–10 docs | Review report | 5–10 min |
| 4.3 | Báo cáo tuần từ logs | Test/deploy logs | Weekly report | 5–10 min |
| 4.4 | Convert Word ↔ Markdown | `.docx` hoặc `.md` | `converted/` folder | 5–15 min |
| 4.5 | Glossary Enforcement | Docs + `glossary.md` | Check report | 10–15 min |
| 4.6 | Training materials | Tech specs/arch docs | Slide outline / guide | 15–30 min |
| 4.7 | Extract data từ PDF | `.pdf`, `.png`, `.jpg` | CSV files | 10–20 min |
| 4.8 | Tổ chức folder | Messy folder | Organized + report | 15–30 min |
| 4.9 | Release notes từ git | `git-log.txt` + changed files | `RELEASE-NOTES.md` | 5–10 min |
| 4.10 | Meeting prep | Notes + emails + docs | Briefing 1–2 trang | 5–10 min |
| 4.11 | Incident report | Logs + screenshots + notes | Incident report | 10–20 min |
| 4.12 | So sánh documents | File v1 + v2 | Diff report | 5–10 min |

### Workflow theo loại task

| Cần làm gì | Dùng workflow |
|-----------|-------------|
| Tạo tài liệu từ notes | 4.1 SOP from notes |
| Kiểm tra chất lượng | 4.2 Batch review |
| Tạo báo cáo | 4.3 Weekly report / 4.11 Incident report |
| Chuyển đổi format | 4.4 Word ↔ Markdown |
| Chuẩn hóa thuật ngữ | 4.5 Glossary enforcement |
| Tạo tài liệu đào tạo | 4.6 Training materials |
| Số hóa dữ liệu | 4.7 Extract from PDF |
| Dọn dẹp thư mục | 4.8 Folder organization |
| Chuẩn bị release | 4.9 Release notes |
| Chuẩn bị họp | 4.10 Meeting prep |
| Theo dõi thay đổi | 4.12 Diff report |

### Batch processing — 4 bước

```text
1. Chọn scope      → Files/folders nào?
2. Mô tả I/O       → Input gì, output gì?
3. Review plan      → Claude đề xuất, bạn approve
4. Execute          → Claude chạy, bạn verify
```

Xem chi tiết: [doc/04 — Cowork Workflows](../doc/04-cowork-workflows.md)

---

## 5. Claude Code cho Documentation

### 5.1 Khi nào dùng Claude Code thay Cowork?

| Tình huống | claude.ai | Cowork | Claude Code |
|-----------|:---------:|:------:|:-----------:|
| Chat & brainstorm | ✅ Best | ✅ | ✅ |
| Sửa 1 file | ✅ | ✅ Best | ✅ |
| Batch edit nhiều file | ❌ | ⚠️ | ✅ Best |
| Batch find & replace | ❌ | ⚠️ | ✅ Best |
| Git-based workflows | ❌ | ❌ | ✅ Best |
| QA automation | ❌ | ⚠️ | ✅ Best |

### 5.2 Config files — `.claude/` structure

| File | Mục đích |
|------|---------|
| `settings.json` | Model mặc định, token limits |
| `settings.local.json` | Overrides cho máy hiện tại |
| `.claudeignore` | Files to ignore |
| `rules/` | Auto-loaded rules per file type |
| `hooks/` | PostToolUse, PreCommit validation |
| `skills/` | Custom session skills |
| `commands/` | Custom CLI commands |

Xem chi tiết: [doc/05 — Claude Code for Documentation](../doc/05-claude-code-doc.md)

---

## 6. Custom Style — Chọn nhanh

### 6.1 Style theo tình huống

| Tình huống | Style khuyến nghị |
|-----------|------------------|
| Debug session | Normal / Concise |
| Tài liệu khách hàng | Formal / Custom "Technical" |
| Hỏi đáp ROS commands | Concise |
| Brainstorm solutions | Explanatory |
| Email nội bộ | Custom "Internal Communication" |
| Training materials | Explanatory |

### 6.2 Tạo Custom Style — 2 cách

| Cách | Phù hợp khi |
|------|------------|
| Upload writing sample | Có sẵn 1–2 văn bản mẫu đúng tone |
| Viết instructions | Muốn kiểm soát chính xác từng yếu tố |

### 6.3 Phenikaa-X — 2 style templates

**Technical Documentation:**

```text
- Ngôn ngữ: Tiếng Việt, thuật ngữ kỹ thuật giữ Anh
- Tone: Professional, direct, actionable
- Format: Headings rõ, steps đánh số, code blocks
- Khi không chắc: nói rõ + cách verify
```

**Internal Communication:**

```text
- Ngôn ngữ: Tiếng Việt, thân thiện nhưng chuyên nghiệp
- Tone: Collaborative, supportive
- Format: TL;DR đầu, bullets cho actions, deadlines rõ
- Độ dài: ≤ 1 trang
```

### 6.4 Multi-Style workflow

```text
Style = tone & format (HOW Claude writes)
Project Instructions = content & scope (WHAT Claude writes)

→ Tạo 2–3 Custom Styles cho team
→ Switch style theo task type, không theo ngày
```

Xem chi tiết: [doc/06 — Custom Style](../doc/06-custom-style.md)

---

## Cross-references

- **Base tier cheatsheet:** [cheatsheet-base.md](cheatsheet-base.md)
- **Templates universal (T-01–T-05):** [quick-templates.md](quick-templates.md)
- **Skills guide:** [skills-guide.md](skills-guide.md)
- **Config architecture:** [config-architecture.md](config-architecture.md)
- **Doc workflows đầy đủ:** [doc/01](../doc/01-doc-workflows.md)
- **Template library đầy đủ:** [doc/02](../doc/02-template-library.md)
- **Cowork setup:** [doc/03](../doc/03-cowork-setup.md)
- **Cowork workflows:** [doc/04](../doc/04-cowork-workflows.md)
- **Claude Code for docs:** [doc/05](../doc/05-claude-code-doc.md)
- **Custom Style:** [doc/06](../doc/06-custom-style.md)
