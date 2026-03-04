# Session Guide — Upgrade Plan Execution

**Tạo:** 2026-03-04 | **Dùng với:** `_process/upgrade-plan.md`

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
# Grep emoji banned — kỳ vọng 0 kết quả
# (chạy trên Claude Code, dùng grep với unicode ranges)
grep -rP '[\x{1F600}-\x{1F64F}\x{1F680}-\x{1F6FF}\x{2728}\x{1F4A1}\x{1F4CC}\x{1F3AF}\x{1F525}]' guide/ .claude/
# Expected: 0 matches (trừ allowlist)

# Cross-ref check
# Chạy skill cross-ref-checker

/checkpoint
```

**Thành công khi:** Grep trả về 0 banned emoji. Báo Cowork.

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

# Check số dòng trong mapping table
grep -c "|.*|.*|.*|" guide/reference/skills-list.md | tail -1
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

## S15 — Dependency Tags

**Phase:** 5 (Process Maturity)
**Plan task:** 5.1 (D7-P2)
**Model:** Sonnet
**Chi tiết:** Lập kế hoạch cụ thể sau khi Phase 4 hoàn thành.

---

## S16 — Upgrade Skill

**Phase:** 5 (Process Maturity)
**Plan task:** 5.2 (D7-P3)
**Model:** Opus — thiết kế skill phức tạp
**Chi tiết:** Lập kế hoạch cụ thể sau khi Phase 4 hoàn thành.

---

## Workflow sau mỗi session

### Trên Claude Code (sau khi xong)

1. Chạy verification commands (theo từng session)
2. Nếu PASS: `/checkpoint` với message mô tả task
3. Chuẩn bị báo cáo ngắn: "S0X done. [Số files edited]. [Issues nếu có]."

### Trên Cowork (verify + next)

Paste báo cáo và hỏi:

```text
Session S0X hoàn thành. Kết quả:
- [Mô tả ngắn những gì đã làm]
- [Verification results]
- [Issues nếu có]

Yêu cầu:
1. Verify kết quả có đúng với plan
2. Cập nhật upgrade-plan.md (đánh dấu tasks done)
3. Cho tôi prompt session tiếp theo (S0Y)
```

Cowork sẽ:
- Đọc lại plan, check alignment
- Cập nhật status trong upgrade-plan.md
- Điều chỉnh session tiếp theo nếu cần (dựa trên kết quả thực tế)
- Trả về session guide cho session tiếp

---

## Quick Reference — Commands

| Command | Khi nào |
|---------|---------|
| `/start` | Đầu mỗi session |
| `/checkpoint` | Sau khi hoàn thành task |
| `/validate-doc XX` | Sau khi edit module XX |
| `/review-module XX` | Deep review sau khi rewrite module XX |
| `cross-ref-checker` | Sau khi thay đổi links/references |

## Quick Reference — Model Selection

| Tình huống | Model |
|-----------|-------|
| Edit nhiều files, search-replace | Sonnet |
| Tạo file mới, drafting content | Sonnet |
| Thiết kế flowchart, architecture | Sonnet (hoặc Opus nếu phức tạp) |
| Review chất lượng examples | Opus |
| Tạo skill mới (S16) | Opus |
