# Skills & Commands Guide — Chi tiết

**Cập nhật:** 2026-03-07 | Mô tả chi tiết mọi skill và command trong project

---

Hướng dẫn sử dụng chi tiết cho từng skill và command trong Guide Claude project. Bao gồm mục đích, cách trigger, input/output, và tips thực tế.

> [!NOTE]
> Tra cứu nhanh (tên, trust level, install) → xem [skills-list.md](skills-list.md).
> File này tập trung vào **cách dùng** và **khi nào dùng**.

[Nguồn: Đọc trực tiếp từ SKILL.md và command files trong `.claude/`] [Cập nhật 03/2026]

---

## 1. Session Management

### `/start` (Command)

**Mục đích:** Quick orientation đầu mỗi session — đọc git state, trả về tóm tắt ngắn.

**Trigger:** Gõ `/start` hoặc tự động đầu session.

**Input:** Không cần argument.

**Output:** Block tối đa 6 dòng:

```text
Project v{version} | Branch: {branch}
Last commit: {hash} {message}
Working tree: {N} modified, {M} untracked
```

**Tips:**
- Không đọc project-state.md (tiết kiệm token) — chỉ đọc khi user yêu cầu
- Chỉ đếm số files, không liệt kê từng file
- Dùng thay cho `git status` + `git log` thủ công

---

### `session-start` (Skill)

**Mục đích:** Orientation đầy đủ hơn `/start` — thêm suggested next action.

**Trigger:** "bắt đầu", "tiếp tục", "session mới", "còn lại gì", "tóm tắt"

**Input:** Không cần.

**Output:** Block tối đa 8 dòng — giống `/start` nhưng thêm suggested action.

**Tips:**
- `/start` đủ cho sessions thông thường
- `session-start` phù hợp hơn khi bắt đầu session mới hoặc sau thời gian dài không làm việc
- Hỏi user xác nhận trước khi bắt đầu task

---

### `/checkpoint` (Command)

**Mục đích:** Quick commit — phân tích changes và đề xuất commit message.

**Trigger:** Gõ `/checkpoint` trước/sau khi edit module lớn.

**Input:** Không cần argument. Phân tích working tree tự động.

**Output:**
1. Danh sách files changed (git diff --stat)
2. Proposed commit message (max 72 chars, prefix: Module XX: / Infra: / Docs:)
3. Ba lựa chọn: "Commit & push", "Commit only", "Edit message"

**Tips:**
- Nếu working tree clean → cảnh báo, không tạo empty commit
- Cảnh báo nếu có `.bak` files trong staging
- Dùng trước khi bắt đầu edit lớn (backup point) và sau khi hoàn thành task

---

## 2. Quality Assurance

### `/validate-doc` (Command)

**Mục đích:** Kiểm tra nhanh 1 module theo 5 tiêu chí format.

**Trigger:** Gõ `/validate-doc base/03` hoặc `/validate-doc 03`

**Input:** Module identifier — số (`03`), tier/số (`base/03`, `dev/01`), hoặc full path.

**Output:** Pass/fail report cho 5 checks:

| Check | Kiểm tra gì |
|-------|-------------|
| 1. Heading hierarchy | `#` title duy nhất, không skip level |
| 2. Cross-links | Relative paths tồn tại, anchors valid |
| 3. Code blocks | Tất cả có language tag |
| 4. Source markers | Format `[Nguồn: ...]`, dates hợp lệ |
| 5. Version refs | Module 00 có VERSION link, modules khác không hardcode |

**Tips:**
- Chạy sau mỗi lần edit module
- Output tối đa 20 dòng — nhóm issues nếu nhiều
- Nhanh hơn `/review-module` — dùng cho format check thường xuyên

---

### `/review-module` (Command)

**Mục đích:** Deep review 1 module — đánh giá 5 chiều content quality.

**Trigger:** Gõ `/review-module base/03` hoặc `/review-module dev/01`

**Input:** Module identifier (giống `/validate-doc`).

**Output:** Review report:
- Score /10 tổng thể
- 5 chiều: Completeness, Clarity, Examples, Cross-refs, Writing Standards
- Strengths (điểm mạnh)
- Issues (vấn đề cụ thể với line references)
- Suggestions (đề xuất cải thiện)

**Tips:**
- Dùng cuối phase hoặc trước version bump
- File > 20KB: recommend chạy trên Opus cho accuracy
- Chỉ report, không tự edit — user quyết định fix gì

---

### `doc-standard-enforcer` (Skill)

**Mục đích:** Manual deep review content theo writing standards — 6-point checklist.

**Trigger:** "review format", "kiểm tra standards", "deep review"

**Input:** Target file path hoặc module identifier (optional — nếu không chỉ định, hỏi user).

**Output:** Report với 6 checks:

| Check | Nội dung |
|-------|----------|
| Structure | Heading hierarchy, section flow |
| Code Blocks | Language tags, format |
| Cross-links | Link validity, anchor existence |
| Source Markers | Presence, format, freshness |
| Language | Emoji compliance, thuật ngữ |
| Content Quality | Accuracy, completeness |

**Tips:**
- Kỹ hơn `/validate-doc` — bao gồm content quality, không chỉ format
- Automation đã cover phần lớn format checks (hooks + rules) — skill này cho review thủ công on-demand
- Output score X/6 với pass/fail mỗi check

---

### `module-review` (Skill)

**Mục đích:** Review có cấu trúc theo 5 tiêu chí content (underlying skill cho `/review-module`).

**Trigger:** "review module X", "kiểm tra module", "đánh giá chất lượng module"

**Input:** Module identifier.

**Output:** Review report với:
- 5 criteria: Accuracy, Consistency, Completeness, Clarity, Actionability
- Status: Ready / Minor fixes needed / Major issues
- Action items phân loại: Must fix, Should fix, Nice to have

**Tips:**
- Skill này là engine đằng sau `/review-module` command
- Dùng trực tiếp khi cần customize review scope
- Đọc VERSION và git log để lấy context

---

### `/weekly-review` (Command)

**Mục đích:** Weekly scan toàn bộ project — git activity, cross-links, glossary.

**Trigger:** Gõ `/weekly-review` hoặc "weekly review"

**Input:** Không cần.

**Output:** Summary table (~40 dòng max) với 5 sections:
1. Git activity (commits, files changed trong 7 ngày)
2. Cross-link issues (broken relative paths)
3. Glossary inconsistencies (variant terms)
4. Overall summary
5. Suggested priorities (2-3 tasks)

**Tips:**
- Lightweight scan — dùng grep, không đọc full files
- Kiểm tra 7 key terms: Cowork, Claude Code, context window, prompt, token, skill, hook
- Output ngắn gọn — actionable priorities, không chi tiết từng issue

---

## 3. Content Management

### `cross-ref-checker` (Skill)

**Mục đích:** Scan toàn bộ guide/ tìm stale cross-references sau restructure hoặc version change.

**Trigger:** "kiểm tra cross-references", "tìm stale references", "scan references", "cross-ref sweep", trước version bump

**Input:** Không cần (scan toàn bộ guide/).

**Output:** Checklist phân loại 4 mức:
- **Critical:** Old file paths (outputs/, _memory/)
- **High:** Hardcoded versions
- **Medium/Low:** Internal links cần update
- **Pass:** Không có issues

**Tips:**
- Chạy trước mỗi `/checkpoint` quan trọng
- Chạy bắt buộc trước version bump
- Chỉ scan `.md` files, skip `.bak`
- Đề xuất fix ngay hoặc export danh sách

---

### `source-audit` (Skill)

**Mục đích:** Scan source markers theo 3-tier verification standard.

**Trigger:** "source audit", "kiểm tra sources", "scan sources", "audit markers", cuối session

**Input:** Không cần (scan toàn bộ guide/ + guide/reference/).

**Output:** 3 bảng:
1. **Missing Markers:** Sections thiếu `[Nguồn:]` hoặc `[Cập nhật]`
2. **Stale Markers:** `[Cập nhật MM/YYYY]` > 6 tháng
3. **Format Issues:** Markers sai format

**Tips:**
- Chạy cuối mỗi session viết content mới
- Phân biệt Tier 1 (official), Tier 2 (verified repos), Tier 3 (community + disclaimer)
- Stale threshold: > 6 tháng = flag review

---

## 4. Version & Project Management

### `version-bump` (Skill)

**Mục đích:** Atomic version bump — update VERSION (SSOT), changelog, project-state.md.

**Trigger:** "bump version", "lên version mới", "release vX.X"

**Input:** New version number (bắt buộc — luôn confirm với user trước).

**Output:** Summary:
1. VERSION file updated
2. Changelog entry thêm vào 00-overview.md
3. project-state.md header updated
4. Đề xuất commit + optional upload

**Preconditions (kiểm tra trước khi bump):**
- Cross-ref sweep passed
- Module reviews passed
- User confirmed version number

**Tips:**
- Không tự ý bump — luôn hỏi user
- Module headers tự reflect version qua VERSION link — không sửa thủ công
- Dùng `/checkpoint` (git commit) trước khi edit — đảm bảo có rollback point

---

### `upgrade-guide` (Skill)

**Mục đích:** Health check tổng thể — scan stale data, broken refs, dependencies, volatile data, emoji violations.

**Trigger:** "upgrade scan", "health check", "kiểm tra stale", "scan project", trước update cycle

**Input:** Optional: module number (`03`), `all` (default: hỏi user).

**Output:** 5 bảng:
1. Stale Content (`[Cập nhật]` > 3 tháng)
2. Broken References (relative paths không tồn tại)
3. Dependency Warnings (`depends-on:` / `impacts:` sai)
4. Volatile Data (model IDs, pricing, context windows)
5. Emoji Violations (banned emoji)

**Priority order:** Broken refs > Dependencies > Emoji > Stale > Volatile

**Tips:**
- Chạy đầu mỗi phase mới hoặc trước update cycle
- Stale threshold: > 3 tháng (strict hơn source-audit)
- Scan cả `depends-on:` và `impacts:` frontmatter

---

## Quick Decision — Dùng tool nào?

| Tình huống | Tool |
|-----------|------|
| Bắt đầu session | `/start` |
| Sau khi edit 1 module | `/validate-doc` |
| Review sâu 1 module | `/review-module` |
| Trước checkpoint | `cross-ref-checker` |
| Cuối session | `source-audit` |
| Trước version bump | `upgrade-guide` + `cross-ref-checker` + `/review-module` |
| Weekly maintenance | `/weekly-review` |
| Commit changes | `/checkpoint` |

---

### `nav-update` (Skill)

**Mục đích:** Auto-update prev/next navigation links trong guide/ files khi thêm/xóa/rename module.

**Trigger:** "update nav", "fix navigation", "nav-update", sau khi thêm/xóa/rename module

**Input:** Không cần (scan toàn bộ guide/).

**Output:** Danh sách files updated + verification:
- Files có nav links sai hoặc thiếu
- Nav links đã sửa
- Verification: tất cả nav links trỏ đến file tồn tại

**Tips:**
- Chạy sau khi thêm hoặc xóa module
- Chạy sau rename file
- Verify output trước khi commit — nav links ảnh hưởng UX đọc tài liệu

---

## Cross-references

- **Tra cứu nhanh skills:** [skills-list.md](skills-list.md) — tên, trust level, install commands
- **Config architecture:** [config-architecture.md](config-architecture.md) — settings, rules, hooks
- **Writing standards:** xem `.claude/rules/writing-standards.md`
- **Dev workflows:** [dev/06](../dev/06-dev-workflows.md) — session management, git workflows
