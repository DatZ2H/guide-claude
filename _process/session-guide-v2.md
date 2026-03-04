# Session Guide v2 — Upgrade Plan Execution

**Tạo:** 2026-03-04 | **Cập nhật:** 2026-03-04 — Rebuild với D9, re-number S15-S22
**Dùng với:** `_process/upgrade-plan-v2.md`

---

## Cách sử dụng file này

**Workflow:**

1. **Cowork:** Mở file này, đọc session tiếp theo cần làm
2. **Claude Code:** Mở project Guide Claude, paste prompt, thực thi
3. **Claude Code:** Chạy verification commands sau khi xong
4. **Cowork:** Báo cáo kết quả → Cowork verify → cập nhật plan + chỉ session tiếp

**Quy tắc chung cho MỌI session:**

- Bắt đầu bằng `/start` để orientation
- Trước khi edit lớn: `/checkpoint` (backup)
- Sau khi xong: chạy verification commands
- Nếu FAIL → fix tại chỗ, KHÔNG chuyển session mới
- Khi PASS → báo Cowork để verify và cập nhật plan

**Thay đổi so với v1:**
- S01-S14: giữ nguyên
- S15-S16 cũ (dependency tags, upgrade skill): đẩy thành S20-S21
- S15-S19 mới: Phase 4B — Claude Code Documentation (D9)
- S22 mới: Final consistency check
- Tổng: 16 → 22 sessions

---

## S01 — Emoji/Icon Rules + Release Checklist ✅ Done

**Phase:** 0 (Foundation Rules)
**Plan tasks:** 0.1, 0.2
**Model:** Sonnet — task edit nhỏ, nhiều files nhưng đơn giản
**Branch:** `feat/upgrade-rules`

**Kết quả:**
- `.claude/CLAUDE.md` — đã thêm section Icon & Emoji Rules ✅
- `guide/00-overview.md` — đã thêm subsection Icon và Emoji ✅
- `_process/release-checklist.md` — đã tạo ✅
- Global `~/.claude/CLAUDE.md` — cần update thủ công trên máy (ngoài project scope)

---

## S02 — Scan & Remove Emoji vi phạm

**Phase:** 0 (Foundation Rules)
**Plan task:** 0.3
**Model:** Sonnet — batch search-and-replace
**Branch:** tiếp tục `feat/upgrade-rules`
**Estimated:** 1 giờ

### Bước 1: Orientation

```
/start
```

### Bước 2: Scan emoji vi phạm

**Prompt:**

```text
Scan toàn bộ thư mục guide/ và .claude/ tìm emoji NGOÀI allowlist (⚠️ ✅ ❌ 🔴 🟡 🟢 🔵).

Bao gồm nhưng KHÔNG giới hạn: 💡 🚀 😊 🎯 ✨ 📌 🔥 👉 📝 💪 🤔 ⭐ 🏗️ 📊 🛠️
và bất kỳ Unicode emoji nào khác.

Cách scan: dùng Python regex với \p{Emoji} hoặc Unicode category, rồi exclude allowlist.
Không dùng grep với hex ranges (không cover hết).

Liệt kê: file, dòng, emoji tìm thấy, đề xuất thay thế (callout hoặc text marker).
Chưa thay thế — chỉ liệt kê để tôi review.
```

### Bước 3: Thay thế (sau khi review danh sách)

**Prompt:**

```text
Thay thế toàn bộ emoji vi phạm theo danh sách đã review.

Quy tắc thay thế:
- Emoji trong prose (💡, 📌, 🎯) → Obsidian callout tương ứng
- Emoji trang trí (🚀, ✨, 🔥) → xóa, không thay thế
- Emoji trong bảng mà không phải status → xóa hoặc thay bằng text

Mỗi file: cho xem diff trước khi save.
```

### Verification — S02

```bash
# Scan emoji bằng Python — kỳ vọng chỉ còn allowlist
python3 -c "
import re, glob
allowed = set('⚠️✅❌🔴🟡🟢🔵')
emoji_pattern = re.compile(r'[\U0001F600-\U0001F9FF\U00002702-\U000027B0\U0000FE00-\U0000FE0F\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U00002B50\U000023F0-\U000023FA\U0000200D\U00002328\U000023CF\U000023E9-\U000023F3\U000025AA-\U000025AB\U000025B6\U000025C0\U000025FB-\U000025FE\U00002600-\U000027BF\U00002934-\U00002935\U00003030\U0000303D\U00003297\U00003299\U0001F000-\U0001F9FF]')
for f in glob.glob('guide/**/*.md', recursive=True) + glob.glob('.claude/**/*.md', recursive=True):
    for i, line in enumerate(open(f), 1):
        for m in emoji_pattern.finditer(line):
            if m.group() not in allowed:
                print(f'{f}:{i}: {m.group()} ({hex(ord(m.group()[0]))})')
"
# Expected: 0 results

# Cross-ref check
# Chạy skill cross-ref-checker

/checkpoint
```

**Thành công khi:** Scan trả về 0 banned emoji. Báo Cowork.

---

## S03 — Centralize Model Specs

**Phase:** 1 (Infrastructure)
**Plan task:** 1.1 (D6)
**Model:** Sonnet — tạo file mới + refactor nhiều files
**Branch:** `feat/centralize-specs`
**Estimated:** 2-3 giờ (session lớn nhất trước Phase 4)

### Bước 1: Orientation + Branch

```
/start
git checkout -b feat/centralize-specs
```

### Bước 2: Tạo reference/model-specs.md

**Prompt:**

```text
Đọc các file sau để lấy thông tin:
- guide/06-tools-features.md (mục 6.1, 6.2, bảng context window)
- VERSION

Tạo file mới guide/reference/model-specs.md với cấu trúc:

# Model Specs & Platform Data

[Snapshot 03/2026] — File này chứa thông tin thay đổi theo thời gian.
Cập nhật khi Anthropic release model mới hoặc thay đổi pricing/features.

Nguồn chính thức:
- Model specs: https://docs.anthropic.com/en/docs/about-claude/models/overview
- Pricing: https://www.anthropic.com/pricing
- Feature updates: https://www.anthropic.com/news

## Chọn Model — Decision Flowchart

[placeholder — sẽ tạo ở S05]

## Model Comparison

[chuyển bảng từ Module 06 mục 6.2, BỎ benchmark scores]
[thay benchmark bằng mô tả định tính: "Sonnet và Opus đạt điểm tương đương trên agentic benchmarks"]
[context window table chuyển sang đây]

## Nguyên tắc chọn nhanh

[giữ nguyên nội dung evergreen từ 6.2: "Bắt đầu với Sonnet..."]

## Feature Availability by Plan

[chuyển bảng 6.1 sang đây]
[bỏ pricing cụ thể, thay bằng "Xem pricing tại [URL]"]

## Lịch sử cập nhật

| Ngày | Thay đổi |
|------|---------|
| 03/2026 | Khởi tạo — Opus 4.6, Sonnet 4.6, Haiku 4.5 |

Cho tôi xem file trước khi save.
```

### Bước 3: Refactor Module 06

**Prompt:**

```text
Đọc guide/06-tools-features.md.

Refactor:
1. Mục 6.1: thay bảng toàn bộ bằng "Chi tiết plan và features: xem [Model Specs](../reference/model-specs.md#feature-availability-by-plan)"
   Giữ lại 1 dòng mô tả ngắn: "Claude có nhiều plan từ Free đến Enterprise với tính năng khác nhau."

2. Mục 6.2:
   - BỎ: bảng model comparison chi tiết, benchmark quotes, context window table
   - GIỮ: "Nguyên tắc chọn nhanh" paragraph (evergreen)
   - THÊM: link "Chi tiết và so sánh: xem [Model Specs](../reference/model-specs.md)"
   - GIỮ: "Cách chọn model: Click tên model..." instruction

Cho tôi xem diff trước khi save.
```

### Bước 4: Refactor module headers

**Prompt:**

```text
Đọc tất cả 12 files trong guide/ (00-overview.md đến 11-cowork-workflows.md).

Mỗi file có header dạng:
**Cập nhật:** 2026-03-0X | Claude Opus 4.6 / Sonnet 4.6

Thay đổi TOÀN BỘ thành:
**Cập nhật:** 2026-03-0X | Models: xem [specs](../reference/model-specs.md)

Lưu ý: giữ nguyên ngày cập nhật hiện tại, chỉ thay phần model names.

Liệt kê 12 files sẽ thay đổi và cho tôi confirm trước khi thực hiện.
```

### Verification — S03

```bash
# Check model-specs.md tồn tại và có nội dung
wc -l guide/reference/model-specs.md
# Expected: >50 lines

# Check không còn hardcode benchmark
grep -r "72.5%" guide/
grep -r "91.3%" guide/
# Expected: 0 kết quả mỗi grep

# Check headers đã refactor
grep -r "Opus 4.6 / Sonnet 4.6" guide/
# Expected: 0 kết quả (chỉ còn trong model-specs.md nếu có)

# Cross-ref check
# Chạy cross-ref-checker

/checkpoint
```

**Thành công khi:** 4 checks PASS. Báo Cowork.

---

## S04 — Trust Labels + Recommendation Tier

**Phase:** 1 (Infrastructure)
**Plan task:** 1.2 (D1)
**Model:** Sonnet — edit 1 file
**Branch:** tiếp tục `feat/centralize-specs`
**Estimated:** 1-2 giờ

### Bước 1: Orientation

```
/start
```

### Bước 2: Thêm trust labels

**Prompt:**

```text
Đọc guide/reference/skills-list.md.

Sửa các bảng skill (section 2, 3, 4, 5) — thêm cột `Trust`:
- Section 2 (Pre-built): ✅ Official
- Section 3 (Official Standalone): ✅ Official
- Section 4 (Official Plugins): ✅ Official
- Section 5a (skillhub.club): ⚠️ Community
- Section 5b (GitHub): ⚠️ Community
- Section 7 (Custom/Project): ✅ Internal (Phenikaa-X)

Thêm section mới `## Khuyến nghị cài đặt` SAU section 1 (Tổng quan) với 3 tier:

### Must-have
Pre-built Skills — tự động có, không cần cài:
- docx, xlsx, pptx, pdf

### Nice-to-have
Official + community đã test, khuyến nghị cài thêm:
- doc-coauthoring (Official — workflow viết tài liệu có cấu trúc)
- skill-creator (Official — tạo và đo lường skill)
- obsidian-markdown (Community — tốt cho Obsidian users)
- mermaidjs-v11 (Community — tạo diagrams)

### Reference-only
Danh mục để tra cứu. Cài khi có nhu cầu cụ thể, đọc SKILL.md trước khi cài:
- Toàn bộ community skills còn lại (section 5)

Cho tôi xem diff trước khi save.
```

### Verification — S04

```bash
# Check Trust column tồn tại
grep -c "Official\|Community\|Internal" guide/reference/skills-list.md
# Expected: >20

# Check recommendation section tồn tại
grep -c "Must-have\|Nice-to-have\|Reference-only" guide/reference/skills-list.md
# Expected: 3

/checkpoint
```

**Thành công khi:** 2 checks PASS. Báo Cowork.

---

## S05 — Audience Tags + Model Flowchart

**Phase:** 2 (Structure)
**Plan tasks:** 2.1 (D2), 2.2 (D5)
**Model:** Sonnet cho audience tags. Có thể switch Opus cho flowchart design nếu cần suy luận phức tạp.
**Branch:** `feat/skill-structure` (hoặc tiếp tục `feat/centralize-specs`)
**Estimated:** 2 giờ

### Bước 1: Orientation + Branch

```
/start
git checkout -b feat/skill-structure
# Hoặc: tiếp tục trên feat/centralize-specs nếu chưa merge
```

### Bước 2: Audience tags (D2)

**Prompt:**

```text
Đọc guide/reference/skills-list.md.

Thêm cột `Audience` vào các bảng skill. Giá trị:
- `maintainer` — chỉ dùng cho người duy trì project/tài liệu
- `end-user` — dùng cho kỹ sư cuối (người đọc guide)
- `both` — cả hai

Đánh giá cụ thể:
- Pre-built (docx, xlsx, pptx, pdf): `end-user`
- doc-coauthoring: `both`
- internal-comms: `end-user`
- skill-creator: `maintainer`
- Project skills (session-start, version-bump, cross-ref-checker, module-review, doc-standard-enforcer): `maintainer`
- Community doc skills (docs-review, technical-writing, documentation-review...): `end-user`
- Community dev skills (systematic-debugging, architecture-design...): `end-user`
- Plugins (productivity, product-management, data): `end-user`

Thêm badge `[Approved PX]` cho skills đã dùng tại Phenikaa-X:
- docx, xlsx, pptx, pdf — `[Approved PX]`
- doc-coauthoring — `[Approved PX]`
- obsidian-markdown — `[Approved PX]`
- mermaidjs-v11 — `[Approved PX]`
- 5 project skills — `[Approved PX]`

Thêm cảnh báo ngay trước section 5 (Community):
> [!WARNING]
> Skills chưa có badge `[Approved PX]` có thể tạo output không phù hợp với Phenikaa-X conventions.
> Luôn đọc SKILL.md và test trên dữ liệu không nhạy cảm trước khi áp dụng vào công việc chính thức.

Cho tôi xem diff trước khi save.
```

### Bước 3: Model Decision Flowchart (D5)

**Prompt (có thể switch Opus ở bước này):**

```text
Đọc guide/reference/model-specs.md.

Thay `[placeholder — sẽ tạo ở S05]` bằng Mermaid flowchart:

flowchart TD:
- Start: "Task của bạn là gì?"
- Q1: "Cần suy luận sâu, nhiều bước logic (>3 bước)?"
  - Yes → "Dữ liệu/context lớn (>100 trang)?"
    - Yes → Opus (deep reasoning + large context)
    - No → "Opus hoặc Sonnet đều được. Ưu tiên Opus nếu critical decision."
  - No → Q2
- Q2: "Task đơn giản, cần nhanh (Q&A, tra cứu, format)?"
  - Yes → Haiku
  - No → Sonnet (default cho hầu hết công việc)

Sau flowchart, thêm 5 ví dụ thực tế:

| Task | Model | Lý do |
|------|-------|-------|
| Review 5 SOP tìm inconsistencies | Sonnet | Batch processing, tốc độ đủ, chất lượng đủ |
| Đánh giá kiến trúc multi-AMR fleet | Opus | Multi-system reasoning, nhiều dependency |
| Tra cứu nhanh syntax YAML | Haiku | Đơn giản, cần nhanh |
| Viết style guide cho team | Sonnet | Drafting content, iterative |
| Phân tích root cause lỗi SLAM + Lidar + Navigation | Opus | Cross-system, nhiều bước suy luận |

Cho tôi xem trước khi save.
```

### Verification — S05

```bash
# Check Audience column
grep -c "maintainer\|end-user\|both" guide/reference/skills-list.md
# Expected: >20

# Check Approved badge
grep -c "Approved PX" guide/reference/skills-list.md
# Expected: >8

# Check flowchart trong model-specs
grep -c "flowchart" guide/reference/model-specs.md
# Expected: >=1

# Check ví dụ
grep -c "Sonnet\|Opus\|Haiku" guide/reference/model-specs.md
# Expected: >10

/checkpoint
```

**Thành công khi:** 4 checks PASS. Đây là milestone — sẵn sàng release v5.1. Báo Cowork.

---

## S06 — Skill-Recipe Mapping Table

**Phase:** 3 (Mapping)
**Plan task:** 3.1 (D3)
**Model:** Sonnet
**Branch:** `feat/skill-mapping`
**Estimated:** 2 giờ

### Bước 1: Orientation + Branch

```
/start
git checkout -b feat/skill-mapping
```

### Bước 2: Đọc recipes và workflows

**Prompt:**

```text
Đọc 3 files:
- guide/05-workflow-recipes.md (toàn bộ — liệt kê 14 recipe names)
- guide/07-template-library.md (toàn bộ — liệt kê templates liên quan)
- guide/11-cowork-workflows.md (toàn bộ — liệt kê 12 workflow names)

Tạo danh sách 26+ recipes/workflows với tên và mô tả 1 dòng.
Chưa thêm skill — chỉ liệt kê để tôi review.
```

### Bước 3: Tạo mapping table

**Prompt (sau khi review danh sách):**

```text
Đọc guide/reference/skills-list.md.

Thêm section `## Skill-Recipe Mapping` SAU section "Khuyến nghị cài đặt" và TRƯỚC section "Pre-built Skills".

Bảng có 4 cột:
| Recipe/Workflow | Module | Skill khuyến nghị | Input → Output |

Quy tắc:
- Chỉ khuyến nghị skill có badge [Approved PX] hoặc Official
- Nếu không có skill phù hợp → ghi "Không cần skill đặc biệt"
- Input/Output mô tả 1 dòng ngắn

Ví dụ dòng đầu:
| 5.1 Viết tài liệu từ đầu | 05 | doc-coauthoring | Notes/brief → Document hoàn chỉnh |
| 11.1 Viết SOP từ notes | 11 | docx (nếu output Word) | Folder notes → SOP file |

Cho tôi xem trước khi save.
```

### Verification — S06

```bash
# Check mapping section tồn tại
grep -c "Skill-Recipe Mapping" guide/reference/skills-list.md
# Expected: 1

# Check số dòng trong mapping table (đếm dòng có 4+ pipes)
grep -cP "(\|.*){4}" guide/reference/skills-list.md
# Expected: >26

/checkpoint
```

**Thành công khi:** Mapping table có 26+ dòng. Báo Cowork.
**Milestone:** Sẵn sàng bump v5.2 và bắt đầu Phase 4.

---

## S07-S08 — Pilot Hybrid Examples (2 sessions)

**Phase:** 4 (Content Evolution)
**Plan task:** 4.1
**Model:** Sonnet cho rewrite. Switch Opus nếu cần review chất lượng examples.
**Branch:** `feat/hybrid-examples`
**Estimated:** 3-4 giờ (2 sessions)

### S07: Pilot Module 05 (3 recipes)

**Prompt:**

```text
Đọc guide/05-workflow-recipes.md.

Rewrite ví dụ cho 3 recipes đầu tiên (5.1, 5.2, 5.3) theo pattern Hybrid:

1. Ví dụ CHÍNH: Documentation/Technical Writing context
   - 5.1: "Viết Style Guide cho team documentation"
   - 5.2: "Review SOP draft của đồng nghiệp theo rubric"
   - 5.3: [chọn ví dụ doc phù hợp]

2. AMR callout box sau ví dụ chính:
   > [!NOTE] **AMR Context**
   > Áp dụng recipe này cho [AMR use case cụ thể].
   > Thay: `{{loai_tai_lieu}}` = "...", `{{san_pham}}` = "..."

3. Model hint:
   > [!TIP] **Model:** Sonnet 4.6 cho [lý do]. Xem [decision flowchart](../reference/model-specs.md#chon-model)

4. Skill hint (nếu có):
   > [!TIP] **Skill:** [tên skill] — [mô tả 1 dòng]

Giữ nguyên cấu trúc recipe (Khi nào dùng, Setup, Quy trình, Tips).
Chỉ thay đổi phần ví dụ và thêm callout boxes.

Cho tôi xem diff từng recipe trước khi save.
```

### S08: Pilot Module 11 (3 workflows)

**Prompt tương tự S07 nhưng cho Module 11, workflows 11.1, 11.2, 11.3.**

### Verification — S07/S08

```bash
# Check callout boxes tồn tại
grep -c "AMR Context" guide/05-workflow-recipes.md
# Expected: >=3

grep -c "AMR Context" guide/11-cowork-workflows.md
# Expected: >=3

# Check model hints
grep -c "\[!TIP\].*Model" guide/05-workflow-recipes.md
# Expected: >=3

# Validate modules
/validate-doc 05
/validate-doc 11

/checkpoint
```

**Thành công khi:** Callouts render đúng, validate pass.
**Quyết định:** Đánh giá effort thực tế. Nếu OK → go full rewrite (S09-S14). Nếu quá nặng → điều chỉnh approach. Báo Cowork.

---

## S09 → S14 — Full Rewrite (6 sessions ước tính)

**Phase:** 4 (Content Evolution)
**Plan task:** 4.2
**Chi tiết:** Lập kế hoạch cụ thể sau khi pilot (S07-S08) hoàn thành và đánh giá effort.

Phân bổ dự kiến:
- S09: Module 05 recipes còn lại (4-11)
- S10: Module 05 recipes còn lại (12-14) + review toàn module
- S11: Module 11 workflows còn lại (4-9)
- S12: Module 11 workflows còn lại (10-12) + review toàn module
- S13: Module 03 (prompt examples) + Module 08 (error examples)
- S14: Module 07 (template contexts) + final cross-module review

**Mỗi session:**
- Model: Sonnet
- Bắt đầu: `/start`, đọc ví dụ pilot làm reference
- Kết thúc: `/validate-doc`, `/checkpoint`
- Sau mỗi module hoàn thành: `/review-module`

---

## S15 — Reference File: claude-code-setup.md

**Phase:** 4B (Claude Code Documentation)
**Plan task:** 4B.1 (D9-A)
**Model:** Sonnet
**Branch:** `feat/claude-code-docs`
**Estimated:** 2 giờ

### Bước 1: Orientation + Branch

```
/start
git checkout -b feat/claude-code-docs
```

### Bước 2: Tạo reference file

**Prompt:**

```text
Tạo file mới guide/reference/claude-code-setup.md.

Đây là cheat sheet / reference file cho Claude Code dùng trong documentation workflow. Copy-paste ready, KHÔNG phải tutorial. Tuân thủ Icon & Emoji Rules trong .claude/CLAUDE.md.

Cấu trúc:

# Claude Code Setup & Reference cho Documentation

[Cập nhật 03/2026]

Nguồn chính thức: https://code.claude.com/docs/en/best-practices

## 1. Quick Setup Checklist

Checklist 8 bước:
□ Cài đặt Claude Code (link: https://code.claude.com)
□ Chạy `claude --version` — verify cài đặt
□ Chạy `claude` trong thư mục project → first session
□ Chạy `/init` — tạo CLAUDE.md starter
□ Tùy chỉnh CLAUDE.md cho documentation project (xem template bên dưới)
□ Tạo `.claude/settings.json` — cấu hình permissions
□ Tạo slash commands cơ bản (xem Module 12 mục 12.5)
□ Test: chạy session, verify Claude đọc đúng CLAUDE.md

## 2. CLAUDE.md Reference

### Vị trí và scope

| Vị trí | Scope | Shared |
|--------|-------|--------|
| `~/.claude/CLAUDE.md` | Mọi project | Không |
| `./CLAUDE.md` hoặc `./.claude/CLAUDE.md` | Project hiện tại | Có (commit vào git) |
| `./.claude/CLAUDE.local.md` | Cá nhân, project này | Không (gitignored) |
| Thư mục con chứa `CLAUDE.md` | Load khi làm việc trong thư mục đó | Có |

[Nguồn: Claude Code Docs — CLAUDE.md]

### Include vs Exclude

| Include (nên có) | Exclude (không nên có) |
|-------------------|------------------------|
| Bash commands Claude không đoán được | Thứ Claude đã biết từ code |
| Writing/coding style khác default | Conventions chuẩn của ngôn ngữ |
| Test/build commands cụ thể | API documentation chi tiết (link thay thế) |
| Branch naming, commit conventions | Thông tin thay đổi thường xuyên |
| Project-specific decisions | Giải thích dài / tutorials |
| Gotchas, non-obvious behaviors | Mô tả từng file trong codebase |

[Nguồn: Claude Code Docs — Best Practices]

Giữ CLAUDE.md dưới 200 dòng. Nếu dài hơn → chuyển reference content sang Skills.

### Template cho Documentation Project

```markdown
# CLAUDE.md — {{project_name}}

## Project context
{{mô tả project, đối tượng, phase hiện tại}}

## Folder structure
{{liệt kê cấu trúc chính}}

## Language rules
- Ngôn ngữ chính: {{ngôn ngữ}}
- Thuật ngữ kỹ thuật: giữ tiếng Anh
- Placeholders: {{variable}}

## Writing standards
- Heading hierarchy: # title → ## section → ### subsection — KHÔNG skip level
- Code blocks luôn có language tag
- Cross-links dùng relative paths

## Rules — PHẢI tuân thủ
1. Backup trước khi sửa file content
2. Commit message {{ngôn ngữ}}, ngắn gọn
3. KHÔNG tự ý xóa file mà không hỏi
```

## 3. Settings Reference

### settings.json template cho doc project

File: `.claude/settings.json`

```json
{
  "permissions": {
    "allow": [
      "Read(./guide/**)",
      "Read(./.claude/**)",
      "Bash(git status *)",
      "Bash(git log *)",
      "Bash(git diff *)",
      "Bash(git add *)",
      "Bash(wc -l *)"
    ],
    "deny": [
      "Read(./.env*)",
      "Bash(rm -rf *)",
      "Bash(git push --force *)"
    ]
  }
}
```

### Environment Variables quan trọng

| Variable | Mục đích | Ví dụ |
|----------|----------|-------|
| `ANTHROPIC_MODEL` | Override default model | `claude-sonnet-4-6` |
| `CLAUDE_CODE_EFFORT_LEVEL` | Reasoning effort | `low`, `medium`, `high` |

## 4. Essential Commands Cheat Sheet

| Command | Khi nào | Ví dụ documentation context |
|---------|---------|----------------------------|
| `/start` | Đầu session | Orientation: version, branch, recent commits |
| `/clear` | Chuyển task không liên quan | Xong review Module 03, chuyển sang edit Module 05 |
| `/rewind` | Undo sai — restore code + conversation | Claude sửa sai section, rewind về checkpoint |
| `/compact` | Context đầy, cần giải phóng | Session dài, đọc nhiều files |
| `/compact Focus on changes to Module 05` | Compact có hướng dẫn | Giữ lại context quan trọng |
| `/rename` | Đặt tên session | `/rename review-module-03` |
| `/init` | Tạo CLAUDE.md starter | Project mới, chưa có config |
| `/permissions` | Xem/sửa permissions | Cho phép git commit |
| `/status` | Xem settings đang active | Debug config |
| `/mcp` | Kiểm tra MCP connections | Verify Notion/GitHub connected |
| `/plugin` | Browse plugin marketplace | Cài thêm tools |
| `--continue` | Resume session gần nhất | `claude --continue` |
| `--resume` | Chọn session cũ | `claude --resume` (list sessions) |
| `claude -p "..."` | Non-interactive, 1 lệnh | `claude -p "Scan guide/ tìm broken links"` |
| `Esc` | Dừng Claude giữa chừng | Claude đang đi sai hướng |
| `Esc + Esc` | Mở rewind menu | Quay lại checkpoint trước |

## 5. Permission Templates cho Documentation

### Read-only reviewer

```json
{
  "permissions": {
    "allow": ["Read(./guide/**)", "Bash(grep *)", "Bash(wc *)"],
    "deny": ["Edit(*)", "Write(*)", "Bash(git *)"]
  }
}
```

### Full documentation editor

```json
{
  "permissions": {
    "allow": [
      "Read(./guide/**)", "Read(./.claude/**)",
      "Edit(./guide/**)", "Write(./guide/**)",
      "Bash(git *)", "Bash(wc *)", "Bash(grep *)"
    ],
    "deny": [
      "Read(./.env*)", "Bash(rm -rf *)",
      "Bash(git push --force *)", "Bash(git reset --hard *)"
    ]
  }
}
```

## 6. Hooks Templates

### SessionStart — Context tự động

File: `.claude/settings.json`

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "v=$(cat VERSION 2>/dev/null || echo '?'); n=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' '); echo \"Project v${v}. ${n} files modified.\""
          }
        ]
      }
    ]
  }
}
```

### Notification — Cảnh báo khi edit file quan trọng

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"$CLAUDE_NOTIFICATION\" >> ~/.claude/notifications.log"
          }
        ]
      }
    ]
  }
}
```

## 7. External Links (Curated)

| Chủ đề | URL |
|--------|-----|
| Best Practices | https://code.claude.com/docs/en/best-practices |
| Extend Claude Code | https://code.claude.com/docs/en/features-overview |
| CLAUDE.md Guide | https://code.claude.com/docs/en/memory |
| Skills | https://code.claude.com/docs/en/skills |
| Subagents | https://code.claude.com/docs/en/sub-agents |
| Hooks | https://code.claude.com/docs/en/hooks-guide |
| Settings | https://code.claude.com/docs/en/settings |
| Permissions | https://code.claude.com/docs/en/permissions |
| Plugins | https://code.claude.com/docs/en/plugins |
| Common Workflows | https://code.claude.com/docs/en/common-workflows |
| Mintlify — CC cho Tech Writing | https://www.mintlify.com/blog/how-mintlify-uses-claude-code-as-a-technical-writing-assistant |

Cho tôi xem file trước khi save.
```

### Verification — S15

```bash
# Check file tồn tại và có nội dung
wc -l guide/reference/claude-code-setup.md
# Expected: >150 lines

# Check 7 sections
grep -c "^## " guide/reference/claude-code-setup.md
# Expected: 7

# Check emoji compliance
python3 -c "
import re
allowed = set('⚠️✅❌🔴🟡🟢🔵')
emoji_pattern = re.compile(r'[\U0001F600-\U0001F9FF\U00002702-\U000027B0\U0001FA00-\U0001FAFF]')
with open('guide/reference/claude-code-setup.md') as f:
    for i, line in enumerate(f, 1):
        for m in emoji_pattern.finditer(line):
            if m.group() not in allowed:
                print(f'Line {i}: {m.group()}')
"
# Expected: 0 banned emoji

# Check source markers
grep -c "Nguồn:" guide/reference/claude-code-setup.md
# Expected: >=3

/checkpoint
```

**Thành công khi:** File có 7 sections, 0 banned emoji, source markers đầy đủ. Báo Cowork.

---

## S16 — Module 12 Skeleton

**Phase:** 4B (Claude Code Documentation)
**Plan task:** 4B.2 (D9-B)
**Model:** Sonnet
**Branch:** tiếp tục `feat/claude-code-docs`
**Estimated:** 1-2 giờ

### Bước 1: Orientation

```
/start
```

### Bước 2: Tạo Module 12 skeleton

**Prompt:**

```text
Tạo file mới guide/12-claude-code-documentation.md.

Module header format chuẩn:

# Module 12: Claude Code cho Documentation & Technical Writing

**Thời gian đọc:** 35 phút | **Mức độ:** Intermediate
**Cập nhật:** 2026-03-XX | Models: xem [specs](../reference/model-specs.md)

---

Module này hướng dẫn sử dụng Claude Code — CLI agent chạy trong terminal — cho documentation và technical writing workflow. Nếu bạn không viết code, đây vẫn là công cụ mạnh cho quản lý tài liệu có Git, batch editing, và quality assurance tự động.

> [!NOTE]
> Module này focus vào **non-coding documentation workflow**. Nếu bạn dùng Claude Code để viết code, tham khảo official docs tại https://code.claude.com/docs.
> Nếu bạn chỉ cần tạo/sửa file đơn lẻ mà không cần Git → xem [Module 10: Cowork](10-claude-desktop-cowork.md).

**Config & Commands reference:** [Claude Code Setup](../reference/claude-code-setup.md)

---

Sau đó tạo 15 section headers với intro paragraph (3-5 dòng) mỗi section:

## 12.1 Claude Code là gì — cho Non-coders
[Intro: CC là CLI agent, dùng chung kiến trúc với Cowork nhưng chạy trong terminal, có Git tích hợp. Bảng so sánh CC vs Cowork vs claude.ai — khi nào dùng cái nào cho documentation.]

## 12.2 Cài đặt & First Session
[Intro: Cài đặt, --version, first session, /init. Link: reference/claude-code-setup.md#quick-setup-checklist]

## 12.3 Cấu hình 4 lớp
[Intro: User → Project → Local → Managed. CLAUDE.md template, .claude/rules/, Include/Exclude. Link: reference/claude-code-setup.md#claudemd-reference]

## 12.4 Plan Mode — Explore → Plan → Execute → Commit
[Intro: 4-phase workflow, Ctrl+G, khi nào skip plan. Ví dụ: lập kế hoạch rewrite 1 module.]

## 12.5 Slash Commands & Custom Commands
[Intro: .claude/commands/, tạo custom commands cho doc project. Ví dụ từ Guide Claude: /start, /checkpoint, /validate-doc]

## 12.6 Skills cho Documentation
[Intro: invocable vs reference, tạo custom skill, disable-model-invocation, context cost. Ví dụ: doc-standard-enforcer. Link: reference/skills-list.md]

## 12.7 Subagents cho Review & Research
[Intro: Writer/Reviewer pattern, .claude/agents/ template, khi nào dùng subagent vs main session. Ví dụ: subagent review SOP.]

## 12.8 Session Management
[Intro: /clear, /rewind, /rename, --continue, --resume, /compact. Failure patterns: kitchen sink, over-correction. Link: reference/claude-code-setup.md#essential-commands]

## 12.9 Git Integration cho Documentation
[Intro: Branch naming, commit conventions, pre-commit hooks, SessionStart hook. Ví dụ từ Guide Claude.]

## 12.10 Verification & Quality Assurance
[Intro: Self-verification patterns, /validate-doc, cross-ref-checker. "Highest-leverage thing" = cho Claude cách tự kiểm tra.]

## 12.11 Permissions & Safety
[Intro: /permissions, allow/deny patterns, sandbox mode. Link: reference/claude-code-setup.md#permission-templates]

## 12.12 Token Optimization & Cost
[Intro: Model selection (link flowchart), /compact, offset/limit, effort level, status line. Link: reference/model-specs.md]

## 12.13 Batch & Automation
[Intro: claude -p, pipe in/out, CI integration, fan-out. Ví dụ: lint docs trong PR.]

## 12.14 Plugins & MCP cho Documentation
[Intro: /plugin marketplace, relevant plugins (GitHub, Notion), claude mcp add.]

## 12.15 External Resources & Further Reading
[Intro: Curated links, community resources. Link: reference/claude-code-setup.md#external-links]

Mỗi section body là intro paragraph + "[Full content sẽ viết ở S17/S18]".
Cross-link placeholders phải dùng relative paths đúng.

Cho tôi xem file trước khi save.
```

### Verification — S16

```bash
# Check file tồn tại
wc -l guide/12-claude-code-documentation.md
# Expected: >100 lines

# Check 15 sections
grep -c "^## 12\." guide/12-claude-code-documentation.md
# Expected: 15

# Check cross-link placeholders
grep -c "reference/" guide/12-claude-code-documentation.md
# Expected: >=5

# Check emoji compliance
python3 -c "
import re
allowed = set('⚠️✅❌🔴🟡🟢🔵')
emoji_pattern = re.compile(r'[\U0001F600-\U0001F9FF\U00002702-\U000027B0\U0001FA00-\U0001FAFF]')
with open('guide/12-claude-code-documentation.md') as f:
    for i, line in enumerate(f, 1):
        for m in emoji_pattern.finditer(line):
            if m.group() not in allowed:
                print(f'Line {i}: {m.group()}')
"
# Expected: 0 banned emoji

/checkpoint
```

**Thành công khi:** 15 sections, cross-links đúng format, 0 banned emoji. Báo Cowork.

---

## S17 — Module 12 Content Part 1 (12.1-12.8)

**Phase:** 4B (Claude Code Documentation)
**Plan task:** 4B.3 (D9-C part 1)
**Model:** Sonnet cho hầu hết. Switch Opus cho 12.7 (subagent design).
**Branch:** tiếp tục `feat/claude-code-docs`
**Estimated:** 3-4 giờ

### Bước 1: Orientation

```
/start
```

### Bước 2: Viết sections 12.1-12.4

**Prompt:**

```text
Đọc các file:
- guide/12-claude-code-documentation.md (skeleton đã tạo ở S16)
- guide/reference/claude-code-setup.md (reference cho cross-links)
- guide/10-claude-desktop-cowork.md (mục 10.1, 10.12 — để consistent)

Viết full content cho sections 12.1-12.4. Thay thế placeholder "[Full content...]".

Quy tắc viết:
- Documentation/Technical Writing context — KHÔNG phải coding
- Ví dụ thực tế cho documentation workflow (viết SOP, review tài liệu, quản lý glossary)
- Source markers: [Nguồn: Claude Code Docs] cho facts từ official docs
- [Ứng dụng Kỹ thuật] cho applied examples
- Tuân thủ Icon & Emoji Rules (.claude/CLAUDE.md)
- Cross-links dùng relative paths

12.1: Bảng so sánh CC vs Cowork vs claude.ai cho documentation (mở rộng từ 10.12, thêm chi tiết)
12.2: Step-by-step cài đặt + first session walkthrough. Link đến reference/claude-code-setup.md
12.3: 4-scope system giải thích chi tiết + template CLAUDE.md (link reference) + .claude/rules/ path-specific example
12.4: Plan Mode 4-phase với ví dụ cụ thể: "Lập kế hoạch rewrite Module 05 từ AMR-focused sang Documentation-first"

Mỗi section 40-80 dòng. Cho tôi xem diff từng section trước khi save.
```

### Bước 3: Viết sections 12.5-12.6

**Prompt:**

```text
Tiếp tục viết guide/12-claude-code-documentation.md — sections 12.5-12.6.

Đọc thêm:
- guide/reference/skills-list.md (skill ecosystem, trust labels)
- .claude/commands/ (ví dụ thực tế slash commands)
- .claude/skills/ (ví dụ thực tế skills)

12.5: Slash Commands
- Giải thích .claude/commands/ structure
- 4 commands thiết yếu: /start, /checkpoint, /validate-doc, /weekly-review (ví dụ từ Guide Claude)
- Cách tạo custom command mới cho doc project
- Link skill vs command: khi nào dùng cái nào

12.6: Skills cho Documentation
- Skills ecosystem overview (link skills-list.md)
- Invocable vs Reference skills — ví dụ documentation context
- Tạo custom skill: doc-standard-enforcer example
- disable-model-invocation: khi nào dùng
- Context cost: skill descriptions load mỗi session

Mỗi section 50-80 dòng. Cho tôi xem diff trước khi save.
```

### Bước 4: Viết sections 12.7-12.8

**Prompt (switch Opus cho 12.7 nếu cần):**

```text
Tiếp tục viết guide/12-claude-code-documentation.md — sections 12.7-12.8.

12.7: Subagents cho Review & Research
- Concept: subagent chạy trong isolated context, trả về summary
- Writer/Reviewer pattern cho documentation:
  Session A: "Viết SOP cho quy trình onboarding"
  Session B: "Review SOP vừa viết, check consistency với existing SOPs, style guide compliance"
- .claude/agents/ template:
  ```markdown
  ---
  name: doc-reviewer
  description: Reviews documentation for quality
  tools: Read, Grep, Glob, Bash
  model: sonnet
  ---
  Bạn là document reviewer. Kiểm tra:
  - Heading hierarchy (không skip level)
  - Cross-link integrity
  - Terminology consistency
  - Style guide compliance
  ```
- Khi nào dùng subagent vs main session (context full, parallel tasks, specialized review)

12.8: Session Management
- /clear — QUAN TRỌNG NHẤT. Clear giữa tasks không liên quan.
- /rewind — undo mistakes, restore code + conversation
- /compact — khi context đầy, custom instructions
- /rename — naming sessions cho dễ tìm
- --continue, --resume — resume sessions
- 3 failure patterns (adapt từ official best practices):
  1. Kitchen sink session — quá nhiều tasks trong 1 session → /clear
  2. Over-correction — sửa nhiều lần cùng lỗi → /clear + prompt mới tốt hơn
  3. Over-specified CLAUDE.md — quá dài, rules bị ignore → prune

Mỗi section 50-100 dòng. Cho tôi xem diff trước khi save.
```

### Verification — S17

```bash
# Check sections written (không còn placeholder)
grep -c "Full content sẽ viết" guide/12-claude-code-documentation.md
# Expected: 7 (sections 12.9-12.15 chưa viết)

# Check 12.1-12.8 có content
for i in 1 2 3 4 5 6 7 8; do
  echo "--- 12.$i ---"
  sed -n "/^## 12\.$i /,/^## 12\.$((i+1)) /p" guide/12-claude-code-documentation.md | wc -l
done
# Expected: mỗi section >30 dòng

# Check cross-links
grep -c "reference/" guide/12-claude-code-documentation.md
# Expected: >=8

# Validate
/validate-doc 12

/checkpoint
```

**Thành công khi:** 8 sections có full content, validate pass. Báo Cowork.

---

## S18 — Module 12 Content Part 2 (12.9-12.15)

**Phase:** 4B (Claude Code Documentation)
**Plan task:** 4B.4 (D9-C part 2)
**Model:** Sonnet
**Branch:** tiếp tục `feat/claude-code-docs`
**Estimated:** 3-4 giờ

### Bước 1: Orientation

```
/start
```

### Bước 2: Viết sections 12.9-12.12

**Prompt:**

```text
Đọc guide/12-claude-code-documentation.md (sections 12.1-12.8 đã viết).
Đọc guide/reference/claude-code-setup.md (reference).

Viết sections 12.9-12.12:

12.9: Git Integration cho Documentation
- Branch naming cho doc project: feat/add-module-07, fix/broken-crosslinks, docs/update-readme
- Commit message conventions (tiếng Việt hoặc English tùy team)
- Pre-commit hook: validate heading hierarchy, check broken links, check VERSION
- SessionStart hook: inject context tự động
- Ví dụ thực tế từ Guide Claude project

12.10: Verification & Quality Assurance
- "Give Claude a way to verify its work" — highest-leverage practice [Nguồn: Claude Code Docs]
- Self-verification patterns cho documentation:
  | Strategy | Ví dụ |
  |----------|-------|
  | Provide verification criteria | "Viết SOP, sau đó kiểm tra: mỗi step có action verb, heading hierarchy đúng" |
  | Automated checks | /validate-doc, cross-ref-checker skill |
  | Subagent review | "Dùng subagent review Module 03 cho consistency" |
- Mintlify lesson: "Don't publish something just because Claude suggested it." [Nguồn: Mintlify Blog]

12.11: Permissions & Safety
- /permissions — xem rules hiện tại
- allow/deny patterns (link reference file)
- Sandbox mode — khi nào hữu ích cho doc review
- --dangerously-skip-permissions — CẢNH BÁO, chỉ dùng trong sandbox

12.12: Token Optimization & Cost
- Model selection (link model-specs.md flowchart)
- /compact custom: "/compact Focus on API changes"
- Đọc file thông minh: offset/limit cho file >500 dòng
- Effort level: CLAUDE_CODE_EFFORT_LEVEL
- Slash commands tiết kiệm token (5 tokens vs 200 tokens)
- Auto-activate skills: 0 prompt tokens

Mỗi section 40-80 dòng. Cho tôi xem diff trước khi save.
```

### Bước 3: Viết sections 12.13-12.15

**Prompt:**

```text
Tiếp tục guide/12-claude-code-documentation.md — sections 12.13-12.15.

12.13: Batch & Automation
- claude -p "prompt" — non-interactive mode
  Ví dụ: claude -p "Scan guide/ tìm broken cross-links, output dạng CSV"
- Pipe in/out:
  Ví dụ: cat guide/05-workflow-recipes.md | claude -p "Liệt kê tất cả recipe names"
- CI integration: chạy docs linting trong GitHub Actions / pre-commit
- Fan-out pattern:
  ```bash
  for file in guide/*.md; do
    claude -p "Check heading hierarchy in $file. Return OK or list violations." \
      --allowedTools "Read"
  done
  ```
- --output-format json cho structured output

12.14: Plugins & MCP cho Documentation
- /plugin — browse marketplace
- Relevant plugins: GitHub (PR management), Notion (knowledge base), Slack (notifications)
- claude mcp add — connect external services
- Ví dụ: query Notion database cho cross-reference checking
- "MCP provides tools, Skills teach how to use them" [Nguồn: Claude Code Docs]

12.15: External Resources & Further Reading
- Bảng curated links (từ reference/claude-code-setup.md nhưng dạng annotated):
  | Resource | Mô tả | Khi nào đọc |
  |----------|-------|-------------|
  | Best Practices | Hướng dẫn tổng thể | Đọc đầu tiên |
  | Extend Claude Code | Feature comparison matrix | Khi cần chọn skill vs hook vs MCP |
  | ... | ... | ... |
- Community: Mintlify blog, ClaudeLog
- Link Module 10 (Cowork) cho comparison
- Link Module 05 (Workflow Recipes) cho documentation patterns

Mỗi section 30-60 dòng. Cho tôi xem diff trước khi save.
```

### Verification — S18

```bash
# Check NO placeholder left
grep -c "Full content sẽ viết" guide/12-claude-code-documentation.md
# Expected: 0

# Check total length
wc -l guide/12-claude-code-documentation.md
# Expected: 600-1200 lines

# Check 15 sections all have content
grep -c "^## 12\." guide/12-claude-code-documentation.md
# Expected: 15

# Check source markers
grep -c "Nguồn:" guide/12-claude-code-documentation.md
# Expected: >=10

# Check external links section
grep -c "https://" guide/12-claude-code-documentation.md
# Expected: >=15

# Deep review
/validate-doc 12
/review-module 12

/checkpoint
```

**Thành công khi:** Toàn bộ 15 sections viết xong, review pass. Báo Cowork.

---

## S19 — Refactor Module 10 + Update Cross-refs

**Phase:** 4B (Claude Code Documentation)
**Plan task:** 4B.5 (D9-D)
**Model:** Sonnet
**Branch:** tiếp tục `feat/claude-code-docs`
**Estimated:** 2-3 giờ

### Bước 1: Orientation

```
/start
```

### Bước 2: Refactor Module 10.13

**Prompt:**

```text
Đọc guide/10-claude-desktop-cowork.md — đặc biệt mục 10.13 và các subsections.

Refactor 10.13:
- GIỮ LẠI: heading "## 10.13 Claude Code cho Documentation Workflow" + 1 intro paragraph ngắn (5-7 dòng)
- Intro mới:

  Claude Code (CC) là CLI agent chạy trong terminal, dùng chung kiến trúc agent với Cowork nhưng tối ưu cho workflow có Git. Với sự phát triển của CC, nội dung hướng dẫn chi tiết đã được chuyển sang module riêng.

  > [!NOTE]
  > **Hướng dẫn đầy đủ:** [Module 12: Claude Code cho Documentation & Technical Writing](12-claude-code-documentation.md)
  > **Config & Commands reference:** [Claude Code Setup](reference/claude-code-setup.md)

- XÓA: toàn bộ 10.13.1 → 10.13.5 (đã chuyển sang Module 12)
- GIỮ: 10.12 (bảng so sánh) — update link "Xem chi tiết Claude Code → Module 12"
- GIỮ: 10.14 trở đi không thay đổi

Cho tôi xem diff trước khi save.
```

### Bước 3: Update Module 00

**Prompt:**

```text
Đọc guide/00-overview.md.

Cập nhật:

1. Tiêu đề "## Cấu trúc 12 Modules" → "## Cấu trúc 13 Modules"

2. Bảng modules — thêm row:
   | **12** | Claude Code cho Documentation | Claude Code workflow, setup, skills, subagents cho technical writing | Intermediate |

3. Learning Paths — Path C (Power User), thêm Module 12:
   Sau Module 10/11, thêm:
   12 Claude Code cho Documentation (nếu dùng CC)

4. Kiểm tra heading "12 Modules" còn xuất hiện ở đâu trong file → thay thành "13 Modules"

Cho tôi xem diff trước khi save.
```

### Bước 4: Update cross-references

**Prompt:**

```text
Tìm và update cross-references đến 10.13 trong toàn bộ project:

1. guide/04-context-management.md dòng ~394: "Module 10 (mục 10.13)" → "Module 12"
2. .claude/CLAUDE.md:
   - Folder structure section: thêm `guide/12-claude-code-documentation.md`
   - Module status table: thêm row | 12 | New v6.5 — Claude Code Documentation 🔵 |
3. project-state.md: update module count và structure nếu cần

Scan toàn bộ guide/ cho bất kỳ reference nào đến "10.13" mà chưa update:
grep -r "10\.13" guide/

Cho tôi xem từng thay đổi trước khi save.
```

### Verification — S19

```bash
# Check Module 10.13 chỉ còn intro
grep -c "^### 10\.13\." guide/10-claude-desktop-cowork.md
# Expected: 0 (không còn subsections 10.13.X)

# Check Module 00 có 13 modules
grep -c "13 Modules" guide/00-overview.md
# Expected: >=1

# Check Module 12 row in overview table
grep "Claude Code cho Documentation" guide/00-overview.md
# Expected: 1 match

# Check cross-refs updated
grep -r "10\.13\." guide/ | grep -v "10-claude-desktop-cowork.md"
# Expected: 0 results (không còn refs đến 10.13.X ngoài Module 10)

# Check .claude/CLAUDE.md updated
grep "12-claude-code" .claude/CLAUDE.md
# Expected: >=1

# Full cross-ref check
# Chạy cross-ref-checker

/checkpoint
```

**Thành công khi:** Refactor sạch, cross-refs đúng, checker pass. Báo Cowork.
**Milestone:** Sẵn sàng bump v6.5. Phase 4B hoàn tất.

---

## S20 — Dependency Tags

**Phase:** 5 (Process Maturity)
**Plan task:** 5.1 (D7-P2)
**Model:** Sonnet
**Branch:** `feat/process-maturity`
**Estimated:** 2 giờ

> **Lưu ý:** Session này cover **13 modules** (thêm Module 12 so với plan v1).

### Bước 1: Orientation + Branch

```
/start
git checkout -b feat/process-maturity
```

### Bước 2: Thêm dependency tags

**Prompt:**

```text
Đọc tất cả 13 files module trong guide/ (00-overview.md đến 12-claude-code-documentation.md).

Thêm metadata block ngay sau module header (trước content) cho mỗi module:

---
depends-on: [list of module files this module references]
impacts: [list of module files that reference this module]
---

Ví dụ cho Module 12:
---
depends-on: [reference/model-specs, reference/skills-list, reference/claude-code-setup, 10-claude-desktop-cowork]
impacts: [00-overview, 04-context-management]
---

Scan cross-links trong mỗi file để xác định dependencies chính xác.
Liệt kê 13 modules với proposed metadata để tôi review trước khi edit.
```

### Bước 3: Tạo dependency graph

**Prompt (sau khi review metadata):**

```text
Dựa trên metadata đã thêm, tạo Mermaid dependency graph.
Thêm vào guide/00-overview.md SAU bảng modules, TRƯỚC Learning Paths.

Heading: ### Dependency Graph

Graph bao gồm 13 modules + 3 reference files.
Dùng color coding: 🟢 (core), 🔵 (reference), 🟡 (workflow).
```

### Verification — S20

```bash
# Check metadata exists in all modules
for f in guide/0*.md guide/1*.md; do
  echo "$f: $(grep -c 'depends-on:' $f)"
done
# Expected: mỗi file = 1

# Check Mermaid graph in 00-overview
grep -c "graph\|flowchart" guide/00-overview.md
# Expected: >=1

/checkpoint
```

**Thành công khi:** 13 modules có metadata, graph render đúng. Báo Cowork.

---

## S21 — Upgrade Skill

**Phase:** 5 (Process Maturity)
**Plan task:** 5.2 (D7-P3)
**Model:** Opus — thiết kế skill phức tạp
**Branch:** tiếp tục `feat/process-maturity`
**Estimated:** 2-3 giờ

> **Lưu ý:** Skill cần cover **13 modules + 3 reference files** (thêm Module 12 và claude-code-setup.md so với plan v1).

### Bước 1: Orientation

```
/start
```

### Bước 2: Tạo upgrade skill

**Prompt:**

```text
Tạo skill mới: .claude/skills/upgrade-guide/SKILL.md

Purpose: Tự động scan Guide Claude project, phát hiện stale data, broken refs, dependency warnings.

Skill definition:

---
name: upgrade-guide
description: Scan Guide Claude project for stale data, broken references, and dependency issues. Use when planning updates or checking project health.
---

Input: $ARGUMENTS — module number (vd "03") hoặc "all"

Workflow:
1. Đọc VERSION — lấy current version
2. Nếu "all": scan toàn bộ 13 modules + 3 reference files
   Nếu module number: scan module đó + files nó depends-on
3. Check từng file:
   - [Cập nhật MM/YYYY] markers: flag nếu >3 tháng cũ
   - Cross-links: verify target files tồn tại
   - depends-on metadata: verify referenced files tồn tại
   - Volatile data: check hardcoded model names, version numbers, pricing
   - Emoji compliance: scan cho banned emoji
4. Output report:

   ## Upgrade Report — {{scope}}
   **Version:** {{version}} | **Date:** {{date}}

   ### Stale Content
   | File | Marker | Age | Recommendation |
   ...

   ### Broken References
   | File | Line | Link | Status |
   ...

   ### Dependency Warnings
   | File | Issue |
   ...

   ### Emoji Violations
   (nếu có)

   ### Summary
   X files scanned. Y issues found.

Cho tôi xem SKILL.md trước khi save.
```

### Verification — S21

```bash
# Check skill file exists
ls -la .claude/skills/upgrade-guide/SKILL.md
# Expected: file exists

# Test skill
# Gọi: /upgrade-guide 12
# Expected: report cho Module 12

# Test all
# Gọi: /upgrade-guide all
# Expected: report cho toàn bộ project

/checkpoint
```

**Thành công khi:** Skill hoạt động cho cả single module và "all". Báo Cowork.

---

## S22 — Final Consistency Check

**Phase:** 5 (Process Maturity)
**Plan task:** 5.3
**Model:** Sonnet (main) + Opus subagent cho deep review
**Branch:** tiếp tục `feat/process-maturity`
**Estimated:** 2-3 giờ

### Bước 1: Orientation

```
/start
```

### Bước 2: Run upgrade skill

```
/upgrade-guide all
```

Review output. Fix issues nếu có.

### Bước 3: Terminology consistency check

**Prompt:**

```text
Scan toàn bộ guide/ cho terminology inconsistency:

1. "Claude Code" vs "CC" — standardize: dùng "Claude Code" lần đầu nhắc trong mỗi section, sau đó dùng "CC" viết tắt. Check file 12-claude-code-documentation.md đặc biệt.

2. "Cowork" vs "cowork" — capitalize: luôn "Cowork"

3. Model names: "Opus 4.6" vs "Claude Opus 4.6" — standardize theo model-specs.md

4. "Skills" vs "skills" — capitalize: "Skills" khi nhắc đến feature name, "skills" khi nói chung

Liệt kê inconsistencies tìm thấy. Cho tôi review trước khi fix.
```

### Bước 4: Deep review Module 12

**Prompt:**

```text
Dùng subagent review guide/12-claude-code-documentation.md:

Tiêu chí review:
- Accuracy: facts khớp với official Claude Code docs (cross-check source markers)
- Completeness: 15 sections đều có nội dung substantive (không chỉ là intro)
- Consistency: terminology, formatting, icon policy đúng quy định
- Actionability: ví dụ có thể follow ngay, không mơ hồ
- Cross-refs: tất cả links hoạt động

Output: report với score 1-5 cho mỗi tiêu chí + specific issues cần fix.
```

### Verification — S22

```bash
# Full cross-ref check
# Chạy cross-ref-checker

# Emoji final scan
python3 -c "
import re, glob
allowed = set('⚠️✅❌🔴🟡🟢🔵')
emoji_pattern = re.compile(r'[\U0001F600-\U0001F9FF\U00002702-\U000027B0\U0001FA00-\U0001FAFF]')
for f in glob.glob('guide/**/*.md', recursive=True) + glob.glob('.claude/**/*.md', recursive=True):
    for i, line in enumerate(open(f), 1):
        for m in emoji_pattern.finditer(line):
            if m.group() not in allowed:
                print(f'{f}:{i}: {m.group()}')
"
# Expected: 0

# Total file count check
ls guide/*.md | wc -l
# Expected: 13

ls guide/reference/*.md | wc -l
# Expected: 3 (model-specs, skills-list, claude-code-setup)

/checkpoint
```

**Thành công khi:** 0 issues remaining, all checks pass. Báo Cowork.
**Milestone:** Sẵn sàng bump v7.0. Project upgrade hoàn tất.

---

## Workflow sau mỗi session

### Trên Claude Code (sau khi xong)

1. Chạy verification commands (theo từng session)
2. Nếu PASS: `/checkpoint` với message mô tả task
3. Chuẩn bị báo cáo ngắn: "S0X done. [Số files edited]. [Issues nếu có]."

### Trên Cowork (verify + next)

Paste báo cáo và hỏi:

```text
Session SXX hoàn thành. Kết quả:
- [Mô tả ngắn những gì đã làm]
- [Verification results]
- [Issues nếu có]

Yêu cầu:
1. Verify kết quả có đúng với plan
2. Cập nhật upgrade-plan-v2.md (đánh dấu tasks done)
3. Cho tôi prompt session tiếp theo (SXX+1)
```

---

## Quick Reference — Commands

| Command | Khi nào |
|---------|---------|
| `/start` | Đầu mỗi session |
| `/checkpoint` | Sau khi hoàn thành task |
| `/validate-doc XX` | Sau khi edit module XX |
| `/review-module XX` | Deep review sau khi rewrite module XX |
| `cross-ref-checker` | Sau khi thay đổi links/references |
| `/upgrade-guide XX` | Check stale data, broken refs (sau S21) |

## Quick Reference — Model Selection

| Tình huống | Model |
|-----------|-------|
| Edit nhiều files, search-replace | Sonnet |
| Tạo file mới, drafting content | Sonnet |
| Thiết kế flowchart, architecture | Sonnet (hoặc Opus nếu phức tạp) |
| Review chất lượng examples | Opus |
| Thiết kế subagent/skill (S17, S21) | Opus |
| Final consistency check (S22) | Sonnet + Opus subagent |

## Quick Reference — Version Bumps

| Sau session | Bump to | Trigger |
|-------------|---------|---------|
| S05 | v5.1 | Phase 0+1+2 complete |
| S06 | v5.2 | Phase 3 complete |
| S14 | v6.0 | Phase 4 complete |
| S19 | v6.5 | Phase 4B complete |
| S22 | v7.0 | Phase 5 complete — project upgrade done |
