---
name: session-start
description: Workflow mở đầu Cowork session cho Guide Claude project. Trigger khi user bắt đầu session mới, nói "bắt đầu", "tiếp tục", "session mới", hoặc hỏi "còn lại gì cần làm". Đọc _memory/ và trả về orientation ngắn gọn trước khi làm việc.
---

# Session Start Workflow — Guide Claude Project

Skill này chạy đầu mỗi Cowork session để nhanh chóng nắm bối cảnh và tránh lãng phí thời gian đọc nhiều files.

## Trigger

Kích hoạt khi user:
- Bắt đầu session với "tiếp tục", "bắt đầu", "session mới", "hôm nay làm gì"
- Hỏi trạng thái project: "còn lại gì", "đang ở đâu rồi", "tóm tắt"
- Không có context rõ ràng về việc cần làm

## Quy trình

### Bước 1 — Đọc memory files (LUÔN làm trước)

Đọc 2 files theo thứ tự:
1. `_memory/session-state.md` — active tasks, last session summary
2. `_memory/decisions-log.md` — 5 decisions gần nhất (cuối file)

Sau đó đọc `VERSION` để biết version hiện tại.

### Bước 2 — Orientation summary (ngắn gọn, ~5 dòng)

Output theo format cố định:

```
**Session orientation — Guide Claude v[VERSION]**
- Last session ([date]): [1 dòng tóm tắt]
- Active tasks: [list task chưa done từ session-state]
- Pending decisions: [nếu có decisions-log entry chưa được reflect vào modules]
- Suggested next: [1 action cụ thể dựa trên active tasks]
```

### Bước 3 — Hỏi confirm

Kết thúc bằng: "Tiếp tục với [suggested action] hay anh muốn làm việc khác?"

## Rules

- KHÔNG tự ý bắt đầu làm gì trước khi user confirm
- Nếu session-state.md và decisions-log.md không tồn tại → báo "files _memory/ chưa có, khởi tạo không?" và dừng
- Giữ orientation summary dưới 10 dòng — đủ để orient, không cần đọc thêm
- Nếu VERSION file không tồn tại → ghi "(xem VERSION file — không tìm thấy)"

## Ví dụ output

```
**Session orientation — Guide Claude v3.5**
- Last session (2026-03-02): Task 3 hoàn thành — update 4 modules + cross-reference sweep
- Active tasks: Task 2 (Skills), Task 4 (_scaffold/), Task 5 (version bump → v4.0)
- Suggested next: Task 2 — tạo Skills cho .claude/skills/ (đang làm)
```
