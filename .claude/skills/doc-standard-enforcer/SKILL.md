---
name: doc-standard-enforcer
description: >
  Manual deep review mode cho guide/ content. Trigger khi user nói "review format",
  "kiểm tra standards", "deep review", hoặc muốn kiểm tra thủ công chất lượng content.
  Enforcement rules tự động đã chuyển sang .claude/rules/writing-standards.md (auto-load)
  và .claude/hooks/format-check.py (PostToolUse hook). Skill này chỉ dùng cho on-demand review.
user-invocable: true
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
---

# Doc Standard Enforcer — Guide Claude Project (Manual Review Mode)

Skill này thực hiện deep review thủ công cho content trong `guide/`. Enforcement tự động đã được chuyển sang:
- `.claude/rules/writing-standards.md` — auto-load khi edit guide/ files
- `.claude/hooks/format-check.py` — PostToolUse hook kiểm tra format sau mỗi Edit/Write

## Khi nào kích hoạt

- User nói "review format", "kiểm tra standards", "deep review content"
- Sau khi edit xong 1 module (manual QA pass)
- Trước phase review gate

## Deep Review Checklist

Khi được trigger, kiểm tra file theo thứ tự:

### 1. Structure Check

- [ ] `#` title chỉ 1 lần, dòng đầu tiên
- [ ] Heading hierarchy `#` > `##` > `###` — không skip level
- [ ] Mỗi `##`/`###` có 1-2 câu context mở đầu
- [ ] Không có đoạn văn > 5 câu liên tục

### 2. Code Block Check

- [ ] Mọi code block có language tag
- [ ] Syntax trong code block chính xác
- [ ] Code examples chạy được (nếu applicable)

### 3. Cross-link Check

- [ ] Links dùng relative path
- [ ] Không có hardcoded version numbers
- [ ] Tất cả links trỏ đến file/section tồn tại

### 4. Source Marker Check

- [ ] Feature sections có source marker (Tier 1/2/3)
- [ ] Time-sensitive content có `[Cập nhật MM/YYYY]`
- [ ] Tier 3 content có disclaimer

### 5. Language Check

- [ ] Tiếng Việt là ngôn ngữ chính
- [ ] Thuật ngữ kỹ thuật giữ tiếng Anh
- [ ] Emoji chỉ dùng allowlist (trong bảng/status markers)
- [ ] Prose dùng Obsidian callout syntax

### 6. Content Quality Check

- [ ] Thông tin chính xác (cross-check với source nếu cần)
- [ ] Không có nội dung duplicate với module khác
- [ ] Audience-appropriate (base vs doc vs dev)

## Output Format

```
## Doc Standard Review — [file name]

### Results
- Structure: ✅ / ❌ [details]
- Code Blocks: ✅ / ❌ [details]
- Cross-links: ✅ / ❌ [details]
- Source Markers: ✅ / ❌ [details]
- Language: ✅ / ❌ [details]
- Content Quality: ✅ / ❌ [details]

### Issues Found: [count]
[List chi tiết]

### Score: [X/6 passed]
```

## Rules

- KHÔNG tự ý sửa file — chỉ report
- Report cụ thể: file, line number, issue, suggested fix
- Nếu không tìm thấy issues → output "All 6 checks PASS"
- Hỏi user trước khi sửa: "Fix ngay hay ghi vào checklist?"

## So sánh với automation

| Aspect | Automation (rules + hook) | Skill (manual review) |
|--------|--------------------------|----------------------|
| Khi nào | Mỗi lần edit | User trigger |
| Check gì | Format (heading, code tags, emoji) | Format + content + quality |
| Action | Warning → Claude self-correct | Report → user decide |
| Depth | Surface (syntax) | Deep (semantics + accuracy) |
