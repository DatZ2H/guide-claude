# Danh sách Skills & Plugins — Phenikaa-X

Cập nhật: 2026-03-03 | Phân loại: Type × Trust

[Nguồn: Claude Code Docs — Plugins] [Cập nhật 03/2026]

> [!TIP]
> Hướng dẫn chi tiết cách dùng từng skill/command → xem [skills-guide.md](skills-guide.md)

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

### doc/01 — Doc Workflows (Recipes)

| Recipe/Workflow | Module | Skill khuyến nghị | Input → Output |
|----------------|--------|-------------------|----------------|
| 1.1 Viết tài liệu từ đầu | [doc/01](../doc/01-doc-workflows.md) | `doc-coauthoring` [Approved PX] | Notes/brief → Document hoàn chỉnh |
| 1.2 Document Review | [doc/01](../doc/01-doc-workflows.md) | `doc-coauthoring` [Approved PX] | File tài liệu → Review report có issues list |
| 1.3 Structured Troubleshooting | [doc/01](../doc/01-doc-workflows.md) | Không cần skill đặc biệt | Log/error data → Root cause analysis |
| 1.4 Terminology Management | [doc/01](../doc/01-doc-workflows.md) | Không cần skill đặc biệt | Tài liệu → Glossary + inconsistency report |
| 1.5 Document Generation | [doc/01](../doc/01-doc-workflows.md) | `docx` / `xlsx` / `pptx` [Approved PX] | Prompt → File Word/Excel/PowerPoint |
| 1.6 Research & Synthesis | [doc/01](../doc/01-doc-workflows.md) | Không cần skill đặc biệt | Topic → Research report có citations |
| 1.7 Structured Output | [doc/01](../doc/01-doc-workflows.md) | Không cần skill đặc biệt | Data input → JSON/CSV sẵn sàng parse |
| 1.8 Convert & Migrate | [doc/01](../doc/01-doc-workflows.md) | `docx` [Approved PX] (nếu output Word) | File cũ → File đã convert sang format mới |
| 1.9 MCP Connectors | [doc/01](../doc/01-doc-workflows.md) | Không cần skill đặc biệt | Prompt → Action trực tiếp trên connected service |
| 1.10 Document Lifecycle | [doc/01](../doc/01-doc-workflows.md) | `doc-coauthoring` [Approved PX] | Brief → Published document (end-to-end) |
| 1.11 Batch Processing | [doc/01](../doc/01-doc-workflows.md) | `docx` [Approved PX] (nếu output Word) | Folder files → Batch processed output |
| 1.12 Scheduled Tasks | [doc/01](../doc/01-doc-workflows.md) | Không cần skill đặc biệt | Prompt template → Automated periodic output |

> [!NOTE]
> Recipes 5.11-5.14 (Hybrid Workflow, Task Planning, Multi-file Editing, Session Planning) đã chuyển vào [base/05 — Tools & Features](../base/05-tools-features.md) vì là universal patterns.

### doc/02 — Template Library

| Recipe/Workflow | Module | Skill khuyến nghị | Input → Output |
|----------------|--------|-------------------|----------------|
| T-03 Viết Email báo cáo | [doc/02](../doc/02-template-library.md) | `internal-comms` Official | Context tiến độ → Email professional ≤200 từ |
| T-06 User Manual Section | [doc/02](../doc/02-template-library.md) | `doc-coauthoring` [Approved PX] | Spec/context → Section user manual có cấu trúc |
| T-07 Technical Specification | [doc/02](../doc/02-template-library.md) | `doc-coauthoring` [Approved PX] | System context → Tech spec có requirements + criteria |
| T-11 Standard Operating Procedure | [doc/02](../doc/02-template-library.md) | `doc-coauthoring` [Approved PX] | Procedure notes → SOP hoàn chỉnh 10 sections |
| T-12 Incident Report | [doc/02](../doc/02-template-library.md) | `doc-coauthoring` [Approved PX] | Incident data → Report có RCA + corrective actions |
| T-16 Tạo file Word | [doc/02](../doc/02-template-library.md) | `docx` [Approved PX] | Prompt → .docx professional có TOC |
| T-17 Tạo file Excel | [doc/02](../doc/02-template-library.md) | `xlsx` [Approved PX] | Prompt → .xlsx có conditional formatting + dashboard |
| T-18 Tạo file PowerPoint | [doc/02](../doc/02-template-library.md) | `pptx` [Approved PX] | Prompt → .pptx presentation |
| T-21 Multi-file Consistency Check | [doc/02](../doc/02-template-library.md) | `cross-ref-checker` [Approved PX] (Internal) | File list → Inconsistency report + cascade fixes |

Templates còn lại (T-01→T-05 universal: xem [quick-templates.md](quick-templates.md); T-08→T-22 còn lại) — Không cần skill đặc biệt: dùng trực tiếp làm prompt template.

### doc/04 — Cowork Workflows

| Recipe/Workflow | Module | Skill khuyến nghị | Input → Output |
|----------------|--------|-------------------|----------------|
| 4.1 Viết SOP từ notes | [doc/04](../doc/04-cowork-workflows.md) | `doc-coauthoring` [Approved PX] + `docx` (nếu output Word) | Folder notes → SOP file hoàn chỉnh |
| 4.2 Batch review tài liệu | [doc/04](../doc/04-cowork-workflows.md) | Không cần skill đặc biệt | Folder tài liệu → Review report có priority ranking |
| 4.3 Báo cáo tuần từ log | [doc/04](../doc/04-cowork-workflows.md) | Không cần skill đặc biệt | Folder logs → Weekly report có executive summary |
| 4.4 Convert Word ↔ Markdown | [doc/04](../doc/04-cowork-workflows.md) | `docx` [Approved PX] (nếu output Word) | Folder .docx/.md → Files converted + conversion report |
| 4.5 Glossary Enforcement | [doc/04](../doc/04-cowork-workflows.md) | `cross-ref-checker` [Approved PX] (Internal) | Folder docs + glossary → Inconsistency report theo file |
| 4.6 Training materials | [doc/04](../doc/04-cowork-workflows.md) | `doc-coauthoring` [Approved PX] + `pptx` (nếu slides) | Tech docs → Training guide/slide outline |
| 4.7 Extract data từ PDF | [doc/04](../doc/04-cowork-workflows.md) | `pdf` [Approved PX] | Folder PDF/images → CSV data table |
| 4.8 Tổ chức folder | [doc/04](../doc/04-cowork-workflows.md) | Không cần skill đặc biệt | Folder lộn xộn → Folder organized + reorganization report |
| 4.9 Release notes từ git | [doc/04](../doc/04-cowork-workflows.md) | Không cần skill đặc biệt | git log → Release notes 2 tầng (stakeholder + technical) |
| 4.10 Meeting prep | [doc/04](../doc/04-cowork-workflows.md) | Không cần skill đặc biệt | Folder meeting docs → Briefing 1–2 trang + agenda |
| 4.11 Incident report | [doc/04](../doc/04-cowork-workflows.md) | `doc-coauthoring` [Approved PX] | Raw logs/notes → Incident report có RCA + prevention |
| 4.12 Diff report | [doc/04](../doc/04-cowork-workflows.md) | Không cần skill đặc biệt | 2 file versions → Diff report có impact + recommendation |

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

```text
0 8 * * 1      # Mỗi thứ Hai 8:00 AM
0 17 * * 5     # Mỗi thứ Sáu 5:00 PM
0 9 1 * *      # Ngày 1 hàng tháng 9:00 AM
0 9 * * 1-5    # Mỗi ngày trong tuần 9:00 AM
```

**Chi tiết và recipe:** [doc/03 — Cowork Setup](../doc/03-cowork-setup.md) | [doc/01 — Doc Workflows, recipe 1.12](../doc/01-doc-workflows.md)

---

> [!WARNING]
> Skills chưa có badge `[Approved PX]` có thể tạo output không phù hợp với Phenikaa-X conventions.
> Luôn đọc SKILL.md và test trên dữ liệu không nhạy cảm trước khi áp dụng vào công việc chính thức.

## 5. Community Standalone Skills

> [!WARNING]
> Community skills không được Anthropic review. Bắt buộc đọc file SKILL.md và kiểm tra thư mục `scripts/` trước khi cài đặt. Test trên thư mục không chứa sensitive data.

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
| `source-audit` [Approved PX] | "source audit", "kiểm tra sources" | Scan source markers theo 3-tier standard | ✅ Internal (Phenikaa-X) | maintainer |
| `upgrade-guide` [Approved PX] | "health check", "scan project" | Scan stale data, broken refs, emoji violations | ✅ Internal (Phenikaa-X) | maintainer |
| `nav-update` [Approved PX] | "update nav", "fix navigation" | Auto-update prev/next nav links | ✅ Internal (Phenikaa-X) | maintainer |
| `plan` [Approved PX] | `/plan`, "tạo plan", "xem plan", "task list" | Planning workflow — tạo/xem/update plans xuyên session | ✅ Internal (Phenikaa-X) | maintainer |

---

## 8. Ghi chú

Skills KHÔNG sync giữa các surface. Skill cài trên claude.ai không tự có trên Cowork hay Claude Code. Cần cài riêng cho từng surface. (Nguồn: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
