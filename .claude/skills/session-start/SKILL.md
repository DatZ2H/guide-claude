---
name: session-start
description: Workflow mở đầu Cowork session cho Guide Claude project. Trigger khi user bắt đầu session mới, nói "bắt đầu", "tiếp tục", "session mới", hoặc hỏi "còn lại gì cần làm". Đọc git history và trả về orientation ngắn gọn trước khi làm việc.
user-invocable: true
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
---

Current version: !cat VERSION

# Session Start Workflow — Guide Claude Project

Skill này chạy đầu mỗi Cowork session để nhanh chóng nắm bối cảnh và tránh lãng phí thời gian đọc nhiều files.

> [!NOTE]
> `/start` (command) = orientation nhanh, chỉ show status. `/session-start` (skill) = full workflow, có suggested next action + hỏi confirm trước khi bắt đầu.

## Trigger

Kích hoạt khi user:
- Bắt đầu session với "tiếp tục", "bắt đầu", "session mới", "hôm nay làm gì"
- Hỏi trạng thái project: "còn lại gì", "đang ở đâu rồi", "tóm tắt"
- Không có context rõ ràng về việc cần làm

## Quy trình

### Bước 1 — Đọc trạng thái từ git (LUÔN làm trước)

1. Chạy `git log --oneline -5` — 5 commits gần nhất (version đã inject ở trên)
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
**Session orientation — Guide Claude v9.0**
- Last commit: 9b8e89c Docs: xóa stale ref upgrade-plan-v8 trong README
- Working tree: clean
- Suggested next: Tiếp tục infra hardening Phase 2
```
