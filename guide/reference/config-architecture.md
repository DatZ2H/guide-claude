# Configuration Architecture — Kiến trúc Cấu hình Claude

**Cập nhật:** 2026-03-02 | Tham chiếu nhanh — không cần đọc tuần tự

---

Tài liệu này là **single source of truth** cho toàn bộ hệ thống cấu hình Claude. Kỹ sư thường mất thời gian vì không biết "rule này đặt ở đâu" — bảng dưới đây giải quyết vấn đề đó.

---

## Bức tranh tổng thể: 6 lớp cấu hình

Claude có 6 lớp cấu hình, chia theo hai surface chính. Mỗi lớp có scope, vị trí, và loại nội dung khác nhau.

```
SCOPE: GLOBAL (tất cả conversations/tasks)
│
├── [claude.ai]  Profile Preferences      → Settings > Profile
├── [CC]         Global CLAUDE.md         → ~/.claude/CLAUDE.md (file, không phải UI setting)
│
SCOPE: PROJECT/FOLDER (một nhóm công việc cụ thể)
│
├── [claude.ai]  Project Instructions     → Project Settings > Instructions
├── [claude.ai]  Project Knowledge        → Project > Add Content
├── [Cowork]     Folder Instructions      → project-folder/.claude/CLAUDE.md
│
SCOPE: ON-DEMAND (chạy khi gọi)
│
└── [Cowork/CC]  Skills                   → project-folder/.claude/skills/
    [Cowork]     Plugins                  → Cài đặt qua Claude Desktop
    [Cowork]     Scheduled Tasks          → Cài đặt trong Cowork UI
```

---

## Bảng chi tiết: Tất cả 6 lớp

| Lớp | Surface | Vị trí | Scope | Versioning | Shareable | Thay đổi khi nào |
|-----|---------|--------|-------|------------|-----------|-----------------|
| Profile Preferences | Claude.ai | Settings > Profile | Account-wide | Không (UI) | Không | Role/context của bạn thay đổi |
| Global CLAUDE.md | CC (file) | `~/.claude/CLAUDE.md` | Tất cả tasks | Không (user-level) | Không tự động | Identity/toolchain thay đổi |
| Project Instructions | Claude.ai | Project Settings | Một Project | Không (UI) | Không | Mục đích project thay đổi |
| Project Knowledge | Claude.ai | Project > Content | Một Project | Không (UI) | Với team | Có tài liệu mới |
| Folder Instructions | Cowork | `project/.claude/CLAUDE.md` | Một folder | **Có** (Git) | **Có** (commit) | Project structure thay đổi |
| Skills | Cowork | `project/.claude/skills/` | On-demand | **Có** (Git) | **Có** (commit) | Workflow cần automation |

---

## Phân tích từng lớp

### Lớp 1 — Profile Preferences (claude.ai, Global)

**Là gì:** Hướng dẫn account-wide, áp dụng cho TẤT CẢ conversations trong claude.ai. Tương đương "tính cách mặc định" của Claude với bạn.

**Đặt ở đâu:** Settings > Profile > "What should Claude know about you?"

**Loại nội dung phù hợp:**
- Ngôn ngữ phản hồi (Tiếng Việt + thuật ngữ kỹ thuật tiếng Anh)
- Background của bạn (kỹ sư AMR, Phenikaa-X)
- Format preference cơ bản (code blocks, bullet points)
- Cách xử lý uncertainty ("nói rõ khi không chắc")

**KHÔNG đặt ở đây:**
- Rules đặc thù của một project cụ thể → dùng Project Instructions
- Tài liệu tham khảo dài → dùng Project Knowledge
- Workflow automation → dùng Skills (Cowork)

**Priority:** Profile Preferences < Project Instructions (Project Instructions override khi conflict)

**Template:** → Xem Module 02, mục 2.1

---

### Lớp 2 — Global CLAUDE.md (Cowork, Global)

**Là gì:** File CLAUDE.md đặt ở thư mục người dùng, áp dụng cho TẤT CẢ Cowork tasks. Tương đương Profile Preferences nhưng cho Cowork và có thể versioning.

**Đặt ở đâu:** `~/.claude/CLAUDE.md` (user-level, không trong project folder)

**Loại nội dung phù hợp:**
- Giống Profile Preferences nhưng chi tiết hơn
- Toolchain conventions (Obsidian, GitHub, file format defaults)
- Response behavior rules
- File operations safety rules

**Khác Profile Preferences:**
- Là file → có thể track thay đổi thủ công, copy sang máy mới
- Markdown format → có thể structured hơn
- Không versioned tự động (không trong Git)

**Template:** → Xem `_scaffold/global-instructions/global-CLAUDE-phenikaa-x.md`

---

### Lớp 3 — Project Instructions (claude.ai, Project-level)

**Là gì:** System prompt áp dụng cho TẤT CẢ conversations trong một claude.ai Project. Đây là cách "setup Claude cho một mục đích cụ thể" trên claude.ai.

**Đặt ở đâu:** Project > (⚙️) Settings > Instructions

**Loại nội dung phù hợp:**
- Role của Claude trong project này ("bạn là Senior Robotics Engineer")
- Context kỹ thuật cụ thể (tech stack, environment, audience)
- Output format rules cho project
- Constraints và safety rules

**KHÔNG đặt ở đây:**
- Tài liệu dài → dùng Project Knowledge
- Rules chung cho tất cả projects → dùng Profile Preferences
- Automation workflows → không thể (dùng Skills trên Cowork)

**Giới hạn:** Khoảng 2,000-4,000 tokens. Nếu instructions dài hơn → Claude có thể không follow hết.

**Versioning:** Không có — nếu cần lịch sử chỉnh sửa, paste instructions vào một file trong Project Knowledge.

**Templates (3 loại):** → Xem `_scaffold/project-instructions/`

---

### Lớp 4 — Project Knowledge (claude.ai, Project-level)

**Là gì:** Tài liệu tham khảo được upload vào Project, Claude đọc và dùng trong mọi conversation của project đó.

**Đặt ở đâu:** Project > Add Content (upload files hoặc paste text)

**Loại nội dung phù hợp:**
- Technical specs, datasheets, API docs
- Coding standards, naming conventions
- Templates mà Claude sẽ follow
- Context dài không fit vào Project Instructions

**Chiến lược tổ chức:**
```
Project Knowledge/
  References/     # Tài liệu tra cứu (specs, datasheets)
  Standards/      # Coding/naming conventions
  Templates/      # Output templates Claude phải follow
  Context/        # Background info (company, team, product)
```

**Giới hạn kích thước:** Mỗi file khuyến nghị < 10MB. Tổng project knowledge < 200MB.

**Chi tiết:** → Xem Module 02, mục 2.2 (Project Knowledge)

---

### Lớp 5 — Folder Instructions (Cowork, Project-level)

**Là gì:** File CLAUDE.md đặt trong `.claude/` subfolder của project. Cowork đọc file này trước khi bắt đầu bất kỳ task nào trong folder đó. Đây là lớp quan trọng nhất trong Cowork workflow.

**Đặt ở đâu:** `your-project/.claude/CLAUDE.md`

**Loại nội dung phù hợp:**
- Project overview (mô tả project là gì, dùng để làm gì)
- Folder structure (giải thích từng subfolder)
- Conventions (language, naming, source markers)
- Memory protocol (Claude đọc gì đầu session)
- Safety rules (KHÔNG xóa file nào, backup trước khi sửa gì)
- Skills list (liệt kê skills có trong `.claude/skills/`)

**Khác Project Instructions (claude.ai):**

| | Folder Instructions | Project Instructions |
|--|--|--|
| Surface | Cowork | Claude.ai |
| Format | Markdown file | Free text trong UI |
| Versioning | Có (Git) | Không |
| Shareable | Có (commit) | Không |
| Scope | Một folder | Một Project |

**2-Tier Architecture:** Folder Instructions là trung tâm của pattern:
```
project/
├── .claude/
│   ├── CLAUDE.md    ← Folder Instructions (bạn đang ở đây)
│   └── skills/      ← On-demand workflows
├── _memory/         ← (deprecated — dùng git history thay thế)
└── project-state.md ← Project overview
```

**Template:** → Xem `_scaffold/.claude/CLAUDE-template.md`

---

### Lớp 6 — Skills (Cowork, On-demand)

**Là gì:** File SKILL.md định nghĩa một workflow phức tạp mà Claude thực hiện khi được gọi bằng trigger phrase. Không chạy tự động — chỉ khi user invoke.

**Đặt ở đâu:** `your-project/.claude/skills/skill-name/SKILL.md`

**Khi nào tạo Skill:**
```
Tôi cần automation X → câu hỏi đầu tiên:
│
├── Cần chạy tự động theo lịch? → Scheduled Task
├── Cần workflow nhiều bước khi tôi gọi? → Skill ✓
└── Chỉ cần prompt tái sử dụng? → Prompt Template (Module 07)
```

**Anatomy của một Skill:**
```markdown
---
name: skill-name
description: Mô tả ngắn — QUAN TRỌNG cho trigger detection
---
# Skill Title
## Trigger         ← Khi nào activate
## Pre-conditions  ← Kiểm tra trước khi chạy
## Quy trình       ← Workflow chi tiết
## Rules           ← Constraints
```

**Ví dụ thực tế:** Project Guide Claude đang dùng 4 skills:
- `session-start` — Orientation đầu session
- `version-bump` — Bump version an toàn
- `cross-ref-checker` — Scan stale references
- `module-review` — QA trước release

**Template:** → Xem `_scaffold/skill-templates/SKILL-template/SKILL-template.md`

---

## Decision Framework: "Rule này đặt ở đâu?"

### Bước 1: Bạn đang làm việc trên surface nào?

```
Surface?
├── Claude.ai (web/mobile) → Dùng: Profile Preferences, Project Instructions, Project Knowledge
└── Cowork (Claude Desktop) → Dùng: Global CLAUDE.md, Folder Instructions, Skills
```

### Bước 2: Rule này dùng cho bao nhiêu projects?

```
Scope?
├── Tất cả projects/tasks → Profile Preferences (claude.ai) / Global CLAUDE.md (Cowork)
└── Chỉ project này → Project Instructions / Folder Instructions
```

### Bước 3: Loại nội dung?

```
Nội dung là gì?
├── Rule/instruction → Project Instructions (claude.ai) / Folder Instructions (Cowork)
├── Tài liệu dài → Project Knowledge (claude.ai)
└── Workflow automation → Skills (Cowork)
```

### Bảng tổng hợp quyết định nhanh

| Tôi muốn... | Dùng lớp nào |
|---|---|
| Claude luôn trả lời tiếng Việt (claude.ai) | Profile Preferences |
| Claude luôn trả lời tiếng Việt (Cowork) | Global CLAUDE.md |
| Claude đóng vai Senior Robotics Engineer cho project X (claude.ai) | Project Instructions |
| Claude biết folder structure của project Y (Cowork) | Folder Instructions |
| Upload datasheet để Claude tham khảo (claude.ai) | Project Knowledge |
| Tự động hóa workflow version-bump | Skill |
| Chạy task kiểm tra cross-reference hàng tuần | Scheduled Task |

---

## Volatile vs Stable: Tổ chức _scaffold/

Một nguyên tắc quan trọng trong quản lý cấu hình:

- **Stable content** (khái niệm, decision framework, best practices) → đặt trong modules
- **Dynamic content** (templates, fill-in examples) → đặt trong `_scaffold/`

```
_scaffold/
├── CLAUDE-template.md              ← Folder Instructions template
├── project-state-template.md
├── VERSION
│
├── skill-templates/                ← Template tạo skill (tham khảo, KHÔNG copy)
│   └── SKILL-template/
│       └── SKILL-template.md
│
├── project-instructions/           ← Templates cho claude.ai Projects (tham khảo)
│   ├── README.md
│   ├── template-basic.md
│   ├── template-troubleshooting.md
│   ├── template-tech-doc.md
│   └── template-code-review.md
│
├── global-instructions/            ← Template Global CLAUDE.md (tham khảo)
│   └── global-CLAUDE-phenikaa-x.md
│
└── memory-starter/             ← DEPRECATED (Phase 5, 2026) — pattern "_memory/" đã bỏ
    ├── session-state.md            Không dùng template này cho project mới
    └── decisions-log.md
```

Khi template cần update (vì Claude features thay đổi) → chỉ cần sửa file trong `_scaffold/`, không phải sửa và re-version toàn bộ module.

---

## Cross-references

- **Profile Preferences + Projects (claude.ai):** Module 02 — Setup & Personalization
- **Global CLAUDE.md + Folder Instructions (Cowork):** Module 10, mục 10.3–10.4
- **Skills creation workflow:** Module 10, mục 10.6
- **Plugins:** Module 10, mục 10.6
- **Scheduled Tasks:** Module 10, mục 10.5
- **Templates cho từng lớp:** `_scaffold/` folder

---

*Tài liệu này là reference — đọc khi cần quyết định "rule đặt ở đâu". Đọc modules liên quan để hiểu chi tiết từng lớp.*
