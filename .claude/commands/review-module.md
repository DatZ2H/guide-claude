Deep review một module guide. Argument: $ARGUMENTS (số module, vd "03").

**Bước 1 — Resolve và đọc file:**
- Tìm file match `guide/$ARGUMENTS-*.md`
- Đọc file VERSION để biết version hiện tại
- Nếu file > 20KB: ghi note đầu output `⚠️ Module lớn ({size}KB) — recommend /model opus cho review chính xác hơn`

**Bước 2 — Đọc context:**
- Đọc `.claude/CLAUDE.md` — lấy writing standards và language rules
- KHÔNG đọc project-state.md hay modules khác (trừ khi cần verify cross-link)

**Bước 3 — Review theo 5 criteria:**

**1. Content completeness (0-2 điểm)**
- Module có cover đủ topic theo title/scope không
- Có thiếu section quan trọng nào không
- So sánh TOC với expected coverage cho topic đó

**2. Clarity cho đối tượng (0-2 điểm)**
- Đối tượng: kỹ sư tự động hóa, R&D, Robotics tại Phenikaa-X
- Thuật ngữ có giải thích đủ không
- Flow đọc có logic không (concept → example → practice)

**3. Practical examples (0-2 điểm)**
- Có ví dụ cụ thể context AMR/Robotics/Automation không
- Ví dụ có actionable không (copy-paste được prompt/config)
- Có marker `[Ứng dụng Kỹ thuật]` cho applied examples không

**4. Cross-references (0-2 điểm)**
- Có link đến modules liên quan không
- Link có đúng target không (kiểm tra file tồn tại)
- Có link đến config-architecture.md nếu relevant không

**5. Writing standards (0-2 điểm)**
- Heading hierarchy đúng (H1→H2→H3, không skip)
- Code blocks có language tag
- Source markers đúng format
- Version ref đúng (không hardcode)

**Bước 4 — Output format:**

```
## Review: {filename} ({size}KB)

**Score: {tổng}/10**

### Strengths
- {2-3 điểm mạnh}

### Issues
- L{line}: {mô tả cụ thể}
- L{line}: {mô tả cụ thể}
- ...

### Suggestions
- {2-3 đề xuất cải thiện, ưu tiên theo impact}
```

Rules:
- Score phải reflect thực tế — KHÔNG cho điểm cao vô căn cứ
- Issues PHẢI có line reference cụ thể
- Suggestions phải actionable — "thêm ví dụ X vào section Y", không phải "cải thiện ví dụ"
- Tổng output tối đa 30 dòng
- KHÔNG tự sửa file — chỉ review và report
