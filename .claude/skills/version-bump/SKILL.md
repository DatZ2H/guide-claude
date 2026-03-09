---
name: version-bump
description: Workflow bump version cho Guide Claude project: cập nhật VERSION file, thêm changelog entry vào 00-overview.md, update project-state.md. Trigger khi user nói "bump version", "lên version", "release v[X.X]", hoặc "version mới". KHÔNG tự ý bump — luôn confirm version number với user trước.
---

# Version Bump Workflow — Guide Claude Project

Skill này đảm bảo version bump được thực hiện nhất quán: VERSION là SSOT, không hardcode trong modules, changelog entry đầy đủ.

## Trigger

Kích hoạt khi user:
- Nói "bump version", "lên version mới", "release vX.X"
- Hoàn thành sprint và muốn chốt version
- Sau khi cross-ref-checker và module-review đã PASS

## Pre-conditions (kiểm tra trước khi bắt đầu)

Trước khi bump, hỏi user:
1. "Version mới là bao nhiêu?" (đề xuất: nếu thêm features lớn → minor bump, nếu chỉ fixes → patch)
2. "Cross-ref sweep đã chạy chưa?" — nếu chưa → đề xuất chạy `cross-ref-checker` trước
3. "Modules nào thay đổi trong sprint này?"

Nếu user confirm đủ → tiến hành.

## Quy trình

### Bước 1 — Đọc trạng thái hiện tại

Đọc:
- `VERSION` — version cũ
- `git log --oneline -10` — recent changes (dùng cho changelog)
- `project-state.md` — bảng trạng thái modules

### Bước 2 — Cập nhật VERSION file

Sửa `VERSION`:
```
[new version number]
```
*Chỉ chứa version number, không có text khác.*

### Bước 3 — Thêm changelog entry vào 00-overview.md

Tìm section "## Thông tin cập nhật" trong `guide/base/00-overview.md`.

Thêm entry MỚI ở đầu (trước version cũ):

```markdown
### Version [X.X] ([MM/YYYY])

- [Thay đổi 1 — từ git log]
- [Thay đổi 2]
- ...
- Bump version từ [old version]
```

**Quy tắc viết changelog:**
- Dùng động từ: "Thêm", "Update", "Sửa", "Bỏ"
- Ghi rõ module và section số: "Update section 10.8.1:", "Thêm mục 4.7:"
- Không viết chung chung như "Cải thiện chất lượng"

### Bước 4 — KHÔNG sửa module headers

Module headers dùng link `[VERSION](../VERSION)` — tự động reflect version mới. **Không cần sửa từng file.**

### Bước 5 — Cập nhật project-state.md

Cập nhật dòng đầu:
```
Version guide: [new version] | Last synced: [date]
```

### Bước 6 — Xác nhận hoàn thành

Output summary:

```
**Version bump hoàn thành: v[old] → v[new]**

Files đã cập nhật:
- VERSION: [old] → [new]
- guide/base/00-overview.md: thêm changelog entry
- project-state.md: version header updated

Bước tiếp theo: commit changes và upload project-state.md lên Project Knowledge nếu cần.
```

## Rules

- KHÔNG bump version mà không confirm number với user
- KHÔNG sửa module headers — VERSION file là SSOT, link tự động cập nhật
- Chạy `/checkpoint` trước khi bump để git-based backup
- Nếu user muốn bump nhiều level cùng lúc (ví dụ 3.5 → 4.0) → hỏi confirm thêm vì là major bump
- Major bump (X.0) → hỏi user có muốn thêm "Migration notes" trong changelog không
