# Ecosystem Overview — Claude Code Community Tools

**Cập nhật:** 2026-03-07 | Tham chiếu nhanh — tra cứu khi cần tìm tools

---

Danh sách curated các community tools, extensions, và resources cho Claude Code. Phân loại theo chức năng, kèm disclaimer cho sources không phải Anthropic official.

> [!NOTE]
> Danh sách này chủ yếu từ community sources. Verify compatibility và security trước khi dùng trong production.

[Ghi chú: tổng hợp từ community repositories, không phải Anthropic official] [Cập nhật 03/2026]

---

## Official Resources

Tài liệu và tools từ Anthropic — nguồn tin cậy nhất.

| Resource | URL | Mô tả |
|----------|-----|--------|
| Claude Code Docs | code.claude.com/docs | Documentation chính thức |
| Anthropic API Docs | platform.claude.com/docs | API reference |
| Anthropic Help | support.anthropic.com | Help Center cho UI/plans/limits |
| Claude Code GitHub | github.com/anthropics/claude-code | Source code + devcontainer reference |
| Agent SDK | platform.claude.com/docs/en/agent-sdk | Python + TypeScript SDK |
| MCP Specification | modelcontextprotocol.io | Model Context Protocol spec |
| MCP Servers (official) | github.com/anthropics/mcp-servers | Official MCP server implementations |

[Nguồn: Anthropic Official]

---

## Community Reference Repositories

Repositories tổng hợp best practices và resources.

| Repository | Maintainer | Nội dung | Notes |
|-----------|------------|----------|-------|
| `claude-code-best-practice` | shanraisshan (GitHub) | CLI tips, workflow patterns, URL index | Cập nhật thường xuyên |
| `awesome-claude-code` | hesreallyhim (GitHub) | Curated list: tools, plugins, tutorials | Danh mục phong phú |
| `claude-cowork-guide` | FlorianBruniaux (GitHub) | Cowork workflows, config patterns | Focus Cowork/Desktop |

[Ghi chú: Community repositories — tên repo và maintainer dựa trên GitHub tại thời điểm viết. Verify thông tin tại official docs trước khi áp dụng.]

---

## MCP Servers — Phổ biến

MCP servers mở rộng Claude Code với external tools và data sources.

### Anthropic-maintained MCP Servers

MCP servers từ repo `github.com/anthropics/mcp-servers` — do Anthropic phát triển và duy trì.

| Server | Chức năng |
|--------|-----------|
| GitHub | Issues, PRs, repos, code search |
| Slack | Channels, messages, search |
| Google Drive | Documents, spreadsheets |

[Nguồn: Anthropic GitHub — mcp-servers] [Cập nhật 03/2026]

### Vendor/Third-party MCP Servers

MCP servers phổ biến — do vendor hoặc community phát triển, không phải Anthropic.

| Server | Chức năng | Maintainer |
|--------|-----------|------------|
| Jira | Tickets, projects | Atlassian ecosystem |
| Linear | Issues, projects | Linear team |
| Notion | Pages, databases | Community |

[Ghi chú: Verify maintainer và trust level trước khi cài. Xem `/mcp` trong Claude Code để kiểm tra available servers.]

### Community MCP Servers

| Server | Chức năng | Category |
|--------|-----------|----------|
| Playwright MCP | Browser automation, testing | Testing |
| Chrome MCP | Chrome DevTools control | Debugging |
| PostgreSQL MCP | Database queries, schema | Database |
| Redis MCP | Cache management | Database |
| Sentry MCP | Error tracking | Monitoring |
| Docker MCP | Container management | DevOps |

[Ghi chú: Community MCP servers — kiểm tra trust level và permissions trước khi cài]

Chi tiết cài đặt MCP: xem [dev/05 — Plugins & MCP](../dev/05-plugins.md).

---

## Plugins — Marketplace

Plugins mở rộng Claude Code với skills, agents, hooks, và MCP servers bundled.

### Code Intelligence Plugins

Plugins cung cấp precise symbol navigation và error detection:

| Plugin | Ngôn ngữ | Chức năng |
|--------|----------|-----------|
| TypeScript LSP | TypeScript/JavaScript | Go-to-definition, find-references, diagnostics |
| `pyright-lsp` | Python | Type checking, auto-import, diagnostics |
| Rust Analyzer | Rust | Full language server features |
| Go LSP | Go | Navigation, completion, diagnostics |

[Nguồn: Claude Code Docs — Discover Plugins]

### Workflow Plugins

| Plugin | Chức năng |
|--------|-----------|
| Todoist | Task management integration |
| Figma | Design file access |
| AWS | Cloud resource management |

[Ghi chú: Plugin ecosystem đang phát triển nhanh — chạy `/plugin` để xem marketplace mới nhất]

Chi tiết plugin system: xem [dev/05 — Plugins](../dev/05-plugins.md).

---

## Community Patterns

Workflow patterns từ community — không phải Anthropic official nhưng được nhiều người dùng.

| Pattern | Mô tả | Source |
|---------|--------|--------|
| RIPER | Structured 5-phase workflow: Research → Innovate → Plan → Execute → Review | Community |
| Ralph Wiggum | "Explain like I'm 5" debugging — force Claude to simplify assumptions | Community |
| Writer/Reviewer | 2-session pattern: một viết code, một review với clean context | Best Practices (official) |
| Plan → Execute | Plan Mode exploration, rồi switch Normal Mode implementation | Best Practices (official) |

[Ghi chú: RIPER và Ralph Wiggum là community patterns, không phải Anthropic official. Hiệu quả phụ thuộc use case.]

---

## CI/CD Integrations

| Platform | Integration | Docs |
|----------|------------|------|
| GitHub Actions | `anthropics/claude-code-action` | code.claude.com/docs/en/github-actions |
| GitLab CI/CD | Agent SDK CLI trong pipeline | code.claude.com/docs/en/gitlab-ci-cd |
| Custom CI | `claude -p` headless mode | code.claude.com/docs/en/headless |

Chi tiết: xem [dev/04 — CI/CD Integration](../dev/04-agents-automation.md).

---

## IDE Integrations

| IDE | Type | Status |
|-----|------|--------|
| VS Code | Official extension | Stable |
| JetBrains (IntelliJ, PyCharm...) | Official plugin | Beta |
| Cursor | Compatible (VS Code-based) | Stable |
| Neovim | Community | Community |
| Emacs | Community | Community |

Chi tiết setup: xem [dev/03 — IDE Integration](../dev/03-ide-integration.md).

---

## Cross-references

- **CLI setup và configuration:** [dev/01](../dev/01-claude-code-setup.md)
- **CLI commands reference:** [dev/02](../dev/02-cli-reference.md)
- **IDE integrations chi tiết:** [dev/03](../dev/03-ide-integration.md)
- **Agents và automation:** [dev/04](../dev/04-agents-automation.md)
- **Plugins và MCP chi tiết:** [dev/05](../dev/05-plugins.md)
- **Dev workflows:** [dev/06](../dev/06-dev-workflows.md)

---

*Ecosystem này thay đổi nhanh. Chạy `/plugin` trong Claude Code để xem marketplace mới nhất. Verify tại official docs trước khi dùng community tools trong production.*
