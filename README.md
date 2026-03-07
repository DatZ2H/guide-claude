# Claude Guide cho Kỹ sư Phenikaa-X

**v9.0** | Claude Opus 4.6 / Sonnet 4.6 / Haiku 4.5 | Tiếng Việt

Bộ tài liệu 3-tier (32 files) hướng dẫn sử dụng Claude AI cho công việc kỹ thuật — prompt engineering, context management, documentation workflows, CLI automation, agents, plugins.

**Đối tượng:** Kỹ sư tự động hóa, R&D, Robotics tại Phenikaa-X (AMR, ROS, SLAM, Lidar). Mở rộng cho bất kỳ kỹ sư nào muốn dùng Claude hiệu quả.

---

## Bắt đầu từ đâu?

| Bạn là... | Bắt đầu tại | Thời gian |
|-----------|-------------|-----------|
| Người mới dùng Claude | [Quick Start](guide/base/01-quick-start.md) → [Setup](guide/base/02-setup.md) | 1-2 giờ |
| Đã dùng, muốn nâng cao | [Prompt Engineering](guide/base/03-prompt-engineering.md) → [Context Management](guide/base/04-context-management.md) | 2-3 giờ |
| Technical Writer / Doc author | base/ xong → [Doc Workflows](guide/doc/01-doc-workflows.md) | +2 giờ |
| Developer / CLI user | base/ xong → [Claude Code Setup](guide/dev/01-claude-code-setup.md) | +2 giờ |

> Mục lục đầy đủ, learning paths chi tiết, conventions: xem [base/00-overview.md](guide/base/00-overview.md)

---

## Nội dung

### Base — Nền tảng (ai cũng cần)

8 modules: prompt engineering, context management, tools & features, mistakes & fixes, evaluation framework.

[Xem danh sách modules](guide/base/00-overview.md#base--kiến-thức-nền-tảng-ai-cũng-cần)

### Doc — Technical Writing & Cowork

6 modules: doc workflows, template library, Cowork setup & workflows, Claude Code cho documentation, Custom Style.

[Xem danh sách modules](guide/base/00-overview.md#doc--technical-writing--documentation)

### Dev — Developer & Automation

6 modules: CLI setup, CLI reference, IDE integration (VS Code), agents & automation (subagents, Agent Teams, CI/CD), plugins & MCP, dev workflows (git, testing, code review).

[Xem danh sách modules](guide/base/00-overview.md#dev--developer--automation)

### Reference — Tra cứu nhanh

12 files: [cheatsheet base](guide/reference/cheatsheet-base.md), [cheatsheet doc](guide/reference/cheatsheet-doc.md), [cheatsheet dev](guide/reference/cheatsheet-dev.md), model specs, config architecture, prompt format guide, skills guide, ecosystem overview.

---

## Tạo project Claude mới

Thư mục `_scaffold/` chứa starter templates để bootstrap project Claude từ zero — CLAUDE.md, commands, hooks, skills, checklists.

Xem [_scaffold/README-scaffold.md](_scaffold/README-scaffold.md) để bắt đầu.

---

## Cho maintainers

| File | Vai trò |
|------|---------|
| `VERSION` | SSOT cho version number |
| `project-state.md` | Trạng thái modules, decisions gần nhất |
| `upgrade-plan-v8.md` | Plan upgrade v7.0 → v9.0 (completed) |
| `.claude/SETUP.md` | Onboarding cho maintainer mới |
| `.claude/` | Infra: rules, hooks, skills, commands, settings |
| `machine-readable/llms.txt` | Machine-readable index cho AI tools |
