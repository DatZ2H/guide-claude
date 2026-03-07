Quick commit workflow:

1. Chạy `git status` — show modified/untracked files
2. Chạy `git diff --stat` — summary changes
3. Nếu không có thay đổi → báo "Nothing to commit" và dừng

4. Đề xuất commit message:
   - English, imperative mood, tối đa 72 ký tự
   - Ví dụ: "Add user authentication endpoint"

5. Show cho user:
```
Changes:
{git diff --stat output}

Proposed commit: "{message}"
```

6. Hỏi user confirm:
   - "Commit & push"
   - "Commit only"
   - "Edit message"

Rules:
- KHÔNG tự ý commit — PHẢI có user confirm
- KHÔNG dùng `git add -A` — liệt kê files cụ thể
- KHÔNG commit `.env`, credentials, hoặc large binaries
