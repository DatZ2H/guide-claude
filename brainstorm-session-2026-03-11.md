# Brainstorm Session 4 — Scaffold cho Team Dev

> Tiếp nối session 1-3 (2026-03-10). Context shift: từ "1 maintainer" sang "xây cho team dev Phenikaa-X".
> Chấp nhận cải tổ nếu cần. Đánh giá tương lai xa.
> **Ngày:** 2026-03-11

---

## 1. Context shift — Tại sao thay đổi phương trình

### Trước (session 1-3)
- Target: Đạt (1 maintainer) dùng Guide Claude
- _scaffold = bonus, "nice-to-have" cho project mới
- Câu hỏi: "nâng cấp Guide Claude như thế nào?"

### Bây giờ (session 4)
- Target: **Team dev Phenikaa-X** (10-20 kỹ sư)
- _scaffold = **delivery mechanism** cho team
- Câu hỏi: "_scaffold đủ để team dùng không? Cần gì thêm?"

### Tại sao context shift quan trọng

| Yếu tố | 1 maintainer | Team 10-20 |
|---------|-------------|------------|
| Update mechanism | Không cần (tự biết) | **BẮT BUỘC** — phải propagate changes |
| Convention enforcement | Self-discipline | **BẮT BUỘC** — phải tự động |
| Onboarding | Không cần | **BẮT BUỘC** — zero-to-productive path |
| Skill levels | Expert | Mixed (zero → intermediate) |
| Maintenance | 1 person reviews all | Cần distributed ownership |
| Customization | Full control | Cần balance: shared standards + project-specific |

---

## 2. _scaffold hiện tại — Đủ hay không?

### Cái _scaffold ĐANG LÀM tốt

1. **Templates chất lượng** — CLAUDE-template.md, project-state-template.md, skill/rule templates
2. **Hai examples minh họa** growth path: minimal → mature
3. **Checklists actionable** — phase-based, copy-paste ready
4. **Nhất quán** với project conventions

### Cái _scaffold KHÔNG LÀM ĐƯỢC cho team

| Vấn đề | Chi tiết | Hệ quả |
|---------|----------|--------|
| **Copy-once, diverge-forever** | Scaffold được copy → customize → mất liên kết với nguồn | Team member A dùng v1, member B dùng v3 — không nhất quán |
| **Không có update mechanism** | Khi conventions thay đổi, phải manual notify + manual update từng project | Conventions drift. Stale practices tích lũy |
| **Không enforce** | Scaffold khuyến nghị, không bắt buộc | Team member có thể bỏ qua toàn bộ standards |
| **Designed for experts** | Giả định user biết CLAUDE.md, hooks, skills | Kỹ sư robotics mới tiếp xúc Claude → lost |
| **Không role-based** | Cùng 1 template cho dev, doc writer, ops | Mỗi role cần setup khác nhau |

### Kết luận: _scaffold là NECESSARY nhưng NOT SUFFICIENT

_scaffold = **starter kit**. Team cần thêm:
- **Living foundation** (auto-update)
- **Guardrails** (enforce, không chỉ recommend)
- **Onboarding path** (zero → productive)

---

## 3. Phân tích 4 delivery mechanisms cho team

### Option S: Scaffold-only (hiện tại + cải tiến)

```
_scaffold/ → copy → project/.claude/
            ↑
            không có feedback loop
```

**Cách cải tiến:**
- Thêm SETUP.md template, MEMORY.md template, hook templates
- Thêm role-based templates (dev/, doc/, ops/)
- Thêm "Why" layer trước "How" (giải thích tại sao cần CLAUDE.md, hooks...)
- Versioned scaffold (tag releases, CHANGELOG)

**Ưu điểm:**
- Effort thấp nhất (~3-4 sessions)
- Không dependency vào Claude Code features mới
- Ai cũng hiểu "copy template, customize"
- Backward-compatible hoàn toàn

**Nhược điểm:**
- Vẫn diverge-forever — **chấp nhận drift** sau setup
- Conventions thay đổi → phải manual notify team
- Không guardrails — dựa vào kỷ luật cá nhân
- Kỹ sư mới vẫn cần đọc + hiểu trước khi dùng

**Phù hợp khi:** Team nhỏ (3-5), skill level tương đối đồng đều, conventions ít thay đổi

**ROI timeline:** Nhanh (tuần), nhưng giảm dần khi team grow

---

### Option G: Git Submodule / Shared Repo

```
pnx-claude-standards/   (shared repo)
├── CLAUDE.md            (conventions chung)
├── rules/               (shared rules)
├── hooks/               (shared hooks)
├── skills/              (shared skills)
└── templates/           (scaffold)

project-abc/.claude/
├── CLAUDE.md            @import ../pnx-claude-standards/CLAUDE.md
├── rules/               → symlink or @import
└── settings.json        (project-specific)
```

**Ưu điểm:**
- **Single source of truth** cho conventions
- `git pull` = update conventions cho tất cả projects
- Team members contribute back (PR workflow)
- Version history tự nhiên (git)

**Nhược điểm:**
- Git submodules notoriously annoying (init, update, detached HEAD...)
- Symlinks không reliable trên Windows (cần Developer Mode hoặc admin)
- `@import` syntax giải quyết cleaner nhưng max 5 hops
- Cần git workflow discipline (PR cho shared repo)

**Phù hợp khi:** Team có git experience, projects cùng trên 1 máy hoặc CI

**ROI timeline:** Trung bình (2-3 tuần setup), ROI tăng dần khi team grow

---

### Option P: Plugin Distribution

```
pnx-claude-plugin/
├── .claude-plugin/
│   ├── manifest.json
│   ├── CLAUDE.md        (shared conventions)
│   ├── hooks.json       (shared hooks)
│   └── skills/          (shared skills)
├── agents/              (shared agents)
└── rules/               (shared rules)

Mỗi project:
  claude plugins install pnx-claude-plugin
```

**Ưu điểm:**
- **Official distribution mechanism** — Anthropic designed for this
- Auto-update (plugin version management)
- Namespaced (không conflict với project-specific skills)
- Có thể publish internal marketplace
- Clean separation: shared (plugin) vs project-specific (.claude/)

**Nhược điểm:**
- Plugin ecosystem còn early — breaking changes possible
- **Security surface**: plugin hooks execute full user permissions
- Không có automatic security scanning cho marketplace submissions
- Supply chain risk: installed plugins bypass blocklist
- Cần maintain plugin repo riêng
- Plugin structure specific — learning curve

**Phù hợp khi:** Team > 5, nhiều projects, cần standardized workflows across org

**ROI timeline:** Chậm (1-2 tháng setup), nhưng ROI cao nhất long-term

---

### Option M: Managed CLAUDE.md + Selective Features

```
Company level:
  C:\Program Files\ClaudeCode\CLAUDE.md    (managed policy)
  → enforce: language, icon rules, git workflow, security

Team level:
  ~/.claude/CLAUDE.md                       (user preferences)
  → set: default model, personal shortcuts

Project level:
  project/.claude/CLAUDE.md                 (project-specific)
  → set: folder structure, project context
  project/.claude/ (rules, hooks, skills)   → from scaffold + customize
```

**Ưu điểm:**
- **Strongest enforcement** — managed policy > mọi level khác
- Team-wide conventions tự động apply cho MỌI project
- Separation of concerns rõ ràng (company → user → project)
- Không cần team member biết về conventions — tự enforce

**Nhược điểm:**
- Cần IT admin hoặc Group Policy deployment
- Windows Registry (HKLM/HKCU) hoặc file-based — cần quyền admin
- **Chỉ 1 managed source** — phải chọn mechanism duy nhất
- **Array settings concatenate, KHÔNG replace** — lower scope có thể mở permissions
- Nếu set sai managed policy → ảnh hưởng MỌI project của MỌI user
- Overkill nếu chỉ 1-2 teams dùng Claude Code

**Phù hợp khi:** Org-wide Claude Code deployment, có IT support

**ROI timeline:** Chậm (1-3 tháng), phù hợp phase 3+ của adoption

---

## 4. Đề xuất: Phased Adoption Roadmap

### Tầm nhìn xa — 4 phases

```
Phase 1 (Now → +1 tháng)          Phase 2 (+1 → +3 tháng)
┌──────────────────────┐          ┌──────────────────────┐
│  Enhanced Scaffold   │          │  Shared Foundation   │
│  + Role-based setup  │    →     │  + @import + symlinks│
│  + Onboarding path   │          │  + Shared rules repo │
│  + Quick wins infra  │          │  + Custom agents     │
└──────────────────────┘          └──────────────────────┘
           │                                 │
           ▼                                 ▼
Phase 3 (+3 → +6 tháng)          Phase 4 (+6 → +12 tháng)
┌──────────────────────┐          ┌──────────────────────┐
│  Plugin Distribution │          │  Managed Policy      │
│  + Internal plugin   │    →     │  + Org-wide deploy   │
│  + Auto-update       │          │  + CI/CD integration │
│  + Agent fleet       │          │  + Metrics/feedback  │
└──────────────────────┘          └──────────────────────┘
```

### Phase 1: Enhanced Scaffold (chấp nhận drift, optimize onboarding)

**Mục tiêu:** Bất kỳ kỹ sư PNX nào cũng setup được Claude Code trong 30 phút.

**Cải tổ _scaffold:**

```
_scaffold/ (v2.0)
├── README-scaffold.md              ← thêm "Why" section
├── QUICK-START.md                  ← MỚI: 5-minute guide (zero → dùng được)
│
├── roles/                          ← MỚI: role-based starter kits
│   ├── developer/                  Python/ROS2 dev
│   │   ├── CLAUDE.md
│   │   ├── settings.json           (hooks cho code quality)
│   │   └── skills/
│   ├── doc-writer/                 Technical Writer
│   │   ├── CLAUDE.md
│   │   ├── settings.json           (hooks cho doc format)
│   │   └── skills/
│   └── solution-lead/              Orchestrator role
│       ├── CLAUDE.md
│       ├── settings.json           (hooks cho planning)
│       └── skills/
│
├── shared/                         ← MỚI: conventions dùng chung
│   ├── conventions.md              → @import vào mọi CLAUDE.md
│   ├── pnx-rules/                  shared rules (copy hoặc symlink)
│   │   ├── language-standards.md
│   │   ├── git-workflow.md
│   │   └── security-basics.md
│   └── pnx-hooks/                  shared hooks (copy hoặc symlink)
│       ├── format-check.py
│       └── pre-commit-guard.py
│
├── templates/                      ← rename từ cũ
│   ├── CLAUDE-template.md
│   ├── project-state-template.md
│   ├── SETUP-template.md          ← MỚI
│   ├── MEMORY-template.md         ← MỚI
│   ├── hook-template.py           ← MỚI
│   └── settings-template.json     ← MỚI (comprehensive, commented)
│
├── project-instructions/           (giữ nguyên)
├── skill-templates/                (giữ nguyên)
├── examples/                       (giữ nguyên + thêm examples)
└── checklists/
    ├── new-project-checklist.md    (update cho role-based flow)
    ├── daily-workflow.md           (giữ nguyên)
    └── team-onboarding.md         ← MỚI: checklist cho team lead
```

**Quick wins infra (thêm vào Guide Claude .claude/):**
- `@import` syntax tách CLAUDE.md
- `PreCompact` hook re-inject context
- `AUTOCOMPACT_PCT=70`
- `prompt` hook semantic check
- Document bundled skills

**Effort:** 5-7 sessions
**Risk:** Thấp
**Output:** Mỗi kỹ sư PNX có thể setup + bắt đầu dùng Claude Code trong 30 phút

### Phase 2: Shared Foundation (giảm drift)

**Mục tiêu:** Conventions update 1 nơi → propagate tới mọi project.

**Triển khai:**
- Tạo `pnx-claude-standards` repo riêng (hoặc folder trong Vault)
- Dùng `@import` để reference shared conventions
- Shared rules via symlinks (Windows: junction points hoặc `mklink /D`)
- 2-3 custom subagents (`.claude/agents/`) cho common tasks
- Merge commands → skills (unified architecture)

**Effort:** 5-7 sessions
**Risk:** Trung bình (symlinks trên Windows cần test)
**Prerequisite:** Phase 1 done, 3+ team members đang dùng Claude Code

### Phase 3: Plugin Distribution (auto-update)

**Mục tiêu:** `claude plugins install pnx-standards` — 1 lệnh setup mọi thứ.

**Triển khai:**
- Package shared conventions, rules, hooks, skills thành plugin
- Internal distribution (private git repo, không public marketplace)
- Versioned releases (tag + CHANGELOG)
- Plugin hooks cho enforcement

**Effort:** 5-8 sessions
**Risk:** Trung bình-Cao (plugin API stability, security surface)
**Prerequisite:** Phase 2 done, team > 5, plugin ecosystem stable

### Phase 4: Managed Policy (org-wide)

**Mục tiêu:** IT deploy managed CLAUDE.md — enforce cho toàn bộ Phenikaa-X.

**Triển khai:**
- Managed CLAUDE.md via Windows file-based (`C:\Program Files\ClaudeCode\`)
- Org-wide security policies, model selection, API key management
- CI/CD integration cho content freshness detection
- Metrics: adoption rate, skill usage, error patterns

**Effort:** 8-12 sessions
**Risk:** Cao (IT coordination, org-wide impact)
**Prerequisite:** Phase 3 done, Claude Code adopted company-wide

---

## 5. Phản biện đa chiều

### Góc nhìn 1: "Kỹ sư robotics mới bắt đầu"

> "Tôi cần viết code ROS2, không cần biết CLAUDE.md là gì."

- Phase 1 role-based scaffold giải quyết: chọn `roles/developer/`, copy, done
- Nhưng **vẫn cần đọc QUICK-START.md** — tối thiểu 5 phút
- Trade-off: càng abstract (ẩn complexity) → càng khó customize sau
- **Risk:** Nếu quá "magic" → engineer không hiểu tại sao → không debug được khi hỏng

### Góc nhìn 2: "Team lead muốn kiểm soát chất lượng"

> "Tôi cần biết team dùng Claude đúng cách."

- Phase 1 chỉ có scaffold → KHÔNG kiểm soát được (copy xong = tự do)
- Phase 2 shared foundation → partial control (conventions update, nhưng không enforce)
- Phase 3 plugin → good control (hooks enforce standards)
- Phase 4 managed → full control (IT-level enforcement)
- **Risk:** Over-control → team resent → shadow usage (dùng Claude bên ngoài quy trình)

### Góc nhìn 3: "Maintainer lo bảo trì"

> "32 files cho Guide Claude đã đuối. Giờ thêm shared repo, plugin, managed policy?"

- Phase 1 thực ra **GIẢM** maintenance: role-based scaffold = template, không phải prose dài
- Phase 2 **GIẢM** tiếp: shared conventions = 1 file thay vì copy across projects
- Phase 3 **CHUYỂN** maintenance sang versioned releases (quarterly, không daily)
- **Risk:** Mỗi layer thêm = thêm infra cần maintain. Giảm content nhưng tăng tooling

### Góc nhìn 4: "CTO nhìn 2-3 năm"

> "Claude Code có còn tồn tại sau 2 năm không?"

- **AI tooling landscape thay đổi nhanh** — Cursor, Windsurf, Copilot, Claude Code đều compete
- Plugin API có thể breaking change
- Managed CLAUDE.md format có thể thay đổi
- **Mitigation:** Phase 1-2 (scaffold + shared repo) có risk thấp nhất — markdown + git = universal. Phase 3-4 lock-in nhiều hơn
- **Nguyên tắc:** Đầu tư vào KNOWLEDGE (conventions, standards, workflows) — portable. Đầu tư vừa phải vào TOOLING (plugins, managed) — có thể phải migrate

### Góc nhìn 5: Brainstorm session 3 — câu hỏi chưa trả lời

Từ session 3:
> *"Khi nào stop analyzing và start testing với real users?"*

**Đề xuất:** Phase 1 enhanced scaffold = **test point đầu tiên**.
- Không cần chờ hoàn hảo
- Chọn 2-3 kỹ sư volunteer
- Cho setup bằng role-based scaffold
- Thu feedback sau 2 tuần
- Feedback quyết định Phase 2 có cần không

---

## 6. Rủi ro đặc biệt cho Phenikaa-X

### Windows environment

| Risk | Impact | Mitigation |
|------|--------|------------|
| Symlinks cần admin/Developer Mode | Team không thể tự setup | Phase 2: dùng `@import` thay symlink |
| Agent Teams không support Windows Terminal | Chặn hoàn toàn | KHÔNG adopt Agent Teams cho đến khi support |
| Path separators (\ vs /) trong hooks | Hook scripts có thể fail | format-check.py đã handle, nhưng shared hooks cần test |
| Python availability | format-check.py cần Python 3 | Verify Python installed trên tất cả máy dev |

### Security (CVE-documented)

| Risk | Chi tiết | Mitigation |
|------|----------|------------|
| CVE-2025-59536 | Malicious .claude/settings.json auto-execute hooks | Đã fix v1.0.111. Team phải dùng version >= v2.0 |
| CVE-2026-21852 | ANTHROPIC_BASE_URL exfiltrate API keys | Đã fix v2.0.65. Managed policy có thể lock base URL |
| Plugin supply chain | Plugin hooks = full user permissions | Phase 3: chỉ internal plugins, không third-party |
| Shared repo trust | Malicious PR vào pnx-claude-standards | Phase 2: PR review required, branch protection |

### Organizational

| Risk | Impact | Mitigation |
|------|--------|------------|
| Low adoption | "Thêm 1 tool nữa à?" → team ignore | Phase 1: chứng minh value trước (quick win demos) |
| Knowledge silos | Chỉ Đạt hiểu infra → bus factor = 1 | SETUP.md + QUICK-START.md + 1 backup maintainer |
| Over-engineering | Build full platform trước khi có user | **Phased approach — Phase 1 test trước** |
| Cost sensitivity | Token cost tăng khi team dùng | Set cost alerts, dùng Haiku/Sonnet default |

---

## 7. Quyết định cần user chốt

### Q1: Scope Phase 1 — ✅ ĐÃ CHỐT

> **Chốt:** Build complete → roll out thử nghiệm toàn team
>
> Lý do: Nền móng cho Phenikaa-X, cần chất lượng trước khi ship

### Q2: Shared conventions repo — ✅ ĐÃ CHỐT

> **Chốt:** Repo riêng (`pnx-claude-standards`)
>
> Lý do: Clean separation, team contribute via PR, versioned riêng

### Q3: Role definitions — ✅ ĐÃ CHỐT

> **Chốt:** 3 roles
> - Developer (Python/ROS2/C++)
> - Doc writer (Technical Writing)
> - Solution lead (Orchestration)

### Q4: Timeline commitment — ✅ ĐÃ CHỐT

> **Chốt:** Thorough — đầu tư chất lượng nền móng, không rush
>
> Lý do: Liên quan đến nền móng Phenikaa-X, chấp nhận dành nhiều thời gian

### Q5: Guide Claude content direction — ✅ ĐÃ CHỐT

> **Chốt:** Chưa động guide content — focus workspace + scaffold trước
>
> Lý do: Xây nền móng infra/delivery mechanism trước, content update sau

---

## 8. Tóm tắt

### Trả lời "dừng ở _scaffold thì sao?"

**Được — nhưng cần enhanced scaffold (v2.0), không phải scaffold hiện tại.**

Scaffold hiện tại thiếu:
- Role-based setup
- Onboarding zero-to-productive
- Shared conventions layer
- "Why" explanations cho beginners

Enhanced scaffold + quick wins infra = **đủ cho Phase 1** (pilot 2-3 người, 2-3 tuần feedback).

### Trả lời "tương lai xa chấp nhận cải tổ?"

**Phase 1 → 2 → 3 là lộ trình khả thi.**

- Phase 1 (scaffold): risk thấp, effort 5-7 sessions
- Phase 2 (shared foundation): risk trung bình, effort 5-7 sessions
- Phase 3 (plugin): risk trung bình-cao, evaluate sau Phase 2 feedback
- Phase 4 (managed): chỉ nếu org-wide adoption

**Nguyên tắc:** Ship Phase 1 → test → feedback → quyết định Phase 2. KHÔNG design Phase 3-4 trước khi Phase 1 validated.

---

## Nguồn tham khảo

- [Claude Code Skills](https://code.claude.com/docs/en/skills) — skills architecture, bundled skills
- [Claude Code Hooks](https://code.claude.com/docs/en/hooks) — 4 hook types, 18 events
- [Claude Code Memory](https://code.claude.com/docs/en/memory) — @import, managed CLAUDE.md, 200-line limit
- [Claude Code Sub-agents](https://code.claude.com/docs/en/sub-agents) — custom agents, persistent memory
- [Claude Code Plugins](https://code.claude.com/docs/en/plugins) — distribution, security model
- [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices) — anti-patterns, verification-first
- [Claude Code Settings](https://code.claude.com/docs/en/settings) — sandbox, managed policy, array merging
- [HumanLayer Blog](https://www.humanlayer.dev/blog/writing-a-good-claude-md) — 150-200 instruction budget
- [CVE-2025-59536](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/) — hook injection
- [Agent Teams Best Practices](https://claudefa.st/blog/guide/agents/agent-teams-best-practices) — coordination failures
- research-claude-code-2026.md — 29 gaps analysis
- research-upgrade-strategy-2026.md — 5 strategic options
- research-workspace-upgrade-2026-03-11.md — infrastructure analysis
- brainstorm-session-2026-03-10.md — sessions 1-3 handoff
