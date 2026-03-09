Chạy orientation nhanh đầu session (version, git status, recent commits — không suggest action).
Dùng `/session-start` nếu cần full workflow với suggested next action + confirm.

Current version: !cat VERSION

Thực hiện tuần tự:

1. Chạy `git status --short` — đếm số files modified/untracked
2. Chạy `git log --oneline -5` — lấy 5 commits gần nhất
3. Scan auto memory directory cho active plans — tìm files có `## Phase` + status PENDING/IN-PROGRESS (xem MEMORY.md cho links tới plan files)

Output một block duy nhất, format:

```
Project v{version} | Branch: {branch}
Last commit: {hash} {message}
Working tree: {N} modified, {M} untracked
Active plans: {plan name} ({done}/{total} phases)
```

Rules:
- KHÔNG đọc project-state.md (tốn token) — chỉ đọc khi user yêu cầu rõ
- KHÔNG liệt kê từng file modified — chỉ đếm số lượng
- Nếu working tree sạch: ghi "Working tree: clean"
- Nếu không có active plans: bỏ dòng "Active plans"
- Tổng output KHÔNG quá 7 dòng
