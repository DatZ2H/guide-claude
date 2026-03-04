# Release Prompts — Guide Claude v5.0 (Internal Review)

**Mục tiêu:** Đưa project đến trạng thái internal review cho team Phenikaa-X
**Scope:** 2 sessions trên Claude Code terminal
**Quyết định:** Changelog Option 1 (trim + CHANGELOG.md), internal release cho team dùng thử

---

## Chuẩn bị

```bash
cd <path-to-Guide-Claude>
/start
git checkout -b release/v5.0-internal
```

---

## Session R1: Content Fixes + Module Review

### Prompt 1 — Fix Module 10 (3 sections thiếu + enterprise plugins)

```text
Đọc guide/10-claude-desktop-cowork.md.

Cần bổ sung 4 thay đổi. Giữ nguyên tone, format, conventions hiện có.
Chèn vào vị trí hợp lý trong flow hiện tại (sau section cuối cùng về features,
trước section "Tiếp theo" cuối file).

**1. Thêm section: Context Compaction (beta)**

## 10.x Context Compaction

[Cập nhật 03/2026]

Context compaction là tính năng beta giúp Cowork tự động nén conversation history
khi session dài. Thay vì bị giới hạn bởi context window, Cowork nén các phần
đã xử lý xong, giữ lại thông tin quan trọng.

Nội dung cần cover (~15 dòng):
- Không cần cấu hình — tự động kích hoạt khi conversation gần đầy context
- Ưu tiên giữ: instructions gần nhất, file paths đang thao tác, decisions đã confirm
- Có thể mất: chi tiết conversation cũ, intermediate outputs
- Tip: nếu Cowork "quên" context quan trọng giữa session dài → nhắc lại trong message tiếp theo
- [Nguồn: Anthropic — Context compaction documentation]

**2. Thêm section: Agent Teams (research preview)**

## 10.x Agent Teams

[Cập nhật 03/2026]

Agent Teams cho phép nhiều Claude agents phối hợp trong một task phức tạp.
Một orchestrator agent điều phối, các sub-agents xử lý chuyên biệt.

Nội dung cần cover (~15 dòng):
- Orchestrator nhận yêu cầu → phân task → giao sub-agents → tổng hợp kết quả
- Mỗi sub-agent có fresh context riêng, không share memory với agent khác
- Phù hợp khi: batch xử lý nhiều files, task cần chuyên môn khác nhau (phân tích + viết + format)
- Research preview — behavior có thể thay đổi, không dùng cho production workflows
- [Ứng dụng Kỹ thuật] Ví dụ: review 20 SOP AMR cùng lúc — orchestrator chia mỗi sub-agent 4 files,
  tổng hợp report cuối cùng
- [Nguồn: Anthropic Blog — Agent Teams research preview]

**3. Thêm section: Troubleshooting**

## 10.x Troubleshooting

Các vấn đề thường gặp khi dùng Cowork và cách xử lý:

Nội dung cover (~25 dòng, dạng bảng hoặc subsections):

| Vấn đề | Nguyên nhân | Giải pháp |
|--------|-------------|-----------|
| Cowork không hiện trong app | Claude Desktop chưa update | Menu → Check for Updates, hoặc download lại từ claude.ai/download |
| VPN bật → Cowork lỗi kết nối | VM routing conflict — issue phổ biến nhất | Tắt VPN trước khi dùng Cowork |
| "Usage limit reached" | Pro ~1-1.5h intensive use, reset mỗi 5h | Chờ reset hoặc upgrade Max ($100-200/mo). Chia task nhỏ để tối ưu quota |
| File không truy cập được | Folder chưa được grant access | Cowork sẽ hỏi quyền → chọn đúng folder. Không grant Documents/Desktop toàn bộ |
| Session chậm, output không đầy đủ | Folder quá nhiều files (>500) | Chia nhỏ folder, hoặc dùng subfolder cụ thể thay vì root folder |
| Claude "quên" context giữa session | Context compaction nén quá mức | Nhắc lại key information trong message mới. Dùng memory.md cho context quan trọng |
| Output sai format (VD: .md thay vì .docx) | Prompt không specify rõ format | Ghi rõ format trong prompt: "Output: filename.docx trong folder output/" |

[Nguồn: Anthropic Help Center — Troubleshooting Cowork]

**4. Update section Plugins — thêm enterprise plugins**

Tìm section về Plugins/Skills (khoảng 10.6). Thêm vào cuối section hoặc tạo
subsection mới:

### Enterprise Plugins & Connectors (02/2026)

[Cập nhật 03/2026]

Từ 24/02/2026, Anthropic ra mắt 13 enterprise connectors mới:

| Loại | Connectors |
|------|-----------|
| Google Workspace | Calendar, Drive, Gmail |
| Sales & Outreach | Apollo, Clay, Outreach, Similarweb |
| Legal & Finance | DocuSign, LegalZoom, FactSet, MSCI |
| Development | Harvey, WordPress |

Cộng với 11 official plugins đã có: Asana, Canva, Cloudflare, Figma, GitHub,
Google Drive, Jira, Linear, Notion, Sentry, Slack.

Với Team/Enterprise plans: admin có thể tạo private marketplace để quản lý
plugins nào team được dùng.

[Ứng dụng Kỹ thuật] Team Phenikaa-X có thể dùng: GitHub plugin (code review,
PR tracking), Jira/Linear (task management), Notion (knowledge base).
Nếu công ty dùng Google Workspace → kết nối Calendar + Drive + Gmail trực tiếp.

[Nguồn: Anthropic Blog — Cowork plugins across enterprise, 24/02/2026]

---

Sau khi thêm xong, kiểm tra:
1. Section numbers có liên tục không (không nhảy số)
2. Heading hierarchy đúng (## section → ### subsection)
3. Cross-link "Tiếp theo" cuối file vẫn đúng
```

### Prompt 2 — Review Module 10

```text
/review-module 10
```

Nếu score < 8.0 → fix issues rồi review lại.

### Prompt 3 — Review Module 11

```text
/review-module 11
```

Nếu score < 8.0 → fix issues rồi review lại.

### Commit sau R1

```text
/checkpoint
```

Message: `Fix Module 10: thêm Context Compaction, Agent Teams, Troubleshooting, enterprise plugins. Review 10+11 passed.`

---

## Session R2: Release Cleanup

### Prompt 4 — Changelog trim (Option 1)

```text
Thực hiện tuần tự:

**Bước 1: Tạo CHANGELOG.md ở root**

Tạo file CHANGELOG.md với nội dung:

```markdown
# Changelog — Claude Guide cho Kỹ sư Phenikaa-X

Lịch sử thay đổi đầy đủ. Version hiện tại: xem `VERSION`.

---

[Copy toàn bộ section "## Thông tin cập nhật" từ guide/00-overview.md vào đây,
giữ nguyên format, KHÔNG sửa nội dung]
```

**Bước 2: Trim 00-overview.md**

Trong guide/00-overview.md, thay thế section "## Thông tin cập nhật" bằng:

## Thông tin cập nhật

### Version 5.0 (03/2026)

[Giữ nguyên nội dung v5.0 hiện có]

### Version 4.2 (03/2026)

[Giữ nguyên nội dung v4.2 hiện có — đây là bản stable trước đó]

> Lịch sử đầy đủ từ v3.0: xem [CHANGELOG.md](../CHANGELOG.md)

[XÓA tất cả versions cũ hơn v4.2 — chúng đã được move sang CHANGELOG.md]

**Bước 3: Verify**

- Đếm dòng 00-overview.md trước và sau → báo cáo giảm bao nhiêu dòng
- CHANGELOG.md có đủ từ v3.0 đến v5.0 không?
- Link ../CHANGELOG.md trong 00-overview.md có valid không?
```

### Prompt 5 — Fix "11 modules" → "12 modules" + metadata updates

```text
Tìm và sửa tất cả chỗ ghi "11 modules" thành "12 modules" trong toàn bộ project.

Files cần check (đọc từng file, sửa nếu tìm thấy):
1. README.md — "11 modules hướng dẫn" → "12 modules hướng dẫn"
2. project-state.md — "Mục tiêu: 11 modules" → "Mục tiêu: 12 modules"
3. .claude/CLAUDE.md — "11 modules" nếu có
4. machine-readable/llms.txt — kiểm tra

Ngoài ra, update các metadata sau:

**project-state.md:**
- Phase: "Development — đang iterate, chưa publish" → "Internal Review — v5.0 cho team Phenikaa-X dùng thử"
- Xóa dòng "Sẵn sàng internal review" ở cuối bảng — thay bằng: "v5.0 released for internal review. Modules 10+11: scored after review cycle."

**.claude/CLAUDE.md:**
- Module status (quick ref):
  ```
  | Range | Status |
  |-------|--------|
  | 00–09 | v4.2 base + v5.0 currency sweep — 🟢 |
  | 10 | Refactored v5.0 — Scheduled Tasks, Security, Troubleshooting 🟢 |
  | 11 | New v5.0 — 12 workflow templates 🔵 |
  | reference/ | config-architecture 🟢, skills-list Updated v5.0 🟢 |
  ```

**README.md:**
- Thêm dòng: `| machine-readable/ | llms.txt — machine-readable index cho AI | AI tools |`
  vào bảng cấu trúc dự án (nếu chưa có)

Báo cáo tất cả files đã sửa và changes cụ thể.
```

### Prompt 6 — Final cross-ref check

```text
Chạy cross-ref check toàn bộ project.

Kiểm tra:
1. Tất cả cross-links trong guide/*.md — có valid target không?
2. Links từ Module 11 → Module 05, 09, 10 — đúng path?
3. Links từ Module 10 → Module 11 — đúng path?
4. Link CHANGELOG.md trong 00-overview.md — valid?
5. README.md links — valid?

Liệt kê mọi broken links.
```

### Prompt 7 — Commit + Tag

```text
/checkpoint
```

Message: `Release cleanup v5.0: trim changelog, fix module count, update metadata for internal review`

Sau đó:

```bash
git checkout master
git merge release/v5.0-internal --no-ff -m "Release v5.0 — internal review cho team Phenikaa-X"
git tag -a v5.0 -m "v5.0: Module 10 refactor, Module 11 new, machine-readable layer, enterprise plugins"
```

---

## Checklist cuối cùng

| # | Task | Session | Done |
|---|------|---------|------|
| 1 | Module 10: thêm Context Compaction section | R1 | ☐ |
| 2 | Module 10: thêm Agent Teams section | R1 | ☐ |
| 3 | Module 10: thêm Troubleshooting section | R1 | ☐ |
| 4 | Module 10: thêm enterprise plugins list | R1 | ☐ |
| 5 | /review-module 10 → score ≥ 8.0 | R1 | ☐ |
| 6 | /review-module 11 → score ≥ 8.0 | R1 | ☐ |
| 7 | Tạo CHANGELOG.md (full history v3.0→v5.0) | R2 | ☐ |
| 8 | Trim 00-overview.md (giữ v5.0 + v4.2 only) | R2 | ☐ |
| 9 | Fix "11 modules" → "12 modules" (4 files) | R2 | ☐ |
| 10 | Update project-state.md phase → "Internal Review" | R2 | ☐ |
| 11 | Update .claude/CLAUDE.md module status | R2 | ☐ |
| 12 | Cross-ref check pass | R2 | ☐ |
| 13 | Merge to master + git tag v5.0 | R2 | ☐ |

---

## Sau khi release — Next steps

1. **Chia sẻ cho team:** Copy folder Guide Claude vào shared drive hoặc push lên GitHub internal
2. **Thu thập feedback:** Tạo form đơn giản hoặc dùng Notion page để team ghi feedback
3. **Focus areas cho feedback:**
   - Module 10 + 11 có actionable không? Workflows có dùng được thực tế không?
   - Có thiếu workflow nào team cần mà chưa có?
   - Terminology có consistent với cách team nói không?
4. **Timeline:** 1-2 tuần internal review → collect feedback → plan v5.1 fixes

---

*File này là planning document — xóa sau khi release hoàn tất.*
