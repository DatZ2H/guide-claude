# Upgrade Plan — Guide Claude v7.0 → v9.0

**Created:** 2026-03-06 | **Baseline:** v7.0 (commit 49f5ac4)
**Last updated:** 2026-03-06 | **Status:** Approved — ready for S0

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
│   ├── 04-context-management.md   Context Window, Drift, Session Lifecycle
│   ├── 05-tools-features.md       Cheat sheet tính năng (mở rộng từ M06)
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
                  (v7.1–v7.3)       (v8.0)         │    (v8.1–v8.3)
                                                    │
                                                    ├──> P4 Enhancement
                                                    │    (v8.4–v8.5)
                                                    │
                                                    └──> P5 Polish
                                                         (v9.0)
```

S0 → P1 → P2 (tuần tự bắt buộc). P3 và P4 song song sau P2. P5 cuối.

---

## Content Mapping (chuẩn bị P2)

| Source | Section | → Target | Notes |
|--------|---------|:--------:|-------|
| M00 | Toàn bộ | base/00 | Rewrite cho 3-tier |
| M01 | Toàn bộ | base/01 | Thêm Claude Code quick start |
| M02 | 2.1-2.5 Setup cơ bản | base/02 | Giữ |
| M02 | 2.6 Custom Style | doc/06 | Tách |
| M02 | 2.7 Two-Layer Knowledge | base/04 | Rebuild → Context Sync (P1) |
| M03 | 3.1-3.4 Core techniques | base/03 | Giữ |
| M03 | 3.5+ AMR examples | doc/ (inline) | Tách hoặc callout |
| M04 | 4.1-4.8 Core context | base/04 | Giữ |
| M04 | 4.9 Two-Layer | base/04 | Rebuild → Context Sync (P1) |
| M04 | Decision Matrix | base/04 | Expand 3-way (P1) |
| M05 | 5.11-5.14 Universal | base/ (merge) | Planning, decomposition |
| M05 | 5.1-5.10, 5.15-5.16 | doc/01 | Doc recipes |
| M06 | Toàn bộ | base/05 | Mở rộng significantly |
| M07 | T-01~T-05 Universal | base/ (ref) | Giữ compact |
| M07 | T-06~T-22 Doc | doc/02 | Tách |
| M08 | Nhóm 1-4 Universal | base/06 | Giữ |
| M08 | Nhóm 5-6 Doc | doc/ (inline) | Tách |
| M09 | Framework core | base/07 | Giữ |
| M09 | Doc criteria | doc/ (inline) | Tách |
| M10 | 10.1-10.3 Desktop | base/05 | Merge vào Tools |
| M10 | 10.4-10.12 Cowork | doc/03 | Tách |
| M11 | Toàn bộ | doc/04 | Move nguyên |
| M12 | Toàn bộ | doc/05 | Move (giữ doc scope) |
| Ref | Tất cả | reference/ | Giữ + thêm files mới |

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

#### Phase 1 Review Gate

- [ ] 0 broken internal cross-links
- [ ] 0 stale external URLs
- [ ] Source markers trên mọi section
- [ ] Prompt format nhất quán
- [ ] "Two-Layer" → "Context Sync" hoàn tất
- [ ] Decision Matrix 3-way
- [ ] Session Lifecycle documented
- [ ] M08 ≥ 11 failure patterns
- [ ] Automation (hooks + rules) operational
- [ ] Version = 7.3

**Pass → P2. Fail → fix items → re-review.**

---

### Phase 2: Structure (v8.0)

**Mục tiêu:** Tách guide/ thành base/doc/dev.
**Rủi ro:** 🔴 Cao — mitigated bằng sub-phases + git rollback.

#### S8: Folder structure + mapping verify

1. Tạo guide/base/, guide/doc/, guide/dev/
2. Tạo `.claude/rules/` GĐ2 (tier-base.md, tier-doc.md, tier-dev.md)
3. Review Content Mapping → user confirm
4. Tạo placeholder files

**Checkpoint:** "P2.S8: folder structure + tier rules"

#### S9-S10: Move Base content (2 sessions)

**S9:** M01, M02(base), M03(base), M04(base) → base/01-04
**S10:** M06→base/05, M08(base)→base/06, M09(core)→base/07

#### S11-S12: Move Doc content (2 sessions)

**S11:** M05(doc)→doc/01, M07(doc)→doc/02
**S12:** M10(Cowork)→doc/03, M11→doc/04, M12→doc/05, M02(Style)→doc/06

#### S13: M00 Overview + Navigation

1. Rewrite M00 cho 3-tier
2. Learning paths per audience
3. Prev/next nav links toàn bộ files
4. Dependency graph update

#### S14: Cleanup + validation

1. Remove old guide/*.md
2. Update CLAUDE.md, project-state.md
3. Full `/cross-ref-checker`
4. **Version bump v8.0**

#### Phase 2 Review Gate

- [ ] 3-tier structure hoạt động
- [ ] Tier-specific rules load đúng
- [ ] Navigation links trên mọi file
- [ ] 0 broken cross-links
- [ ] CLAUDE.md + project-state.md updated
- [ ] Version = 8.0

---

### Phase 3: Dev Content (v8.1 → v8.3)

**Mục tiêu:** Viết mới nội dung developer — hoàn toàn mới.
**Rủi ro:** 🟡 TB — content mới, ít ảnh hưởng existing.

#### S15: CLI setup + reference → dev/01, dev/02 (v8.1)
#### S16: VS Code extension → dev/03
#### S17-S18: Agents & Automation → dev/04 (v8.2)
#### S19: Plugins → dev/05
#### S20: Dev workflows → dev/06 (v8.3)

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

#### S21: Skills guide → reference/skills-guide.md
#### S22-S23: Cheatsheets (3 files) (v8.4)
#### S24: _scaffold restructure (templates + examples + workflows)
#### S25: /nav-update skill + validation hooks (v8.5)
#### S26: prompt-format-guide + custom-style reference

#### Phase 4 Review Gate

- [ ] Skills guide complete
- [ ] 3 cheatsheets complete
- [ ] _scaffold restructured + examples
- [ ] Tooling operational
- [ ] Version = 8.5

---

### Phase 5: Polish (v9.0)

**Mục tiêu:** Final quality pass.

#### S27: Full cross-ref audit
#### S28-S29: Content review per tier (module-review × 5 dimensions)
#### S30: Index, navigation, llms.txt finalize
#### S31: Version bump v9.0 + release notes

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

| Phase | Sessions | Versions | Risk |
|-------|:--------:|----------|:----:|
| S0 Automation | 1-2 | — | 🟢 |
| P1 Foundation | S1–S7 (7) | v7.1–v7.3 | 🟢 |
| P2 Structure | S8–S14 (7) | v8.0 | 🔴 |
| P3 Dev Content | S15–S20 (6) | v8.1–v8.3 | 🟡 |
| P4 Enhancement | S21–S26 (6) | v8.4–v8.5 | 🟢 |
| P5 Polish | S27–S31 (5) | v9.0 | 🟢 |
| **Total** | **~32 sessions** | **v7.0 → v9.0** | |

Ước tính giảm 30-60% effort nhờ automation (S0).

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
| — | (trống — ghi khi phát sinh) | — | — | — |

---

## Quy tắc an toàn

1. **Checkpoint trước mỗi edit lớn** — `/checkpoint` = git commit
2. **Không force push, không reset --hard** — CLAUDE.md rule
3. **Phase 2 rollback** — `git checkout [pre-restructure-commit]`
4. **Review checkpoint bắt buộc** — không skip
5. **1 session = 1 deliverable** — không để dở dang
6. **File > 500 dòng** — split trong cùng session
7. **Scope lock** — task ngoài scope → BACKLOG
8. **Source verify** — core features phải có Tier 1 source
