---
paths:
  - "guide/**/*.md"
---

# Writing Standards — Guide Claude Project

Rules này tự động load khi Claude edit bất kỳ file nào trong guide/.

## Verification Requirements

- Mỗi section mô tả feature/behavior PHẢI có source marker
- Tier 1 claims: `[Nguồn: Claude Code Docs]` hoặc tương đương
- Tier 3 claims: PHẢI có disclaimer `[Ghi chú: ...]`
- Thông tin time-sensitive: bắt buộc `[Cập nhật MM/YYYY]`

## Format Rules

- Heading hierarchy: `#` → `##` → `###` — KHÔNG skip level (VD: `##` → `####` là SAI)
- Code blocks: LUÔN có language tag (`python`, `yaml`, `bash`, `markdown`...) — KHÔNG dùng ``` không tag
- Mỗi `##` hoặc `###` bắt đầu bằng 1-2 câu context trước khi đi vào chi tiết
- Tránh đoạn văn > 5 câu liên tục — break bằng list, code block, hoặc sub-heading

## Language Rules

- Tiếng Việt là ngôn ngữ chính
- Thuật ngữ kỹ thuật giữ tiếng Anh — KHÔNG Việt hóa (AMR, ROS, SLAM, Lidar, skill, hook, prompt, context window, token, API...)
- Placeholders: `{{variable}}`

## Cross-links

- Dùng relative path: `[tên](../base/04-context-management.md#section-name)`
- KHÔNG dùng absolute path hoặc URL đến repo
- KHÔNG hardcode version numbers — link về `../VERSION`

## Source Markers

- `[Nguồn: ...]` — official documentation (Tier 1-2)
- `[Ứng dụng Kỹ thuật]` — applied examples từ Phenikaa-X context
- `[Cập nhật MM/YYYY]` — thông tin time-sensitive
- `[Ghi chú: ...]` — non-official patterns (Tier 3)

## Emoji Rules

- ALLOWED (chỉ trong bảng và status markers): ⚠️ ✅ ❌ 🔴 🟡 🟢 🔵
- Prose warnings/tips/notes: dùng Obsidian callout syntax (`> [!WARNING]`, `> [!TIP]`, `> [!NOTE]`, `> [!IMPORTANT]`)
