# Brainstorm — 2026-03-11 (Session 4)

> Context shift: từ "1 maintainer" sang "xây cho team dev Phenikaa-X".
> Chấp nhận cải tổ nếu cần. Đánh giá tương lai xa.

---

## 1. Context shift — Thay đổi phương trình

### Trước (session 1-3)

- Target: Đạt (1 maintainer) dùng Guide Claude
- _scaffold = bonus, "nice-to-have"
- Câu hỏi: "nâng cấp Guide Claude như thế nào?"

### Bây giờ (session 4)

- Target: **Team dev Phenikaa-X** (10-20 kỹ sư)
- _scaffold = **delivery mechanism** cho team
- Câu hỏi: "_scaffold đủ để team dùng không? Cần gì thêm?"

### Tại sao quan trọng

| Yếu tố | 1 maintainer | Team 10-20 |
|---------|-------------|------------|
| Update mechanism | Không cần | **BẮT BUỘC** — phải propagate changes |
| Convention enforcement | Self-discipline | **BẮT BUỘC** — phải tự động |
| Onboarding | Không cần | **BẮT BUỘC** — zero-to-productive path |
| Skill levels | Expert | Mixed (zero → intermediate) |
| Maintenance | 1 person reviews all | Cần distributed ownership |
| Customization | Full control | Balance: shared standards + project-specific |

---

## 2. Đánh giá _scaffold hiện tại

### Đang làm tốt

- Templates chất lượng (CLAUDE-template.md, project-state-template.md, skill/rule templates)
- Hai examples minh họa growth path: minimal → mature
- Checklists actionable, copy-paste ready
- Nhất quán với project conventions

### Không làm được cho team

| Vấn đề | Hệ quả |
|---------|--------|
| Copy-once, diverge-forever | Member A dùng v1, member B dùng v3 — không nhất quán |
| Không có update mechanism | Conventions drift, stale practices tích lũy |
| Không enforce | Team member có thể bỏ qua toàn bộ standards |
| Designed for experts | Kỹ sư robotics mới tiếp xúc Claude → lost |
| Không role-based | Cùng 1 template cho dev, doc writer, ops |

### Kết luận

_scaffold là **necessary nhưng not sufficient**. Team cần thêm: living foundation (auto-update), guardrails (enforce), onboarding path (zero → productive).

---

## 3. Phương hướng phát triển — 4 phases

```
Phase 1 (Now → +1 tháng)          Phase 2 (+1 → +3 tháng)
  Enhanced Scaffold                  Shared Foundation
  + Role-based setup                 + @import + shared repo
  + Onboarding path                  + Shared rules
  + Quick wins infra                 + Custom agents

Phase 3 (+3 → +6 tháng)           Phase 4 (+6 → +12 tháng)
  Plugin Distribution                Managed Policy
  + Internal plugin                  + Org-wide deploy
  + Auto-update                      + CI/CD integration
  + Agent fleet                      + Metrics/feedback
```

### Nguyên tắc

Ship Phase 1 → test → feedback → quyết định Phase 2. KHÔNG design Phase 3-4 trước khi Phase 1 validated.

---

## 4. Quyết định đã chốt

### Q1: Scope Phase 1

> Build complete → roll out thử nghiệm toàn team.
> Nền móng cho Phenikaa-X, cần chất lượng trước khi ship.

### Q2: Shared conventions

> Repo riêng (`pnx-claude-standards`).
> Clean separation, team contribute via PR, versioned riêng.

### Q3: Role definitions

> 3 roles:
> - Developer (Python/ROS2/C++)
> - Doc writer (Technical Writing)
> - Solution lead (Orchestration)

### Q4: Timeline

> Thorough — đầu tư chất lượng nền móng, không rush.
> Liên quan đến nền móng Phenikaa-X, chấp nhận dành nhiều thời gian.

### Q5: Guide Claude content

> Chưa động guide content — focus workspace + scaffold trước.
> Xây nền móng infra/delivery mechanism trước, content update sau.

---

> [!NOTE]
> Đây là tài liệu brainstorm — không phải kế hoạch thực thi.
