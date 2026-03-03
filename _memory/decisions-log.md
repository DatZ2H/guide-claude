# Decisions Log

| Date | Decision | Rationale | Source |
|------|----------|-----------|--------|
| 2026-03-03 | Version bump 4.0 → 4.1 | Sprint v4.1 complete — config-architecture.md, project-instructions scaffold, global-instructions scaffold, SETUP.md, Module 10 §10.4.1+10.6.7-10.6.9, conflict review 9 fixes | Version bump workflow |
| 2026-03-02 | Tạo guide/reference/config-architecture.md làm single source of truth cho 6 lớp cấu hình | Unified mental model. Thay vì phân tán khắp Module 02 và 10, reference doc độc lập dễ cross-link, dễ update | Brainstorm session gaps |
| 2026-03-02 | Stable vs Dynamic content split: stable (khái niệm, framework) → modules; dynamic (templates) → _scaffold/ | Templates hay thay đổi theo Claude features. Đặt trong _scaffold/ → update một chỗ, không re-version toàn bộ module | Architecture decision |
| 2026-03-02 | Deprecate _scaffold/skill-templates/SKILL-template.md (file format) → folder format SKILL-template/SKILL-template.md | Actual skills đều là folder/SKILL.md. Template phải match format thực tế | Consistency fix |
| 2026-03-02 | Tạo .claude/SETUP.md — project manifest cho maintainer mới | Gap: kỹ sư mới vào project không biết "cần cài gì, có skills gì, trigger phrase là gì". SETUP.md = onboarding checklist | Gap H fill |
| 2026-03-02 | Tạo _scaffold/project-instructions/ với 4 templates + README | Project Instructions là lớp cấu hình thiếu trong scaffold. 4 templates cover 80% use cases (basic, tech-doc, troubleshooting, code-review) | Gap G fill |
| 2026-03-02 | Tạo _scaffold/global-instructions/global-CLAUDE-phenikaa-x.md | Global CLAUDE.md cần template cụ thể cho Phenikaa-X identity + toolchain conventions | Gap G fill |
| 2026-03-02 | Version bump 3.5 → 4.0 | Sprint v4.0 complete — 3-tier architecture, Cowork-primary, _scaffold/, 4 skills | Version bump workflow |
| 2026-03-02 | Chuyển sang 3-tier architecture (guide/ + .claude/ + _memory/) | Phân tách rõ content vs infrastructure vs persistence. Giảm token overhead khi Claude phân loại files | Brainstorm session 2026-03-02 |
| 2026-03-02 | Giảm _memory/ từ 4 files → 2 files (session-state + decisions-log) | Giảm token cost đầu session. handoff overlap project-state, todo overlap TodoWrite built-in, context-map dễ stale | Anthropic best practices: context fills up fast |
| 2026-03-02 | Thêm VERSION file làm SSOT | Tránh hardcode version trong 11+ files. Pattern từ Florian repo | FlorianBruniaux/claude-cowork-guide |
| 2026-03-02 | Rename 00-README.md → 00-overview.md | Root đã có README.md. Tránh 2 files cùng tên README | Standard OSS practice |
| 2026-03-02 | Dùng .claude/skills/ thay _project-setup/ | Skills on-demand loading tiết kiệm token hơn static markdown files. Anthropic recommend skills cho domain workflows | Anthropic Agent Skills docs |
| 2026-03-02 | Reframe Two-Layer → Cowork-primary + context transfer | Sync protocol overhead > benefit. Cowork có web search + brainstorm dẫn đến action ngay. project-state.md chuyển từ "sync bridge" → "briefing doc paste khi cần" | Brainstorm session 2026-03-02 |
| 2026-03-01 | Áp dụng Two-Layer Knowledge Model | Giải quyết desync Project Knowledge ↔ Cowork folder | Dự án nội bộ |
| 2026-02-28 | Kiến trúc layered: Core Principles → Type-Specific → Templates → Glossary | Phân tầng cho Documentation Standard use case | Dự án nội bộ |
