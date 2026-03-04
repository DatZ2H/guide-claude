# Release Checklist — Guide Claude

Dùng cho mỗi version release. Copy checklist này vào PR description.

## Pre-edit
- [ ] Đọc `VERSION` hiện tại
- [ ] Chạy `/start` để orientation
- [ ] Tạo branch: `feat/<topic>` hoặc `fix/<topic>`
- [ ] `/checkpoint` backup trước khi edit

## Editing
- [ ] Edit theo plan (xem `_process/upgrade-plan.md`)
- [ ] Tuân thủ Icon & Emoji Rules (xem CLAUDE.md)
- [ ] Tuân thủ Writing Standards (xem CLAUDE.md)
- [ ] Mỗi module edit xong → `/validate-doc <so_module>`

## Post-edit Review
- [ ] Chạy `cross-ref-checker` kiểm tra links
- [ ] Grep kiểm tra: không còn emoji banned
- [ ] Grep kiểm tra: không còn hardcoded version/benchmark (nếu Phase 1+)
- [ ] Đọc lại diff toàn bộ: `git diff feat/<branch>...HEAD`

## Version Bump (khi release)
- [ ] `/version-bump` — cập nhật VERSION, changelog, project-state
- [ ] Verify VERSION file đúng
- [ ] Verify 00-overview.md changelog section đúng

## Merge
- [ ] Tạo PR: `git push -u origin feat/<branch>`
- [ ] PR description: paste checklist này với các mục đã check
- [ ] Review PR trên GitHub
- [ ] Merge vào master

## Post-merge
- [ ] `git checkout master && git pull`
- [ ] Cập nhật `_process/upgrade-plan.md` — đánh dấu tasks hoàn thành
- [ ] Thông báo Cowork session để verify và lấy session tiếp theo
