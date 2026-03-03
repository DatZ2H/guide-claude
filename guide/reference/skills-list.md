# Danh sách Skills & Plugins — Phenikaa-X

Cập nhật: 2026-03-01 | Phân loại: Type × Trust

---

## 1. Tổng quan — Ma trận phân loại

|  | Official | Community |
|--|----------|-----------|
| **Pre-built Skill** | docx, xlsx, pptx, pdf | — |
| **Standalone Skill** | doc-coauthoring, internal-comms, skill-creator | docs-review, obsidian-markdown, voice-and-tone, mermaidjs-v11, knowledge-capture, technical-clarity, troubleshooting-docs, organizing-documentation, architecture-design, specification-management, document-converter, technical-writing, format-markdown-table, context-optimization, documentation-review, md-docs, meeting-synthesizer, stakeholder-updates, prd-generator, market-research, meeting-minutes-taker, systematic-debugging |
| **Plugin** | productivity, product-management, data | — |

Trục **Type** phản ánh kiến trúc kỹ thuật: Pre-built Skill được Anthropic tích hợp sẵn và tự kích hoạt, Standalone Skill là thư mục chứa SKILL.md cần cài thủ công, Plugin là package đóng gói nhiều thành phần (skills + slash commands + connectors + sub-agents). Trục **Trust** phản ánh mức độ tin cậy dựa trên nguồn gốc và quy trình review.

---

## 2. Pre-built Skills (Official)

Tích hợp sẵn trên mọi surface (claude.ai, Cowork, Claude Code, API). Claude tự động activate khi task phù hợp, người dùng không cần cài đặt. Trên claude.ai, chỉ cần bật Settings > Capabilities > Code Execution.

| Tên | Chức năng | Surface hỗ trợ | Cài đặt |
|-----|-----------|-----------------|---------|
| `docx` | Tạo, đọc, sửa file Word (.docx) | claude.ai, Cowork, Claude Code, API | Tích hợp sẵn |
| `xlsx` | Tạo, đọc, sửa file Excel (.xlsx) | claude.ai, Cowork, Claude Code, API | Tích hợp sẵn |
| `pptx` | Tạo, đọc, sửa file PowerPoint (.pptx) | claude.ai, Cowork, Claude Code, API | Tích hợp sẵn |
| `pdf` | Tạo, đọc, merge, split, fill form PDF | claude.ai, Cowork, Claude Code, API | Tích hợp sẵn |

---

## 3. Official Standalone Skills

| Tên | Mô tả ngắn | Repository URL | Cài đặt |
|-----|-------------|----------------|---------|
| `doc-coauthoring` | Workflow co-authoring tài liệu có cấu trúc | github.com/anthropics/skills/tree/main/skills/doc-coauthoring [Cần xác minh] | Xem hướng dẫn bên dưới |
| `internal-comms` | Template viết internal communications | github.com/anthropics/skills/tree/main/skills/internal-comms | Xem hướng dẫn bên dưới |
| `skill-creator` | Tạo mới, sửa, đo lường hiệu quả skill | github.com/anthropics/skills/tree/main/skills/skill-creator | Xem hướng dẫn bên dưới |

Cách cài đặt theo từng surface:

- **Cowork:** Claude Desktop > Settings > Skills > Upload, hoặc cài qua Plugin marketplace.
- **Claude Code:** `/plugin marketplace add anthropics/skills` → `/plugin install <tên>`
- **claude.ai:** Settings > Features > Upload .skill file.

---

## 4. Official Plugins

| Tên plugin | Mô tả ngắn | Repository URL | Cài đặt |
|------------|-------------|----------------|---------|
| `productivity` | Quản lý task, notes, workflow | github.com/anthropics/knowledge-work-plugins/tree/main/plugins/productivity | Xem hướng dẫn bên dưới |
| `product-management` | Hỗ trợ PM workflows (PRD, roadmap, specs) | github.com/anthropics/knowledge-work-plugins/tree/main/plugins/product-management | Xem hướng dẫn bên dưới |
| `data` | Phân tích dữ liệu, visualization | github.com/anthropics/knowledge-work-plugins/tree/main/plugins/data | Xem hướng dẫn bên dưới |

Anthropic cung cấp 11+ plugins chính thức tại repo `anthropics/knowledge-work-plugins`. Ngoài 3 plugin liệt kê ở đây, còn có: sales, marketing, finance, legal, customer-support, enterprise-search, bio-research, cowork-plugin-management. [Cập nhật 03/2026 — kiểm tra repo để xem danh sách mới nhất]

Cách cài đặt theo từng surface:

- **Cowork:** Sidebar > Plugins > Browse > tìm tên plugin > Install.
- **Claude Code:** `claude plugin marketplace add anthropics/knowledge-work-plugins` → `claude plugin install <tên>`

---

## 5. Community Standalone Skills

> **CẢNH BÁO:** Community skills không được Anthropic review. Bắt buộc đọc file SKILL.md và kiểm tra thư mục `scripts/` trước khi cài đặt. Test trên thư mục không chứa sensitive data.

### 5a. Từ skillhub.club

| ID   | Tên                        | Author          | skillhub URL                                                                                  | CLI install                                           |
| ---- | -------------------------- | --------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| SH1  | `docs-review`              | @metabase       | skillhub.club/skills/metabase-metabase-docs-review                                            | `npx @skill-hub/cli install docs-review`              |
| SH2  | `obsidian-markdown`        | @kepano         | skillhub.club/skills/kepano-obsidian-markdown                                                 | `npx @skill-hub/cli install obsidian-markdown`        |
| SH3  | `voice-and-tone`           | @lerianstudio   | skillhub.club/skills/lerianstudio-voice-and-tone                                              | `npx @skill-hub/cli install voice-and-tone`           |
| SH4  | `mermaidjs-v11`            | @mrgoonie       | skillhub.club/skills/mrgoonie-mermaidjs-v11                                                   | `npx @skill-hub/cli install mermaidjs-v11`            |
| SH5  | `knowledge-capture`        | @rsmdt          | skillhub.club/skills/rsmdt-knowledge-capture                                                  | `npx @skill-hub/cli install knowledge-capture`        |
| SH6  | `technical-clarity`        | @panaversity    | skillhub.club/skills/panaversity-technical-clarity                                            | `npx @skill-hub/cli install technical-clarity`        |
| SH7  | `troubleshooting-docs`     | @glittercowboy  | skillhub.club/skills/glittercowboy-troubleshooting-docs                                       | `npx @skill-hub/cli install troubleshooting-docs`     |
| SH8  | `organizing-documentation` | @cipherstash    | skillhub.club/skills/cipherstash-organizing-documentation                                     | `npx @skill-hub/cli install organizing-documentation` |
| SH9  | `architecture-design`      | @rsmdt          | skillhub.club/skills/rsmdt-architecture-design                                                | `npx @skill-hub/cli install architecture-design`      |
| SH10 | `specification-management` | @rsmdt          | skillhub.club/skills/rsmdt-specification-management                                           | `npx @skill-hub/cli install specification-management` |
| SH11 | `document-converter`       | @benbrastmckie  | skillhub.club/skills/benbrastmckie-document-converter                                         | `npx @skill-hub/cli install document-converter`       |
| SH12 | `technical-writing`        | @rsmdt          | skillhub.club/skills/rsmdt-technical-writing                                                  | `npx @skill-hub/cli install technical-writing`        |
| SH13 | `format-markdown-table`    | @maslennikov-ig | skillhub.club/skills/maslennikov-ig-format-markdown-table                                     | `npx @skill-hub/cli install format-markdown-table`    |
| SH14 | `context-optimization`     | @muratcankoylan | skillhub.club/skills/muratcankoylan-agent-skills-for-context-engineering-context-optimization | `npx @skill-hub/cli install context-optimization`     |
| SH15 | `documentation-review`     | @lerianstudio   | skillhub.club/skills/lerianstudio-documentation-review                                        | `npx @skill-hub/cli install documentation-review`     |
| SH16 | `md-docs`                  | @paulrberg      | skillhub.club/skills/paulrberg-md-docs                                                        | `npx @skill-hub/cli install md-docs`                  |

### 5b. Từ GitHub

| ID | Tên | Repository URL | Cách tải |
|----|-----|----------------|----------|
| D1a | `meeting-synthesizer` | github.com/luckybajaj22031996/pm-ba-claude-skills | Download ZIP > extract `meeting-synthesizer.skill` |
| D1b | `stakeholder-updates` | github.com/luckybajaj22031996/pm-ba-claude-skills | Download ZIP > extract `stakeholder-updates.skill` |
| D1c | `prd-generator` | github.com/luckybajaj22031996/pm-ba-claude-skills | Download ZIP > extract `prd-generator.skill` |
| D1d | `market-research` | github.com/luckybajaj22031996/pm-ba-claude-skills | Download ZIP > extract `market-research.skill` |
| D2 | `meeting-minutes-taker` | github.com/daymade/claude-code-skills | Download ZIP > extract folder |
| D3 | `systematic-debugging` | github.com/obra/superpowers | Download ZIP > extract `systematic-debugging` folder |

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

## 7. Ghi chú

Custom Skills (Phenikaa-X) sẽ được bổ sung khi hoàn thành.

Skills KHÔNG sync giữa các surface. Skill cài trên claude.ai không tự có trên Cowork hay Claude Code. Cần cài riêng cho từng surface. (Nguồn: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
