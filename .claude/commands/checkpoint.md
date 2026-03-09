Quick commit workflow. Thực hiện tuần tự:

1. Chạy `git status` — show modified/untracked files
2. Chạy `git diff --stat` — summary số dòng thay đổi per file
3. Nếu không có thay đổi → báo "Working tree clean, nothing to commit" và dừng
3.5. Nếu có thay đổi trong `guide/` → chạy `python3 .claude/hooks/link-check.py` và báo kết quả. Nếu có broken links → cảnh báo trước khi commit (user vẫn có thể chọn commit)

4. Phân tích changes và đề xuất commit message:
   - Format: `Module XX: mô tả ngắn` (nếu thay đổi liên quan module)
   - Format: `Infra: mô tả ngắn` (nếu thay đổi .claude/, _scaffold/)
   - Format: `Docs: mô tả ngắn` (nếu thay đổi README, project-state...)
   - Tiếng Việt, tối đa 72 ký tự dòng đầu

5. Show cho user:
```
Changes:
{git diff --stat output}

Proposed commit: "{message}"
```

6. Hỏi user confirm — đưa ra 3 lựa chọn:
   - "Commit & push" — commit rồi push
   - "Commit only" — commit, không push
   - "Edit message" — user sửa message trước khi commit

Rules:
- KHÔNG tự ý commit — PHẢI có user confirm
- KHÔNG dùng `git add -A` — liệt kê files cụ thể khi stage
- KHÔNG commit `.bak` files — cảnh báo nếu có trong changes
- KHÔNG push nếu user chưa chọn push
- Nếu có `.bak` trong changes: cảnh báo và hỏi có muốn exclude không
