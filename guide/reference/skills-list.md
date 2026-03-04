# Danh sách Skills & Plugins — Phenikaa-X

Cập nhật: 2026-03-03 | Phân loại: Type × Trust

---

## 1. Tổng quan — Ma trận phân loại

|  | Official | Community |
|--|----------|-----------|
| **Pre-built Skill** | docx, xlsx, pptx, pdf | — |
| **Standalone Skill** | doc-coauthoring, internal-comms, skill-creator | docs-review, obsidian-markdown, voice-and-tone, mermaidjs-v11, knowledge-capture, technical-clarity, troubleshooting-docs, organizing-documentation, architecture-design, specification-management, document-converter, technical-writing, format-markdown-table, context-optimization, documentation-review, md-docs, meeting-synthesizer, stakeholder-updates, prd-generator, market-research, meeting-minutes-taker, systematic-debugging |
| **Plugin** | productivity, product-management, data | — |

Trục **Type** phản ánh kiến trúc kỹ thuật: Pre-built Skill được Anthropic tích hợp sẵn và tự kích hoạt, Standalone Skill là thư mục chứa SKILL.md cần cài thủ công, Plugin là package đóng gói nhiều thành phần (skills + slash commands + connectors + sub-agents). Trục **Trust** phản ánh mức độ tin cậy dựa trên nguồn gốc và quy trình review.

---

## Khuyến nghị cài đặt

### Must-have

Pre-built Skills — tự động có, không cần cài:

| Tên | Chức năng |
|-----|-----------|
| `docx` | Tạo, đọc, sửa file Word |
| `xlsx` | Tạo, đọc, sửa file Excel |
| `pptx` | Tạo, đọc, sửa file PowerPoint |
| `pdf` | Tạo, đọc, merge, split, fill form PDF |

### Nice-to-have

Official + community đã test, khuyến nghị cài thêm:

| Tên | Nguồn | Mô tả |
|-----|-------|-------|
| `doc-coauthoring` | Official | Workflow viết tài liệu có cấu trúc |
| `skill-creator` | Official | Tạo và đo lường skill |
| `obsidian-markdown` | Community | Tốt cho Obsidian users |
| `mermaidjs-v11` | Community | Tạo diagrams |

### Reference-only

Danh mục để tra cứu. Cài khi có nhu cầu cụ thể, đọc SKILL.md trước khi cài:

Toàn bộ community skills còn lại — xem [Section 5](#5-community-standalone-skills).

---

## Skill-Recipe Mapping

Bảng tra cứu nhanh: recipe/workflow nào dùng skill nào. Chỉ liệt kê skills có badge `[Approved PX]` hoặc `Official`.

### Module 05 — Workflow Recipes

| Recipe/Workflow | Module | Skill khuyến nghị | Input → Output |
|----------------|--------|-------------------|----------------|
| 5.1 Viết tài liệu từ đầu | 05 | `doc-coauthoring` [Approved PX] | Notes/brief → Document hoàn chỉnh |
| 5.2 Document Review | 05 | `doc-coauthoring` [Approved PX] | File tài liệu → Review report có issues list |
| 5.3 Structured Troubleshooting | 05 | Không cần skill đặc biệt | Log/error data → Root cause analysis |
| 5.4 Terminology Management | 05 | Không cần skill đặc biệt | Tài liệu → Glossary + inconsistency report |
| 5.5 Document Generation | 05 | `docx` / `xlsx` / `pptx` [Approved PX] | Prompt → File Word/Excel/PowerPoint |
| 5.6 Research & Synthesis | 05 | Không cần skill đặc biệt | Topic → Research report có citations |
| 5.7 Structured Output | 05 | Không cần skill đặc biệt | Data input → JSON/CSV sẵn sàng parse |
| 5.8 Convert & Migrate | 05 | `docx` [Approved PX] (nếu output Word) | File cũ → File đã convert sang format mới |
| 5.9 MCP Connectors | 05 | Không cần skill đặc biệt | Prompt → Action trực tiếp trên connected service |
| 5.10 Document Lifecycle | 05 | `doc-coauthoring` [Approved PX] | Brief → Published document (end-to-end) |
| 5.11 Hybrid Workflow | 05 | Không cần skill đặc biệt | Research/notes → Final document qua Chat+Project+Cowork |
| 5.12 Task Planning trước Chain Prompt | 05 | Không cần skill đặc biệt | Task description → Task map + dependency table |
| 5.13 Multi-file Editing | 05 | `cross-ref-checker` [Approved PX] (Internal) | File changes → Impact report + verified consistency |
| 5.14 Cowork Session Planning | 05 | Không cần skill đặc biệt | Task brief → Scope analysis + task plan |
| 5.15 Cowork Batch Processing | 05 | `docx` [Approved PX] (nếu output Word) | Folder files → Batch processed output |
| 5.16 Scheduled Tasks | 05 | Không cần skill đặc biệt | Prompt template → Automated periodic output |

### Module 07 — Templates

| Recipe/Workflow | Module | Skill khuyến nghị | Input → Output |
|----------------|--------|-------------------|----------------|
| T-03 Viết Email báo cáo | 07 | `internal-comms` Official | Context tiến độ → Email professional ≤200 từ |
| T-06 User Manual Section | 07 | `doc-coauthoring` [Approved PX] | Spec/context → Section user manual có cấu trúc |
| T-07 Technical Specification | 07 | `doc-coauthoring` [Approved PX] | System context → Tech spec có requirements + criteria |
| T-11 Standard Operating Procedure | 07 | `doc-coauthoring` [Approved PX] | Procedure notes → SOP hoàn chỉnh 10 sections |
| T-12 Incident Report | 07 | `doc-coauthoring` [Approved PX] | Incident data → Report có RCA + corrective actions |
| T-16 Tạo file Word | 07 | `docx` [Approved PX] | Prompt → .docx professional có TOC |
| T-17 Tạo file Excel | 07 | `xlsx` [Approved PX] | Prompt → .xlsx có conditional formatting + dashboard |
| T-18 Tạo file PowerPoint | 07 | `pptx` [Approved PX] | Prompt → .pptx presentation |
| T-21 Multi-file Consistency Check | 07 | `cross-ref-checker` [Approved PX] (Internal) | File list → Inconsistency report + cascade fixes |

Templates còn lại (T-01, T-02, T-04, T-05, T-08, T-09, T-10, T-13, T-14, T-15, T-19, T-20, T-22) — Không cần skill đặc biệt: dùng trực tiếp làm prompt template.

### Module 11 — Cowork Workflows

| Recipe/Workflow | Module | Skill khuyến nghị | Input → Output |
|----------------|--------|-------------------|----------------|
| 11.1 Viết SOP từ notes | 11 | `doc-coauthoring` [Approved PX] + `docx` (nếu output Word) | Folder notes → SOP file hoàn chỉnh |
| 11.2 Batch review tài liệu | 11 | Không cần skill đặc biệt | Folder tài liệu → Review report có priority ranking |
| 11.3 Báo cáo tuần từ log | 11 | Không cần skill đặc biệt | Folder logs → Weekly report có executive summary |
| 11.4 Convert Word ↔ Markdown | 11 | `docx` [Approved PX] (nếu output Word) | Folder .docx/.md → Files converted + conversion report |
| 11.5 Glossary Enforcement | 11 | `cross-ref-checker` [Approved PX] (Internal) | Folder docs + glossary → Inconsistency report theo file |
| 11.6 Training materials | 11 | `doc-coauthoring` [Approved PX] + `pptx` (nếu slides) | Tech docs → Training guide/slide outline |
| 11.7 Extract data từ PDF | 11 | `pdf` [Approved PX] | Folder PDF/images → CSV data table |
| 11.8 Tổ chức folder | 11 | Không cần skill đặc biệt | Folder lộn xộn → Folder organized + reorganization report |
| 11.9 Release notes từ git | 11 | Không cần skill đặc biệt | git log → Release notes 2 tầng (stakeholder + technical) |
| 11.10 Meeting prep | 11 | Không cần skill đặc biệt | Folder meeting docs → Briefing 1–2 trang + agenda |
| 11.11 Incident report | 11 | `doc-coauthoring` [Approved PX] | Raw logs/notes → Incident report có RCA + prevention |
| 11.12 Diff report | 11 | Không cần skill đặc biệt | 2 file versions → Diff report có impact + recommendation |

---

## 2. Pre-built Skills (Official)

Tích hợp sẵn trên mọi surface (claude.ai, Cowork, Claude Code, API). Claude tự động activate khi task phù hợp, người dùng không cần cài đặt. Trên claude.ai, chỉ cần bật Settings > Capabilities > Code Execution.

| Tên | Chức năng | Surface hỗ trợ | Cài đặt | Trust | Audience |
|-----|-----------|-----------------|---------|-------|----------|
| `docx` [Approved PX] | Tạo, đọc, sửa file Word (.docx) | claude.ai, Cowork, Claude Code, API | Tích hợp sẵn | ✅ Official | end-user |
| `xlsx` [Approved PX] | Tạo, đọc, sửa file Excel (.xlsx) | claude.ai, Cowork, Claude Code, API | Tích hợp sẵn | ✅ Official | end-user |
| `pptx` [Approved PX] | Tạo, đọc, sửa file PowerPoint (.pptx) | claude.ai, Cowork, Claude Code, API | Tích hợp sẵn | ✅ Official | end-user |
| `pdf` [Approved PX] | Tạo, đọc, merge, split, fill form PDF | claude.ai, Cowork, Claude Code, API | Tích hợp sẵn | ✅ Official | end-user |

---

## 3. Official Standalone Skills

| Tên | Mô tả ngắn | Repository URL | Cài đặt | Trust | Audience |
|-----|-------------|----------------|---------|-------|----------|
| `doc-coauthoring` [Approved PX] | Workflow co-authoring tài liệu có cấu trúc | github.com/anthropics/skills/tree/main/skills/doc-coauthoring [Cần xác minh] | Xem hướng dẫn bên dưới | ✅ Official | both |
| `internal-comms` | Template viết internal communications | github.com/anthropics/skills/tree/main/skills/internal-comms | Xem hướng dẫn bên dưới | ✅ Official | end-user |
| `skill-creator` | Tạo mới, sửa, đo lường hiệu quả skill | github.com/anthropics/skills/tree/main/skills/skill-creator | Xem hướng dẫn bên dưới | ✅ Official | maintainer |

Cách cài đặt theo từng surface:

- **Cowork:** Claude Desktop > Settings > Skills > Upload, hoặc cài qua Plugin marketplace.
- **Claude Code:** `/plugin marketplace add anthropics/skills` → `/plugin install <tên>`
- **claude.ai:** Settings > Features > Upload .skill file.

---

## 4. Official Plugins

| Tên plugin | Mô tả ngắn | Repository URL | Cài đặt | Trust | Audience |
|------------|-------------|----------------|---------|-------|----------|
| `productivity` | Quản lý task, notes, workflow | github.com/anthropics/knowledge-work-plugins/tree/main/plugins/productivity | Xem hướng dẫn bên dưới | ✅ Official | end-user |
| `product-management` | Hỗ trợ PM workflows (PRD, roadmap, specs) | github.com/anthropics/knowledge-work-plugins/tree/main/plugins/product-management | Xem hướng dẫn bên dưới | ✅ Official | end-user |
| `data` | Phân tích dữ liệu, visualization | github.com/anthropics/knowledge-work-plugins/tree/main/plugins/data | Xem hướng dẫn bên dưới | ✅ Official | end-user |

Anthropic cung cấp 11+ plugins chính thức tại repo `anthropics/knowledge-work-plugins`. Ngoài 3 plugin liệt kê ở đây, còn có: sales, marketing, finance, legal, customer-support, enterprise-search, bio-research, cowork-plugin-management. [Cập nhật 03/2026 — kiểm tra repo để xem danh sách mới nhất]

**Enterprise plugins:** Anthropic cung cấp thêm bộ enterprise-tier plugins (ước tính 13+ packages) cho Team/Enterprise plan — bao gồm SSO integration, audit logging, custom connectors. Cần xác minh danh sách đầy đủ tại admin console.

Cách cài đặt theo từng surface:

- **Cowork:** Sidebar > Plugins > Browse > tìm tên plugin > Install. Hoặc: Settings > **Customize** tab > Plugins.
- **Claude Code:** `claude plugin marketplace add anthropics/knowledge-work-plugins` → `claude plugin install <tên>`

---

## 4b. Scheduled Tasks (Cowork only)

[Cập nhật 03/2026]

Scheduled Tasks không phải Skills hay Plugins — đây là tính năng riêng của Cowork cho phép chạy prompt tự động theo lịch. Không cần file cài đặt, cấu hình trực tiếp trong Cowork UI.

| Thuộc tính | Chi tiết |
|------------|----------|
| **Surface** | Cowork (Claude Desktop) — không có trên claude.ai |
| **Cài đặt** | Claude Desktop > Cowork > Scheduled Tasks > New Task |
| **Cú pháp lịch** | Cron standard: `phút giờ ngày_tháng tháng ngày_tuần` |
| **Yêu cầu** | Máy phải đang bật khi task chạy |
| **Use case** | Weekly report, daily log digest, monthly summary |

**Ví dụ cron syntax:**

```
0 8 * * 1      # Mỗi thứ Hai 8:00 AM
0 17 * * 5     # Mỗi thứ Sáu 5:00 PM
0 9 1 * *      # Ngày 1 hàng tháng 9:00 AM
0 9 * * 1-5    # Mỗi ngày trong tuần 9:00 AM
```

**Chi tiết và recipe:** Module 10, mục 10.5 | Module 05, mục 5.16

---

> [!WARNING]
> Skills chưa có badge `[Approved PX]` có thể tạo output không phù hợp với Phenikaa-X conventions.
> Luôn đọc SKILL.md và test trên dữ liệu không nhạy cảm trước khi áp dụng vào công việc chính thức.

## 5. Community Standalone Skills

> **CẢNH BÁO:** Community skills không được Anthropic review. Bắt buộc đọc file SKILL.md và kiểm tra thư mục `scripts/` trước khi cài đặt. Test trên thư mục không chứa sensitive data.

### 5a. Từ skillhub.club

| ID   | Tên                        | Author          | skillhub URL                                                                                  | CLI install                                           | Trust | Audience |
| ---- | -------------------------- | --------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ----- | -------- |
| SH1  | `docs-review`              | @metabase       | skillhub.club/skills/metabase-metabase-docs-review                                            | `npx @skill-hub/cli install docs-review`              | ⚠️ Community | end-user |
| SH2  | `obsidian-markdown` [Approved PX] | @kepano  | skillhub.club/skills/kepano-obsidian-markdown                                                 | `npx @skill-hub/cli install obsidian-markdown`        | ⚠️ Community | end-user |
| SH3  | `voice-and-tone`           | @lerianstudio   | skillhub.club/skills/lerianstudio-voice-and-tone                                              | `npx @skill-hub/cli install voice-and-tone`           | ⚠️ Community | end-user |
| SH4  | `mermaidjs-v11` [Approved PX] | @mrgoonie    | skillhub.club/skills/mrgoonie-mermaidjs-v11                                                   | `npx @skill-hub/cli install mermaidjs-v11`            | ⚠️ Community | end-user |
| SH5  | `knowledge-capture`        | @rsmdt          | skillhub.club/skills/rsmdt-knowledge-capture                                                  | `npx @skill-hub/cli install knowledge-capture`        | ⚠️ Community | end-user |
| SH6  | `technical-clarity`        | @panaversity    | skillhub.club/skills/panaversity-technical-clarity                                            | `npx @skill-hub/cli install technical-clarity`        | ⚠️ Community | end-user |
| SH7  | `troubleshooting-docs`     | @glittercowboy  | skillhub.club/skills/glittercowboy-troubleshooting-docs                                       | `npx @skill-hub/cli install troubleshooting-docs`     | ⚠️ Community | end-user |
| SH8  | `organizing-documentation` | @cipherstash    | skillhub.club/skills/cipherstash-organizing-documentation                                     | `npx @skill-hub/cli install organizing-documentation` | ⚠️ Community | end-user |
| SH9  | `architecture-design`      | @rsmdt          | skillhub.club/skills/rsmdt-architecture-design                                                | `npx @skill-hub/cli install architecture-design`      | ⚠️ Community | end-user |
| SH10 | `specification-management` | @rsmdt          | skillhub.club/skills/rsmdt-specification-management                                           | `npx @skill-hub/cli install specification-management` | ⚠️ Community | end-user |
| SH11 | `document-converter`       | @benbrastmckie  | skillhub.club/skills/benbrastmckie-document-converter                                         | `npx @skill-hub/cli install document-converter`       | ⚠️ Community | end-user |
| SH12 | `technical-writing`        | @rsmdt          | skillhub.club/skills/rsmdt-technical-writing                                                  | `npx @skill-hub/cli install technical-writing`        | ⚠️ Community | end-user |
| SH13 | `format-markdown-table`    | @maslennikov-ig | skillhub.club/skills/maslennikov-ig-format-markdown-table                                     | `npx @skill-hub/cli install format-markdown-table`    | ⚠️ Community | end-user |
| SH14 | `context-optimization`     | @muratcankoylan | skillhub.club/skills/muratcankoylan-agent-skills-for-context-engineering-context-optimization | `npx @skill-hub/cli install context-optimization`     | ⚠️ Community | end-user |
| SH15 | `documentation-review`     | @lerianstudio   | skillhub.club/skills/lerianstudio-documentation-review                                        | `npx @skill-hub/cli install documentation-review`     | ⚠️ Community | end-user |
| SH16 | `md-docs`                  | @paulrberg      | skillhub.club/skills/paulrberg-md-docs                                                        | `npx @skill-hub/cli install md-docs`                  | ⚠️ Community | end-user |

### 5b. Từ GitHub

| ID | Tên | Repository URL | Cách tải | Trust | Audience |
|----|-----|----------------|----------|-------|----------|
| D1a | `meeting-synthesizer` | github.com/luckybajaj22031996/pm-ba-claude-skills | Download ZIP > extract `meeting-synthesizer.skill` | ⚠️ Community | end-user |
| D1b | `stakeholder-updates` | github.com/luckybajaj22031996/pm-ba-claude-skills | Download ZIP > extract `stakeholder-updates.skill` | ⚠️ Community | end-user |
| D1c | `prd-generator` | github.com/luckybajaj22031996/pm-ba-claude-skills | Download ZIP > extract `prd-generator.skill` | ⚠️ Community | end-user |
| D1d | `market-research` | github.com/luckybajaj22031996/pm-ba-claude-skills | Download ZIP > extract `market-research.skill` | ⚠️ Community | end-user |
| D2 | `meeting-minutes-taker` | github.com/daymade/claude-code-skills | Download ZIP > extract folder | ⚠️ Community | end-user |
| D3 | `systematic-debugging` | github.com/obra/superpowers | Download ZIP > extract `systematic-debugging` folder | ⚠️ Community | end-user |

---

## 6. Lệnh cài đặt nhanh (Community — skillhub.club)

```bash
npx @skill-hub/cli install obsidian-markdown
npx @skill-hub/cli install mermaidjs-v11
npx @skill-hub/cli install docs-review
npx @skill-hub/cli install voice-and-tone
npx @skill-hub/cli install knowledge-capture
npx @skill-hub/cli install technical-clarity
npx @skill-hub/cli install troubleshooting-docs
npx @skill-hub/cli install organizing-documentation
npx @skill-hub/cli install context-optimization
npx @skill-hub/cli install systematic-debugging
npx @skill-hub/cli install architecture-design
npx @skill-hub/cli install specification-management
npx @skill-hub/cli install document-converter
npx @skill-hub/cli install technical-writing
npx @skill-hub/cli install format-markdown-table
npx @skill-hub/cli install documentation-review
npx @skill-hub/cli install md-docs
```

---

## 7. Custom Skills — Phenikaa-X (Project Skills)

Skills nội bộ dùng trong Guide Claude project, nằm tại `.claude/skills/`. Chỉ hoạt động trong Cowork (Claude Code) khi mở đúng thư mục project.

| Tên | Trigger | Chức năng | Trust | Audience |
|-----|---------|-----------|-------|----------|
| `session-start` [Approved PX] | `/start` hoặc "bắt đầu session" | Orientation đầu session: đọc git log, trả về tóm tắt trạng thái project | ✅ Internal (Phenikaa-X) | maintainer |
| `version-bump` [Approved PX] | `/version-bump`, "lên version vX.X" | Bump VERSION file, thêm changelog entry, update project-state.md | ✅ Internal (Phenikaa-X) | maintainer |
| `doc-standard-enforcer` [Approved PX] | Khi edit file trong `guide/` | Enforce writing standards: heading hierarchy, code block tags, cross-links | ✅ Internal (Phenikaa-X) | maintainer |
| `cross-ref-checker` [Approved PX] | Kiểm tra module | Scan cross-references, báo cáo broken links và inconsistencies | ✅ Internal (Phenikaa-X) | maintainer |
| `module-review` [Approved PX] | `/review-module <số>` | Deep review 1 module theo scoring rubric | ✅ Internal (Phenikaa-X) | maintainer |

---

## 8. Ghi chú

Skills KHÔNG sync giữa các surface. Skill cài trên claude.ai không tự có trên Cowork hay Claude Code. Cần cài riêng cho từng surface. (Nguồn: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
