# Nghiên cứu chiến lược nâng cấp Guide Claude — Phân tích đa chiều

> Tài liệu nghiên cứu nội bộ — phân tích chuyên sâu, phản biện, đánh giá rủi ro
> Người phân tích: Claude (Opus 4.6) — vai trò: chuyên gia Claude Code + kiến trúc sư tài liệu
> [Cập nhật 03/2026]

---

## Mục lục

1. [Hiện trạng và vấn đề gốc](#1-hiện-trạng-và-vấn-đề-gốc)
2. [5 hướng chiến lược](#2-5-hướng-chiến-lược)
3. [Phản biện các giả định trước đó](#3-phản-biện-các-giả-định-trước-đó)
4. [Ma trận rủi ro](#4-ma-trận-rủi-ro)
5. [So sánh chi phí 6 tháng](#5-so-sánh-chi-phí-6-tháng)
6. [Khuyến nghị cuối cùng](#6-khuyến-nghị-cuối-cùng)
7. [Quyết định cần user chốt](#7-quyết-định-cần-user-chốt)
8. [Bổ sung từ Web Research](#8-bổ-sung-từ-web-research-032026)
9. [Insights tổng hợp sau Web Research](#9-insights-tổng-hợp-sau-web-research)

---

## 1. Hiện trạng và vấn đề gốc

### 1.1. Dữ liệu cứng

| Metric | Giá trị |
|--------|---------|
| Tổng files | 97 (32 content + 15 infra + 20 scaffold + 30 git) |
| Tổng dung lượng content | ~687 KB (32 files guide/) |
| Gap với Claude Code 2026 | **29 items** (18 thiếu + 7 lệch + 4 lạc hậu) |
| HIGH priority modules | **11/32 files** cần cập nhật lớn |
| Estimated stale content | ~40-50% dev/ tier, ~25% base/ tier |
| Sessions đã đầu tư | ~36 sessions (v7.0 → v9.1, ~3 tháng) |
| Maintainer | **1 người** (Đạt) |
| Đối tượng | ~10-20 kỹ sư Phenikaa-X |

### 1.2. Vấn đề gốc (Root Causes)

**RC1: Guide trộn lẫn Knowledge với Guidance**

"Skills" xuất hiện trong **6 files** khác nhau:
- base/05-tools-features.md (khái niệm)
- dev/01-claude-code-setup.md (cấu hình)
- dev/04-agents-automation.md (sử dụng)
- reference/skills-list.md (danh sách)
- reference/skills-guide.md (hướng dẫn chi tiết)
- reference/config-architecture.md (cấu trúc config)

Khi update 1 feature → phải review/edit 3-6 files → dễ bỏ sót → inconsistency.

**RC2: Tài liệu volatile như code nhưng không có CI/CD**

Claude Code release mới mỗi 2-4 tuần. Guide hiện tại là static documentation — không có cách tự động detect khi content trở nên stale. Hook format-check.py kiểm tra FORMAT, không kiểm tra ACCURACY.

**RC3: Comprehensive = Unsustainable với 1 maintainer**

32 files x 500-800 dòng = ~20,000 dòng cần review mỗi quarter. Với 1 maintainer và 29 gaps, backlog sẽ chỉ tăng, không giảm.

**RC4: Kỹ sư cần KẾT QUẢ, không cần TÀI LIỆU**

Vấn đề thực sự: kỹ sư PNX cần sử dụng Claude hiệu quả trong công việc. Đọc 687KB tài liệu KHÔNG phải là cách hiệu quả nhất để đạt mục tiêu này. Cái họ cần là:
- Setup đúng → dùng ngay
- Khi bị kẹt → tra cứu nhanh
- Khi cần nâng cao → học thêm

---

## 2. 5 Hướng chiến lược

### Hướng A: Incremental Update — vá 29 gaps vào v9.1

**Mô tả:** Giữ nguyên kiến trúc, cập nhật từng module theo priority (CAO → Trung bình → Thấp).

**Ưu điểm:**
- Không cần migration, không mất công tái cấu trúc
- Bắt đầu được ngay, ROI nhanh
- Team đã quen với cấu trúc hiện tại

**Nhược điểm:**
- KHÔNG giải quyết RC1-RC3 — vấn đề gốc vẫn còn
- 3 tháng sau lại phải làm tương tự khi Claude tiếp tục update
- Content tiếp tục phình → 40+ files nếu thêm features mới
- Maintenance cost tăng tuyến tính theo số features

**Phù hợp khi:** Cần kết quả nhanh, không có bandwidth cho restructure.

**Session estimate:** 8-12 sessions

---

### Hướng B: Full Rebuild v2.0 — xây lại từ đầu

**Mô tả:** Archive v9.1, thiết kế lại kiến trúc từ zero, viết lại toàn bộ content với cấu trúc mới.

**Ưu điểm:**
- Cơ hội áp dụng mọi bài học từ 36 sessions trước
- Kiến trúc sạch, không tech debt
- Có thể thiết kế cho maintainability từ đầu

**Nhược điểm:**
- Mất 36 sessions công sức → nhiều content vẫn còn giá trị (prompt engineering, evaluation, workflows)
- Estimate 15-20 sessions chỉ để đạt lại mức tương đương v9.1
- Trong thời gian rebuild, team KHÔNG có tài liệu cập nhật
- Risk cao: scope creep, feature creep, perfectionism

**Phù hợp khi:** Kiến trúc hiện tại THẬT SỰ không thể cải tiến (chưa phải trường hợp này).

**Session estimate:** 15-20 sessions

> [!WARNING]
> Full rebuild là lựa chọn TỐN KÉM NHẤT và RISKIEST. Chỉ chọn khi các hướng khác đã được đánh giá và loại bỏ.

---

### Hướng C: Split Architecture — tách Stable khỏi Volatile

**Mô tả:** Giữ content ổn định (methodology, patterns), tách phần hay thay đổi (feature specs, CLI reference) thành layer riêng hoặc link tới official docs.

**Kiến trúc:**

```
guide/                        ← STABLE CORE (cập nhật quarterly)
  base/                       Methodology, principles, patterns
    03-prompt-engineering.md  ← Ít thay đổi — giữ nguyên
    04-context-management.md  ← Khái niệm ổn định — giữ, update chi tiết nhỏ
    06-mistakes-fixes.md      ← Patterns ổn định — giữ
    07-evaluation.md          ← Framework ổn định — giữ

  doc/                        Workflows, templates
    01-doc-workflows.md       ← Workflow ổn định — giữ
    02-template-library.md    ← Templates ổn định — giữ

  dev/                        Developer methodology
    06-dev-workflows.md       ← Workflow patterns — giữ

knowledge/                    ← VOLATILE LAYER (cập nhật mỗi release)
  features/                   Claude feature specs (SSOT)
    skills.md                 ← Tất cả về skills: spec, frontmatter, bundled skills
    agents.md                 ← Subagents, Agent Teams, custom agents
    hooks.md                  ← 16 event types, hook types
    plugins.md                ← Plugin system, marketplace, LSP
    context.md                ← Context window, /compact, checkpoints, /rewind
    permissions.md            ← Permission modes, rule syntax
    cli.md                    ← CLI flags, surfaces, modes
    models.md                 ← Model specs, pricing, effort levels

  changelog/                  What changed, when
    2026-03.md                ← Thay đổi tháng 3/2026

reference/                    ← QUICK LOOKUP (auto-gen hoặc minimal maintenance)
  cheatsheet-*.md             ← Generated từ knowledge/ + guide/
  config-architecture.md      ← SSOT — cập nhật khi config thay đổi
  quick-templates.md          ← Ổn định
```

**Ưu điểm:**
- Guide ổn định, ít cần update → chất lượng cao, kỹ sư tin tưởng
- Knowledge thay đổi ở 1 nơi → consistency đảm bảo
- Stale detection dễ: chỉ scan knowledge/ (~8 files thay vì 32)
- Phân biệt rõ: "cách dùng" (stable) vs "feature gì" (volatile)

**Nhược điểm:**
- Migration effort: tách 32 files → 2 layers (~5-8 sessions)
- Crosslinks phức tạp hơn
- Người đọc phải nhảy giữa 2 nơi
- knowledge/ layer có thể trùng với official docs

**Phù hợp khi:** Muốn giảm maintenance cost dài hạn và chấp nhận migration cost ngắn hạn.

**Session estimate:** 5-8 sessions (migration) + 3-5 sessions (update content)

---

### Hướng D: Framework-First — đầu tư vào tools, guide lean

**Mô tả:** Chuyển trọng tâm từ "TÀI LIỆU dạy cách dùng" sang "CÔNG CỤ giúp dùng đúng". Guide trở thành companion doc ngắn gọn, không còn là sản phẩm chính.

**Triết lý cốt lõi:**

> Một CLAUDE.md tốt + 5 skills tốt > 50 trang hướng dẫn

Kỹ sư không cần đọc về "cách quản lý context" nếu .claude/ config ĐÃ TỰ ĐỘNG gọi /compact khi context > 70%. Kỹ sư không cần đọc về "cách review code" nếu ĐÃ CÓ agent reviewer chạy tự động.

**Kiến trúc:**

```
pnx-claude-framework/              ← SẢN PHẨM CHÍNH
  configs/
    global-CLAUDE.md                Company-wide instructions
    team-profiles/
      robotics.md                   Config cho team Robotics
      solution.md                   Config cho team Solution
      rd.md                         Config cho team R&D

  agents/
    code-reviewer.yml               Auto review code changes
    doc-reviewer.yml                Auto review documentation
    test-generator.yml              Generate tests
    context-manager.yml             Auto compact + summarize

  skills/
    /onboard                        Onboarding kỹ sư mới
    /review                         Structured code review
    /plan                           Planning workflow
    /handoff                        Session handoff document
    /daily                          Daily standup assistant

  hooks/
    pre-commit-check.py             Standard quality gate
    context-auto-compact.py         Auto compact at 70%
    security-scan.py                Block common vulnerabilities

  templates/
    project-bootstrap/              Init project mới trong 5 phút
    skill-starter/                  Tạo skill mới
    agent-starter/                  Tạo agent mới

guide/                              ← COMPANION DOC (lean, ~10 files)
  00-philosophy.md                  Tại sao dùng framework này
  01-getting-started.md             Setup trong 15 phút
  02-prompt-craft.md                Prompt engineering principles (stable)
  03-patterns.md                    Workflow patterns (stable)
  04-anti-patterns.md               Common mistakes (stable)
  05-advanced.md                    Power user techniques
  reference/
    cheatsheet.md                   1-page reference
    model-guide.md                  Chọn model nào
    troubleshooting.md              FAQ + fixes
    glossary.md                     Thuật ngữ
```

**Ưu điểm:**
- Kỹ sư HỌC BẰNG CÁCH DÙNG, không cần đọc 687KB
- Framework tự encode best practices — không phụ thuộc vào việc đọc guide
- Maintenance cost THẤP: update config files, không cần update prose
- Scale tốt: thêm team mới = thêm profile, không cần viết guide mới
- Claude Code features mới → update config, không cần update docs
- Phục vụ đúng nhu cầu: kỹ sư cần tools, không cần tài liệu

**Nhược điểm:**
- Đầu tư ban đầu: xây framework ~8-10 sessions
- Cần testing với team thực tế trước khi roll out
- Kỹ sư vẫn cần hiểu "tại sao" → vẫn cần guide (dù lean hơn)
- Framework bị lock-in vào Claude Code — nếu Anthropic thay đổi API, phải update
- Không phù hợp cho người hoàn toàn mới (cần onboarding path)

**Phù hợp khi:** Mục tiêu là "kỹ sư PNX dùng Claude hiệu quả" thay vì "có bộ tài liệu đầy đủ".

**Session estimate:** 8-10 sessions (framework) + 3-5 sessions (lean guide) = 11-15 total

---

### Hướng E: Hybrid Ecosystem — kết hợp C + D

**Mô tả:** Tách knowledge layer (C) + xây framework (D) + giữ guide lean. Đây là hướng đầy đủ nhất.

**Kiến trúc:**

```
pnx-ai-ecosystem/
│
├── framework/                   ← CÔNG CỤ (sản phẩm chính)
│   ├── configs/                 Team configs, profiles
│   ├── agents/                  Custom agents
│   ├── skills/                  Shared skills
│   ├── hooks/                   Automation hooks
│   └── templates/               Project bootstraps
│
├── guide/                       ← HƯỚNG DẪN (lean, stable)
│   ├── philosophy/              Tại sao, cách nghĩ
│   ├── methodology/             Prompt craft, patterns
│   ├── workflows/               Doc workflows, Dev workflows
│   └── reference/               Cheatsheets, FAQ
│
├── knowledge/                   ← KIẾN THỨC (volatile, SSOT)
│   ├── features/                Claude feature specs
│   ├── models/                  Model specs
│   └── changelog/               What changed when
│
├── scaffold/                    ← BOOTSTRAP
│   ├── project-setup/           Init project mới
│   └── team-setup/              Init team mới
│
└── .claude/                     ← META-INFRA
    ├── agents/                  Agents cho chính project này
    ├── skills/                  Skills quản lý project
    ├── hooks/                   Quality gates
    └── rules/                   Writing standards
```

**Ưu điểm:**
- Đầy đủ nhất, giải quyết mọi vấn đề gốc
- Từng layer có lifecycle riêng, update độc lập
- Scale từ 1 người → team → nhiều team
- Có thể build incrementally (không cần xong 100% mới có giá trị)

**Nhược điểm:**
- Phức tạp nhất — risk over-engineering cho team 10-20 người
- Estimate 15-20 sessions tổng
- Cần discipline cao để không scope creep
- Nhiều layers = nhiều crosslinks = nhiều điểm có thể break

**Phù hợp khi:** Vision dài hạn 1-2 năm, sẵn sàng đầu tư.

**Session estimate:** 15-20 sessions (full), nhưng có thể deliver incrementally

---

## 3. Phản biện các giả định trước đó

### PB1: "Tách knowledge ra khỏi guide" — có thật sự cần?

**Giả định:** Tách knowledge/ layer giảm maintenance 50%.

**Phản biện:** knowledge/ layer là gì nếu không phải DUPLICATE của official docs?

- Claude official docs tại code.claude.com ĐÃ là SSOT cho features
- Tạo knowledge/ layer = tạo bản sao thứ 2 của official docs, BẰNG TIẾNG VIỆT
- Mỗi khi Anthropic update docs → phải update knowledge/ → vẫn là manual work

**Counter-counter:** Nhưng official docs không có context PNX. Knowledge/ có thể là:
- Curated subset (chỉ features PNX cần)
- Vietnamese annotations (giải thích cho audience PNX)
- Applied examples (ví dụ AMR, ROS, Robotics)

**Kết luận:** knowledge/ chỉ có giá trị nếu NÓ KHÁC với official docs — không phải bản dịch. Nếu chỉ là dịch docs → tốt hơn là LINK tới official docs + thêm PNX notes ngắn.

### PB2: "Framework-first" — kỹ sư có thực sự dùng?

**Giả định:** Framework (configs, agents, skills) hiệu quả hơn tài liệu.

**Phản biện:**
- Framework chỉ hoạt động trong Claude Code — 50%+ kỹ sư PNX có thể dùng claude.ai (web), KHÔNG dùng CLI
- Framework cần maintenance: agents/skills broken khi Claude Code update
- Framework không dạy "tại sao" — kỹ sư copy-paste không hiểu nguyên lý → khi gặp trường hợp mới, không biết cách xử lý

**Counter-counter:** Nhưng...
- Framework có thể có cả Cowork (claude.ai) configs trong project-instructions/
- "Tại sao" vẫn có trong lean guide
- Kỹ sư học nhanh hơn khi CÓ CÔNG CỤ + đọc ngắn, hơn là CHỈ ĐỌC

**Kết luận:** Framework-first đúng nhưng PHẢI đi kèm lean guide. Không thể chỉ có tools mà không có context.

### PB3: "6-layer architecture" — có over-engineered?

**Giả định:** Nhiều layers = dễ maintain.

**Phản biện:**
- Đối với team 10-20 người, 1 maintainer, 6 layers là ENTERPRISE-LEVEL complexity
- Mỗi layer thêm chi phí: folder structure, crosslinks, naming conventions, documentation
- Parkinson's Law: công việc phình ra lấn cấu trúc cho phép

**Counter-counter:**
- Không cần build 6 layers cùng lúc — build incrementally
- Mỗi layer là OPTIONAL — bắt đầu với 2-3, thêm khi cần

**Kết luận:** 6 layers là target architecture, KHÔNG phải day-1 requirement. Bắt đầu với 3 layers (framework + lean guide + infra), thêm sau.

### PB4: "Full rebuild" — có đáng?

**Giả định:** Rebuild từ đầu tốt hơn incremental.

**Phản biện:**
- 70% content hiện tại VẪN CÒN GIÁ TRỊ:
  - Prompt engineering (base/03) — phần lớn ổn định
  - Evaluation framework (base/07) — hoàn toàn ổn định
  - Doc workflows (doc/01-06) — phần lớn ổn định
  - Anti-patterns (base/06) — phần lớn ổn định
- Rebuild mất ~15-20 sessions nhưng 70% là VIẾT LẠI cái đã có
- Trong thời gian rebuild, team KHÔNG CÓ TÀI LIỆU → mất productivity

**Counter-counter:**
- Rebuild không có nghĩa là viết lại — có thể MIGRATE content tốt vào cấu trúc mới
- Migration ≠ rewrite

**Kết luận:** KHÔNG nên rebuild từ zero. Nên RESTRUCTURE + migrate content tốt + viết mới phần thiếu.

### PB5: "Stale content là vấn đề kiến trúc" — hay là vấn đề quy trình?

**Giả định:** Thay đổi kiến trúc sẽ giải quyết stale content.

**Phản biện:**
- Bất kể kiến trúc nào, NẾU KHÔNG CÓ QUY TRÌNH cập nhật thì content vẫn stale
- Kiến trúc chỉ giúp GIẢM SCOPE cần update, không TỰ ĐỘNG update
- Vấn đề thực sự: không có trigger khi Claude Code release mới → content cũ

**Giải pháp thực sự:**
- Hook/agent tự động scan official docs changelog
- Scheduled task (/loop) kiểm tra version Claude Code
- Quy trình: mỗi khi Claude Code release → 1 session cập nhật knowledge

**Kết luận:** Kiến trúc GIÚP nhưng không ĐỦ. Cần cả quy trình + automation.

### PB6: "Guide cần bao phủ mọi feature" — tại sao?

**Giả định ngầm:** Guide tốt = guide đầy đủ.

**Phản biện MẠNH NHẤT:**
- Official docs Anthropic có **60 trang**, cập nhật liên tục, bằng tiếng Anh
- Guide Claude có **32 files, ~687KB** — cố gắng bao phủ tương tự nhưng bằng tiếng Việt
- Đây là cuộc chạy VÔ TẬN — Anthropic có team docs, Guide Claude có 1 người
- **KHÔNG AI THẮNG ĐƯỢC official docs về độ đầy đủ**

**Góc nhìn mới:**
- Guide Claude KHÔNG nên cạnh tranh với official docs
- Guide Claude nên là **"Effective Claude" cho kỹ sư PNX** — opinionated, practical, curated
- Tương tự: Python docs vs "Effective Python" (sách)
  - Python docs: đầy đủ, reference, cho mọi người
  - Effective Python: 90 items chọn lọc, opinionated, cho người muốn giỏi
- Guide Claude = **"Effective Claude for PNX Engineers"**

**Kết luận:** Chuyển từ "comprehensive reference" sang "opinionated methodology guide". Đây là PARADIGM SHIFT lớn nhất.

---

## 4. Ma trận rủi ro

### 4.1. Rủi ro theo hướng

| Rủi ro | A (Patch) | B (Rebuild) | C (Split) | D (Framework) | E (Hybrid) |
|--------|-----------|-------------|-----------|---------------|-------------|
| **Scope creep** | Thấp | CAO | Trung bình | Trung bình | CAO |
| **Stale content tiếp tục** | CAO | Thấp | Trung bình | Thấp | Thấp |
| **Over-engineering** | Thấp | Trung bình | Thấp | Thấp | CAO |
| **Team không adopt** | Thấp | Trung bình | Thấp | Trung bình | Trung bình |
| **Maintainer burnout** | CAO | CAO | Trung bình | Thấp | Trung bình |
| **Mất content giá trị** | Thấp | Trung bình | Thấp | Trung bình | Thấp |
| **Bị lock-in Claude Code** | Thấp | Thấp | Thấp | CAO | Trung bình |
| **Feature gap gia tăng** | CAO | Thấp | Thấp | Thấp | Thấp |

### 4.2. Rủi ro cross-cutting

**R1: Claude Code thay đổi lớn (breaking changes)**
- Xác suất: Trung bình (12 tháng tới)
- Impact: Mọi hướng đều bị ảnh hưởng
- Mitigation: Framework + lean guide ít bị ảnh hưởng hơn comprehensive guide

**R2: Team không đọc/dùng tài liệu**
- Xác suất: CAO (thực tế phổ biến)
- Impact: Toàn bộ effort là waste
- Mitigation: Framework-first — kỹ sư DÙNG tools, không cần ĐỌC docs

**R3: Maintainer (Đạt) quá bận để maintain**
- Xác suất: CAO (vai trò Solution Lead + Project Orchestrator)
- Impact: Project stall
- Mitigation: Framework ít maintenance hơn guide. Automation giảm workload.

**R4: Anthropic release tài liệu tiếng Việt**
- Xác suất: Thấp (12 tháng tới)
- Impact: knowledge/ layer mất giá trị nếu chỉ là bản dịch
- Mitigation: Focus vào PNX-specific value (examples, workflows, configs)

**R5: Team growth — cần scale**
- Xác suất: Trung bình
- Impact: 1-maintainer model không scale
- Mitigation: Framework là sharable artifacts — team members có thể contribute configs/skills

---

## 5. So sánh chi phí 6 tháng

### 5.1. Effort estimate (sessions)

| Hoạt động | A (Patch) | B (Rebuild) | C (Split) | D (Framework) | E (Hybrid) |
|-----------|-----------|-------------|-----------|---------------|-------------|
| Setup/migration | 0 | 5 | 5 | 3 | 5 |
| Content update | 8-12 | 15-20 | 5-8 | 3-5 | 5-8 |
| Framework build | 0 | 0 | 0 | 8-10 | 8-10 |
| Infra upgrade | 2-3 | 3-5 | 2-3 | 2-3 | 3-5 |
| **Tháng 1-2 tổng** | **10-15** | **23-30** | **12-16** | **16-21** | **21-28** |
| Maintenance (tháng 3-6) | 8-12 | 3-5 | 4-6 | **2-3** | **3-5** |
| **6-tháng tổng** | **18-27** | **26-35** | **16-22** | **18-24** | **24-33** |

### 5.2. Value delivery timeline

| Milestone | A | B | C | D | E |
|-----------|---|---|---|---|---|
| Team có tài liệu cập nhật | 2 tuần | 6-8 tuần | 3-4 tuần | 3-4 tuần | 4-6 tuần |
| Maintenance cost giảm | Không | Sau rebuild | 3-4 tuần | 4-6 tuần | 6-8 tuần |
| Team có framework | Không | Không | Không | 4-6 tuần | 6-8 tuần |
| Ecosystem sẵn sàng | Không | Không | Không | Không | 8-12 tuần |

### 5.3. Cost per quarter để maintain (sau khi build)

| Hướng | Sessions/quarter | Lý do |
|-------|-----------------|-------|
| A | **4-6** | Phải update nhiều files khi Claude thay đổi |
| B | **2-3** | Kiến trúc mới nhưng vẫn nhiều content |
| C | **2-3** | Chỉ update knowledge/ (~8 files) |
| D | **1-2** | Update configs/agents, ít prose |
| E | **2-3** | Update knowledge/ + configs |

---

## 6. Khuyến nghị cuối cùng

### 6.1. Hướng khuyến nghị: D+ (Framework-First, có bổ sung)

**Lý do chọn D (Framework-First) làm xương sống chính:**

1. **Giải quyết vấn đề thực tế:** Kỹ sư cần DÙNG Claude hiệu quả, không cần ĐỌC về Claude
2. **Maintenance cost thấp nhất:** 1-2 sessions/quarter vs 4-6 sessions/quarter
3. **Scale tốt:** Thêm team = thêm profile, không viết guide mới
4. **Automation-native:** Framework là code, có thể test + CI/CD
5. **Phù hợp với 1 maintainer:** Ít content prose để write/review, nhiều config để maintain

**Bổ sung từ C (Split) và E (Ecosystem):**

- Giữ lean guide (từ hướng C) cho "tại sao" và methodology
- Knowledge layer KHÔNG cần — link tới official docs + PNX notes ngắn
- Scaffold giữ và nâng cấp (từ hướng E) cho project bootstrap

### 6.2. Kiến trúc đề xuất cụ thể

```
Guide Claude v10 — "Effective Claude for PNX Engineers"
│
├── framework/                        ← SẢN PHẨM CHÍNH
│   ├── configs/
│   │   ├── global-CLAUDE.md          PNX company-wide rules
│   │   ├── profiles/
│   │   │   ├── robotics.md           Team Robotics config
│   │   │   ├── solution.md           Team Solution config
│   │   │   └── rd.md                 Team R&D config
│   │   └── project-types/
│   │       ├── code-project.md       .claude/CLAUDE.md cho code project
│   │       ├── doc-project.md        .claude/CLAUDE.md cho doc project
│   │       └── research-project.md   .claude/CLAUDE.md cho research project
│   │
│   ├── agents/                       Custom agents chia sẻ
│   │   ├── reviewer.yml              Code/doc reviewer
│   │   ├── planner.yml               Project planner
│   │   └── onboarder.yml             Help new engineer
│   │
│   ├── skills/                       Shared skills
│   │   ├── review/SKILL.md           Structured review workflow
│   │   ├── handoff/SKILL.md          Session handoff
│   │   ├── daily/SKILL.md            Daily standup prep
│   │   └── retro/SKILL.md            Sprint retrospective
│   │
│   ├── hooks/                        Standard hooks
│   │   ├── quality-gate.py           Pre-commit quality check
│   │   ├── context-monitor.py        Auto compact at 70%
│   │   └── security-basic.py         Block common vulnerabilities
│   │
│   └── project-init/                 Bootstrap script
│       ├── init.sh                   Setup project từ zero
│       └── checklist.md              Manual steps
│
├── guide/                            ← TÀI LIỆU LEAN (~10-12 files)
│   ├── 00-overview.md                Map + learning paths
│   ├── 01-getting-started.md         15 phút setup (merge base/01+02)
│   ├── 02-prompt-craft.md            Prompt engineering (stable, từ base/03)
│   ├── 03-context-mastery.md         Context management (stable, từ base/04)
│   ├── 04-effective-patterns.md      Best patterns + anti-patterns (merge base/05+06)
│   ├── 05-evaluation.md              Đánh giá output (stable, từ base/07)
│   ├── 06-doc-workflows.md           Cho Technical Writers (merge doc/ essentials)
│   ├── 07-dev-workflows.md           Cho Developers (merge dev/ essentials)
│   ├── 08-team-collaboration.md      Làm việc nhóm với Claude (MỚI)
│   ├── 09-advanced.md                Power user: agents, plugins, MCP
│   └── reference/
│       ├── cheatsheet.md             1-page quick ref
│       ├── model-guide.md            Chọn model + pricing
│       ├── glossary.md               Thuật ngữ
│       └── links.md                  Links tới official docs (thay knowledge/)
│
├── scaffold/                         ← BOOTSTRAP (nâng cấp từ _scaffold/)
│   ├── project-setup/
│   ├── team-setup/                   MỚI: setup team workflow
│   └── examples/
│
├── .claude/                          ← META-INFRA
│   ├── CLAUDE.md                     Dùng @import, <150 dòng
│   ├── agents/                       MỚI: agents cho chính project này
│   ├── skills/                       Giữ + nâng cấp skills hiện tại
│   ├── hooks/                        Giữ + nâng cấp hooks hiện tại
│   └── rules/                        Giữ + nâng cấp rules hiện tại
│
├── machine-readable/
│   └── llms.txt                      Cập nhật index
│
├── VERSION
├── project-state.md
└── README.md
```

### 6.3. So sánh v9.1 vs v10 (đề xuất)

| Aspect | v9.1 (hiện tại) | v10 (đề xuất) |
|--------|-----------------|---------------|
| **Content files** | 32 | ~12-14 |
| **Content size** | ~687 KB | ~200-250 KB |
| **Framework** | Không có | configs + agents + skills + hooks |
| **Guide focus** | Comprehensive reference | Opinionated methodology |
| **Feature docs** | In-guide (dễ stale) | Links to official + PNX notes |
| **Maintenance/quarter** | 4-6 sessions | 1-2 sessions |
| **Onboarding path** | Đọc 8 modules base/ | Setup framework + đọc 3-4 modules |
| **Team support** | Không có | Team profiles + collaboration guide |
| **Automation** | Format check only | Quality gates + context monitor + review agents |

### 6.4. Phased delivery

```
PHASE 1 (2-3 sessions): Infra Foundation
  - .claude/ upgrade: @import, agents/, hooks expansion
  - Migrate CLAUDE.md sang modular @import
  - Tạo 2-3 custom agents (reviewer, explorer)
  → Deliverable: Infra v10.0-alpha

PHASE 2 (3-4 sessions): Framework Core
  - Tạo framework/ structure
  - Build shared configs (global + 2-3 team profiles)
  - Build 3-4 shared skills (review, handoff, daily)
  - Build 2-3 hooks (quality-gate, context-monitor)
  → Deliverable: Framework v0.1

PHASE 3 (3-4 sessions): Lean Guide
  - Migrate content tốt từ v9.1 → 12-14 files mới
  - Merge + condense (32 → 12-14)
  - Viết mới: team-collaboration, links-to-official
  - KHÔNG viết lại content ổn định — chỉ restructure
  → Deliverable: Guide v10.0-beta

PHASE 4 (2-3 sessions): Polish + Release
  - Scaffold update
  - Cross-links, navigation
  - Testing với 1-2 team members
  - Version bump v10.0
  → Deliverable: v10.0 release

PHASE 5 (ongoing, 1-2 sessions/quarter): Ecosystem Growth
  - Thêm team profiles khi cần
  - Thêm skills/agents từ team feedback
  - Update knowledge links khi Claude release
```

### 6.5. Rủi ro của khuyến nghị này và mitigation

| Rủi ro | Xác suất | Mitigation |
|--------|----------|------------|
| Framework không được adopt | Trung bình | Pilot với 2-3 người trước, iterate |
| Lean guide quá ngắn, thiếu context | Thấp | Vẫn có crosslinks tới official docs |
| Migration mất content giá trị | Thấp | Git history bảo toàn v9.1, có thể refer |
| Scope creep trong Phase 2-3 | Trung bình | Time-box mỗi phase, checkpoint thường xuyên |
| Claude Code breaking changes | Thấp | Framework là code, dễ update hơn prose |

---

## 7. Quyết định cần user chốt

Trước khi bắt tay vào, cần chốt:

1. **Hướng chiến lược:** D+ (Framework-First) hay hướng khác?
2. **Scope framework:** Chỉ Claude Code hay cả Cowork (claude.ai)?
3. **Team profiles:** Những team nào cần profile riêng?
4. **Lean guide:** 12-14 files có chấp nhận được? Hay cần giữ nhiều hơn?
5. **Timeline:** Phân bổ sessions như thế nào (intensive 2 tuần hay spread 1-2 tháng)?
6. **Pilot:** Ai sẽ là early adopter để test framework?
7. **v9.1 archive:** Giữ trong branch riêng hay xoá?

---

> [!NOTE]
> File này là TÀI LIỆU NGHIÊN CỨU — không phải kế hoạch thực thi.
> Mọi quyết định cần user confirm trước khi triển khai.
> Giá trị chính: cung cấp góc nhìn đa chiều để ra quyết định informed.

---

## 8. Bổ sung từ Web Research (03/2026)

### 8.1. Custom Agents — Thực tế sử dụng

- **Supervisor-subagent architecture** đã mature: Opus 4.6 Agent Teams là built-in
- **100+ agent examples** tại VoltAgent/awesome-claude-code-subagents (GitHub)
- **Patterns phổ biến:** spec-writing pipelines, code simplification, end-to-end verification, multi-agent orchestration (4+ agents)
- **Caution:** Quá nhiều isolation → main agent mất khả năng reasoning tổng thể. Cần balance.
- **Cost optimization:** Haiku 4.5 = 90% Sonnet agentic performance, tốc độ 2x, chi phí 3x rẻ hơn → dùng cho lightweight agents

[Nguồn: code.claude.com/docs/en/sub-agents, pubnub.com, claudefa.st, medium.com/@the.gigi]

### 8.2. CLAUDE.md Modularity — Thực tế

- **@import syntax** đã confirmed: `@path/to/file` trong CLAUDE.md, recursive max 5 hops, approval dialog cho external imports
- **CLAUDE.local.md DEPRECATED** — dùng @import thay thế
- **Cách chính để modular hoá:** `.claude/rules/` directory — auto-load cùng CLAUDE.md
- Mỗi file trong `.claude/rules/` được load tự động — KHÔNG cần import
- **Best practice cộng đồng:** CLAUDE.md < 200 dòng, tách chi tiết vào rules/
- **Team pattern:** Frontend lead owns `frontend.md`, backend lead owns `api-design.md` trong rules/
- Ref: Trail of Bits đã publish claude-code-config repo làm template

[Nguồn: serenitiesai.com, claude.com/blog, trailofbits/claude-code-config, institute.sfeir.com]

### 8.3. Documentation Maintenance — Bài học ngành

- **80% effort là MAINTAIN, không phải CREATE** — đây là vấn đề phổ biến, không riêng Guide Claude
- **Documentation drift** chưa được giải quyết trong hầu hết CI/CD pipelines
- **Tools mới:** Swimm (auto-sync với code), DeepDocs (detect drift), GitBook Docs Agent
- **DocOps** là discipline mới — áp dụng DevOps principles cho doc lifecycle
- **AI cho docs:** 24.8% devs đã dùng AI cho documentation (Stack Overflow 2025)
- **Insight:** Building/deploying docs KHÔNG phải bottleneck — DETECTING STALENESS mới là vấn đề

[Nguồn: deepdocs.dev, apprecode.com, Stack Overflow Survey 2025]

### 8.4. llms.txt — Trạng thái hiện tại

- **844,000+ websites** đã implement (BuiltWith, 10/2025)
- **2 variants:** `/llms.txt` (nav overview) + `/llms-full.txt` (full content)
- **NHƯNG:** Major LLMs (Gemini, ChatGPT) KHÔNG crawl llms.txt. Server logs confirm.
- **Giá trị thực:** inference-time context (paste vào conversation/RAG), KHÔNG phải training/search
- **Kết luận cho Guide Claude:** llms.txt vẫn hữu ích cho LOCAL use (Claude Code đọc, Cowork) nhưng đừng kỳ vọng crawler

[Nguồn: llmstxt.org, semrush.com, mintlify.com, buildwithfern.com]

### 8.5. Plugin Sharing cho Teams — Đã mature

- **Plugin Marketplace** hoạt động như npm cho AI workflows
- **9,000+ plugins** tính đến đầu 2026
- **3 hosting models:** Git-based, URL-based, Organization marketplace
- **Enterprise (02/2026):** Admins connect private GitHub repo → Cowork auto-sync plugins
- **Official directory:** anthropics/claude-plugins-official (GitHub)
- **Community registry:** claude-plugins.dev
- **Insight cho PNX:** Có thể tạo private marketplace cho team — distribute configs/skills/hooks như plugins

[Nguồn: code.claude.com/docs/en/plugins, claude.com/blog, support.claude.com]

---

## 9. Insights tổng hợp sau Web Research

### Thay đổi so với phân tích ban đầu:

1. **@import ĐÃ CONFIRMED:** Syntax `@path/to/file` trong CLAUDE.md, recursive max 5 hops, approval dialog. **CLAUDE.local.md DEPRECATED** — dùng imports thay thế. Đây là tin tốt: có thể modular hoá CLAUDE.md chính thức.

2. **`.claude/rules/` VẪN LÀ CÁCH CHÍNH:** Auto-load mọi `.md` trong rules/ — Guide Claude ĐÃ dùng 7 files. Kết hợp @import + rules/ = full modularity.

3. **9,000+ plugins:** Ecosystem lớn hơn dự kiến. 3 hosting models (git, URL, org marketplace). PNX có thể tạo **private marketplace** để distribute framework.

4. **Custom agents MATURE:** 100+ examples (VoltAgent/awesome-claude-code-subagents). Patterns: supervisor-subagent, parallel execution, cost optimization (Haiku 4.5 = 90% Sonnet quality, 2x speed, 3x rẻ hơn).

5. **Stale docs là VẤN ĐỀ NGÀNH:** 80% SaaS knowledge bases go stale within months. Chỉ 6% engineers update docs daily. Tools mới: Swimm, DeepDocs, Ferndesk — nhưng chưa có standard solution.

6. **llms.txt v1.1.0:** 844K+ sites. Nhưng major LLMs KHÔNG crawl. Giá trị = local inference context.

7. **Haiku 4.5 insight:** 90% Sonnet agentic performance, 2x speed, 3x rẻ → dùng cho exploration agents, review agents. Chỉ Sonnet/Opus cho complex reasoning.

### Điều chỉnh khuyến nghị:

- **Phase 1 (Infra):** @import + rules/ kết hợp. Tạo custom agents (reviewer, explorer). Dùng Haiku 4.5 cho lightweight agents.
- **Phase 2 (Framework):** **PLUGIN FORMAT** để distribute — dùng marketplace thay vì manual copy. Đây là cách PNX share configs/skills cho team.
- **Phase 3 (Guide):** Lean guide confirmed — 80% effort là maintain, không phải create. Giảm scope = giảm maintenance.
- **Reference architecture:** Trail of Bits claude-code-config (GitHub) — xem để học patterns.
- **Cost optimization:** Haiku agents cho scan/review, Sonnet cho orchestration, Opus cho architectural decisions.

---

> [Nguồn: Phân tích từ dữ liệu project v9.1 + research-claude-code-2026.md + web research 03/2026 + kiến thức chuyên gia Claude Code]
> [Cập nhật 03/2026]
