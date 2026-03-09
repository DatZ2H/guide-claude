---
paths:
  - "project-state.md"
---

# Planning Standards

## Khi nào dùng TaskCreate
- Task có nhiều bước phụ thuộc nhau (dependency chain)
- Công việc kéo dài qua nhiều session
- Cần track progress rõ ràng (done/pending/in-progress)

## Khi nào KHÔNG cần TaskCreate
- Task đơn giản hoàn thành trong 1 session
- Chỉ cần checklist trong memory file
- Edit/fix nhỏ không cần tracking

## Plan format trong memory files
- Mỗi plan có: Bối cảnh, Nguyên tắc, Phases, Decisions
- Phase format: `## Phase N: Tên — STATUS` (DONE/PENDING/IN-PROGRESS)
- Task format: `- N.M: Mô tả ngắn`
- Khi hoàn thành task: ghi commit hash, số files changed
- Khi hoàn thành phase: update status → DONE, ghi commit hash

## Cleanup
- Plan hoàn thành → giữ lại trong memory (reference cho tương lai)
- Đánh dấu `## COMPLETED` ở đầu file khi tất cả phases done
- KHÔNG xóa plan files — chúng là institutional knowledge

## Rules
- KHÔNG tạo plan mới mà không confirm với user
- KHÔNG thay đổi scope plan đang chạy mà không hỏi user
- Update memory file SAU mỗi phase hoàn thành
