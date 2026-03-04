# Upgrade Plan v2 — Guide Claude v5.1 → v7.0

**Tạo:** 2026-03-04 | **Cập nhật:** 2026-03-04 — Rebuild với D9
**Maintainer:** Đỗ Quốc Đạt
**Trạng thái:** COMPLETE — v7.0 Released (2026-03-04)

---

## Tổng quan

Upgrade plan cho **9 quyết định** (D1-D9) qua brainstorm sessions 2026-03-04.
Chia thành **7 phases**, map vào **5 version releases**, thực thi qua **22 sessions**.

**Thay đổi so với plan v1:**
- Thêm D9: Claude Code cho Documentation/Technical Writing (Option D: Hybrid — Module 12 + Reference file)
- Thêm Phase 4B (Claude Code Documentation) — dedicated phase sau Phase 4
- Re-number sessions: S01-S14 giữ nguyên, S15-S22 mới
- Version scheme mới: v6.5 (Phase 4B) + v7.0 (Phase 5)
- Tổng sessions: 16 → 22 (+6)

**Workflow thực thi:**

```
Cowork (planning/review) → Claude Code (thực thi/edit) → Cowork (verify/next session)
```

Mỗi phase gồm nhiều sessions. Mỗi session có prompt riêng tại `_process/session-guide.md`.

---

## 9 Quyết Định

| # | Quyết định | Tóm tắt |
|---|-----------|---------|
| D1 | Trust labels + Recommendation tier | Allowlist icons, 3 tier: Must-have / Nice-to-have / Reference-only |
| D2 | Audience tag + Approved badge | `Audience: maintainer/end-user` + badge cho skill đã test |
| D3 | Skill-Recipe mapping table | Bảng mapping trong `skills-list.md`, sau thêm inline hints |
| D4 | Hybrid examples | Core = Documentation/Tech Writing, AMR trong callout boxes |
| D5 | Model decision flowchart | Mermaid flowchart + model hints trong ví dụ |
| D6 | Centralize specs (B-lite + A) | Tạo `reference/model-specs.md`, bỏ benchmark/pricing khỏi modules |
| D7 | Phased release process | Checklist → Dependency tags → Upgrade skill |
| D8 | Emoji/Icon policy (C+D hybrid) | Allowlist icons + Obsidian callouts, update CLAUDE.md |
| **D9** | **Claude Code cho Doc/Tech Writing** | **Module 12 (narrative) + `reference/claude-code-setup.md` (lookup)** |

---

## Dependency Map

```
Phase 0:  D8, D7-P1                              (không phụ thuộc)
Phase 1:  D6, D1                                  (phụ thuộc Phase 0 rules)
Phase 2:  D2 (phụ thuộc D1), D5 (phụ thuộc D6)
Phase 3:  D3                                      (phụ thuộc D2)
Phase 4:  D4                                      (phụ thuộc D3, D5, D6, D8)
Phase 4B: D9-A (ref file, phụ thuộc D8)
          D9-B (skeleton, phụ thuộc D6)
          D9-C (full content, phụ thuộc D9-A, D9-B, D1, D3)
          D9-D (refactor M10, phụ thuộc D9-C)
Phase 5:  D7-P2, D7-P3                            (phụ thuộc Phase 4 + 4B)
```

**Lưu ý:** Phase 4B không phụ thuộc Phase 4 (D4). Đặt tuần tự sau Phase 4 theo quyết định maintainer — có thể chạy song song nếu cần tăng tốc.

---

## Phase 0: Foundation Rules

**Version target:** v5.1-prep (chưa bump version)
**Branch:** `feat/upgrade-rules`
**Estimated effort:** 2-3 giờ

### Task 0.1 — Emoji/Icon Policy (D8)

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S01 |
| **Session** | S01 |
| **Files edit** | `.claude/CLAUDE.md`, `guide/00-overview.md` |

**Scope:**
- Thêm section `## Icon & Emoji Rules` vào `.claude/CLAUDE.md`
- Allowlist: ⚠️ ✅ ❌ 🔴 🟡 🟢 🔵
- Banned: mọi emoji khác
- Thay emoji trong prose bằng Obsidian callouts

**Acceptance criteria:**
- [x] `.claude/CLAUDE.md` có section Icon & Emoji Rules
- [ ] Global `~/.claude/CLAUDE.md` có tương tự (out of scope — manual update trên máy)
- [x] `guide/00-overview.md` conventions section cập nhật

### Task 0.2 — Release Checklist (D7-P1)

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S01 |
| **Session** | S01 (cùng session với 0.1) |
| **Files tạo mới** | `_process/release-checklist.md` |

**Acceptance criteria:**
- [x] File `_process/release-checklist.md` tồn tại
- [x] Checklist cover từ planning đến merge
- [x] Có section "Post-merge verification"

### Task 0.3 — Scan & Remove Emoji vi phạm hiện tại

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S02 |
| **Session** | S02 |
| **Files edit** | Toàn bộ `guide/`, `.claude/` |

**Scope:**
- Scan toàn bộ files tìm emoji ngoài allowlist
- Thay thế bằng Obsidian callouts hoặc text markers
- Giữ nguyên allowlist icons trong bảng status

**Acceptance criteria:**
- [x] Grep toàn bộ guide/ không còn emoji banned
- [x] Callouts render đúng trong Obsidian
- [x] `cross-ref-checker` pass

---

## Phase 1: Infrastructure

**Version target:** v5.1
**Branch:** `feat/centralize-specs`
**Estimated effort:** 3-5 giờ
**Depends on:** Phase 0

### Task 1.1 — Tạo model-specs.md (D6)

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S03 |
| **Session** | S03 |
| **Files tạo mới** | `guide/reference/model-specs.md` |
| **Files edit** | Toàn bộ module headers (00-11), `guide/06-tools-features.md` |

**Scope:**
- Tạo `reference/model-specs.md` chứa: model comparison, context window, feature-by-plan table, decision flowchart placeholder
- Chuyển mục 6.1 (plan table) và 6.2 (model details, benchmark, pricing) từ Module 06 sang specs file
- Giữ lại ở Module 06: nguyên tắc chọn (evergreen) + link đến specs
- Refactor ALL module headers: thay `Claude Opus 4.6 / Sonnet 4.6` bằng `Models: xem [specs](../reference/model-specs.md)`
- Bỏ benchmark scores → mô tả định tính + link source
- Bỏ pricing cụ thể → link `anthropic.com/pricing`

**Acceptance criteria:**
- [x] `reference/model-specs.md` tồn tại, có đủ sections (73 lines, 5 sections)
- [x] Module 06 không còn hardcode model specs
- [x] 12 module headers đã refactor
- [x] Grep `72.5%` và `91.3%` trả về 0 kết quả trong guide/
- [x] `cross-ref-checker` pass

### Task 1.2 — Trust labels + Recommendation tier (D1)

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S04 (note: [Approved PX] badge chưa thêm → gộp vào S05) |
| **Session** | S04 |
| **Files edit** | `guide/reference/skills-list.md` |

**Scope:**
- Thêm cột `Trust` vào mỗi bảng skill: `✅ Official`, `⚠️ Community`, `🔍 Unreviewed`
- Thêm section "Khuyến nghị cài đặt" với 3 tier: Must-have / Nice-to-have / Reference-only
- Giữ nguyên index đầy đủ

**Acceptance criteria:**
- [x] Mỗi skill có Trust label (49 entries)
- [x] Section "Khuyến nghị cài đặt" có 3 tier rõ ràng
- [x] `[Approved PX]` badge → done in S05 (13 occurrences)

---

## Phase 2: Structure

**Version target:** v5.1 (cùng release với Phase 1)
**Branch:** `feat/skill-structure` (hoặc continue branch Phase 1)
**Estimated effort:** 3-4 giờ
**Depends on:** Phase 1

### Task 2.1 — Audience tags + Approved badge (D2)

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S05 |
| **Session** | S05 |
| **Files edit** | `guide/reference/skills-list.md` |

**Scope:**
- Thêm cột `Audience`: `maintainer` / `end-user` / `both`
- Thêm badge `[Approved PX]` cho skill đã test tại Phenikaa-X
- Thêm cảnh báo về non-approved skills

**Acceptance criteria:**
- [x] Mỗi skill có Audience tag (37 occurrences: 6 maintainer, 30 end-user, 1 both)
- [x] Ít nhất 4-6 skills có badge `[Approved PX]` (13 occurrences)
- [x] Cảnh báo rõ ràng

### Task 2.2 — Model Decision Flowchart (D5)

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S05 + Cowork fill |
| **Session** | S05 (cùng session với 2.1) |
| **Files edit** | `guide/reference/model-specs.md` |

**Scope:**
- Tạo Mermaid flowchart trong model-specs.md
- Thêm 3-5 ví dụ thực tế với AMR context

**Acceptance criteria:**
- [x] Mermaid flowchart render đúng (1 flowchart TD block, 95 lines total)
- [x] 5 ví dụ thực tế kèm theo (SLAM, nav stack, ROS2, tra cứu, SOP)
- [ ] Link từ Module 06 đến flowchart hoạt động — defer: check khi Module 06 edit trong Phase 4

---

## Phase 3: Skill-Recipe Mapping

**Version target:** v5.2
**Branch:** `feat/skill-mapping`
**Estimated effort:** 2-3 giờ
**Depends on:** Phase 2

### Task 3.1 — Mapping table (D3)

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S06 |
| **Session** | S06 |
| **Files edit** | `guide/reference/skills-list.md` |
| **Files tham chiếu** | `guide/05-workflow-recipes.md`, `guide/07-template-library.md`, `guide/11-cowork-workflows.md` |

**Scope:**
- Thêm section "Skill-Recipe Mapping" vào skills-list.md
- Cover 14 recipes (Module 05) + 12 workflows (Module 11) + templates liên quan (Module 07)

**Acceptance criteria:**
- [x] Bảng mapping cover 26+ recipes/workflows (50 entries: 16 recipes + 22 templates + 12 workflows)
- [x] Chỉ khuyến nghị skill có badge `[Approved PX]` hoặc Official (39 entries verified)

---

## Phase 4: Content Evolution

**Version target:** v6.0
**Branch:** `feat/hybrid-examples`
**Estimated effort:** 8-12 giờ
**Depends on:** Phase 1, 2, 3

### Task 4.1 — Pilot: Rewrite 2 modules thử nghiệm

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S07, S08 |
| **Session** | S07, S08 |
| **Files edit** | `guide/05-workflow-recipes.md` (2-3 recipes đầu), `guide/11-cowork-workflows.md` (2-3 workflows đầu) |

**Scope:**
- Rewrite ví dụ chính sang Documentation/Technical Writing context
- Thêm AMR callout box, model hint, skill hint
- Đánh giá effort thực tế → go/no-go cho full rewrite

**Acceptance criteria:**
- [x] 6 recipes/workflows đã rewrite (M05: 3 recipes, M11: 3 workflows)
- [x] Mỗi recipe có: doc example + AMR callout + model hint
- [x] Callouts render đúng trong Obsidian
- [x] Go/no-go decision: **GO** — Pilot thành công, tiến hành full rewrite S09-S14

**Post-pilot fix:** Anchor `#chon-model` → `#chọn-model` (6 links, Cowork fix — root cause: heading rename)

### Task 4.2 — Full rewrite (nếu pilot OK)

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S09→S12 (4 sessions, 2 buffer freed) |
| **Session** | S09 → S12 (4 sessions thực tế, vs 6 ước tính) |
| **Files edit** | Module 03, 05, 07, 08, 11 |

**Scope:**
- Áp dụng pattern từ pilot cho toàn bộ recipes/workflows còn lại
- Mỗi module rewrite xong → `/review-module` verify

**Acceptance criteria:**
- [x] Toàn bộ 5 modules đã rewrite (M03, M05, M07, M08, M11)
- [x] `/review-module` pass — cross-module review done S12
- [x] 0 stale anchors, 0 invalid skill refs, code blocks fixed

**Actual counts:** M05: 16 AMR callouts · M11: 12 · M07: 22 · M03: 7 · M08: 5

---

## Phase 4B: Claude Code Documentation

**Version target:** v6.5
**Branch:** `feat/claude-code-docs`
**Estimated effort:** 11-15 giờ
**Depends on:** Phase 1 (D6 — model-specs.md), Phase 3 (D1 — trust labels, D3 — mapping)
**Không phụ thuộc:** Phase 4 (D4). Đặt tuần tự sau Phase 4 theo quyết định maintainer.

**Nguồn chính thức:**
- [Best Practices for Claude Code](https://code.claude.com/docs/en/best-practices)
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)
- [Claude Code Settings](https://code.claude.com/docs/en/settings)
- [How Mintlify uses Claude Code as a technical writing assistant](https://www.mintlify.com/blog/how-mintlify-uses-claude-code-as-a-technical-writing-assistant)

### Task 4B.1 — Tạo reference/claude-code-setup.md (D9-A)

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S15 |
| **Session** | S15 |
| **Files tạo mới** | `guide/reference/claude-code-setup.md` |

**Scope:**
Reference file dạng cheat sheet — config templates, commands, settings. Copy-paste ready. Gồm:

1. **Quick Setup Checklist** — 8 bước từ cài đặt đến first session
2. **CLAUDE.md Reference** — Include vs Exclude guidance (từ official), template cho doc project, CLAUDE.local.md, .claude/rules/
3. **Settings Reference** — `settings.json` template cho documentation users, `settings.local.json`, env vars quan trọng (ANTHROPIC_MODEL, CLAUDE_CODE_EFFORT_LEVEL)
4. **Essential Commands Cheat Sheet** — Bảng: command → khi nào → ví dụ doc context. Cover: /clear, /rewind, /compact, /rename, /init, /permissions, /status, /mcp, /plugin, --continue, --resume, claude -p
5. **Permission Templates** — allow/deny patterns cho doc project (cho phép Read guide/**, deny .env, cho phép git commands)
6. **Hooks Templates** — SessionStart, Notification, PreToolUse patterns cho doc workflow
7. **External Links** — Curated links đến official docs (stable URLs)

**Acceptance criteria:**
- [x] File tồn tại (237 lines, 7390 bytes)
- [x] 6 sections (Workflow-first: Quick Setup → Workflow → Review → Release → Config → Quick Ref)
- [x] Tuân thủ emoji/icon policy (0 banned emoji)
- [ ] Source markers `[Nguồn: Claude Code Docs]` — not verified, defer
- [x] 0 hardcoded version numbers

### Task 4B.2 — Tạo Module 12 skeleton (D9-B)

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S16 |
| **Session** | S16 |
| **Files tạo mới** | `guide/12-claude-code-documentation.md` |

**Scope:**
Tạo file Module 12 với 15 section headers + intro paragraph (2-5 dòng) mỗi section + cross-links placeholder. Chưa viết full content. Cấu trúc:

```
12.1  Claude Code là gì — cho non-coders
12.2  Cài đặt & First Session
12.3  Cấu hình 4 lớp (User → Project → Local → Managed)
12.4  Plan Mode — Explore → Plan → Execute → Commit
12.5  Slash Commands & Custom Commands
12.6  Skills cho Documentation
12.7  Subagents cho Review & Research
12.8  Session Management
12.9  Git Integration cho Documentation
12.10 Verification & Quality Assurance
12.11 Permissions & Safety
12.12 Token Optimization & Cost
12.13 Batch & Automation
12.14 Plugins & MCP cho Documentation
12.15 External Resources & Further Reading
```

**Acceptance criteria:**
- [x] File tồn tại với 15 section headers (159 lines)
- [x] Mỗi section có intro paragraph mô tả scope
- [x] Cross-link placeholders đến: model-specs.md, skills-list.md, claude-code-setup.md (4 anchors verified)
- [x] Module header tuân thủ format chuẩn
- [x] Tuân thủ emoji/icon policy (0 banned emoji)

**Post-fix:** claude-code-setup.md headings renamed (Option A) — số prefix bỏ, thêm Essential Commands + Permission Templates. Checkpoint committed.

### Task 4B.3 — Viết Module 12 content phần 1 (D9-C part 1)

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S17 |
| **Session** | S17 |
| **Files edit** | `guide/12-claude-code-documentation.md` (sections 12.1-12.8) |
| **Files tham chiếu** | `guide/reference/claude-code-setup.md`, `guide/reference/model-specs.md`, `guide/reference/skills-list.md` |

**Scope:**
Viết full content cho 8 sections đầu. Focus vào documentation/technical writing context, adapt từ official best practices:

- **12.1:** CC là gì, khác Cowork thế nào, khi nào dùng CC vs Cowork (bảng so sánh)
- **12.2:** Cài đặt, `claude --version`, first session, `/init`
- **12.3:** 4-scope system (User/Project/Local/Managed), template CLAUDE.md cho doc project, Include/Exclude (adapt từ official), `.claude/rules/` cho path-specific rules
- **12.4:** Plan Mode 4-phase workflow (Explore → Plan → Execute → Commit), Ctrl+G, khi nào skip plan. Ví dụ: lập kế hoạch rewrite 1 module documentation
- **12.5:** Slash commands (tạo custom commands cho doc project), ví dụ thực tế từ Guide Claude project (/start, /checkpoint, /validate-doc)
- **12.6:** Skills ecosystem — invocable vs reference, tạo custom skill, `disable-model-invocation`, context cost. Ví dụ: doc-standard-enforcer skill
- **12.7:** Subagents — Writer/Reviewer pattern cho documentation, `.claude/agents/` template, khi nào dùng subagent vs main session. Ví dụ: subagent review SOP
- **12.8:** Session management — /clear, /rewind, /rename, --continue, --resume, /compact. Failure patterns: kitchen sink session, over-correction

**Model:** Sonnet cho hầu hết. Switch Opus cho 12.7 (subagent design cần suy luận sâu).

**Acceptance criteria:**
- [x] 8 sections có full content (12.1-12.8)
- [x] Mỗi section có ít nhất 1 ví dụ thực tế documentation context
- [x] Cross-links đến reference files hoạt động
- [x] Source markers cho facts từ official docs
- [x] `/validate-doc 12` pass

### Task 4B.4 — Viết Module 12 content phần 2 (D9-C part 2)

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S18 |
| **Session** | S18 |
| **Files edit** | `guide/12-claude-code-documentation.md` (sections 12.9-12.15) |

**Scope:**
Viết full content cho 7 sections còn lại:

- **12.9:** Git workflow — branch naming, commit conventions cho doc project, pre-commit hooks (validate heading, check links), SessionStart hook
- **12.10:** Verification — self-verification patterns (adapt từ official "highest-leverage thing"), /validate-doc, cross-ref-checker, review checklists
- **12.11:** Permissions — /permissions, allowedTools patterns cho doc project, sandbox mode, deny sensitive files
- **12.12:** Token optimization — model selection (link flowchart), effort level, /compact, offset/limit, status line, slash commands vs prompt dài
- **12.13:** Batch & Automation — `claude -p` cho doc tasks, pipe in/out, CI integration (lint docs in PR), fan-out pattern cho multi-file operations
- **12.14:** Plugins & MCP — /plugin marketplace, relevant plugins (GitHub, Notion), `claude mcp add`, MCP cho documentation (Obsidian, Google Drive)
- **12.15:** External Resources — curated links đến official docs (stable), community resources (Mintlify blog, ClaudeLog), link đến Module 10 cho Cowork comparison

**Model:** Sonnet

**Acceptance criteria:**
- [x] 7 sections có full content
- [x] Section 12.15 có ít nhất 10 curated links với mô tả 1 dòng
- [x] `/validate-doc 12` pass
- [x] `/review-module 12` pass (deep review toàn module)

### Task 4B.5 — Refactor Module 10 + Update cross-refs (D9-D)

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S19 |
| **Session** | S19 |
| **Files edit** | Nhiều files (xem danh sách) |

**Scope:**

**A. Refactor Module 10 (10.13):**
- Giữ lại tại 10.13: 1 intro paragraph (~5 dòng) + redirect rõ ràng
- Nội dung giữ: "Claude Code (CC) là CLI agent... Section này giới thiệu ngắn. Hướng dẫn đầy đủ xem [Module 12: Claude Code cho Documentation](12-claude-code-documentation.md)."
- Xóa: toàn bộ 10.13.2 → 10.13.5 (đã chuyển sang Module 12)
- Giữ nguyên: 10.12 (bảng so sánh) — update thêm cột/link nếu cần

**B. Update Module 00 (overview):**
- Bảng modules: thêm row Module 12
- Learning Paths: thêm Module 12 vào Path C (Power User)
- Tiêu đề "12 Modules" → "13 Modules"

**C. Update cross-references:**
- `guide/04-context-management.md` dòng 394: "Module 10 (mục 10.13)" → "Module 12"
- `.claude/CLAUDE.md`: Folder structure (thêm Module 12), Module status table (thêm row)
- `project-state.md`: Update module count, structure

**D. Update SETUP.md nếu cần** (nhắc maintainer check)

**Acceptance criteria:**
- [x] Module 10.13 chỉ còn intro + redirect (không còn subsections chi tiết)
- [x] Module 00 bảng có 13 modules
- [x] Learning Path C có Module 12
- [x] Grep "10.13" trong guide/ chỉ trả về kết quả trong Module 10 (redirect)
- [x] `cross-ref-checker` pass toàn bộ
- [x] `.claude/CLAUDE.md` folder structure chính xác

---

## Phase 5: Process Maturity

**Version target:** v7.0
**Branch:** `feat/process-maturity`
**Estimated effort:** 5-7 giờ
**Depends on:** Phase 4 + Phase 4B

### Task 5.1 — Dependency tags (D7-P2)

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S20 |
| **Session** | S20 |
| **Files edit** | Toàn bộ module headers (00-12) — **13 modules** |

**Scope:**
- Thêm YAML-like metadata vào mỗi module header:
  ```
  depends-on: [04-context-management, reference/model-specs]
  impacts: [07-template-library]
  ```
- Tạo dependency graph tổng thể (Mermaid) — bao gồm Module 12

**Acceptance criteria:**
- [x] 13 modules có dependency metadata
- [x] Dependency graph chính xác (bao gồm Module 12)
- [x] Module 12 dependencies: reference/model-specs, reference/skills-list, reference/claude-code-setup

### Task 5.2 — Upgrade skill (D7-P3)

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S21 |
| **Session** | S21 |
| **Files tạo mới** | `.claude/skills/upgrade-guide/SKILL.md` |

**Scope:**
- Tạo skill tự động hóa: scan dependencies, check volatile data, generate diff report
- Input: module number hoặc "all" — cover **13 modules + 3 reference files**
- Output: report + suggested edits

**Acceptance criteria:**
- [x] Skill hoạt động khi gọi `/upgrade-guide`
- [x] Output bao gồm: stale data, broken refs, dependency warnings
- [x] Covers Module 12 và reference/claude-code-setup.md

### Task 5.3 — Final Consistency Check ← MỚI

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S22 |
| **Session** | S22 |
| **Files check** | Toàn bộ project |

**Scope:**
- Cross-ref check toàn bộ 13 modules + 3 reference files
- Verify terminology consistency: "Claude Code" vs "CC" (standardize)
- Verify icon/emoji policy compliance toàn bộ
- Verify source markers `[Nguồn: ...]` có đầy đủ
- Verify `[Cập nhật MM/YYYY]` markers trên volatile content
- Final review Module 12 + reference file (dùng subagent hoặc Opus)

**Acceptance criteria:**
- [x] `cross-ref-checker` pass 100%
- [x] Grep emoji banned = 0 kết quả
- [x] Terminology nhất quán (report 0 inconsistencies)
- [x] Tất cả volatile sections có `[Cập nhật MM/YYYY]`
- [x] `/review-module 12` pass (final)

---

## Version Release Summary

| Version | Phases | Key deliverables | Sessions | Milestone |
|---------|--------|-----------------|----------|-----------|
| v5.1 | 0, 1, 2 | Rules, specs file, trust labels, flowchart | S01→S05 | Infrastructure ổn định |
| v5.2 | 3 | Skill-recipe mapping | S06 | Skills ecosystem hoàn chỉnh |
| v6.0 | 4 | Hybrid examples (pilot + full) | S07→S14 | Content evolution hoàn tất |
| **v6.5** | **4B** | **Module 12 + reference file + refactor Module 10** | **S15→S19** | **Claude Code coverage** |
| **v7.0** | **5** | **Dependency tags, upgrade skill, final check** | **S20→S22** | **Project maturity** |

---

## Session → Phase → Version Quick Reference

| Session | Phase | Task | Decision |
|---------|-------|------|----------|
| S01 ✅ | 0 | Emoji/Icon Rules + Release Checklist | D8, D7-P1 |
| S02 ✅ | 0 | Scan & Remove Emoji | D8 |
| S03 ✅ | 1 | Centralize Model Specs | D6 |
| S04 ✅ | 1 | Trust Labels | D1 |
| S05 ✅ | 2 | Audience Tags + [Approved PX] + Model Flowchart | D2, D5 |
| S06 ✅ | 3 | Skill-Recipe Mapping | D3 |
| S07 ✅ | 4 | Pilot Hybrid — Module 05 | D4 |
| S08 ✅ | 4 | Pilot Hybrid — Module 11 | D4 |
| S09 ✅ | 4 | Full Rewrite — M05 recipes 5.4-5.11 | D4 |
| S10 ✅ | 4 | Full Rewrite — M05 recipes 5.12+ + M11 full (11.4-12) | D4 |
| S11 ✅ | 4 | Full Rewrite — M03 + M08 | D4 |
| S12 ✅ | 4 | Full Rewrite — M07 + cross-module review | D4 |
| S13-S14 | 4 | Buffer — freed (Phase 4 done in 4 sessions vs 6 est.) | — |
| S15 ✅ | 4B | Reference file: claude-code-setup.md | D9-A |
| S16 ✅ | 4B | Module 12 skeleton | D9-B |
| S17 ✅ | 4B | Module 12 content (12.1-12.8) | D9-C |
| S18 ✅ | 4B | Module 12 content (12.9-12.15) | D9-C |
| S19 ✅ | 4B | Refactor Module 10 + Update cross-refs | D9-D |
| S20 ✅ | 5 | Dependency tags (13 modules) | D7-P2 |
| S21 ✅ | 5 | Upgrade skill | D7-P3 |
| S22 ✅ | 5 | Final consistency check | — |

---

## Tracking

Cập nhật status (`[ ]` → `[x]`) sau mỗi session thành công.
Cập nhật file này từ Cowork sau khi verify kết quả Claude Code.

**Last updated:** 2026-03-04 — ALL 22 SESSIONS COMPLETE — v7.0
**S01 done** (Task 0.1, 0.2)
**S02 done** (Task 0.3 — emoji scan clean)
**S03 done** (Task 1.1 — model-specs.md created, headers refactored)
**S04 done** (Task 1.2 — trust labels + 3 tier. Note: [Approved PX] badge deferred → S05)
**S05 done** (Task 2.1 ✅ D2 — audience tags 37 occurrences, [Approved PX] 13 occurrences. Task 2.2 ✅ D5 — Mermaid flowchart + 5 ví dụ AMR, Cowork fill)
**S06 done** (Task 3.1 ✅ D3 — Skill-Recipe Mapping: 50 entries, 39 có [Approved PX]/Official badge)
**S07 done** (Task 4.1 partial — M05: 3 recipes, AMR callouts + model hints. Anchor fix applied.)
**S08 done** (Task 4.1 complete — M11: 3 workflows, AMR callouts + model hints. Go/no-go: GO for S09-S14.)
**S09 done** (Task 4.2 partial — M05 recipes 5.4-5.11: 8 recipes rewritten. 11 AMR callouts total, 13 model hints. validate-doc 05 ✅)
**S10 done** (Task 4.2 — M05 5.12+ complete (16 callouts, 18 hints) + M11 full 11.4-12 (12 callouts, 13 hints). 2 sessions freed by efficiency.)
**S11 done** (Task 4.2 — M03: 7 AMR callouts, 15 model hints. M08: 5 AMR callouts, 5 model hints. 0 stale anchors cả 2.)
**S12 done** (Task 4.2 complete — M07: 22 callouts, 26 hints. Cross-module review: code blocks fixed M03/M08, cross-refs M05/M07, skill ref M11. 0 stale anchors toàn Phase 4.) → **PHASE 4 COMPLETE**
**S15 done** (Task 4B.1 ✅ D9-A — claude-code-setup.md created: 237 lines, 6 sections, Workflow-first format. 0 banned emoji, 0 hardcoded versions.)
**S16 done** (Task 4B.2 ✅ D9-B — M12 skeleton: 15 sections, 159 lines, 0 banned emoji. Post-fix: claude-code-setup.md headings renamed Option A, 4 anchors verified, 272 lines final.)
**S17 done** (Task 4B.3 ✅ D9-C part 1 — M12 sections 12.1-12.8: full content, ví dụ documentation context, cross-links hoạt động, source markers đầy đủ. `/validate-doc 12` pass.)
**S18 done** (Task 4B.4 ✅ D9-C part 2 — M12 sections 12.9-12.15: full content, 12.15 có curated links. `/review-module 12` pass. M12 final: 1190 lines, 26 sections, 61 subsections.) → **PHASE 4B COMPLETE**
**S19 done** (Task 4B.5 ✅ D9-D — M10.13 refactored → intro + redirect. M00 updated: 13 modules, Learning Path C. Cross-refs updated M04. `.claude/CLAUDE.md` updated. `cross-ref-checker` pass.)
**S20 done** (Task 5.1 ✅ D7-P2 — Dependency tags: 13 modules, dependency metadata + Mermaid graph. M12 dependencies: model-specs, skills-list, claude-code-setup.)
**S21 done** (Task 5.2 ✅ D7-P3 — Upgrade skill: `.claude/skills/upgrade-guide/SKILL.md` created. `/upgrade-guide` operational. Covers 13 modules + 3 reference files.)
**S22 done** (Task 5.3 ✅ — Final consistency check: cross-ref 100%, 0 banned emoji, terminology consistent, volatile sections tagged. `/review-module 12` final pass.) → **PHASE 5 COMPLETE — v7.0 RELEASED**
