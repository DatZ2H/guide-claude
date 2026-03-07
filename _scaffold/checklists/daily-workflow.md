# Daily Workflow Checklist

Quy trình làm việc hàng ngày với Claude Code / Cowork — từ bắt đầu session đến handover.

---

## Session Start

- [ ] Chạy `/start` — đọc orientation (version, branch, recent commits)
- [ ] Xác nhận task: "Session này làm [X], output [Y]"
- [ ] Nếu task lớn: `/checkpoint` trước khi bắt đầu edit

## Trong khi làm việc

- [ ] Một task tại một thời điểm — không chuyển task giữa chừng
- [ ] Edit xong file → verify (chạy test, lint, hoặc `/validate-doc`)
- [ ] Nếu phát hiện task ngoài scope → ghi vào BACKLOG, không làm ngay
- [ ] Nếu file > 500 dòng → đọc có `offset`/`limit`, không load toàn bộ

## Checkpoint (mỗi milestone nhỏ)

- [ ] Chạy `/checkpoint` — review changes + commit
- [ ] Verify commit message mô tả đúng thay đổi
- [ ] Push nếu cần backup remote

## Session End

- [ ] Verify deliverable match scope đầu session
- [ ] `/checkpoint` — commit final
- [ ] Ghi handover trong commit message body:
  ```
  git commit -m "Task: mô tả ngắn" -m "Next: [task tiếp theo]. [Blockers nếu có]."
  ```

---

## Patterns hay

### Branch workflow (cho projects có PR)

```bash
# Đầu session
git checkout master && git pull
git checkout -b feat/task-name

# Làm việc + commit

# Cuối session
git push -u origin feat/task-name
# Tạo PR → review → merge
git checkout master && git pull
```

### Khi bị stuck

1. Đọc lại CLAUDE.md — có rule nào liên quan?
2. Kiểm tra rules/ — có context-specific rule?
3. Chạy `/start` lại — refresh context
4. Nếu vẫn stuck → hỏi user, không đoán

### Khi context window đầy

1. `/compact` — nén conversation history
2. Nếu vẫn dài → `/clear` và `/start` lại
3. Task chưa xong → ghi handover trước khi clear
