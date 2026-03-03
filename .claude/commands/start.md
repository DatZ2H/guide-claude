Chạy orientation đầu session. Thực hiện tuần tự:

1. Đọc file `VERSION` — lấy version number
2. Chạy `git status --short` — đếm số files modified/untracked
3. Chạy `git log --oneline -5` — lấy 5 commits gần nhất

Output một block duy nhất, format:

```
Project v{version} | Branch: {branch}
Last commit: {hash} {message}
Working tree: {N} modified, {M} untracked
```

Rules:
- KHÔNG đọc project-state.md (tốn token) — chỉ đọc khi user yêu cầu rõ
- KHÔNG liệt kê từng file modified — chỉ đếm số lượng
- Nếu working tree sạch: ghi "Working tree: clean"
- Tổng output KHÔNG quá 6 dòng
