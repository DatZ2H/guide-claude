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

## 2. Pre-built Skills (Official)

Tích hợp sẵn trên mọi surface (claude.ai, Cowork, Claude Code, API). Claude tự động activate khi task phù hợp, người dùng không cần cài đặt. Trên claude.ai, chỉ cần bật Settings > Capabilities > Code Execution.

| Tên | Chức năng | Surface hỗ trợ | Cài đặt | Trust |
|-----|-----------|-----------------|---------|-------|
| `docx` | Tạo, đọc, sửa file Word (.docx) | claude.ai, Cowork, Claude Code, API | Tích hợp sẵn | ✅ Official |
| `xlsx` | Tạo, đọc, sửa file Excel (.xlsx) | claude.ai, Cowork, Claude Code, API | Tích hợp sẵn | ✅ Official |
| `pptx` | Tạo, đọc, sửa file PowerPoint (.pptx) | claude.ai, Cowork, Claude Code, API | Tích hợp sẵn | ✅ Official |
| `pdf` | Tạo, đọc, merge, split, fill form PDF | claude.ai, Cowork, Claude Code, API | Tích hợp sẵn | ✅ Official |

---

## 3. Official Standalone Skills

| Tên | Mô tả ngắn | Repository URL | Cài đặt | Trust |
|-----|-------------|----------------|---------|-------|
| `doc-coauthoring` | Workflow co-authoring tài liệu có cấu trúc | github.com/anthropics/skills/tree/main/skills/doc-coauthoring [Cần xác minh] | Xem hướng dẫn bên dưới | ✅ Official |
| `internal-comms` | Template viết internal communications | github.com/anthropics/skills/tree/main/skills/internal-comms | Xem hướng dẫn bên dưới | ✅ Official |
| `skill-creator` | Tạo mới, sửa, đo lường hiệu quả skill | github.com/anthropics/skills/tree/main/skills/skill-creator | Xem hướng dẫn bên dưới | ✅ Official |

Cách cài đặt theo từng surface:

- **Cowork:** Claude Desktop > Settings > Skills > Upload, hoặc cài qua Plugin marketplace.
- **Claude Code:** `/plugin marketplace add anthropics/skills` → `/plugin install <tên>`
- **claude.ai:** Settings > Features > Upload .skill file.

---

## 4. Official Plugins

| Tên plugin | Mô tả ngắn | Repository URL | Cài đặt | Trust |
|------------|-------------|----------------|---------|-------|
| `productivity` | Quản lý task, notes, workflow | github.com/anthropics/knowledge-work-plugins/tree/main/plugins/productivity | Xem hướng dẫn bên dưới | ✅ Official |
| `product-management` | Hỗ trợ PM workflows (PRD, roadmap, specs) | github.com/anthropics/knowledge-work-plugins/tree/main/plugins/product-management | Xem hướng dẫn bên dưới | ✅ Official |
| `data` | Phân tích dữ liệu, visualization | github.com/anthropics/knowledge-work-plugins/tree/main/plugins/data | Xem hướng dẫn bên dưới | ✅ Official |

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

## 5. Community Standalone Skills

> **CẢNH BÁO:** Community skills không được Anthropic review. Bắt buộc đọc file SKILL.md và kiểm tra thư mục `scripts/` trước khi cài đặt. Test trên thư mục không chứa sensitive data.

### 5a. Từ skillhub.club

| ID   | Tên                        | Author          | skillhub URL                                                                                  | CLI install                                           | Trust |
| ---- | -------------------------- | --------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ----- |
| SH1  | `docs-review`              | @metabase       | skillhub.club/skills/metabase-metabase-docs-review                                            | `npx @skill-hub/cli install docs-review`              | ⚠️ Community |
| SH2  | `obsidian-markdown`        | @kepano         | skillhub.club/skills/kepano-obsidian-markdown                                                 | `npx @skill-hub/cli install obsidian-markdown`        | ⚠️ Community |
| SH3  | `voice-and-tone`           | @lerianstudio   | skillhub.club/skills/lerianstudio-voice-and-tone                                              | `npx @skill-hub/cli install voice-and-tone`           | ⚠️ Community |
| SH4  | `mermaidjs-v11`            | @mrgoonie       | skillhub.club/skills/mrgoonie-mermaidjs-v11                                                   | `npx @skill-hub/cli install mermaidjs-v11`            | ⚠️ Community |
| SH5  | `knowledge-capture`        | @rsmdt          | skillhub.club/skills/rsmdt-knowledge-capture                                                  | `npx @skill-hub/cli install knowledge-capture`        | ⚠️ Community |
| SH6  | `technical-clarity`        | @panaversity    | skillhub.club/skills/panaversity-technical-clarity                                            | `npx @skill-hub/cli install technical-clarity`        | ⚠️ Community |
| SH7  | `troubleshooting-docs`     | @glittercowboy  | skillhub.club/skills/glittercowboy-troubleshooting-docs                                       | `npx @skill-hub/cli install troubleshooting-docs`     | ⚠️ Community |
| SH8  | `organizing-documentation` | @cipherstash    | skillhub.club/skills/cipherstash-organizing-documentation                                     | `npx @skill-hub/cli install organizing-documentation` | ⚠️ Community |
| SH9  | `architecture-design`      | @rsmdt          | skillhub.club/skills/rsmdt-architecture-design                                                | `npx @skill-hub/cli install architecture-design`      | ⚠️ Community |
| SH10 | `specification-management` | @rsmdt          | skillhub.club/skills/rsmdt-specification-management                                           | `npx @skill-hub/cli install specification-management` | ⚠️ Community |
| SH11 | `document-converter`       | @benbrastmckie  | skillhub.club/skills/benbrastmckie-document-converter                                         | `npx @skill-hub/cli install document-converter`       | ⚠️ Community |
| SH12 | `technical-writing`        | @rsmdt          | skillhub.club/skills/rsmdt-technical-writing                                                  | `npx @skill-hub/cli install technical-writing`        | ⚠️ Community |
| SH13 | `format-markdown-table`    | @maslennikov-ig | skillhub.club/skills/maslennikov-ig-format-markdown-table                                     | `npx @skill-hub/cli install format-markdown-table`    | ⚠️ Community |
| SH14 | `context-optimization`     | @muratcankoylan | skillhub.club/skills/muratcankoylan-agent-skills-for-context-engineering-context-optimization | `npx @skill-hub/cli install context-optimization`     | ⚠️ Community |
| SH15 | `documentation-review`     | @lerianstudio   | skillhub.club/skills/lerianstudio-documentation-review                                        | `npx @skill-hub/cli install documentation-review`     | ⚠️ Community |
| SH16 | `md-docs`                  | @paulrberg      | skillhub.club/skills/paulrberg-md-docs                                                        | `npx @skill-hub/cli install md-docs`                  | ⚠️ Community |

### 5b. Từ GitHub

| ID | Tên | Repository URL | Cách tải | Trust |
|----|-----|----------------|----------|-------|
| D1a | `meeting-synthesizer` | github.com/luckybajaj22031996/pm-ba-claude-skills | Download ZIP > extract `meeting-synthesizer.skill` | ⚠️ Community |
| D1b | `stakeholder-updates` | github.com/luckybajaj22031996/pm-ba-claude-skills | Download ZIP > extract `stakeholder-updates.skill` | ⚠️ Community |
| D1c | `prd-generator` | github.com/luckybajaj22031996/pm-ba-claude-skills | Download ZIP > extract `prd-generator.skill` | ⚠️ Community |
| D1d | `market-research` | github.com/luckybajaj22031996/pm-ba-claude-skills | Download ZIP > extract `market-research.skill` | ⚠️ Community |
| D2 | `meeting-minutes-taker` | github.com/daymade/claude-code-skills | Download ZIP > extract folder | ⚠️ Community |
| D3 | `systematic-debugging` | github.com/obra/superpowers | Download ZIP > extract `systematic-debugging` folder | ⚠️ Community |

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

| Tên | Trigger | Chức năng | Trust |
|-----|---------|-----------|-------|
| `session-start` | `/start` hoặc "bắt đầu session" | Orientation đầu session: đọc git log, trả về tóm tắt trạng thái project | ✅ Internal (Phenikaa-X) |
| `version-bump` | `/version-bump`, "lên version vX.X" | Bump VERSION file, thêm changelog entry, update project-state.md | ✅ Internal (Phenikaa-X) |
| `doc-standard-enforcer` | Khi edit file trong `guide/` | Enforce writing standards: heading hierarchy, code block tags, cross-links | ✅ Internal (Phenikaa-X) |
| `cross-ref-checker` | Kiểm tra module | Scan cross-references, báo cáo broken links và inconsistencies | ✅ Internal (Phenikaa-X) |
| `module-review` | `/review-module <số>` | Deep review 1 module theo scoring rubric | ✅ Internal (Phenikaa-X) |

---

## 8. Ghi chú

Skills KHÔNG sync giữa các surface. Skill cài trên claude.ai không tự có trên Cowork hay Claude Code. Cần cài riêng cho từng surface. (Nguồn: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
