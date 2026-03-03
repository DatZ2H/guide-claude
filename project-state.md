# Project State — Claude Guide cho Kỹ sư Phenikaa-X
Version guide: 4.1 | Last synced: 2026-03-03

## Phase hiện tại
- **Phase:** Development — đang iterate, chưa publish chính thức
- **Mục tiêu:** Bộ Documentation Standard hoàn chỉnh 11 modules
- **Đối tượng:** Kỹ sư tự động hóa, R&D, Robotics tại Phenikaa-X

## Trạng thái modules

> **Note 2026-03-02:** Tất cả modules đã move vào `guide/`. File paths dưới đây reflect vị trí mới.

| Module | File | Trạng thái | Ghi chú |
|--------|------|------------|---------|
| 00 | guide/00-overview.md | Draft v3.5 | Updated for v4.0 restructure: version ref → VERSION, files section → cấu trúc mới |
| 01 | guide/01-quick-start.md | Draft v3.4 | Không thay đổi |
| 02 | guide/02-setup-personalization.md | Draft v4.0 | + cross-link → _scaffold/project-instructions/ + config-architecture.md |
| 03 | guide/03-prompt-engineering.md | Draft v3.4 | Không thay đổi |
| 04 | guide/04-context-management.md | Draft v3.5 | Updated for v4.0 restructure: _memory/ 4→2 files, _project-setup/ → .claude/, prompts updated |
| 05 | guide/05-workflow-recipes.md | Draft v3.5 | Updated for v4.0 restructure: Recipe 5.11 prompts → session-state.md |
| 06 | guide/06-tools-features.md | Draft v3.4 | Không thay đổi |
| 07 | guide/07-template-library.md | Draft v3.4 | Không thay đổi |
| 08 | guide/08-mistakes-fixes.md | Draft v3.4 | Không thay đổi |
| 09 | guide/09-evaluation-framework.md | Draft v3.4 | Không thay đổi |
| 10 | guide/10-claude-desktop-cowork.md | Draft v4.0 | + §10.4.1 Folder vs Project Instructions; + §10.6.7-10.6.9 Skills creation / Plugins / Config lifecycle |
| ref | guide/reference/config-architecture.md | **New v4.0** | Single source of truth: 6 lớp cấu hình Claude, decision framework |

## Cấu trúc thư mục

> Restructured 2026-03-02: chuyển từ flat layout → 3-tier architecture.

```
Guide Claude/
├── README.md                       Project overview (public-facing)
├── VERSION                         Single source of truth cho version number
├── project-state.md                ← Context transfer document (paste vào Project Chat khi cần)
│
├── guide/                          Tầng A — Content (11 modules)
│   ├── 00-overview.md              (~9 KB) — đổi tên từ 00-README.md
│   ├── 01-quick-start.md           (~8 KB)
│   ├── 02-setup-personalization.md (~19 KB)
│   ├── 03-prompt-engineering.md    (~36 KB)
│   ├── 04-context-management.md    (~25 KB)
│   ├── 05-workflow-recipes.md      (~27 KB)
│   ├── 06-tools-features.md        (~14 KB)
│   ├── 07-template-library.md      (~23 KB)
│   ├── 08-mistakes-fixes.md        (~18 KB)
│   ├── 09-evaluation-framework.md  (~14 KB)
│   ├── 10-claude-desktop-cowork.md (~45 KB)
│   └── reference/
│       ├── skills-list.md          Danh sách skills theo phân loại Type × Trust
│       └── config-architecture.md  Single source of truth: 6 lớp cấu hình Claude
│
├── _scaffold/                      Starter templates cho project Cowork mới
│   ├── README-scaffold.md
│   ├── CLAUDE-template.md
│   ├── project-state-template.md
│   ├── VERSION
│   ├── memory-starter/
│   ├── skill-templates/            Template tạo skill (folder/SKILL.md format)
│   ├── project-instructions/       Templates cho claude.ai Project Instructions
│   └── global-instructions/        Template Global CLAUDE.md cho Cowork
│
├── .claude/                        Tầng B — Infrastructure (Claude config)
│   ├── CLAUDE.md                   Folder Instructions cho project này
│   ├── SETUP.md                    Project manifest (cho maintainer mới)
│   └── skills/                     On-demand skills
│
└── _memory/                        Tầng C — Persistence
    ├── session-state.md            Active tasks + last session summary
    └── decisions-log.md            Append-only decision audit trail
```

## Quyết định gần nhất

| Ngày | Quyết định | Rationale |
|------|-----------|-----------|
| 2026-03-02 | Tạo guide/reference/config-architecture.md — SSOT cho 6 lớp cấu hình | Unified mental model, dễ cross-link, dễ update độc lập với module |
| 2026-03-02 | Stable vs Dynamic content split: concepts → modules; templates → _scaffold/ | Templates hay thay đổi theo Claude features → update một chỗ, không re-version module |
| 2026-03-02 | Deprecate skill-templates/SKILL-template.md → folder format SKILL-template/SKILL-template.md | Template phải match format thực tế (folder/SKILL.md) |
| 2026-03-02 | Tạo .claude/SETUP.md — project manifest cho maintainer mới | Gap: onboarding kỹ sư mới không biết cần cài gì, skills trigger phrase là gì |
| 2026-03-02 | Tạo _scaffold/project-instructions/ (4 templates) + global-instructions/ | Project Instructions là lớp cấu hình thiếu trong scaffold |
| 2026-03-02 | Tạo _scaffold/ — bộ starter templates cho project Cowork mới | Chuẩn hóa 3-tier setup. Copy + customize thay vì tạo từ đầu mỗi lần |
| 2026-03-02 | Restructure sang 3-tier architecture (guide/ + .claude/ + _memory/) | Phân tách content vs infrastructure vs persistence. Giảm token overhead, tăng khả năng mở rộng |
| 2026-03-02 | Rename 00-README.md → 00-overview.md, move vào guide/ | Root đã có README.md riêng. Tránh naming conflict |
| 2026-03-02 | Thêm VERSION làm SSOT cho version number | Tránh hardcode version trong 11+ module files |
| 2026-03-02 | _memory/ chỉ 2 files: session-state + decisions-log | Giảm token overhead đầu session (bỏ handoff, todo, context-map) |
| 2026-03-02 | Reframe Two-Layer → Cowork-primary + context transfer | Sync protocol overhead > benefit. project-state.md = briefing doc, không phải sync target |
| 2026-03-01 | Áp dụng Two-Layer Knowledge Model | Giải quyết desync Project Knowledge ↔ Cowork folder |
| 2026-03-01 | Project Knowledge chỉ chứa project-state.md | Tránh RAG, giảm sync overhead |
| 2026-03-01 | Sync frequency: weekly + trigger-based | ~~Superseded 2026-03-02~~ → chuyển sang on-demand |
| 2026-03-01 | Version bump guide → v3.5 | Thêm Two-Layer Knowledge vào 4 modules (00, 02, 04, 05, 10) |
| 2026-02-28 | Standard trước, Knowledge Base sau | Focus Phase 1 vào rules/templates |
| 2026-02-28 | Core Principles không phụ thuộc domain cụ thể | Rules chung cho mọi loại tài liệu |
| 2026-02-28 | Tiếng Việt + giữ thuật ngữ kỹ thuật tiếng Anh | Không Việt hóa AMR, ROS, SLAM, Lidar |
| 2026-02-28 | Kiến trúc layered: Core Principles → Type-Specific Rules → Templates → Glossary | Phân tầng cho Documentation Standard |

## Conventions
- Tiếng Việt chính, thuật ngữ kỹ thuật giữ tiếng Anh
- `{{variable}}` = placeholder
- Markers: [Nguồn: ...], [Ứng dụng Kỹ thuật], [Cập nhật MM/YYYY]

## Khi nào update project-state.md

File này là **context transfer document** — update trên Cowork, paste vào Project Chat khi cần brainstorm/planning.

Update khi:
- Sau milestone lớn (version bump, hoàn thành module)
- Trước khi brainstorm trên Project Chat (để có context mới nhất)
- Khi cấu trúc thư mục hoặc decisions thay đổi đáng kể

## Hướng dẫn cho Claude khi đọc file này

1. File này là **briefing document** — tổng quan dự án, paste vào Project Chat khi cần context cho brainstorm/planning.
2. Nội dung chi tiết từng module nằm trong **Cowork folder**. Phần lớn công việc diễn ra trên Cowork (Cowork-primary workflow).
3. Nếu cần tham chiếu nội dung cụ thể, yêu cầu người dùng paste excerpt hoặc ghi chú "sẽ kiểm tra trên Cowork".
4. Ưu tiên **quyết định gần nhất** trong bảng trên hơn nội dung file nào nếu có mâu thuẫn.
5. Khi đề xuất thay đổi cho module, output dưới dạng **prompt có thể chạy trên Cowork** — không giả định Claude đang đọc file thật.
