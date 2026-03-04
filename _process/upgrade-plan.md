# Upgrade Plan — Guide Claude v5.1 → v6.1

**Tạo:** 2026-03-04 | **Maintainer:** Đỗ Quốc Đạt
**Trạng thái:** Planning Complete — Chờ thực thi

---

## Tổng quan

Upgrade plan cho 8 quyết định đã confirm qua brainstorm session 2026-03-04.
Chia thành 5 phases, map vào 4 version releases.

**Workflow thực thi:**

```
Cowork (planning/review) → Claude Code (thực thi/edit) → Cowork (verify/next session)
```

Mỗi phase gồm nhiều sessions. Mỗi session có prompt riêng tại `_process/session-guide.md`.

---

## 8 Quyết Định

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

---

## Dependency Map

```
Phase 0: D8, D7-P1 (không phụ thuộc)
Phase 1: D6, D1 (phụ thuộc Phase 0 rules)
Phase 2: D2 (phụ thuộc D1), D5 (phụ thuộc D6)
Phase 3: D3 (phụ thuộc D2)
Phase 4: D4 (phụ thuộc D3, D5, D6, D8)
Phase 5: D7-P2, D7-P3 (phụ thuộc Phase 4)
```

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
| **Files edit** | `.claude/CLAUDE.md`, `~/.claude/CLAUDE.md` |
| **Files tham chiếu** | `guide/00-overview.md` (conventions section) |

**Scope:**
- Thêm section `## Icon & Emoji Rules` vào `.claude/CLAUDE.md`
- Thêm tương tự vào Global CLAUDE.md
- Allowlist: ⚠️ ✅ ❌ 🔴 🟡 🟢 🔵
- Banned: mọi emoji khác
- Thay emoji trong prose bằng Obsidian callouts: `> [!WARNING]`, `> [!TIP]`, `> [!NOTE]`, `> [!IMPORTANT]`
- Rule: "Nếu output chứa emoji ngoài allowlist → remove trước khi trả lời"

**Acceptance criteria:**
- [x] `.claude/CLAUDE.md` có section Icon & Emoji Rules
- [ ] Global `CLAUDE.md` có tương tự (cần update thủ công trên máy)
- [x] `guide/00-overview.md` conventions section cập nhật
- [ ] Test: mở Claude Code session mới, yêu cầu tạo content → không có emoji banned

### Task 0.2 — Release Checklist (D7-P1)

| Attribute | Value |
|-----------|-------|
| **Status** | `[x]` Done — S01 |
| **Session** | S01 (cùng session với 0.1) |
| **Files tạo mới** | `_process/release-checklist.md` |

**Scope:**
- Viết release checklist: Planning → Edit → Review → Merge → Announce
- Bao gồm: pre-edit checks, cross-ref scan, version bump, PR workflow
- Template cho mỗi phase của upgrade plan

**Acceptance criteria:**
- [x] File `_process/release-checklist.md` tồn tại
- [x] Checklist cover từ planning đến merge
- [x] Có section "Post-merge verification"

### Task 0.3 — Scan & Remove Emoji vi phạm hiện tại

| Attribute | Value |
|-----------|-------|
| **Status** | `[ ]` Not started |
| **Session** | S02 |
| **Files edit** | Toàn bộ `guide/`, `.claude/CLAUDE.md` |

**Scope:**
- Scan toàn bộ files tìm emoji ngoài allowlist
- Thay thế bằng Obsidian callouts hoặc text markers
- Giữ nguyên allowlist icons trong bảng status

**Acceptance criteria:**
- [ ] Grep toàn bộ guide/ không còn emoji banned
- [ ] Callouts render đúng trong Obsidian
- [ ] `cross-ref-checker` pass

---

## Phase 1: Infrastructure

**Version target:** v5.1
**Branch:** `feat/centralize-specs`
**Estimated effort:** 3-5 giờ
**Depends on:** Phase 0

### Task 1.1 — Tạo model-specs.md (D6)

| Attribute | Value |
|-----------|-------|
| **Status** | `[ ]` Not started |
| **Session** | S03 |
| **Files tạo mới** | `guide/reference/model-specs.md` |
| **Files edit** | Toàn bộ module headers (00-11), `guide/06-tools-features.md` |

**Scope:**
- Tạo `reference/model-specs.md` chứa: model comparison, context window, feature-by-plan table, decision flowchart placeholder
- Chuyển mục 6.1 (plan table) và 6.2 (model details, benchmark, pricing) từ Module 06 sang specs file
- Giữ lại ở Module 06: nguyên tắc chọn (evergreen) + link đến specs
- Refactor ALL module headers: thay `Claude Opus 4.6 / Sonnet 4.6` bằng `Models: xem [specs](../reference/model-specs.md)`
- Bỏ benchmark scores (72.5%, 91.3%) → thay bằng mô tả định tính + link source
- Bỏ pricing cụ thể → link `anthropic.com/pricing`

**Acceptance criteria:**
- [ ] `reference/model-specs.md` tồn tại, có đủ sections
- [ ] Module 06 không còn hardcode model specs
- [ ] 12 module headers đã refactor
- [ ] Grep `72.5%` và `91.3%` trả về 0 kết quả trong guide/
- [ ] `cross-ref-checker` pass (tất cả links đến specs file hoạt động)

### Task 1.2 — Trust labels + Recommendation tier (D1)

| Attribute | Value |
|-----------|-------|
| **Status** | `[ ]` Not started |
| **Session** | S04 |
| **Files edit** | `guide/reference/skills-list.md` |

**Scope:**
- Thêm cột `Trust` vào mỗi bảng skill: `✅ Official`, `⚠️ Community`, `🔍 Unreviewed`
- Thêm section "Khuyến nghị cài đặt" với 3 tier:
  - **Must-have:** Pre-built (docx, xlsx, pptx, pdf)
  - **Nice-to-have:** Official standalone (doc-coauthoring, skill-creator) + community đã test (obsidian-markdown, mermaidjs-v11)
  - **Reference-only:** Toàn bộ community còn lại — chỉ để tra cứu
- Giữ nguyên index đầy đủ để tìm kiếm

**Acceptance criteria:**
- [ ] Mỗi skill có Trust label
- [ ] Section "Khuyến nghị cài đặt" có 3 tier rõ ràng
- [ ] Index vẫn đầy đủ (không xóa skill nào)

---

## Phase 2: Structure

**Version target:** v5.1 (cùng release với Phase 1)
**Branch:** `feat/skill-structure` (hoặc continue branch Phase 1)
**Estimated effort:** 3-4 giờ
**Depends on:** Phase 1

### Task 2.1 — Audience tags + Approved badge (D2)

| Attribute | Value |
|-----------|-------|
| **Status** | `[ ]` Not started |
| **Session** | S05 |
| **Files edit** | `guide/reference/skills-list.md` |

**Scope:**
- Thêm cột `Audience`: `maintainer` hoặc `end-user` hoặc `both`
- Thêm badge `[Approved PX]` cho skill đã test tại Phenikaa-X context
- Đánh giá từng skill:
  - Project skills (session-start, version-bump...) → `maintainer`
  - Pre-built (docx, xlsx...) → `end-user`
  - doc-coauthoring → `both`
  - Community doc skills → `end-user` (nhưng chưa approved)
- Thêm cảnh báo: "Skill chưa có badge `[Approved PX]` có thể tạo output không phù hợp với Phenikaa-X conventions"

**Acceptance criteria:**
- [ ] Mỗi skill có Audience tag
- [ ] Ít nhất 4-6 skills có badge `[Approved PX]`
- [ ] Cảnh báo về non-approved skills rõ ràng

### Task 2.2 — Model Decision Flowchart (D5)

| Attribute | Value |
|-----------|-------|
| **Status** | `[ ]` Not started |
| **Session** | S05 (cùng session với 2.1) |
| **Files edit** | `guide/reference/model-specs.md` |

**Scope:**
- Tạo Mermaid flowchart trong model-specs.md:
  - Start → "Cần suy luận sâu (>3 bước logic)?" → Yes → Opus / No → next
  - "Cần nhanh, task đơn giản?" → Yes → Haiku / No → Sonnet
  - Edge cases: batch processing, agentic tasks, code generation
- Thêm 3 ví dụ cụ thể:
  - "Review 5 SOP" → Sonnet (batch, tốc độ đủ)
  - "Đánh giá kiến trúc multi-AMR fleet" → Opus (multi-system reasoning)
  - "Tra cứu nhanh API syntax" → Haiku (đơn giản, nhanh)

**Acceptance criteria:**
- [ ] Mermaid flowchart render đúng
- [ ] 3 ví dụ thực tế kèm theo
- [ ] Link từ Module 06 đến flowchart hoạt động

---

## Phase 3: Skill-Recipe Mapping

**Version target:** v5.2
**Branch:** `feat/skill-mapping`
**Estimated effort:** 2-3 giờ
**Depends on:** Phase 2

### Task 3.1 — Mapping table (D3)

| Attribute | Value |
|-----------|-------|
| **Status** | `[ ]` Not started |
| **Session** | S06 |
| **Files edit** | `guide/reference/skills-list.md` |
| **Files tham chiếu** | `guide/05-workflow-recipes.md`, `guide/07-template-library.md`, `guide/11-cowork-workflows.md` |

**Scope:**
- Thêm section "Skill-Recipe Mapping" vào skills-list.md
- Bảng: Recipe/Workflow → Skill khuyến nghị → Input/Output mô tả ngắn
- Cover toàn bộ 14 recipes (Module 05) + 12 workflows (Module 11) + templates liên quan (Module 07)
- Ghi chú: đây là khuyến nghị, không bắt buộc

**Acceptance criteria:**
- [ ] Bảng mapping cover 26+ recipes/workflows
- [ ] Mỗi dòng có: tên recipe, skill khuyến nghị, input/output 1 dòng
- [ ] Chỉ khuyến nghị skill có badge `[Approved PX]` hoặc Official

---

## Phase 4: Content Evolution

**Version target:** v6.0
**Branch:** `feat/hybrid-examples`
**Estimated effort:** 8-12 giờ (lớn nhất)
**Depends on:** Phase 1, 2, 3

### Task 4.1 — Pilot: Rewrite 2 modules thử nghiệm

| Attribute | Value |
|-----------|-------|
| **Status** | `[ ]` Not started |
| **Session** | S07, S08 |
| **Files edit** | `guide/05-workflow-recipes.md` (2-3 recipes đầu), `guide/11-cowork-workflows.md` (2-3 workflows đầu) |

**Scope:**
- Chọn 2-3 recipes trong Module 05 và 2-3 workflows trong Module 11
- Rewrite ví dụ chính sang Documentation/Technical Writing:
  - 5.1: "Viết User Guide AMR" → "Viết Style Guide cho team"
  - 5.2: "Review tài liệu kỹ thuật" → "Review SOP draft của đồng nghiệp"
  - 11.1: "Viết SOP vận hành AMR" → "Viết SOP cho quy trình onboarding kỹ sư mới"
- Thêm AMR callout box: `> [!NOTE] **AMR Context** ...`
- Thêm model hint: `> [!TIP] **Model:** Sonnet 4.6 cho drafting...`
- Thêm skill hint: `> [!TIP] **Skill:** doc-coauthoring...`
- Đánh giá effort thực tế trước khi làm toàn bộ

**Acceptance criteria:**
- [ ] 4-6 recipes/workflows đã rewrite
- [ ] Mỗi recipe có: doc example + AMR callout + model hint
- [ ] Callouts render đúng trong Obsidian
- [ ] Đánh giá: effort thực tế vs dự kiến → go/no-go cho full rewrite

### Task 4.2 — Full rewrite (nếu pilot OK)

| Attribute | Value |
|-----------|-------|
| **Status** | `[ ]` Not started |
| **Session** | S09 → S14 (ước tính 6 sessions) |
| **Files edit** | Module 03, 05, 07, 08, 11 |

**Scope:**
- Áp dụng pattern từ pilot cho toàn bộ recipes/workflows còn lại
- Module 03: prompt examples → Documentation context
- Module 05: 14 recipes
- Module 07: template contexts
- Module 08: error examples
- Module 11: 12 workflows
- Mỗi module rewrite xong → chạy `/review-module` verify

**Acceptance criteria:**
- [ ] Toàn bộ 5 modules đã rewrite
- [ ] `/review-module` pass cho mỗi module
- [ ] `cross-ref-checker` pass toàn bộ

---

## Phase 5: Process Maturity

**Version target:** v6.1
**Branch:** `feat/process-maturity`
**Estimated effort:** 5-7 giờ
**Depends on:** Phase 4

### Task 5.1 — Dependency tags (D7-P2)

| Attribute | Value |
|-----------|-------|
| **Status** | `[ ]` Not started |
| **Session** | S15 |
| **Files edit** | Toàn bộ module headers (00-11) |

**Scope:**
- Thêm YAML-like metadata vào mỗi module header:
  ```
  depends-on: [04-context-management, reference/model-specs]
  impacts: [07-template-library]
  ```
- Tạo dependency graph tổng thể (Mermaid)

**Acceptance criteria:**
- [ ] 12 modules có dependency metadata
- [ ] Dependency graph chính xác

### Task 5.2 — Upgrade skill (D7-P3)

| Attribute | Value |
|-----------|-------|
| **Status** | `[ ]` Not started |
| **Session** | S16 |
| **Files tạo mới** | `.claude/skills/upgrade-guide/SKILL.md` |

**Scope:**
- Tạo skill tự động hóa: scan dependencies, check volatile data, generate diff report
- Input: module number hoặc "all"
- Output: report + suggested edits

**Acceptance criteria:**
- [ ] Skill hoạt động khi gọi `/upgrade-guide`
- [ ] Output bao gồm: stale data, broken refs, dependency warnings

---

## Version Release Summary

| Version | Phases | Key deliverables | Est. sessions |
|---------|--------|-----------------|---------------|
| v5.1 | 0, 1, 2 | Rules, specs file, trust labels, flowchart | S01 → S05 |
| v5.2 | 3 | Skill-recipe mapping | S06 |
| v6.0 | 4 | Hybrid examples (pilot + full) | S07 → S14 |
| v6.1 | 5 | Dependency tags, upgrade skill | S15 → S16 |

---

## Tracking

Cập nhật status (`[ ]` → `[x]`) sau mỗi session thành công.
Cập nhật file này từ Cowork sau khi verify kết quả Claude Code.

**Last updated:** 2026-03-04 — S01 done (Task 0.1, 0.2)
