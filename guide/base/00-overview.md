# Claude Guide cho Kỹ sư Phenikaa-X

**Version:** xem [VERSION](../../VERSION) | **Cập nhật:** 2026-03-07
**Claude models:** Opus 4.6 / Sonnet 4.6 / Haiku 4.5

---

## Giới thiệu

[Ứng dụng Kỹ thuật]

Tài liệu này hướng dẫn sử dụng Claude AI hiệu quả cho công việc kỹ thuật hàng ngày -- từ viết prompt cơ bản đến quản lý context trong conversation dài, từ tạo tài liệu chuyên nghiệp đến phân tích lỗi hệ thống.

**Đối tượng chính:** Kỹ sư tự động hóa, R&D, Robotics tại Phenikaa-X (AMR, ROS, SLAM, Lidar).

**Đối tượng mở rộng:** Bất kỳ kỹ sư kỹ thuật nào muốn sử dụng Claude hiệu quả.

---

## Cấu trúc 3-Tier

Tài liệu được tổ chức thành 3 nhóm theo đối tượng sử dụng:

### Base — Kiến thức nền tảng (ai cũng cần)

| Module | Tên | Mô tả |
|--------|-----|-------|
| **00** | Overview (file này) | Mục lục, learning paths, conventions |
| **01** | [Quick Start](01-quick-start.md) | Bắt đầu với Claude trong 15 phút |
| **02** | [Setup & Personalization](02-setup.md) | Projects, Styles, Memory, MCP |
| **03** | [Prompt Engineering](03-prompt-engineering.md) | 6 nguyên tắc, 7 kỹ thuật, Module System |
| **04** | [Context Management](04-context-management.md) | Context Window, Drift, Session Lifecycle, Decision Framework |
| **05** | [Tools & Features](05-tools-features.md) | Tính năng Claude, Desktop, Planning patterns |
| **06** | [Mistakes & Fixes](06-mistakes-fixes.md) | 7 nhóm lỗi phổ biến và cách sửa |
| **07** | [Evaluation](07-evaluation.md) | Framework đánh giá chất lượng output |

### Doc — Technical Writing & Documentation

| Module | Tên | Mô tả |
|--------|-----|-------|
| **01** | [Doc Workflows](../doc/01-doc-workflows.md) | Recipes doc-specific và Cowork recipes |
| **02** | [Template Library](../doc/02-template-library.md) | Templates doc-specific (T-06 đến T-22) |
| **03** | [Cowork Setup](../doc/03-cowork-setup.md) | Cowork config và workflows |
| **04** | [Cowork Workflows](../doc/04-cowork-workflows.md) | 12 Cowork workflows copy-paste |
| **05** | [Claude Code Doc](../doc/05-claude-code-doc.md) | Claude Code cho documentation |
| **06** | [Custom Style](../doc/06-custom-style.md) | Custom Style reference chi tiết |

### Dev — Developer & Automation (P3 — chưa viết)

| Module | Tên | Mô tả |
|--------|-----|-------|
| **01** | [Claude Code Setup](../dev/01-claude-code-setup.md) | CLI install, auth, config |
| **02** | [CLI Reference](../dev/02-cli-reference.md) | Commands, flags, shortcuts |
| **03** | [IDE Integration](../dev/03-ide-integration.md) | VS Code extension setup & tips |
| **04** | [Agents & Automation](../dev/04-agents-automation.md) | Subagents, Agent Teams, CI/CD |
| **05** | [Plugins](../dev/05-plugins.md) | Discover, install, create plugins |
| **06** | [Dev Workflows](../dev/06-dev-workflows.md) | Git, testing, code review with CC |

### Reference — Tra cứu (ai cũng dùng)

| File | Mô tả |
|------|-------|
| [Model Specs](../reference/model-specs.md) | Bảng so sánh Opus/Sonnet/Haiku |
| [Config Architecture](../reference/config-architecture.md) | Cấu trúc config Claude |
| [Skills List](../reference/skills-list.md) | Lookup table skills |
| [Quick Templates](../reference/quick-templates.md) | 5 templates cơ bản |
| [Workflow Patterns](../reference/workflow-patterns.md) | Patterns tham chiếu |
| [Claude Code Setup](../reference/claude-code-setup.md) | Cheat sheet Claude Code |

---

## Dependency Graph

```mermaid
flowchart TD
    classDef base fill:#86efac,stroke:#16a34a,color:#000
    classDef doc fill:#fde047,stroke:#ca8a04,color:#000
    classDef dev fill:#93c5fd,stroke:#2563eb,color:#000

    subgraph BASE ["Base — Nền tảng"]
        B00["00 Overview"]:::base
        B01["01 Quick Start"]:::base
        B02["02 Setup"]:::base
        B03["03 Prompts"]:::base
        B04["04 Context"]:::base
        B05["05 Tools"]:::base
        B06["06 Mistakes"]:::base
        B07["07 Evaluation"]:::base
    end

    subgraph DOC ["Doc — Technical Writing"]
        D01["doc/01 Workflows"]:::doc
        D02["doc/02 Templates"]:::doc
        D03["doc/03 Cowork Setup"]:::doc
        D04["doc/04 Cowork WF"]:::doc
        D05["doc/05 CC Doc"]:::doc
        D06["doc/06 Custom Style"]:::doc
    end

    subgraph DEV ["Dev — Developer"]
        V01["dev/01 CC Setup"]:::dev
        V02["dev/02 CLI Ref"]:::dev
        V03["dev/03 IDE"]:::dev
        V04["dev/04 Agents"]:::dev
        V05["dev/05 Plugins"]:::dev
        V06["dev/06 Dev WF"]:::dev
    end

    B01 --> B02
    B02 --> B03
    B03 --> B04
    B04 --> B05
    B05 --> B06
    B06 --> B07

    B03 --> D01
    B05 --> D01
    B03 --> D02
    B02 --> D06
    B05 --> D03
    B07 --> D04
    B04 --> D05

    B02 --> V01
    B03 --> V04
    B05 --> V03
    B06 --> V06
```

---

## Learning Paths

[Ứng dụng Kỹ thuật]

### Path A: Người mới bắt đầu (1-2 giờ)

Chưa từng dùng Claude hoặc mới dùng vài lần.

```text
base/01 Quick Start (15 phút)
  |
base/02 Setup & Personalization (20 phút)
  |
base/06 Mistakes & Fixes (15 phút)
  |
reference/ — tra cứu khi cần
```

**Kết quả:** Biết cách dùng Claude cơ bản, đã setup workspace, có templates sẵn sàng dùng.

### Path B: Người muốn nâng cao (2-3 giờ)

Đã dùng Claude, muốn hiệu quả hơn.

```text
base/03 Prompt Engineering (25 phút)
  |
base/04 Context Management (15 phút)
  |
base/05 Tools & Features (20 phút)
  |
base/07 Evaluation Framework (10 phút)
```

**Kết quả:** Viết prompt chuyên nghiệp, quản lý conversation dài, có quy trình cho từng loại task.

### Path C: Documentation track (base → doc)

Đã nắm base, muốn chuyên sâu Technical Writing và Cowork.

```text
base/ (tất cả) --> doc/01 Doc Workflows
                     |
                   doc/02 Template Library
                     |
                   doc/03 Cowork Setup
                     |
                   doc/04 Cowork Workflows
                     |
                   doc/05 Claude Code Doc
                     |
                   doc/06 Custom Style
```

**Kết quả:** Thành thạo documentation workflows, Cowork mode, Claude Code cho technical writing.

### Path D: Developer track (base → dev)

Đã nắm base, muốn dùng Claude Code cho development.

```text
base/ (tất cả) --> dev/01 Claude Code Setup
                     |
                   dev/02 CLI Reference
                     |
                   dev/03 IDE Integration
                     |
                   dev/04 Agents & Automation
                     |
                   dev/05 Plugins
                     |
                   dev/06 Dev Workflows
```

**Kết quả:** Setup Claude Code, thao tác CLI, tích hợp IDE, xây dựng automation pipelines.

> [!NOTE]
> Dev tier đang trong quá trình viết (P3). Hiện tại chỉ có placeholder files.

---

## Conventions trong tài liệu

### Nguồn trích dẫn

| Marker | Nghĩa |
|--------|-------|
| `[Nguồn: Anthropic Docs]` + URL | Thông tin từ tài liệu chính thức Anthropic |
| `[Ứng dụng Kỹ thuật]` | Ví dụ ứng dụng nguyên tắc chính thức vào bối cảnh Phenikaa-X |
| `[Cập nhật MM/YYYY]` | Thông tin mới hoặc thay đổi so với version trước |

### Format

- **Tiếng Việt** là ngôn ngữ chính, thuật ngữ kỹ thuật giữ **tiếng Anh**
- `{{variable_name}}` -- placeholder cần thay bằng giá trị thực
- XML tags trong code blocks -- copy-paste vào Claude
- Mermaid diagrams -- flowcharts và decision trees
- Tables -- so sánh, tra cứu nhanh

### Ký hiệu trạng thái

- BAD/GOOD -- so sánh prompt kém vs tốt
- CẢNH BÁO -- thông tin safety quan trọng
- LƯU Ý -- tips và best practices

### Icon và Emoji

- Tài liệu này chỉ sử dụng icons trong allowlist: ⚠️ ✅ ❌ 🔴 🟡 🟢 🔵
- Icons chỉ xuất hiện trong bảng status và warning markers
- Prose dùng Obsidian callouts: `> [!WARNING]`, `> [!TIP]`, `> [!NOTE]`, `> [!IMPORTANT]`

---

## Thông tin cập nhật

[Cập nhật 03/2026]

### Version 7.3 (03/2026)

- **P2 Restructure:** Tách guide/ thành 3 tier — base/ (nền tảng), doc/ (technical writing), dev/ (developer)
- **Navigation:** Thêm prev/next nav links toàn bộ files
- **M08 Nhóm 7:** Thêm 5 anti-patterns đặc thù Claude Code
- **P1 Final Review:** Hoàn tất Phase 1 Foundation

### Version 7.2 (03/2026)

- **P1.S4 Prompt format:** Áp dụng convention XML/[]/{{}} nhất quán cho M05, M07
- **Code blocks:** Thêm language tags cho tất cả code blocks còn thiếu

### Version 7.1 (03/2026)

- **P1.S1 Cross-link audit:** Fix broken cross-links, cập nhật URLs
- **P1.S2 Source markers:** Thêm source markers 3-tier cho toàn bộ guide/

### Version 7.0 (03/2026)

- **Thêm Module 12:** Claude Code cho Documentation & Technical Writing
- **Thêm reference/claude-code-setup.md:** Cheat sheet Claude Code
- **Thêm Mermaid dependency graph** và metadata depends-on/impacts

> Lịch sử đầy đủ từ v3.0: xem [CHANGELOG.md](../../CHANGELOG.md)

### Kiểm tra thông tin mới

Thông tin về Claude thay đổi nhanh. Luôn kiểm tra nguồn chính thức:

| Nguồn | URL | Nội dung |
|-------|-----|---------|
| Anthropic Docs | https://platform.claude.com/docs/en | API docs, model specs, prompting guides |
| Anthropic Help Center | https://support.claude.com | Claude.ai features, troubleshooting |
| Anthropic News | https://www.anthropic.com/news | Announcements, new features |
| Models Overview | https://platform.claude.com/docs/en/about-claude/models/overview | Model specs mới nhất |

---

## Files trong bộ tài liệu

```text
guide/
├── base/                    Nền tảng — ai cũng cần
│   ├── 00-overview.md       (file này)
│   ├── 01-quick-start.md    Bắt đầu 15 phút
│   ├── 02-setup.md          Setup & Personalization
│   ├── 03-prompt-engineering.md   Prompt Engineering
│   ├── 04-context-management.md   Context Management
│   ├── 05-tools-features.md      Tools, Features, Planning
│   ├── 06-mistakes-fixes.md      Mistakes & Fixes
│   └── 07-evaluation.md          Evaluation Framework
│
├── doc/                     Technical Writing audience
│   ├── 01-doc-workflows.md       Doc Workflows & Recipes
│   ├── 02-template-library.md    Template Library
│   ├── 03-cowork-setup.md        Cowork Setup & Config
│   ├── 04-cowork-workflows.md    12 Cowork Workflows
│   ├── 05-claude-code-doc.md     Claude Code cho Documentation
│   └── 06-custom-style.md        Custom Style Reference
│
├── dev/                     Developer audience (P3)
│   ├── 01-claude-code-setup.md   CLI Setup
│   ├── 02-cli-reference.md       CLI Reference
│   ├── 03-ide-integration.md     VS Code Integration
│   ├── 04-agents-automation.md   Agents & Automation
│   ├── 05-plugins.md             Plugins
│   └── 06-dev-workflows.md       Dev Workflows
│
└── reference/               Tra cứu
    ├── model-specs.md        Model comparison
    ├── config-architecture.md Config structure
    ├── skills-list.md        Skills lookup
    ├── quick-templates.md    Quick templates
    ├── workflow-patterns.md  Workflow patterns
    └── claude-code-setup.md  CC cheat sheet
```

---

**Bắt đầu:** Nếu bạn mới, đọc [base/01 Quick Start](01-quick-start.md). Nếu đã quen Claude, đọc [base/03 Prompt Engineering](03-prompt-engineering.md).

---

[Tổng quan](00-overview.md) | [Quick Start →](01-quick-start.md)
