# Next Phase Plan — Guide Claude
**Date:** 2026-03-03 | **Input:** final-checkpoint.md (post-Sprint 1-2-3 audit)
**Version hiện tại:** 4.1 | **Overall health:** 8.3/10

---

## Task 1: Module Groups

### Nhóm A — Ready 🟢 (≥ 8.0)
Sẵn sàng chia sẻ cho team review / bắt đầu sử dụng nội bộ.
Không cần edit thêm trừ khi có feedback từ engineers.

| Module | Score | Ghi chú |
|--------|:-----:|---------|
| 00 — Overview | 8.8 | Changelog tốt, version SSOT đúng |
| 01 — Quick Start | 8.3 | Ngắn gọn, accurate |
| 02 — Setup & Personalization | 8.0 | ⚠️ Review "Cowork-primary" terminology khi edit lần sau |
| 03 — Prompt Engineering | 8.8 | Không có issue pending |
| 04 — Context Management | 8.0 | ⚠️ L318 WRITE example → đổi `session-state.md` → `project-state.md` (quick win) |
| 06 — Tools & Features | 8.3 | +2.3 từ audit, major fix done |
| 07 — Template Library | 8.8 | Clean, template examples tốt |
| 08 — Mistakes & Fixes | 8.0 | Fixed Sprint 2 |
| 09 — Evaluation Framework | 8.8 | High accuracy, không có pending |
| ref/config-architecture | 8.0 | Deprecation notes đã thêm |

### Nhóm B — Polish 🟡 (6-7)
Cần 1–2 sessions để nâng lên 🟢. Không block internal review nhưng nên fix trước publish.

| Module | Score | Root cause | Tasks | Estimate |
|--------|:-----:|-----------|-------|:--------:|
| **05 — Workflow Recipes** | 7.8 | Structural: heading hierarchy, cross-link density | 1. Audit heading levels (H2/H3 consistency) 2. Kiểm tra/update cross-links đến 04-context 3. Thêm 1–2 ví dụ Phenikaa-X context (AMR, ROS workflow) | 1–2 sessions |
| **10 — Claude Desktop & Cowork** | 7.8 | File quá lớn (1465 ln), 118 unlabeled code blocks | 1. Label code blocks (batch pass `/validate-doc 10`) 2. Review §10.8+ deprecation sections vẫn còn relevant không 3. Consider split thành 10a/10b nếu warranted | 2 sessions |
| **ref/skills-list** | 7.5 | Currency: skill URLs có thể outdated, count accuracy | 1. Verify tất cả skill paths còn đúng 2. Update example outputs 3. Sync với CLAUDE.md skills table | 1 session |

### Nhóm C — Rewrite 🔴 (< 6)

**Không có module nào ở Nhóm C.** Tất cả 3 modules từng 🔴 trước audit (02, 04, 06) đã lên 🟢 sau 3 sprints.

---

## Task 2: Version Bump Assessment

### Metrics
| Dimension | Value |
|-----------|-------|
| Files changed (Sprint 1–3) | 14 files |
| Lines changed | +131 / -124 |
| Audit items resolved | 24/25 (96%) |
| Health score delta | +1.1 (7.2 → 8.3) |
| Modules upgraded tier | 3 (🔴→🟢: 02, 04, 06) |
| CLAUDE.md improvement | +5.0 (4.0 → ~9.0) |

### Verdict: **Bump lên v4.2** ✅

**Lý do warrant bump:**
- 3 sprints sửa 24 issues, bao gồm 9 Critical + 14 High
- CLAUDE.md từ 4.0/10 lên ~9.0 — infrastructure refactor substantial
- Terminology enforcement (ET vs AT) áp dụng globally
- Module 06 gần như viết lại hoàn toàn (+2.3 score)

**Cách thực hiện:**
```
/version-bump
→ Confirm: 4.2
→ Changelog entry: "Sprint 1-2-3: 24 audit fixes, health 7.2→8.3, CLAUDE.md infra overhaul"
```

**Chưa nên bump lên 5.0** — vẫn còn unlabeled code blocks và một số verify-needed items. 5.0 phù hợp sau publish-ready pass.

---

## Task 3: CLAUDE.md Update Draft

### Thay đổi đề xuất

#### Change 1: Rule 1 — `.bak` backup rule → Git-first

**HIỆN TẠI:**
```
1. **Backup trước khi sửa:** KHÔNG edit file trong `guide/` mà không tạo `.bak` trước
```

**ĐỀ XUẤT:**
```
1. **Git-first backup:** Chạy `/checkpoint` trước khi bắt đầu edit module lớn.
   File `.bak` không nên tạo (đã trong `.gitignore`) — trừ khi làm việc offline
   không có Git access.
```

**Lý do:** 10+ .bak files liên tục xuất hiện trong git status = noise. Git là backup thực sự và reliable hơn. `*.bak` đã trong `.gitignore` từ Sprint 1.

---

#### Change 2: Module status table

**HIỆN TẠI:**
```markdown
| Range | Status |
|-------|--------|
| 00, 02, 04, 05, 10 | Draft v3.5–v4.0 (updated for 2-tier) |
| 01, 03, 06–09 | Draft v3.4 (chưa update) |
| reference/ | config-architecture (v4.0), skills-list |
```

**ĐỀ XUẤT:**
```markdown
| Range | Status |
|-------|--------|
| 00–10 | Sprint-patched v4.1–v4.2 — 3 sprints fix, 10/11 modules 🟢, modules 05+10 cần polish |
| reference/ | config-architecture 🟢 8.0, skills-list 🟡 7.5 (cần currency check) |
```

---

#### Change 3: Folder structure — worktrees cleanup

**HIỆN TẠI:** `.claude/worktrees/` không có trong CLAUDE.md (orphan)

**ACTION:** Xóa `.claude/worktrees/` directory, không cần add vào CLAUDE.md vì nó là artifact không phải structure intentional.

---

### Diff summary

| Section | Thay đổi |
|---------|---------|
| Rules #1 | Replace .bak rule → /checkpoint rule |
| Module status | 3 rows → 2 rows, reflect thực tế post-sprint |
| Folder structure | Không thay đổi (worktrees xóa, _review/ không cần add — audit done) |
| Skills/Commands | Không thay đổi — đã correct |
| Language rules | Không thay đổi |

> **Hỏi confirm trước khi ghi:** Bạn có muốn áp dụng 2 changes này vào CLAUDE.md ngay không? (Rule 1 + Module status table)

---

## Task 4: Maintenance Schedule

| Tần suất | Task | Tool | Notes |
|:--------:|------|:----:|-------|
| Mỗi session | `/start` — orientation 30s | CC | Đọc git log + project-state |
| Mỗi session | `/checkpoint` trước edit module lớn | CC | Thay cho .bak rule |
| Hàng tuần | `/weekly-review` — health check nhanh | CC | Phát hiện drift sớm |
| Hàng tuần | Xem feedback từ engineers dùng thử | Manual | Tập hợp thành backlog |
| Hàng tháng | `/validate-doc` pass toàn bộ guide/ | CC | Phát hiện unlabeled code blocks mới |
| Hàng tháng | Verify 1–2 features tại support.claude.com | Manual | RC-3 prevention (features thay đổi) |
| Hàng quý | `/weekly-review` deep — full cross-ref audit | CC | Trước mỗi version minor |
| Hàng quý | Version bump minor (x.Y) nếu đủ thay đổi | CC `/version-bump` | Threshold: ≥ 5 modules sửa hoặc 1 major feature change |
| Trước publish | Code block tag pass (118 unlabeled) | CC `/validate-doc` | Batch qua từng module |
| Trước publish | M-15 SessionStart hook test | Manual | Test `"startup"` vs `""` behavior |

---

## Task 5: Audit Cleanup

### Recommendation: **Archive có chọn lọc**

| File | Action | Lý do |
|------|--------|-------|
| `final-checkpoint.md` | **Giữ** | Permanent record — scorecard, backlog, readiness verdict |
| `s7-action-plan.md` | **Giữ** | Backlog reference — backlog items chưa done vẫn valid |
| `s1-structural.md` | Có thể xóa | Issues đã incorporate vào fixes |
| `s2-accuracy-00-04.md` | Có thể xóa | Issues đã resolve |
| `s3-accuracy-05-09.md` | Có thể xóa | Issues đã resolve |
| `s4-accuracy-10-ref.md` | Có thể xóa | Issues đã resolve |
| `s5-consistency.md` | Có thể xóa | Issues đã resolve |
| `s6-scaffold-infra.md` | Có thể xóa | Issues đã resolve |
| `next-phase-plan.md` | **Giữ** (file này) | Roadmap cho phase tiếp theo |

**Tùy chọn:**
- **Option A (Recommended):** Giữ `final-checkpoint.md` + `s7-action-plan.md` + `next-phase-plan.md`. Xóa s1–s6.
- **Option B:** Giữ toàn bộ _review/ làm archive. Nhỏ (< 50KB), zero cost, có thể useful cho retrospective.
- **Option C:** Xóa toàn bộ _review/ sau khi mọi backlog đã move vào CLAUDE.md hoặc project-state.md.

> _review/ không ảnh hưởng project hoạt động — quyết định tùy preference về documentation trail.

---

## Top 3 Actions — Tuần tới

### 1. Version Bump 4.1 → 4.2 (15 phút)
```
/version-bump → confirm 4.2
```
Ghi nhận 3 sprints work. Changelog entry tóm tắt audit cycle.

### 2. Quick wins batch (30 phút)
Làm ngay 3 items từ backlog:
- [ ] `guide/04` L318: đổi `session-state.md` → `project-state.md` trong bảng WRITE
- [ ] Update CLAUDE.md: Rule 1 (Git-first) + Module status table
- [ ] Xóa `.claude/worktrees/` directory (orphan artifact)

### 3. Polish Module 05 (1–2 sessions)
Module 05 là Nhóm B dễ nhất để nâng lên 🟢:
- Heading audit + cross-link review
- Thêm 1 ví dụ Phenikaa-X context thực tế
- Target: 7.8 → 8.3

---

*Next Phase Plan generated: 2026-03-03 | Audit cycle closed: Sprint 1-2-3*
*Input: final-checkpoint.md | Current health: 8.3/10 → Target: 8.8/10 (sau Polish)*
