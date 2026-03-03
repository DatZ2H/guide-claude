Chạy orientation đầu session. Thực hiện tuần tự:

1. Đọc file `VERSION` — lấy version number
2. Chạy `git status --short` — đếm số files modified/untracked
3. Chạy `git log --oneline -5` — lấy 5 commits gần nhất
4. Đọc `_memory/session-state.md` — chỉ phần "Active tasks" và "Possible next steps"

Output một block duy nhất, format:

```
Project v{version} | Branch: {branch}
Last commit: {hash} {message}
Working tree: {N} modified, {M} untracked

Active tasks:
- {task list từ session-state}

Next steps:
- {từ session-state}
```

Rules:
- KHÔNG đọc project-state.md (tốn token) — chỉ đọc khi user yêu cầu rõ
- KHÔNG đọc decisions-log.md
- KHÔNG liệt kê từng file modified — chỉ đếm số lượng
- Nếu working tree sạch: ghi "Working tree: clean"
- Nếu không có active tasks: ghi "No active tasks"
- Tổng output KHÔNG quá 10 dòng
