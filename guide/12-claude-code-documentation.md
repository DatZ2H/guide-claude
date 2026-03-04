# Module 12: Claude Code cho Documentation & Technical Writing

**Thời gian đọc:** 35 phút | **Mức độ:** Intermediate
**Cập nhật:** 2026-03-04 | Models: xem [specs](reference/model-specs.md)

---

Module này hướng dẫn sử dụng Claude Code — CLI agent chạy trong terminal — cho documentation và technical writing workflow. Nếu bạn không viết code, đây vẫn là công cụ mạnh cho quản lý tài liệu có Git, batch editing, và quality assurance tự động.

> [!NOTE]
> Module này focus vào **non-coding documentation workflow**. Nếu bạn dùng Claude Code để viết code, tham khảo official docs tại https://code.claude.com/docs.
> Nếu bạn chỉ cần tạo/sửa file đơn lẻ mà không cần Git → xem [Module 10: Cowork](10-claude-desktop-cowork.md).

**Config & Commands reference:** [Claude Code Setup](reference/claude-code-setup.md)

[Nguồn: Claude Code Docs]

---

## 12.1 Claude Code là gì — cho Non-coders

Claude Code là CLI agent chạy trong terminal, dùng chung kiến trúc với Claude Desktop (Cowork) nhưng được thiết kế cho môi trường có Git và file system access rộng hơn. Điểm khác biệt cốt lõi: thay vì chat qua UI, bạn làm việc trong terminal với workflow tự động hóa và batch operations. Section này giải thích khi nào dùng Claude Code thay vì Cowork hoặc claude.ai — đặc biệt cho các kỹ sư documentation không viết code.

| Tình huống | claude.ai | Claude Desktop (Cowork) | Claude Code |
|---|---|---|---|
| Chat & brainstorm | ✅ Tốt nhất | ✅ | ✅ |
| Sửa 1 file đơn lẻ | ✅ | ✅ Tốt nhất | ✅ |
| Batch edit nhiều file | ❌ | ⚠️ Hạn chế | ✅ Tốt nhất |
| Git commit & branch | ❌ | ❌ | ✅ Tốt nhất |
| CI/CD integration | ❌ | ❌ | ✅ Tốt nhất |
| Custom hooks & automation | ❌ | ❌ | ✅ Tốt nhất |

[Full content sẽ viết ở S17/S18]

## 12.2 Cài đặt & First Session

Hướng dẫn cài đặt Claude Code qua npm, verify bằng `claude --version`, và khởi tạo first session trong thư mục dự án. Lệnh `/init` tạo `CLAUDE.md` mẫu — bước nên làm ngay với project mới. Section này đi kèm checklist nhanh để xác nhận môi trường sẵn sàng.

Xem thêm: [Claude Code Setup — Quick Setup Checklist](reference/claude-code-setup.md#quick-setup-checklist).

[Nguồn: Claude Code Docs — Installation]

[Full content sẽ viết ở S17/S18]

## 12.3 Cấu hình 4 lớp (User → Project → Local → Managed)

Claude Code có hệ thống cấu hình 4 lớp theo thứ tự ưu tiên tăng dần: **User** (`~/.claude/CLAUDE.md`) → **Project** (`CLAUDE.md` tại root) → **Local** (`.claude/CLAUDE.md`, không commit) → **Managed** (enterprise policy). Mỗi lớp kế thừa và override lớp dưới. Section này giải thích cách cấu hình từng lớp cho documentation project — language rules, writing standards, emoji policy — và khi nào dùng `.claude/rules/` thay vì CLAUDE.md chính.

Xem thêm: [Claude Code Setup — CLAUDE.md Reference](reference/claude-code-setup.md#claudemd-reference).

[Nguồn: Claude Code Docs — Configuration]

[Full content sẽ viết ở S17/S18]

## 12.4 Plan Mode — Explore → Plan → Execute → Commit

Plan Mode là workflow 4 bước: Claude đọc context (Explore), đề xuất approach và xin approve (Plan), thực hiện (Execute), rồi save kết quả (Commit). Kích hoạt bằng toggle Plan Mode trong session hoặc thêm "think step by step" vào prompt. [Cập nhật 03/2026] Với documentation, nên dùng Plan Mode khi rewrite module lớn, refactor cấu trúc nhiều file, hoặc batch update cross-references — skip Plan khi chỉ sửa lỗi nhỏ hoặc thêm vài dòng.

[Nguồn: Claude Code Docs — Plan Mode]

[Full content sẽ viết ở S17/S18]

## 12.5 Slash Commands & Custom Commands

Slash commands là workflow được đóng gói thành file markdown trong `.claude/commands/`, gọi bằng `/command-name` trong session. Custom commands phù hợp cho documentation project vì chuẩn hóa các tác vụ lặp lại. Section này hướng dẫn tạo custom command từ đầu và trình bày các ví dụ thực tế từ Guide Claude: `/start`, `/checkpoint`, `/validate-doc`.

[Nguồn: Claude Code Docs — Custom Slash Commands]

[Full content sẽ viết ở S17/S18]

## 12.6 Skills cho Documentation

Skills là agent chuyên biệt được gọi từ main session để thực hiện tác vụ có quy trình cố định. Phân biệt hai loại: **invocable** (user trigger thủ công) và **reference** (Claude tự load context). Section này hướng dẫn tạo custom skill cho documentation workflow, giải thích `disable-model-invocation`, và phân tích cost/benefit. Ví dụ thực tế: `doc-standard-enforcer` từ project này.

Xem thêm: [Skills List](reference/skills-list.md).

[Nguồn: Claude Code Docs — Skills]

[Full content sẽ viết ở S17/S18]

## 12.7 Subagents cho Review & Research

Subagents là Claude instance độc lập chạy song song hoặc tuần tự với main session, cấu hình qua `.claude/agents/`. Pattern hữu ích nhất cho documentation: **Writer/Reviewer** — main session viết, subagent review theo checklist độc lập không bị bias từ writing context. Section này giải thích khi nào dùng subagent thay vì main session, và cách cấu hình `.claude/agents/` template.

[Nguồn: Claude Code Docs — Sub-agents]

[Full content sẽ viết ở S17/S18]

## 12.8 Session Management

Các lệnh quản lý session: `/clear` (reset context, giữ file), `/rewind` (undo về checkpoint trước), `/rename` (đặt tên để resume sau), `/compact` (tóm tắt context dài). Flag CLI: `--continue` resume session gần nhất, `--resume <id>` resume session cụ thể. Section này cũng đề cập hai failure pattern phổ biến — kitchen sink và over-correction — cùng cách tránh.

Xem thêm: [Claude Code Setup — Essential Commands](reference/claude-code-setup.md#essential-commands).

[Nguồn: Claude Code Docs — Session Management]

[Full content sẽ viết ở S17/S18]

## 12.9 Git Integration cho Documentation

Claude Code tích hợp Git natively: tạo branch, commit, đọc git history trong session. Section này hướng dẫn thiết lập Git workflow cho documentation project — branch naming convention, commit message format, pre-commit hooks để validate trước khi commit. Trình bày `SessionStart` hook: chạy tự động khi mở session, hiển thị git status và nhắc checkpoint.

[Nguồn: Claude Code Docs — Git Integration]

[Full content sẽ viết ở S17/S18]

## 12.10 Verification & Quality Assurance

Pattern hiệu quả nhất trong documentation QA là cung cấp cho Claude checklist kiểm tra output của chính nó — thay vì chỉ yêu cầu "viết tốt". Section này trình bày `/validate-doc` (heading hierarchy, language tags, cross-links, emoji policy), `cross-ref-checker` skill (phát hiện broken links), và nguyên tắc thiết kế checklist có tiêu chí pass/fail rõ ràng.

[Full content sẽ viết ở S17/S18]

## 12.11 Permissions & Safety

Claude Code có hệ thống permissions granular: cho phép hoặc deny từng tool (read, write, bash, git) theo scope session hoặc project. Lệnh `/permissions` hiển thị và chỉnh sửa permissions hiện tại. Section này hướng dẫn cấu hình permissions tối giản cho documentation workflow (thường không cần bash rộng), và giải thích sandbox mode — dry-run trước khi approve execute.

Xem thêm: [Claude Code Setup — Permission Templates](reference/claude-code-setup.md#permission-templates).

[Nguồn: Claude Code Docs — Permissions]

[Full content sẽ viết ở S17/S18]

## 12.12 Token Optimization & Cost

Model selection là đòn bẩy lớn nhất cho cost: Haiku cho tác vụ đơn giản (format check, batch rename), Sonnet cho editing và review thông thường, Opus chỉ khi cần phân tích kiến trúc phức tạp. `/compact` tóm tắt context dài để giảm token trong session nhiều file. Section này còn đề cập `offset`/`limit` khi đọc file lớn, và `effort` level để điều chỉnh thinking depth.

Xem thêm: [Model Specs & Pricing](reference/model-specs.md).

[Nguồn: Claude Code Docs — Token Usage]

[Full content sẽ viết ở S17/S18]

## 12.13 Batch & Automation

Claude Code hỗ trợ non-interactive mode qua `claude -p "prompt"` — cho phép pipe input/output, tích hợp CI pipeline, và fan-out pattern (nhiều instance song song). Section này trình bày các use case documentation: validate docs trong PR check, auto-generate changelog từ git diff, batch format nhiều file. Bao gồm ví dụ tích hợp GitHub Actions.

[Nguồn: Claude Code Docs — CLI Usage]

[Full content sẽ viết ở S17/S18]

## 12.14 Plugins & MCP cho Documentation

MCP (Model Context Protocol) cho phép Claude Code kết nối external services qua standardized interface. Lệnh `claude mcp add` thêm plugin từ marketplace hoặc custom server. Section này điểm qua các plugin có ích cho documentation: GitHub (đọc issues, tạo PR comment), Notion (sync markdown ↔ Notion), và hướng dẫn approve permissions cho từng plugin.

[Nguồn: Claude Code Docs — MCP]

[Full content sẽ viết ở S17/S18]

## 12.15 External Resources & Further Reading

Tổng hợp tài liệu tham khảo và community resources cho Claude Code documentation workflow. Ưu tiên đọc: official docs, changelog để track feature mới, community patterns cho documentation-specific use cases.

- [Claude Code Official Docs](https://code.claude.com/docs)
- [Claude Code Setup Cheat Sheet](reference/claude-code-setup.md)
- [Model Specs & Pricing](reference/model-specs.md)
- [Skills List](reference/skills-list.md)
- [Config Architecture](reference/config-architecture.md)

[Full content sẽ viết ở S17/S18]
