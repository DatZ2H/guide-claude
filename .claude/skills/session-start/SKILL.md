---
name: session-start
description: Workflow mở đầu Cowork session cho Guide Claude project. Trigger khi user bắt đầu session mới, nói "bắt đầu", "tiếp tục", "session mới", hoặc hỏi "còn lại gì cần làm". Đọc git history và trả về orientation ngắn gọn trước khi làm việc.
---

# Session Start Workflow — Guide Claude Project

Skill này chạy đầu mỗi Cowork session để nhanh chóng nắm bối cảnh và tránh lãng phí thời gian đọc nhiều files.

## Trigger

Kích hoạt khi user:
- Bắt đầu session với "tiếp tục", "bắt đầu", "session mới", "hôm nay làm gì"
- Hỏi trạng thái project: "còn lại gì", "đang ở đâu rồi", "tóm tắt"
- Không có context rõ ràng về việc cần làm

## Quy trình

### Bước 1 — Đọc trạng thái từ git (LUÔN làm trước)

1. Đọc `VERSION` — version hiện tại
2. Chạy `git log --oneline -5` — 5 commits gần nhất
3. Chạy `git status --short` — đếm files modified/untracked

### Bước 2 — Orientation summary (ngắn gọn, ~5 dòng)

Output theo format cố định:

```
**Session orientation — Guide Claude v[VERSION]**
- Last commit: [hash] [message]
- Working tree: [N] modified, [M] untracked
- Suggested next: [1 action cụ thể dựa trên recent commits và working tree]
```

### Bước 3 — Hỏi confirm

Kết thúc bằng: "Tiếp tục với [suggested action] hay anh muốn làm việc khác?"

## Rules

- KHÔNG tự ý bắt đầu làm gì trước khi user confirm
- KHÔNG đọc project-state.md (tốn token) — chỉ đọc khi user yêu cầu rõ
- Giữ orientation summary dưới 8 dòng — đủ để orient, không cần đọc thêm
- Nếu VERSION file không tồn tại → ghi "(VERSION file — không tìm thấy)"

## Ví dụ output

```
**Session orientation — Guide Claude v4.1**
- Last commit: 13f41da Thêm 4 core slash commands
- Working tree: 3 modified, 0 untracked
- Suggested next: Cross-ref sweep cho modules chưa update (01, 03, 06–09)
```
