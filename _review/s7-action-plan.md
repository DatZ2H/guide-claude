# S7 — Synthesis & Action Plan
**Date:** 2026-03-03 | **Scope:** Full project audit synthesis (S1–S6)

---

## Overview

| Metric | Count |
|--------|------:|
| Sessions | 6 |
| Total issues (S1–S6) | 199 |
| Critical (block publishing) | 9 |
| High (fix this sprint) | 17 |
| Medium (fix when touching module) | 19 |
| Low / Backlog | 154 (118 code blocks + 36 others) |
| Modules with health ≥ 8/10 | 4 (07, 09, 01, 03) |
| Modules with health ≤ 6/10 | 2 (06, _scaffold) |

---

## Task 1: Issue Classification

### Bucket 1: CRITICAL — Fix ngay (block publishing)

Issues này là **factual errors**, **broken references**, hoặc **contradictions** gây confusion nghiêm trọng.

| ID | Source | File | Issue | Why Critical |
|----|--------|------|-------|:------------|
| C-01 | S2#5 | `guide/02` L457-464 | Memory KHÔNG hoạt động trong Projects — bảng "project memory (riêng)" không tồn tại | Factual error — guides users to expect non-existent feature |
| C-02 | S2#9 | `guide/04` L27 | Sonnet 4.5 KHÔNG có 1M beta context | Factual error — wrong spec |
| C-03 | S4#10 | `guide/10` L1139 | Sonnet 4.5 KHÔNG có 1M beta (lặp lại C-02) | Factual error — duplicated in second module |
| C-04 | S3#3 | `guide/06` L63 | "Adaptive Thinking (trước đây: Extended Thinking)" — SAI. Là 2 concepts riêng biệt | Factual error, gây confusion toàn bộ §6.3 |
| C-05 | S3#4 | `guide/06` L25 | Memory row: "Free: Không" — outdated từ Q1/2026 | Outdated causing wrong user decisions |
| C-06 | S2#10, C4 | `guide/04` L590 | Link đến `_memory/session-state.md` — file đã BỊ XÓA | Broken reference |
| C-07 | S6-3 | `.claude/CLAUDE.md` | Git branch `main` — thực tế là `master` | Broken infra guidance |
| C-08 | S6-2 | `.claude/CLAUDE.md` | Skills table: 3/9 listed; 0/5 commands documented | Broken AI context for Claude |
| C-09 | S6-1 | `_scaffold/memory-starter/` | Folder CÒN TỒN TẠI với "3-tier architecture" — template tạo stale projects | Broken scaffolding |

---

### Bucket 2: HIGH — Fix trong sprint này

| ID | Source | File | Issue | Why High |
|----|--------|------|-------|:---------|
| H-01 | S3#5 | `guide/06` L16-31 | Thiếu Claude Max plan tier ($100/$200) | Outdated — affects user plan decisions |
| H-02 | S3#6 | `guide/06` L63 vs L77 | Contradiction: section title "Adaptive" vs UI instruction "Extended thinking" | Internal contradiction |
| H-03 | S3#8 | `guide/08` L134 | "Connector tốn tokens ngay cả khi không dùng" — **explicitly false** | False guidance |
| H-04 | S3#9 | `guide/08` L359 | `\|-- Memory → Bật Memory (Pro)` — outdated | Misleads user on plan requirement |
| H-05 | S5-C1 | 00, 03, 05, 06, 08 | "Adaptive Thinking" dùng sai làm UI feature name (6 modules) | Systemic terminology confusion |
| H-06 | S5-C3 | 01, 06, 08 | Memory "(Pro)" / "trừ khi bật" outdated (6 mentions, 3 modules) | Outdated — Q1/2026 change |
| H-07 | S4#13 | `guide/10` L1271-1284 | `.claude/commands/` presented as current — thực tế LEGACY | Outdated guidance for new users |
| H-08 | S4#15 | `ref/config-architecture` L19 | Global CLAUDE.md mapped sai surface (Cowork UI vs CC file) | Misleading for new project setup |
| H-09 | S4#18 | `ref/skills-list` L36-38 | `doc-coauthoring` skill có thể không tồn tại trong repo | Potential broken link |
| H-10 | S5-N1 | `_scaffold/memory-starter/decisions-log.md` | "3-tier architecture" trong user template | Propagates stale terminology |
| H-11 | S5-N2 | `ref/config-architecture` L291-293 | `memory-starter/` trong scaffold tree — không có deprecation note | Propagates deprecated pattern |
| H-12 | S5-N4 | `.claude/CLAUDE.md` | `/simplify` listed nhưng là global built-in, không phải project skill | Misleading AI context |
| H-13 | S6-4 | `.claude/SETUP.md` | Thiếu `doc-standard-enforcer` + 0 commands documented | Incomplete maintainer guide |
| H-14 | S6-5 | `_scaffold/skill-templates/SKILL-template.md.bak` | Stray `.bak` không nên commit | Noise in repo |
| H-15 | S6-6 | `_scaffold/CLAUDE-template.md` | `.claude/` structure thiếu `commands/`, `SETUP.md`, `settings.json` | New project scaffold broken |
| H-16 | S4#11 | `guide/10` L1006 | "Context editing" — thuật ngữ đúng là "compaction" | Misleading technical term |
| H-17 | S1-P1 | git | `_memory/` deletion staged nhưng chưa commit | Dirty git history |

---

### Bucket 3: MEDIUM — Fix khi touch module đó

| ID | Source | File | Issue |
|----|--------|------|-------|
| M-01 | S2#1 | `guide/00` L129 | Changelog thiếu entry 3-tier → 2-tier transition |
| M-02 | S2#2 | `guide/00` L214 | Adaptive Thinking vs Extended Thinking trong changelog mô tả chưa chính xác |
| M-03 | S2#4 | `guide/01` L159 | Memory phrasing "trừ khi bật" ngụ ý tắt mặc định |
| M-04 | S2#7 | `guide/02` L512 | MCP connector token cost misleading |
| M-05 | S3#1 | `guide/05` L126, 159-161 | "Adaptive Thinking" terminology trong UI context |
| M-06 | S3#2 | `guide/05` L434 | Connector token cost (cross-module pattern C2) |
| M-07 | S4#4 | `guide/10` L374 | Skill auto-activation unreliable — thiếu caveat |
| M-08 | S4#7 | `guide/10` L435 | claude.ai custom skills install path chưa verify |
| M-09 | S4#12 | `guide/10` L1006 | "72.5% token reduction" không có nguồn |
| M-10 | S4#21 | `ref/skills-list` L56 | "11 plugins" → có thể > 11 |
| M-11 | S5-N3 | `guide/02` L111 | Root-relative path `guide/reference/...` thay vì relative |
| M-12 | S5-N5 | `.claude/CLAUDE.md` | VERSION link rule scope unclear — chỉ áp dụng mod00? |
| M-13 | S5-N7 | `guide/04` L510 | "Custom Instructions" → "Project Instructions" |
| M-14 | S5-A3 | `guide/00` L129 | No changelog entry for 3-tier → 2-tier (overlaps M-01) |
| M-15 | S4#14 | `.claude/CLAUDE.md` | SessionStart hook matcher `""` vs official `"startup"` |
| M-16 | S6-7 | `_scaffold/SKILL-template.md` L104 | `## Skills` → `## Available skills` (convention mismatch) |
| M-17 | S5-N6 | `guide/10` L1405 | "v4.1" hardcoded trong example — sẽ stale sau version bump |
| M-18 | S4#16 | `ref/config-architecture` L29-31 | Skills/Plugins label `[Cowork]` → `[Cowork/CC]` |
| M-19 | S2#11 | `guide/04` L515-516 | Duplicate `.claude/` line trong §4.9 |

---

### Bucket 4: LOW — Backlog

| Category | Count | Details |
|----------|:-----:|---------|
| Unlabeled code blocks | 118 | Toàn bộ guide/ — không block render, chỉ violate standards |
| Missing VERSION links (mod 01–10) | 11 | CLAUDE.md rule scope unclear — defer đến M-12 |
| Prefill "deprecated" → "removed" (guide/00 L215) | 1 | Minor accuracy fix, low visibility |
| Code execution default Off — verify (guide/02 L60) | 1 | Verify UI trực tiếp khi revisiting mod02 |
| Source name "Adaptive Thinking Tips" (guide/08) | 1 | Fix cùng Sprint 2 pass |
| Skill overhead "~100 tokens" unsourced (guide/10) | 1 | Add `[ước lượng]` |
| Partner skills name-drop (guide/10) | 1 | Lower specificity claim |
| Community plugin install via GitHub (guide/10) | 1 | Add `[Cần xác minh]` |
| SessionStart hook matcher `""` vs `"startup"` (guide/10) | 1 | Match official docs format |
| SessionStart hook only on CC, not Cowork (guide/10) | 1 | Add note |
| skills-list: install path + systematic-debugging | 2 | Verify against skillhub.club |
| Anthropic plugin count > 11 (skills-list) | 1 | Update to "11+" |
| Hardcoded "v4.1" in example (guide/10 L1405) | 1 | Low — add note in version bump checklist |
| File cleanup (worktrees, decision-matrix.html, .bak) | 3 | Manual cleanup |
| CLAUDE.md + README minor structure updates | 2 | Add `_review/`, update tree |
| Cowork model: Max → Opus default (guide/10) | 1 | Add "(Max plan: Opus default)" note |

---

## Task 2: Module Health Scorecard

| Module | Structural | Accuracy | Consistency | Overall | Priority |
|--------|:----------:|:--------:|:-----------:|:-------:|:--------:|
| 00 overview | 8/10 | 7/10 | 8/10 | **7.7** | 🟡 |
| 01 quick-start | 7/10 | 8/10 | 9/10 | **8.0** | 🟡 |
| 02 setup | 8/10 | 5/10 | 8/10 | **7.0** | 🔴 |
| 03 prompt-eng | 7/10 | 9/10 | 8/10 | **8.0** | 🟢 |
| 04 context | 7/10 | 6/10 | 7/10 | **6.7** | 🔴 |
| 05 workflow | 6/10 | 8/10 | 8/10 | **7.3** | 🟡 |
| 06 tools | 9/10 | 4/10 | 5/10 | **6.0** | 🔴 |
| 07 templates | 8/10 | 9/10 | 9/10 | **8.7** | 🟢 |
| 08 mistakes | 7/10 | 7/10 | 7/10 | **7.0** | 🟡 |
| 09 evaluation | 7/10 | 9/10 | 9/10 | **8.3** | 🟢 |
| 10 cowork | 6/10 | 7/10 | 7/10 | **6.7** | 🟡 |
| ref/config-arch | 6/10 | 7/10 | 7/10 | **6.7** | 🟡 |
| ref/skills-list | 9/10 | 5/10 | 7/10 | **7.0** | 🟡 |
| _scaffold/ | N/A | 6/10 | 6/10 | **6.0** | 🔴 |

**Scoring notes:**
- Structural: code block tags (40%), VERSION link (20%), file size (20%), heading hierarchy (20%)
- Accuracy: Type A errors weighted ×3, Type B ×2, Type C ×1.5, Type E ×1
- Consistency: terminology, cross-refs, CLAUDE.md compliance
- Priority: 🔴 = có Critical/HIGH issue → fix this sprint | 🟡 = Medium issues | 🟢 = chỉ LOW/backlog

---

## Task 3: Root Cause Analysis

### RC-1: "Adaptive Thinking" naming error propagated globally
**Affected:** `guide/00` (L214), `guide/03` (L298), `guide/05` (L126, 159-161), `guide/06` (L63, 93, 282, 292), `guide/08` (L126, 144, 148) — **6 modules, 10+ locations**

**Root cause:** Khi viết guide (v3.0), thuật ngữ API `thinking: {type: "adaptive"}` được dùng nhầm như tên UI feature. UI toggle thực tế tên là "Extended thinking". Module 06 contradicts itself (§6.3 title vs §6.3 UI instruction), chứng tỏ lỗi được copy mà không cross-check. Không có naming standard nào được enforce lúc viết.

**Fix strategy:** Global find-replace có kiểm soát. Rule: "Extended thinking" (UI toggle) vs "Adaptive Thinking" (API feature — explicit qualifier). Module 06 ưu tiên đầu tiên (worst case: H-02, C-04).

---

### RC-2: `_memory/` deprecation (Phase 5) cleanup chưa hoàn tất
**Affected:** `guide/04` L590 (stale active link), `ref/config-architecture.md` L291-293 (no deprecation note), `_scaffold/memory-starter/` (exists, refs "3-tier"), `_scaffold/memory-starter/decisions-log.md` L5

**Root cause:** Phase 5 xóa `_memory/` folder và đánh deprecated ở đúng chỗ (mod04 §4.3, mod10 §10.8.1), nhưng bỏ sót: (1) một **active instruction link** trong mod04:590, (2) scaffold tree trong reference doc, (3) toàn bộ `_scaffold/memory-starter/` trên disk. Cleanup thiếu checklist post-deprecation.

**Fix strategy:** `git rm -r _scaffold/memory-starter/` + commit (Sprint 1); sửa mod04:590 (Sprint 1); deprecation note trong config-architecture.md (Sprint 2).

---

### RC-3: Memory availability information outdated (Q1/2026 rollout)
**Affected:** `guide/01` L159, `guide/06` L25, `guide/08` L359, `guide/02` L457-464

**Root cause:** Guide viết trước khi Memory became available on Free plan (Q1/2026). Không có "feature change tracking" process — khi Anthropic rolls out feature, guide không được update. Module 02 nghiêm trọng hơn: không chỉ outdated mà còn claim feature không tồn tại (project-scoped memory synthesis).

**Fix strategy:** Module 06 bảng (quick fix H-06 kết hợp với H-01); Module 02 §2.4 rewrite (C-01 — Sprint 2); Module 08 + 01 targeted fixes.

---

### RC-4: CLAUDE.md bản thân không được maintain khi project phát triển
**Affected:** `.claude/CLAUDE.md` (skills table, commands missing, branch wrong, folder structure), `.claude/SETUP.md`

**Root cause:** Infrastructure grow organically (thêm 2 skills → 5 skills, thêm 5 commands) nhưng CLAUDE.md không được update đồng thời. Git branch ghi sai (main vs master). CLAUDE.md là SSOT cho Claude's context — khi nó outdated, Claude không biết toàn bộ toolset và guidance sai.

**Fix strategy:** CLAUDE.md comprehensive update trong Sprint 1 (C-07, C-08, H-12) — highest priority vì ảnh hưởng mọi session sau.

---

### RC-5: Sonnet 4.5 / 1M beta spec error duplicated
**Affected:** `guide/04` L27, `guide/10` L1139

**Root cause:** Token spec table ban đầu viết sai (Sonnet 4.5 + 1M beta), sau đó được copy nguyên sang Module 10 khi tạo comparison table, không qua verification step. Single-source error, duplicated silently.

**Fix strategy:** 2 targeted line edits — 10 phút. Highest ROI per-effort ratio trong toàn bộ audit.

---

## Task 4: Recommended Fix Order

### Sprint 1 — Tuần này: Critical + Quick Wins
*Mỗi task dưới 30 phút. Tổng: ~75 min, 3 commits.*

| # | File(s) | Action | Effort | Issues fixed |
|---|---------|--------|:------:|:------------|
| 1 | `.claude/CLAUDE.md` | (a) Fix branch `main` → `master`; (b) Update skills table: thêm 3 project skills, clarify /simplify là global; (c) Thêm Commands section listing 5 commands; (d) Update folder structure | 25 min | C-07, C-08, H-12 |
| 2 | `guide/04` L27 + `guide/10` L1139 | Xóa "Sonnet 4.5" khỏi danh sách 1M beta trong cả 2 files | 10 min | C-02, C-03 |
| 3 | `guide/04` L590 | Sửa `xem _memory/session-state.md` → `xem project-state.md` hoặc `.claude/CLAUDE.md` | 5 min | C-06 |
| 4 | `guide/04` L515-516 | Xóa 1 dòng `.claude/` duplicate | 2 min | M-19 |
| 5 | git | Commit pending `_memory/` deletion: `git add _memory/ && git commit -m "Xóa _memory/ (Phase 5 cleanup)"` | 5 min | H-17 |
| 6 | git | `git rm -r _scaffold/memory-starter/` + commit | 5 min | C-09, H-10 |
| 7 | git | `git rm "_scaffold/skill-templates/SKILL-template.md.bak"` + commit | 2 min | H-14 |
| 8 | `.claude/SETUP.md` | Thêm `doc-standard-enforcer` vào skills table; thêm Commands section listing 5 commands + triggers | 20 min | H-13 |

**Issues closed by Sprint 1: 9 Critical + 3 High + 1 Medium = 13 total**

---

### Sprint 2 — Tuần sau: High Priority
*Yêu cầu read + rewrite section. 1–2 sessions mỗi task. Tổng: ~235 min.*

| # | File(s) | Action | Effort | Issues fixed |
|---|---------|--------|:------:|:------------|
| 1 | `guide/06` §6.3 | Rewrite: đổi title → "Extended Thinking"; bỏ "(trước đây: Adaptive Thinking)"; viết phân biệt ET (UI toggle) vs AT (API concept); fix bảng L292 | 30 min | C-04, H-02, H-05 (partial) |
| 2 | `guide/06` §6.1 bảng | (a) Memory Free → Có; (b) thêm Max plan column ($100/$200); (c) review rows khác | 20 min | C-05, H-01, H-06 (partial) |
| 3 | `guide/02` §2.4 Memory | Rewrite toàn bộ: Memory chỉ standalone conversations; xóa bảng "project memory (riêng)" false claim; giữ phần Memory synthesis đúng | 45 min | C-01 |
| 4 | `guide/08` §8.2 + §8.6 | Fix connector false claim L134; fix Memory "(Pro)" → "(mọi plan)" L359 | 15 min | H-03, H-04, H-06 (partial) |
| 5 | `guide/00`, `guide/03`, `guide/05`, `guide/08` | Global pass: "Adaptive Thinking" → "Extended thinking" (UI context); add API qualifier chỉ khi cần | 20 min | H-05 (complete), M-02, M-05 |
| 6 | `guide/10` §10.13.3 | Thêm note đầu section: `.claude/commands/` = legacy; Skills là current format | 15 min | H-07 |
| 7 | `ref/config-architecture.md` | Fix Global CLAUDE.md surface (Cowork UI vs CC file) L19; thêm deprecation note cho `memory-starter/` trong tree L291-293 | 20 min | H-08, H-11 |
| 8 | `ref/skills-list.md` | Verify `doc-coauthoring` URL; fix install path; sửa `systematic-debugging` category; update plugin count | 30 min | H-09, M-10 |
| 9 | `_scaffold/CLAUDE-template.md` | Thêm `commands/`, `SETUP.md`, `settings.json` vào `.claude/` structure section | 20 min | H-15 |
| 10 | `guide/10` L1006 | Sửa "context editing" → "compaction"; note API term trong parenthetical | 10 min | H-16 |
| 11 | `guide/01` L159 | Sửa Memory phrasing "trừ khi bật" | 5 min | M-03, H-06 (complete) |

**Issues closed by Sprint 2: 0 Critical + 8 High + 4 Medium = 12 total**

---

### Sprint 3 — 2 tuần tới: Medium Priority
*Kết hợp khi edit module cho mục đích khác. Tổng: ~120 min.*

| # | File(s) | Action | Issues fixed |
|---|---------|--------|:------------|
| 1 | `guide/00` L129 | Thêm changelog entry v4.1: "Deprecate `_memory/`, chuyển 3-tier → 2-tier" | M-01, M-14 |
| 2 | `guide/02` L111 | Root-relative → relative path | M-11 |
| 3 | `guide/02` L512 + `guide/05` L434 | Chuẩn hóa connector token cost phrasing | M-04, M-06 |
| 4 | `guide/04` L510 | "Custom Instructions" → "Project Instructions" | M-13 |
| 5 | `guide/10` §10.6.1 L374 | Thêm caveat: skill auto-activation dựa trên LLM reasoning, không phải keyword matching | M-07 |
| 6 | `guide/10` §10.6.4 L435 | Verify + sửa claude.ai custom skills install path; add `[Cần xác minh]` nếu chưa verify được | M-08 |
| 7 | `guide/10` L1006 | Remove hoặc source "72.5% token reduction" claim | M-09 |
| 8 | `.claude/CLAUDE.md` | Clarify VERSION link rule: "chỉ module 00 cần VERSION link — modules 01-10 không bắt buộc" | M-12 |
| 9 | `ref/config-architecture.md` L29-31 | Skills/Plugins: `[Cowork]` → `[Cowork/CC]` | M-18 |
| 10 | `_scaffold/SKILL-template.md` L104 | `## Skills` → `## Available skills` | M-16 |
| 11 | `guide/10` L1405 | Thêm comment: `# Sẽ cần update khi bump version` | M-17 |
| 12 | `guide/10` §10.13.4 | SessionStart hook matcher: `""` → `"startup"` | M-15 |

---

### Backlog — Không cần schedule

| Category | Action |
|----------|--------|
| **118 code block lang tags** | Batch pass dùng `/validate-doc` từng module. Tag `text`/`bash`/`yaml`/`python`. Module 05 (28 blocks) và 10 (20 blocks) là worst. Pick up cùng Sprint khi edit module đó. |
| **11 VERSION links (mod 01-10)** | Defer đến M-12 resolved. Nếu quyết định thêm → 1 bulk pass. |
| Prefill "deprecated" → "removed" (guide/00 L215) | Minor fix |
| Code execution default Off (guide/02 L60) | Verify UI trực tiếp |
| Source name "Adaptive Thinking Tips" (guide/08 L148) | Fix cùng Sprint 2 pass Module 08 |
| Skill overhead ~100 tokens unsourced (guide/10 L374) | Add `[ước lượng]` |
| Partner skills name-drop Notion/Figma (guide/10 L406) | Lower claim specificity |
| Community plugin GitHub install (guide/10 L440) | Add `[Cần xác minh]` |
| Cowork Max plan uses Opus by default (guide/10 L994) | Add note "(Max: Opus mặc định)" |
| Anthropic plugin count (ref/skills-list L56) | Update to "11+" |
| `systematic-debugging` in skillhub commands (ref/skills-list L115) | Remove or move to GitHub section |
| `guide/*.bak` files | Clean up locally; add `*.bak` to `.gitignore` |
| `.claude/worktrees/` leftover | Manual delete |
| `decision-matrix-project-chat-vs-cowork.html` | Decide: move to `_scaffold/` hoặc delete |

---

## Task 5: CLAUDE.md Update Recommendations

### Rules cần THÊM

**1. Commands section** — Thêm bảng commands song song với Available skills:
```
## Available commands
| Command | Trigger |
|---------|---------|
| `/start` | Đầu mỗi session |
| `/checkpoint` | Quick commit |
| `/validate-doc` | Kiểm tra một module |
| `/review-module` | Deep review module |
| `/weekly-review` | Review hàng tuần |
```

**2. Naming convention cho thinking features** (vào Language rules):
> `Extended thinking` = UI toggle trong Claude.ai (Settings > Search and tools). `Adaptive Thinking` = API feature (`thinking: {type: "adaptive"}`). KHÔNG dùng hoán đổi.

**3. Pre-publish verification rule:**
> Trước khi document Memory/plan availability hoặc feature defaults, verify tại support.claude.com (features thay đổi thường xuyên).

### Rules cần SỬA

1. **Git workflow → Main branch:** `main` → `master`
2. **Available skills table:** Thêm `cross-ref-checker`, `module-review`, `doc-standard-enforcer`; clarify `/simplify` là global built-in (không phải project skill)
3. **Folder structure:** Thêm `.claude/commands/` (5 files), `.claude/settings.json`, `.claude/settings.local.json`
4. **Module version link rule:** Clarify scope → "chỉ module 00 cần link `[VERSION](../VERSION)`; modules 01–10 không bắt buộc"

### Rules cần ĐÁNH GIÁ LẠI

**`.bak` backup rule** (S5 §4.4): Với Git tracking, `.bak` thêm overhead mà không tăng safety cho committed work. Đề xuất 2 options:
- **Option A (conservative):** Giữ rule nhưng tighten: "Tạo `.bak` chỉ khi editing uncommitted section lớn. Không commit `.bak` files."
- **Option B (Git-first):** Thay bằng: "Chạy `/checkpoint` trước khi bắt đầu edit module lớn — Git là backup thực sự." Thêm `*.bak` vào `.gitignore`.

Current evidence: `.bak` files liên tục appear in `git status`, yêu cầu manual exclusion — dấu hiệu rule đang gây friction hơn là safety.

---

## Task 6: Structural Recommendations

### Files nên MERGE
Không có merge candidates. Tất cả files đều serve distinct purposes, không có overlap đáng kể.

### Files nên SPLIT

| File | Current Size | Recommendation |
|------|:-----------:|----------------|
| `guide/10-claude-desktop-cowork.md` | 72 KB | Monitor. Candidate split khi > 100KB: §10.1–10.11 (Cowork guide) + `10b-claude-code-integration.md` (§10.12–10.13). **Không urgent now.** |

### Files nên XÓA

| File/Folder | Reason | Sprint |
|-------------|--------|:------:|
| `_scaffold/memory-starter/` (toàn bộ) | Deprecated `_memory/` pattern, "3-tier" refs, propagates stale methodology | S1 |
| `_scaffold/skill-templates/SKILL-template.md.bak` | Stray `.bak` không nên commit | S1 |
| `guide/*.bak` (nhiều file) | Per CLAUDE.md — không commit | Backlog |
| `.claude/worktrees/quizzical-tereshkova/` | Leftover worktree | Backlog |
| `decision-matrix-project-chat-vs-cowork.html` | Orphan file ở root — không trong spec | Backlog (decide) |

### Files nên TẠO MỚI

| File | Justification | Priority |
|------|---------------|:--------:|
| `.gitignore` entry: `*.bak` | Prevent accidental `.bak` commits (tốt hơn rule) | Sprint 2 |
| `_review/ARCHIVE/` | Post-publish: move audit files, giữ git history | Post-publish |
| `guide/10b-claude-code-integration.md` | Future split nếu Module 10 > 100KB | Backlog |

---

## Summary Dashboard

### Top 5 Critical Issues (phải fix trước khi publish)

| Rank | Issue | File | Fix |
|:----:|-------|------|-----|
| 🥇 | Project Memory false claim | `guide/02` §2.4 | Rewrite section: Memory KHÔNG trong Projects |
| 🥈 | Adaptive Thinking = Extended Thinking (false) | `guide/06` §6.3 | Rename + rewrite; clarify 2 distinct concepts |
| 🥉 | Memory "Free: Không" outdated | `guide/06` §6.1 | Sửa 1 bảng + thêm Max plan tier |
| 4 | Sonnet 4.5 1M beta wrong spec (2 modules) | `guide/04` L27 + `guide/10` L1139 | Delete "Sonnet 4.5" from 1M beta row |
| 5 | CLAUDE.md git branch + skills outdated | `.claude/CLAUDE.md` | Fix branch + update skills/commands table |

### Effort Estimate

| Sprint | Issues Closed | Time |
|--------|:-------------:|:----:|
| Sprint 1 (tuần này) | 9C + 3H + 1M = **13** | ~75 min |
| Sprint 2 (tuần sau) | 0C + 8H + 4M = **12** | ~235 min |
| Sprint 3 (2 tuần) | 0C + 0H + 13M = **13** | ~120 min |
| Backlog | ~154 (118 code blocks + 36 misc) | Ongoing |
| **Total** | **~192** | **~7 hours** |

### Projected Health After Sprint 1+2

| File | Before | After S1+2 | Delta |
|------|:------:|:----------:|:-----:|
| Module 06 | 6.0 | ~8.5 | +2.5 |
| Module 02 | 7.0 | ~8.5 | +1.5 |
| Module 04 | 6.7 | ~8.0 | +1.3 |
| `_scaffold/` | 6.0 | ~8.5 | +2.5 |
| `.claude/CLAUDE.md` | 4.0 | ~9.0 | +5.0 |

---

*Audit hoàn thành: 2026-03-03 | S1–S7 | 6 review sessions → 1 action plan*
