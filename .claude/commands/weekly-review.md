Chạy weekly review cho Guide Claude project. Thực hiện tuần tự 5 bước:

**Bước 1 — Git activity tuần qua:**
- Chạy `git log --since="1 week ago" --oneline` — đếm số commits
- Chạy `git diff --stat HEAD~$(git rev-list --count --since="1 week ago" HEAD) HEAD 2>/dev/null` hoặc tương đương — đếm số files changed
- Nếu không có commit tuần qua: ghi "No commits this week" và vẫn tiếp tục các bước sau

**Bước 2 — Cross-link consistency (scan nhẹ):**
- Với mỗi file `guide/[00-10]-*.md` (11 files, BỎ QUA .bak):
  - Dùng Grep tìm pattern `]\(` — lấy tất cả markdown links
  - Chỉ check relative links (bỏ http/https, bỏ anchor-only `#...`)
  - Verify file target tồn tại bằng Glob
- Ghi nhận broken links (nếu có)
- KHÔNG đọc full file content — chỉ grep links

**Bước 3 — Glossary consistency (scan nhẹ):**
- Grep các thuật ngữ quan trọng across 11 modules, check dùng nhất quán:
  - "Cowork" vs "cowork" vs "Co-work"
  - "Claude Code" vs "Claude code" vs "CC"
  - "context window" vs "cửa sổ ngữ cảnh"
  - "prompt" vs "câu lệnh"
  - "token" vs "tokens"
  - "skill" vs "kỹ năng"
  - "hook" vs "hooks"
- Flag: module nào dùng sai variant (variant đúng = variant phổ biến nhất trong project)
- KHÔNG đọc full file — chỉ grep từng term

**Bước 4 — Output summary:**

Format cố định:

```
## Weekly Review — {ngày hôm nay}

**Tuần này:** {X} commits, {Y} files changed
**Modules:** 11 scanned

### Cross-link issues
- {file:dòng — mô tả} (hoặc "None found ✅")

### Glossary inconsistencies
- {term}: {module dùng sai} dùng "{variant sai}" — nên là "{variant đúng}" (hoặc "All consistent ✅")

### Tóm tắt: {X} commits, {Y} files changed, {Z} issues found
```

**Bước 5 — Priority tasks cho tuần tới:**
- Dựa trên issues found ở bước 2-3 và module status trong CLAUDE.md
- Suggest 2-3 tasks cụ thể, actionable
- Ưu tiên: fix issues > update outdated modules > new content

Format:
```
### Suggested priorities
1. {task cụ thể — lý do}
2. {task cụ thể — lý do}
3. {task cụ thể — lý do}
```

**Rules:**
- Dùng Sonnet model — KHÔNG cần Opus cho task này
- KHÔNG đọc full content modules — chỉ scan headers, links, terms
- KHÔNG sửa file — chỉ report
- Tổng output KHÔNG quá 40 dòng
- Chạy Grep calls song song khi có thể (bước 2 và bước 3 có thể parallel)
