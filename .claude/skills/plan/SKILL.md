---
name: plan
description: >
  Orchestrator cho planning workflow — tạo, xem, và quản lý tasks/plans.
  Trigger khi user nói "tạo plan", "xem plan", "task list", "plan status",
  "backlog", hoặc cần track multi-step work across sessions.
user-invocable: true
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
  - Edit
  - Write
---

Current version: !cat VERSION

## Trigger
Kích hoạt khi user muốn:
- Tạo plan mới cho công việc multi-step
- Xem status plan/tasks đang chạy
- Update progress tasks
- Review backlog

## Quy trình

### Mode 1: Xem status (default khi không có argument)
1. Đọc tất cả files trong auto memory directory (xem MEMORY.md cho links tới plan files) — tìm files có pattern `## Phase`
2. Với mỗi plan file tìm được:
   - Đếm phases DONE / PENDING / IN-PROGRESS
   - Đếm tasks hoàn thành / tổng
3. Output summary table

### Mode 2: Tạo plan mới (khi user mô tả công việc cần plan)
1. Phân tích scope công việc
2. Chia thành phases (mỗi phase độc lập, có thể dừng bất kỳ lúc nào)
3. Mỗi phase có tasks cụ thể (format: `N.M: mô tả`)
4. Xác định dependencies giữa phases
5. Viết plan file vào auto memory directory: `{memory-dir}/{tên-plan}.md`
6. Update MEMORY.md — thêm link tới plan mới

### Mode 3: Update progress (khi user báo hoàn thành task/phase)
1. Đọc plan file liên quan
2. Update status task/phase
3. Ghi commit hash nếu có
4. Nếu phase hoàn thành → update status → DONE

## Output format

### Status view:
```
Plan: {tên plan}
Progress: {done}/{total} phases | {done_tasks}/{total_tasks} tasks
Current: Phase {N} — {tên} ({status})
Next: {mô tả task tiếp theo}
```

### Tạo plan:
```
Plan: {tên plan} — created
Phases: {N} | Tasks: {M}
File: memory/{filename}.md
Ready to start Phase 1: {tên phase}
```

## Rules
- KHÔNG tạo plan mà không confirm structure với user trước
- KHÔNG thay đổi plan đang chạy mà không hỏi
- Mỗi plan PHẢI có Bối cảnh, Nguyên tắc, Phases
- Phase PHẢI độc lập — có thể dừng bất kỳ lúc nào
- Ghi MEMORY.md link sau khi tạo plan mới
