# Upgrade Plan — Guide Claude v7.0 → v9.0

**Created:** 2026-03-06 | **Baseline:** v7.0 (commit 49f5ac4)
**Last updated:** 2026-03-07 | **Status:** P1 complete (v7.3) — ready for P2

---

## Tổng hợp Quyết định

### Quyết định chiến lược (D1-D10)

| # | Quyết định | Chốt |
|---|-----------|------|
| D1 | Tách guide/ thành Base/Doc/Dev | ✅ Tách 3 tier |
| D2 | Two-Layer Knowledge | ✅ Xây lại theo Anthropic official memory system |
| D3 | Prompt format | ✅ Giữ mix: XML cho structured prompts, `[]` cho markers, `{{}}` placeholders |
| D4 | Claude Code scope | ✅ Tách Dev section — viết mới hoàn toàn |
| D5 | _scaffold | ✅ Restructure + examples (Guide Claude + dev example) |
| D6 | Cheatsheets | ✅ Master reference theo nhóm Base/Doc/Dev |
| D7 | Roadmap | ✅ 5 phases, multi-version, review checkpoint mỗi phase |
| D8 | Module 3,5,7,8,9 content | ✅ Tách base/specific + cross-link |
| D9 | Decision Matrix | ✅ Rebuild 3-way (Chat / Cowork / Claude Code) |
| D10 | Navigation | ✅ Full index + prev/next nav links |

### Quyết định triển khai (A1-A5, Q1-Q6)

| # | Quyết định | Chốt |
|---|-----------|------|
| A1 | Thêm S0 automation setup | ✅ Có — trước P1 |
| A2 | Hook script language | ✅ Python |
| A3 | `.claude/rules/` timing | ✅ Hybrid: GĐ1 generic ngay (S0), GĐ2 tier-specific (P2) |
| A4 | _scaffold timing | ✅ P4 (sau khi validate qua P1-P3) |
| A5 | doc-standard-enforcer split | ✅ S0 — tách thành hook + skill |
| Q1 | Navigation | ✅ Full index + nav links |
| Q2 | Phase bắt đầu | ✅ P1 Foundation |
| Q3 | Version naming | ✅ v7.1 → v8.0 → v9.0 |
| Q4 | Session duration | ✅ Tùy task |
| Q5 | Dev content | ✅ Viết mới hoàn toàn |
| Q6 | _scaffold examples | ✅ Guide Claude + dev example |
| — | IDE coverage | ✅ VS Code only (bỏ JetBrains) |
| D1' | M10 extraction strategy | ✅ Session riêng (S10b) — split 4 targets |
| D2' | M05 5.11-5.14 placement | ✅ base/05 (Planning patterns) |
| D3' | P2 session count | ✅ 8+2 sub-sessions (tăng từ 7) |
| D4' | M08 8.7 CC anti-patterns | ✅ Giữ tạm base/06, extract sang dev/ tại P3 |
| D5' | llms.txt update timing | ✅ Cuối P2 (S15) |
| D6' | M10 10.8 vs M04 Decision Matrix | ✅ Merge thông minh vào base/04 + deduplicate |
| D7' | M10 10.13 redirect stub | ✅ Xóa — thay bằng cross-link trong doc/03 |

---

## Quality Assurance Framework

### Nguyên tắc: Tài liệu nền tảng — ưu tiên chất lượng

Dự án này là tài liệu tiền đề cho mọi dự án AI Claude về sau. Sai ở đây → cascade errors. Mọi quyết định ưu tiên **chất lượng trước tốc độ**.

### 4 lớp bảo vệ chất lượng

**Lớp 1 — Prevention (tự động, deterministic):**

| Cơ chế | Mục đích | Trust | Hoạt động |
|--------|---------|:-----:|-----------|
| `.claude/rules/` | Rules đúng context khi edit | ✅ Anthropic Official | Auto — khi Claude mở file |
| Hooks (PostToolUse) | Block format sai | ✅ Anthropic Official | Auto — mỗi lần edit |
| Hooks (PreCommit) | Block commit nếu broken links | ✅ Anthropic Official | Auto — mỗi lần commit |
| CLAUDE.md | Project conventions | ✅ Anthropic Official | Auto — mỗi session |

**Lớp 2 — Detection (on-demand):**

| Cơ chế | Mục đích | Trust | Trigger |
|--------|---------|:-----:|---------|
| `/validate-doc` | Check format 1 module | Custom (verified) | User — sau mỗi edit |
| `cross-ref-checker` | Scan broken links | Custom (verified) | User — trước checkpoint |
| `/source-audit` (NEW) | Scan source markers | Custom | User — cuối session |
| `upgrade-guide` | Health check tổng thể | Custom (verified) | User — cuối phase |

**Lớp 3 — Review (manual + AI):**

| Cơ chế | Mục đích | Trigger |
|--------|---------|---------|
| `module-review` | Deep review 5 criteria | Cuối phase |
| Source verification | Verify claims vs official docs | Trước finalize |
| Audience test | Người mới hiểu không? | Review checkpoint |

**Lớp 4 — Gate (phase boundary):**

| Gate | Tiêu chí | Ai quyết định |
|------|---------|---------------|
| Phase Review | Checklist pass/fail | User approve |
| Version Bump | Tất cả gates pass | User confirm |
| Rollback | Critical issue | User hoặc hook |

### Source Verification Standard

**Tier 1 (bắt buộc cho core features):**
- `code.claude.com/docs/en/*` → `[Nguồn: Claude Code Docs]`
- `docs.anthropic.com/en/*` → `[Nguồn: Anthropic API Docs]`
- `support.anthropic.com/*` → `[Nguồn: Anthropic Help]`

**Tier 2 (best practices, patterns):**
- `github.com/anthropics/*` → `[Nguồn: Anthropic GitHub]`
- `writethedocs.org/*` → `[Nguồn: Write the Docs]`

**Tier 3 (cần disclaimer):**
- Community repos → `[Nguồn: Community — URL]`
- Project experience → `[Ứng dụng Kỹ thuật]`
- Non-official patterns → `[Ghi chú: pattern từ thực tế, không phải official]`

### Content Scoring (5 chiều)

| Score | Meaning | Action |
|:-----:|---------|--------|
| 5 | Excellent — verified, current, clear | Ship |
| 4 | Good — minor gaps | Fix in current phase |
| 3 | Adequate — some issues | Fix before next phase |
| 2 | Poor — significant issues | Block — fix trước khi tiếp |
| 1 | Critical — factually wrong | Immediate fix or remove |

**Gate rule:** Không module nào < 3 khi kết thúc phase. Không module nào < 4 khi release v9.0.

---

## Anti-Derailment Protocol

### Phase Scope Lock

Mỗi phase có scope cố định. Task ngoài scope → ghi vào BACKLOG, không làm.

| Phase | ĐƯỢC LÀM | KHÔNG LÀM |
|-------|----------|-----------|
| S0 | Tạo automation infrastructure | Edit content |
| P1 | Fix quality (format, links, sources, Two-Layer) | Thay đổi cấu trúc, viết content mới |
| P2 | Move files, update paths | Sửa content (ngoài cross-links), viết dev content |
| P3 | Viết dev content mới | Sửa base/doc content |
| P4 | Cheatsheets, _scaffold, skills, tools | Restructure |
| P5 | Review, polish, finalize | Thêm features mới |

### Session Discipline

```
Session Start:
  1. Đọc upgrade-plan-v8.md → xác định task
  2. Confirm scope: "Session này làm [X], output [Y]"
  3. /checkpoint (backup)

Session Work:
  4. Hooks auto-enforce format + links
  5. /validate-doc khi edit xong 1 file

Session End:
  6. Verify deliverable match scope
  7. Ghi tasks phát sinh → BACKLOG
  8. /checkpoint (save)
  9. Handover notes cho session tiếp
```

---

## Automation Architecture

```
Enforcement (Deterministic — Trust cao nhất)
┌─────────────────────────────────────────┐
│  Hooks (settings.json)                  │
│  ├── PostToolUse: format-check.py       │
│  ├── PreCommit: link-check.py           │
│  └── SessionStart: version-info (có)    │
└─────────────────────────────────────────┘

Context (Auto-load — Trust cao)
┌─────────────────────────────────────────┐
│  .claude/rules/ (GĐ1 → GĐ2)           │
│  GĐ1: writing-standards.md (guide/**)  │
│        reference-standards.md           │
│        scaffold-standards.md            │
│  GĐ2: + tier-base.md (guide/base/**)   │
│        + tier-doc.md (guide/doc/**)     │
│        + tier-dev.md (guide/dev/**)     │
└─────────────────────────────────────────┘

On-demand (User trigger)
┌─────────────────────────────────────────┐
│  Skills & Commands                      │
│  ├── /checkpoint, /start (existing)     │
│  ├── /nav-update (NEW — P4)             │
│  ├── /source-audit (NEW — S0)           │
│  ├── cross-ref-checker (existing)       │
│  └── doc-standard-enforcer (trimmed)    │
└─────────────────────────────────────────┘
```

---

## Cấu trúc Target (sau v9.0)

```
guide/
├── base/                          Ai cũng cần
│   ├── 00-overview.md             Index, learning paths, dependency graph
│   ├── 01-quick-start.md          Bắt đầu 15 phút (all surfaces)
│   ├── 02-setup.md                Setup cơ bản (không Custom Style)
│   ├── 03-prompt-engineering.md   Core techniques, XML format
│   ├── 04-context-management.md   Context Window, Drift, Session Lifecycle, Decision Framework 3-way, Task Lifecycle
│   ├── 05-tools-features.md       Tools & Features (M06) + Desktop (M10) + Planning patterns (M05)
│   ├── 06-mistakes-fixes.md       Core mistakes (universal)
│   └── 07-evaluation.md           Core eval framework
│
├── doc/                           Technical Writing audience
│   ├── 01-doc-workflows.md        Recipes doc-specific (từ M05)
│   ├── 02-template-library.md     Templates doc-specific (từ M07)
│   ├── 03-cowork-setup.md         Cowork config + workflows (từ M10)
│   ├── 04-cowork-workflows.md     12 Cowork workflows (từ M11)
│   ├── 05-claude-code-doc.md      CC cho documentation (từ M12)
│   └── 06-custom-style.md         Custom Style reference (từ M02)
│
├── dev/                           Developer audience
│   ├── 01-claude-code-setup.md    CLI install, auth, config
│   ├── 02-cli-reference.md        Commands, flags, shortcuts
│   ├── 03-ide-integration.md      VS Code extension setup & tips
│   ├── 04-agents-automation.md    Subagents, Agent Teams, CI/CD
│   ├── 05-plugins.md              Discover, install, create plugins
│   └── 06-dev-workflows.md        Git, testing, code review with CC
│
└── reference/                     Tra cứu (ai cũng dùng)
    ├── config-architecture.md     existing
    ├── model-specs.md             existing
    ├── skills-list.md             existing (lookup table)
    ├── skills-guide.md            NEW: detailed descriptions
    ├── cheatsheet-base.md         NEW
    ├── cheatsheet-doc.md          NEW
    ├── cheatsheet-dev.md          NEW
    └── prompt-format-guide.md     NEW

_scaffold/
├── README.md                      Step-by-step init workflow
├── templates/
│   ├── base/                      Template chung (mọi dự án)
│   │   └── .claude/ (start, checkpoint, session-start, SessionStart hook)
│   ├── doc-project/               Template documentation
│   │   └── .claude/ (+ validate-doc, doc-standard, format-check hook)
│   └── dev-project/               Template development
│       └── .claude/ (+ code-review agent, simplify)
├── examples/
│   ├── guide-claude/              Config thực tế dự án này
│   └── dev-example/               Ví dụ dev project
└── checklists/
    ├── new-project-checklist.md
    └── daily-workflow.md
```

---

## Dependency Map

```
S0 Automation ──> P1 Foundation ──> P2 Structure ──┬──> P3 Dev Content
  ✅ Done          ✅ Done (v7.3)    ✅ Done (v8.0)  │    (v8.1–v8.3)
                                                    │
                                                    ├──> P4 Enhancement
                                                    │    (v8.4–v8.5)
                                                    │
                                                    └──> P5 Polish
                                                         (v9.0)
```

S0 → P1 → P2 (tuần tự bắt buộc). P3 và P4 song song sau P2. P5 cuối.
P2 tăng từ 7→8 sessions (S9, S10 có sub-sessions = 10 work units) do M10 extraction complexity (D1'-D7' decisions 2026-03-07).

---

## Content Mapping (chuẩn bị P2)

| Source | Section | → Target | Notes |
|--------|---------|:--------:|-------|
| M00 | Toàn bộ | base/00 | Rewrite cho 3-tier |
| M01 | Toàn bộ | base/01 | Thêm Claude Code quick start |
| M02 | 2.1-2.5 Setup cơ bản | base/02 | Giữ (2.6-2.7 summary giữ base) |
| M02 | 2.3 Styles (chi tiết) | doc/06 | Extract phần Custom Style chi tiết |
| M03 | Toàn bộ (3.1-3.5) | base/03 | Giữ nguyên — 3.5 Task Decomposition là universal |
| M04 | 4.1-4.9 + Decision Matrix | base/04 | Giữ (Context Sync + 3-way matrix đã rebuild P1) |
| M05 | 5.11-5.14 Universal | base/05 | Planning patterns → merge vào Tools & Planning |
| M05 | 5.1-5.10, 5.15-5.16 | doc/01 | Doc recipes + Cowork recipes |
| M06 | Toàn bộ | base/05 | Merge với M10 Desktop + M05 planning |
| M07 | T-01~T-05 Universal | base/ (ref) | Giữ compact |
| M07 | T-06~T-22 Doc | doc/02 | Tách (T-19~T-22 advanced giữ doc/02) |
| M08 | 8.1-8.6, 8.8-8.11 | base/06 | Universal + reference tables |
| M08 | 8.7 CC anti-patterns | base/06 (tạm) | Giữ tạm với note — extract sang dev/ tại P3 |
| M09 | Toàn bộ | base/07 | Framework universal (doc examples → callout) |
| M10 | 10.1-10.3 Desktop | base/05 | Merge vào Tools |
| M10 | 10.8 Decision Matrix | base/04 | Extract → merge vào Context Management |
| M10 | 10.8.1, 10.8.3 Memory+Scaffold | reference/ | Extract → reference patterns |
| M10 | 10.9 Pre-task Planning | base/05 | Extract → merge vào Planning section |
| M10 | 10.10 Task Lifecycle | base/04 | Extract → merge vào Context Management |
| M10 | 10.4-10.7, 10.11-10.18 Cowork | doc/03 | Tách (bulk Cowork content) |
| M11 | Toàn bộ | doc/04 | Move nguyên |
| M12 | Toàn bộ | doc/05 | Move (giữ doc scope) |
| Ref | Tất cả | reference/ | Giữ + thêm files mới + M10 extractions |

---

## Session Plans

### S0: Automation Infrastructure Setup

**Mục tiêu:** Dựng hạ tầng tự động hóa trước khi bắt đầu edit content.
**Rủi ro:** 🟢 Thấp — additive, không sửa content.

**Tasks:**

1. **Tạo `.claude/rules/` (GĐ1 — 3 files):**
   - `writing-standards.md` — paths: `guide/**/*.md`
   - `reference-standards.md` — paths: `guide/reference/**`
   - `scaffold-standards.md` — paths: `_scaffold/**`

2. **Tạo hook scripts:**
   - `.claude/hooks/format-check.py` — PostToolUse: verify heading hierarchy + code block tags
   - `.claude/hooks/link-check.py` — PreCommit: verify internal cross-links not broken

3. **Update `settings.json`:**
   - Thêm PostToolUse hook (matcher: `Write|Edit`, command: format-check.py)
   - Thêm PreCommit hook (command: link-check.py)

4. **Tạo skill `/source-audit`:**
   - `.claude/skills/source-audit/SKILL.md`
   - Scan `[Nguồn:`, `[Ứng dụng Kỹ thuật]`, `[Cập nhật` markers
   - Report sections thiếu markers

5. **Refactor `doc-standard-enforcer`:**
   - Enforcement rules → chuyển vào `.claude/rules/writing-standards.md`
   - Skill giữ: manual deep review mode (on-demand)

6. **Test:**
   - Edit 1 file test → verify PostToolUse hook fires
   - Attempt commit → verify PreCommit hook fires
   - Verify rules load đúng khi edit guide/ files

**Verify:**
- Hooks hoạt động (format-check + link-check)
- Rules load (kiểm tra qua `/memory` hoặc test edit)
- `/source-audit` skill hoạt động

**Checkpoint:** git commit "S0: automation infrastructure — rules, hooks, source-audit skill"

---

### Phase 1: Foundation (v7.1 → v7.3)

**Mục tiêu:** Fix nền tảng chất lượng — KHÔNG thay đổi cấu trúc thư mục.
**Rủi ro:** 🟢 Thấp — sửa trong files hiện tại. Hooks bảo vệ format.

#### S1: Cross-link audit + URL migration (→ v7.1-prep)

**Scope:** Toàn bộ guide/*.md — links only, không sửa content.

1. Chạy `cross-ref-checker` trên từng module
2. Grep URLs → cập nhật docs.anthropic.com → code.claude.com
3. Fix broken cross-links (anchor names thay đổi)
4. Thêm missing links nơi mention nhưng không link

**Verify:** 0 broken internal links, 0 stale external URLs.
**Checkpoint:** "P1.S1: cross-link audit + URL migration"

#### S2: Source markers audit (→ v7.1)

**Scope:** Toàn bộ guide/*.md — markers only.

1. Chạy `/source-audit` (skill mới từ S0)
2. Thêm markers thiếu theo 3-tier source standard
3. Verify `[Cập nhật MM/YYYY]` dates chính xác

**Verify:** Mỗi section có source marker. **Version bump: v7.1.**
**Checkpoint:** "P1.S2: source markers audit"

#### S3: Prompt format — M03 (→ v7.2-prep)

**Scope:** guide/03-prompt-engineering.md — format only.

1. Document convention (section đầu hoặc callout):
   - XML tags cho structured prompts
   - `[]` cho metadata markers
   - `{{variable}}` cho placeholders
2. Fix M03 examples theo convention
3. Mỗi code block có language tag

**Verify:** 0 mixed format trong cùng 1 example.
**Checkpoint:** "P1.S3: prompt format — M03"

#### S4: Prompt format — M05, M07 (→ v7.2)

**Scope:** guide/05, guide/07 — format only. Chia sub-session nếu file quá lớn.

1. Apply convention từ S3
2. M05: 16 recipes, M07: 22 templates

**Verify:** Convention nhất quán M03 ↔ M05 ↔ M07. **Version bump: v7.2.**
**Checkpoint:** "P1.S4: prompt format — M05, M07"

#### S5: Two-Layer → Context Sync (→ v7.3-prep)

**Scope:** M02(2.7), M04(4.9), M05(refs), M10(ref) — content rebuild.

1. Rename "Two-Layer Knowledge" → "Context Sync Practices"
2. Rewrite M04 section 4.9 dựa trên Anthropic official memory system
3. Update M02, M05, M10 references
4. Cập nhật disclaimer

**Verify:** 0 mentions "Two-Layer", nội dung reference official sources.
**Checkpoint:** "P1.S5: Two-Layer → Context Sync rebuild"

#### S6: Decision Matrix 3-way + Session Lifecycle (→ v7.3-prep)

**Scope:** M04(matrix), M10(10.8) — content addition.

1. Expand Decision Matrix → 3-way (Chat/Cowork/Claude Code)
2. Thêm Session Lifecycle section
3. Update M10 section 10.8

**Verify:** Matrix covers all scenarios, Session Lifecycle correct.
**Checkpoint:** "P1.S6: 3-way matrix + Session Lifecycle"

#### S7: Failure patterns M08 + P1 final review (→ v7.3)

**Scope:** M08 + full P1 review.

1. Thêm 5 patterns từ Anthropic Best Practices (kitchen sink, correcting loop, over-specified CLAUDE.md, trust-then-verify gap, infinite exploration)
2. Review toàn bộ P1 changes

**Verify:** M08 ≥ 11 patterns, toàn bộ cross-links pass. **Version bump: v7.3.**
**Checkpoint:** "P1.S7: M08 patterns + P1 final"

#### Phase 1 Review Gate — ✅ PASSED (2026-03-07)

- [x] 0 broken internal cross-links
- [x] 0 stale external URLs
- [x] Source markers trên mọi section
- [x] Prompt format nhất quán
- [x] "Two-Layer" → "Context Sync" hoàn tất
- [x] Decision Matrix 3-way
- [x] Session Lifecycle documented
- [x] M08 ≥ 11 failure patterns
- [x] Automation (hooks + rules) operational
- [x] Version = 7.3

**Result: PASSED → P2 approved.**

---

### Phase 2: Structure (v8.0)

**Mục tiêu:** Tách guide/ thành base/doc/dev.
**Rủi ro:** 🔴 Cao — mitigated bằng 8 sessions (10 work units) + git tag rollback.

> [!IMPORTANT]
> Mỗi session move xong → chạy `cross-ref-checker` → fix links ngay.
> KHÔNG để broken links tích lũy đến session cuối.

#### S8: Folder structure + safety setup

1. `git tag v7.3-pre-restructure` — safety rollback point
2. Tạo guide/base/, guide/doc/, guide/dev/
3. Tạo `.claude/rules/` GĐ2 (tier-base.md, tier-doc.md, tier-dev.md)
4. Review Content Mapping (bảng trên) → user confirm
5. Tạo placeholder files

**Checkpoint:** "P2.S8: folder structure + tier rules + safety tag"

#### S9a: Move Base content — M01, M02

1. M01 → base/01 (move nguyên)
2. M02 → base/02 (giữ 2.1-2.7, extract 2.3 Styles chi tiết → draft cho doc/06)
3. Fix cross-links trong files đã move + files trỏ đến M01, M02

**Checkpoint:** "P2.S9a: base/01-02"

#### S9b: Move Base content — M03, M04

1. M03 → base/03 (move nguyên, bao gồm 3.5 Task Decomposition)
2. M04 → base/04 (move nguyên, đã có Context Sync + 3-way Matrix từ P1)
3. Fix cross-links (M03 có 9 inbound links — ưu tiên fix)

**Checkpoint:** "P2.S9b: base/03-04"

#### S10a: Move Base content — M06 + M10 Desktop → base/05

1. M06 → base/05 (toàn bộ tools & features)
2. Merge M10 sections 10.1-10.3 (Desktop) vào base/05
3. Merge M05 sections 5.11-5.14 (Planning patterns) vào base/05
4. Fix cross-links

**Checkpoint:** "P2.S10a: base/05 (tools + desktop + planning)"

#### S10b: M10 universal extraction → base/04, reference/

**Scope:** Extract universal content từ M10 (1650 dòng) trước khi move Cowork phần.

1. Extract 10.8 (Decision Framework: flowchart + bảng tra cứu) → merge vào base/04, deduplicate bảng so sánh trùng với 4.10
2. Extract 10.8.2 (project-state.md pattern) → append base/04
3. Extract 10.10 (Task Lifecycle) → append base/04
4. Extract 10.8.1 (External Memory _memory/) → reference/
5. Extract 10.8.3 (_scaffold/) → reference/
6. Extract 10.9 (Pre-task Planning) → append base/05
7. Xóa 10.13 (redirect stub 8 dòng) — thay bằng cross-link trong doc/03
8. Verify M10 còn lại chỉ chứa Cowork content (10.4-10.7, 10.11-10.18 trừ 10.13)

**Checkpoint:** "P2.S10b: M10 universal extraction"

#### S11: Move Base content — M08, M09 → base/06, base/07

1. M08 → base/06 (8.1-8.11, giữ 8.7 CC anti-patterns tạm với note P3)
2. M09 → base/07 (toàn bộ framework, doc examples → callout)
3. Fix cross-links (M08 có 18 outbound links — cần update nhiều nhất)

**Checkpoint:** "P2.S11: base/06-07"

#### S12: Move Doc content — M05, M07

1. M05 (5.1-5.10, 5.15-5.16) → doc/01 (doc workflows + Cowork recipes). Note: 5.11-5.14 đã extract ở S10a
2. M07 (T-06~T-22) → doc/02 (doc templates)
3. M07 (T-01~T-05) → reference/ hoặc base/ (universal templates)
4. Fix cross-links

**Checkpoint:** "P2.S12: doc/01-02"

#### S13: Move Doc content — M10 Cowork, M11, M12, M02 Styles

1. M10 remaining (10.4-10.7, 10.11-10.18) → doc/03 (Cowork setup & workflows)
2. M11 → doc/04 (move nguyên)
3. M12 → doc/05 (move nguyên)
4. M02 section 2.3 Styles (extracted draft) → doc/06
5. Fix cross-links

**Checkpoint:** "P2.S13: doc/03-06"

#### S14: M00 Overview + Navigation

1. Rewrite M00 → base/00 cho 3-tier structure
2. Learning paths per audience (base → doc, base → dev)
3. Prev/next nav links toàn bộ files
4. Dependency graph update

**Checkpoint:** "P2.S14: overview + navigation"

#### S15: Cleanup + validation

1. Remove old guide/*.md (chỉ sau khi validation pass)
2. Update CLAUDE.md (folder structure, module status)
3. Update project-state.md
4. Update machine-readable/llms.txt
5. Full `/cross-ref-checker` — final sweep
6. **Version bump v8.0**

**Checkpoint:** "P2.S15: cleanup + v8.0"

#### Phase 2 Review Gate — ✅ PASSED (2026-03-07)

- [x] 3-tier structure hoạt động (base/doc/dev/reference)
- [x] Tier-specific rules load đúng (tier-base.md, tier-doc.md, tier-dev.md)
- [x] Navigation links trên mọi file
- [x] 0 broken cross-links (verified — no stale refs to old guide/*.md)
- [x] CLAUDE.md + project-state.md + llms.txt updated
- [x] Old guide/*.md files removed (13 files)
- [x] Version = 8.0

**Result: PASSED → P3 approved.**

---

### Phase 3: Dev Content (v8.1 → v8.3)

**Mục tiêu:** Viết mới nội dung developer — hoàn toàn mới.
**Rủi ro:** 🟡 TB — content mới, ít ảnh hưởng existing.

> [!IMPORTANT]
> Mỗi session P3 bắt đầu bằng: verify features tại code.claude.com/docs trước khi viết.
> Claude Code features thay đổi nhanh — không dựa vào thông tin cũ.

#### S16: CLI setup + reference → dev/01, dev/02 (v8.1)
#### S17: VS Code extension → dev/03
#### S18-S19: Agents & Automation → dev/04 (v8.2)
#### S20: Plugins → dev/05
#### S21: Dev workflows → dev/06 (v8.3)

#### Phase 3 Review Gate

- [ ] 6 dev files complete
- [ ] Cross-links dev ↔ base valid
- [ ] Source verification (Tier 1 cho features)
- [ ] Content score ≥ 4 trên 5 chiều
- [ ] Version = 8.3

---

### Phase 4: Enhancement (v8.4 → v8.5)

**Mục tiêu:** Cheatsheets, _scaffold, skills guide, tooling.
**Rủi ro:** 🟢 Thấp — additive.

#### S22: Skills guide → reference/skills-guide.md
#### S23-S24: Cheatsheets (3 files) (v8.4)
#### S25: _scaffold restructure (templates + examples + workflows)
#### S26: /nav-update skill + validation hooks (v8.5)
#### S27: prompt-format-guide + custom-style reference

#### Phase 4 Review Gate

- [ ] Skills guide complete
- [ ] 3 cheatsheets complete
- [ ] _scaffold restructured + examples
- [ ] Tooling operational
- [ ] Version = 8.5

---

### Phase 5: Polish (v9.0)

**Mục tiêu:** Final quality pass.

#### S28: Full cross-ref audit
#### S29-S30: Content review per tier (module-review × 5 dimensions)
#### S31: Index, navigation finalize
#### S32: Version bump v9.0 + release notes

#### Phase 5 Review Gate

- [ ] 0 broken links
- [ ] All modules score ≥ 4
- [ ] Navigation complete
- [ ] project-state.md, CLAUDE.md, llms.txt current
- [ ] Version = 9.0

---

## Base Toolkit (cho _scaffold — P4)

Skills/commands đủ tin cậy để ship trong mọi project template:

| Component | Type | Trust |
|-----------|------|:-----:|
| `/start` | Command | ✅ Git-based |
| `/checkpoint` | Command | ✅ Git-based |
| `session-start` | Skill | ✅ Git-based |
| `SessionStart` hook | Hook | ✅ Anthropic Official |
| `writing-standards.md` | Rule | ✅ Official format + Doc as Code |

Doc Toolkit thêm: `/validate-doc`, `doc-standard-enforcer`, `format-check.py` hook.
Dev Toolkit thêm: bundled `/simplify`, `/batch`, `/debug`, code-review agent.

---

## Tổng kết

| Phase | Sessions | Versions | Risk | Status |
|-------|:--------:|----------|:----:|:------:|
| S0 Automation | 1-2 | — | 🟢 | ✅ Done |
| P1 Foundation | S1–S7 (7) | v7.1–v7.3 | 🟢 | ✅ Done |
| P2 Structure | S8–S15 (8+2 sub) | v8.0 | 🔴 | ✅ Done |
| P3 Dev Content | S16–S21 (6) | v8.1–v8.3 | 🟡 | — |
| P4 Enhancement | S22–S27 (6) | v8.4–v8.5 | 🟢 | — |
| P5 Polish | S28–S32 (5) | v9.0 | 🟢 | — |
| **Total** | **~34 work units** | **v7.0 → v9.0** | | |

Ước tính giảm 30-60% effort nhờ automation (S0). P2 tăng từ 7→8 sessions (10 work units) do M10 complexity.

---

## Handover Template

```markdown
## Session Handover — S[X] → S[X+1]

**Phase:** P[X] | **Version:** v[X.X]
**Completed:** [task description]
**Files changed:** [list]
**Status:** Done / Partial / Blocked

**Next session (S[X+1]):**
- Task: [description]
- Input files: [list]
- Expected output: [list]
- Dependencies: [none / S[X] must pass]

**Open issues:**
- [any blockers or questions]
```

---

## BACKLOG (Tasks phát sinh — làm đúng phase)

| # | Task | Phát sinh ở | Thuộc Phase | Status |
|---|------|------------|-------------|--------|
| B1 | Code blocks thiếu language tag: M00(4), M01(8), M02(7), M04(4), M08(1) | S1 | P1.S3-S4 | ✅ done (S4) |
| B2 | Heading hierarchy skip: M12(12), ref/claude-code-setup(1) | S1 | P1.S3-S4 | ✅ resolved (verified S4 — 0 issues found) |

---

## Quy tắc an toàn

1. **Checkpoint trước mỗi edit lớn** — `/checkpoint` = git commit
2. **Không force push, không reset --hard** — CLAUDE.md rule
3. **Phase 2 rollback** — `git checkout v7.3-pre-restructure` (tag tạo ở S8)
4. **Review checkpoint bắt buộc** — không skip
5. **1 session = 1 deliverable** — không để dở dang
6. **File > 500 dòng** — split trong cùng session
7. **Scope lock** — task ngoài scope → BACKLOG
8. **Source verify** — core features phải có Tier 1 source
