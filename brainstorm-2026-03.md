# Brainstorm — Tháng 3/2026

> Tổng hợp ý tưởng và phương hướng từ 5 sessions brainstorm (10-13/03/2026).

---

## 1. Bối cảnh

- Bắt đầu tiếp cận AI từ zero — quá nhiều thông tin tiếng Anh, không biết bắt đầu từ đâu
- Xây Guide Claude ban đầu cho bản thân: tra cứu tiếng Việt, copy-paste workflows
- Sau đó nhận ra nhiều người xung quanh cũng cần — muốn chia sẻ
- Thực tế: mọi người ngại đọc tài liệu dài
- Giá trị thực nằm ở **công cụ hỗ trợ** (configs, profiles, skills) hơn là prose

### Thực tế hàng ngày

- Hầu hết thời gian: **làm việc với DOC** (documentation)
- Các hoạt động chính: brainstorming, capture kiến thức, đặt SOT đầu tiên, xây quy trình làm việc với Claude Code
- Nhìn thấy tiềm năng: Claude = đồng nghiệp, giảm khối lượng, scale hiệu suất
- Mục tiêu sau: dùng thành tựu đã xây → áp dụng cho anh em team khác
- Vai trò giống **BA** — cầu nối giữa AI capability và nhu cầu team

---

## 2. Vision tổng thể

### Mục tiêu cuối cùng

Số hóa kiến thức, quy trình, tiêu chuẩn → AI có đủ context → trợ thủ đắc lực → scale cho team/công ty.

### Triết lý

> Chia nhỏ thành đơn vị nhỏ nhất, xây trên nền chân lý đã xác thực → kế thừa, compose, scale.

### Nguyên tắc

- **Đứng trên vai người khổng lồ** — tận dụng SOT uy tín, không tự sáng tạo khi đã có cái tốt
- Nhưng phải **phù hợp**, không gượng ép
- Ưu tiên: Claude built-in → best practices cộng đồng → framework có tên
- Dần dần **tạo SOT riêng** cho PNX / team / cá nhân
- Kiểm soát chất lượng chặt — hạn chế hiệu ứng cánh bướm (sai nhỏ → lệch lớn)

### Phạm vi không chỉ Guide Claude

```
Kiến thức cần số hóa:
├── Cách làm việc với AI           ← Guide Claude (đang làm)
├── Quy trình viết tài liệu       ← Cần xây
├── Tiêu chuẩn kỹ thuật nội bộ    ← Cần xây
├── Quy trình thiết kế             ← Cần xây
├── Kinh nghiệm đúc kết           ← Cần xây
├── Tips, tricks, best practices   ← Cần xây
└── Onboarding cho người mới       ← Cần xây
```

### Đảm bảo xuyên suốt

- Kết quả đồng nhất (không mỗi lần một kiểu)
- Dễ tiếp cận (không cần chuyên gia AI)
- Dễ bảo trì (tách knowledge, update 1 chỗ)
- AI như đồng nghiệp (config context sẵn)

### Scale path

```
Cá nhân (Đạt) → Team (Solution, Software) → Công ty (PNX) → Chia sẻ
```

---

## 3. Painpoints thực tế

### Vòng xoáy khi làm việc với AI

```
Chưa rõ mình muốn gì
  → Diễn đạt chưa rõ cho AI
    → AI trả lời nghe hay nhưng không đúng ý
      → Nghi ngờ, thêm rules/standards để kiểm soát
        → Quá nhiều nội dung, AI bỏ qua
          → Kết quả vẫn chưa ưng
            → Cảm giác "không kiểm soát được AI"
```

### Vòng lặp "build rồi rebuild"

```
Có ý tưởng → làm phần nhỏ với Claude → xong, thấy ổn
  → nhìn lại bức tranh lớn → không khớp
    → đập đi xây lại → lặp lại
```

Lịch sử rebuild Guide Claude:
- v1→v7: xây content, không xác định rõ hướng từ đầu → phình to, khó kiểm soát
- v7→v9: tái cấu trúc 3-tier (33 sessions, 5 phases)
- Đang cân nhắc v10: đổi kiến trúc lần nữa

**Sai lầm lớn nhất:** lần đầu không xác định rõ từ đầu → mọi thứ sau phải tái cấu trúc.

### Painpoints cụ thể

| Vấn đề | Biểu hiện |
|---------|----------|
| Chưa rõ mục tiêu trước khi làm | Lan man, cầu toàn, không biết "thế nào là done" |
| Diễn đạt chưa chính xác | Khả năng ngữ văn hạn chế, AI hiểu khác ý |
| Không biết kết quả đúng hay sai | Nghi ngờ output AI, dựa vào standards nhờ AI đánh giá nhưng chưa hiệu quả |
| Context bị trôi qua sessions | AI bị lạc đề, mất hướng khi session dài hoặc sang session mới |
| Nội dung quá nhiều | Rules/standards dài → AI bỏ qua, không hiệu quả |
| Memory management chưa tốt | Chưa biết quản lý memory đủ tốt |
| Chuyển session không nhất quán | Mỗi lần chuyển session làm 1 kiểu, không có quy trình chuẩn |
| Chọn SOT khó | Trăm ngàn framework — chọn sai từ đầu thì mọi thứ lệch |
| Bị cuốn theo updates | Chạy theo cập nhật trên mạng, thiếu tiêu chí lọc nội tại |
| Không biết cách đúng với Claude | Mỗi lần làm việc thấy 1 kiểu khác nhau |

### Scaffold thất bại — nguyên nhân gốc

- Scaffold thiết kế cho người **đã biết cách** — không giúp người bắt đầu từ zero
- Giống đưa xe đạp cho người chưa biết giữ thăng bằng
- Khi mang sang AMR-T800: gượng gạo, không hiệu quả vì thiếu guided journey

---

## 4. Hệ thống mong muốn — 4 phần

| Phần | Vai trò | Đặc điểm |
|------|---------|----------|
| **Knowledge** | Kiến thức nền, SSOT | Stable concepts, feature specs — update 1 chỗ |
| **Guide** | Sách tham khảo chuẩn tiếng Việt | Gọn, dễ tra, ví dụ thực tế, đáng tin |
| **Công cụ** | Framework thực hành | Configs, profiles, skills, hooks — hỗ trợ từ zero |
| **Ví dụ thực tế** | Trích từ dự án + profile thực | AMR-T800, Guide Claude — minh họa trực quan |

---

## 5. Nhận định quan trọng

- **Guide Claude là dự án pilot**, không phải sản phẩm cuối — đang dùng để học cách làm việc với AI, thử nghiệm quy trình, xây tools reuse
- **AMR-T800 Hub không phải dự án điển hình** — loại khỏi scope brainstorm
- Painpoints team (AMR-T800) trùng painpoints cá nhân → methodology xây cho bản thân có thể áp dụng cho team
- Bản chất công việc: **chuyển hóa kiến thức** (Tìm hiểu → Chọn lọc → Đóng gói → Chuyển giao) — đang kẹt ở Chọn lọc + Đóng gói

---

## 6. Đánh giá v9.1

### Còn giá trị cao (~60%)

- Prompt engineering, Evaluation framework, Anti-patterns, Doc workflows
- Infrastructure (.claude/) — skills, hooks, rules đã hardened

### Cần restructure

- Context management, tools & features — trộn lẫn knowledge và hướng dẫn
- Dev workflows — chưa kết nối với thực hành

### Giá trị thấp

- Feature specs rải rác — stale, trùng lặp
- Một số reference files chỉ dịch lại official docs
- Scaffold hiện tại — cần thiết kế lại

### Kết luận

Content phần lớn vẫn dùng được, nhưng **kiến trúc** (3-tier theo audience) không phù hợp với vision mới (4-part theo chức năng).

---

## 7. Đánh giá .claude hiện tại

### Đã tốt: kiểm soát chất lượng tài liệu

- 7 rules auto-load, hook format-check.py, 9 skills, `/start` orientation

### Thiếu: kiểm soát chất lượng tư duy

| Có (format/output) | Thiếu (thinking/direction) |
|---|---|
| Heading hierarchy đúng | "Cái này có khớp bức tranh lớn không?" |
| Link không broken | "Nên làm cái này hay không?" |
| Source có marker | "Mục tiêu session này nằm ở đâu trong tổng thể?" |
| Format check auto | Handoff context chuẩn giữa sessions |

### Vấn đề cụ thể

- Global CLAUDE.md gần như trống — chỉ emoji rules, không có methodology
- Không có bức tranh tổng thể dưới dạng Claude đọc được
- Không có handoff protocol cho brainstorm sessions
- Không có "thinking check" — chỉ có "format check"

---

## 8. Context shift — Từ cá nhân sang team

### Trước (session 1-3)

- Target: Đạt (1 maintainer) dùng Guide Claude
- _scaffold = bonus, "nice-to-have"

### Bây giờ (session 4)

- Target: **Team dev Phenikaa-X** (10-20 kỹ sư)
- _scaffold = **delivery mechanism** cho team

### Yêu cầu khác khi scale

| Yếu tố | 1 maintainer | Team 10-20 |
|---------|-------------|------------|
| Update mechanism | Không cần | **BẮT BUỘC** — phải propagate changes |
| Convention enforcement | Self-discipline | **BẮT BUỘC** — phải tự động |
| Onboarding | Không cần | **BẮT BUỘC** — zero-to-productive path |
| Skill levels | Expert | Mixed (zero → intermediate) |
| Maintenance | 1 person reviews all | Cần distributed ownership |
| Customization | Full control | Balance: shared standards + project-specific |

---

## 9. Đánh giá _scaffold hiện tại

### Đang làm tốt

- Templates chất lượng, examples minh họa growth path, checklists actionable, nhất quán với conventions

### Không làm được cho team

| Vấn đề | Hệ quả |
|---------|--------|
| Copy-once, diverge-forever | Không nhất quán giữa members |
| Không có update mechanism | Conventions drift, stale practices tích lũy |
| Không enforce | Team member có thể bỏ qua toàn bộ standards |
| Designed for experts | Kỹ sư mới tiếp xúc Claude → lost |
| Không role-based | Cùng 1 template cho mọi role |

### Kết luận

_scaffold là **necessary nhưng not sufficient**. Team cần thêm: living foundation (auto-update), guardrails (enforce), onboarding path (zero → productive).

---

## 10. Phương hướng phát triển — 4 phases

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

## 11. Quyết định đã chốt

| # | Quyết định | Chốt |
|:-:|-----------|------|
| Q1 | Scope Phase 1 | Build complete → roll out thử nghiệm toàn team. Cần chất lượng trước khi ship |
| Q2 | Shared conventions | Repo riêng (`pnx-claude-standards`). Clean separation, team contribute via PR |
| Q3 | Role definitions | 3 roles: Developer (Python/ROS2/C++), Doc writer, Solution lead |
| Q4 | Timeline | Thorough — đầu tư chất lượng nền móng, không rush |
| Q5 | Guide Claude content | Chưa động — focus workspace + scaffold trước |

---

## 12. Phát hiện: `claude-code-guide` agent (Session 5 — 2026-03-13)

### Phát hiện

Claude Code có sẵn agent `claude-code-guide` — trả lời tương tác về Claude Code features, setup, hooks, skills, MCP, API. Fetch docs realtime từ `code.claude.com`.

### Test thực tế — 3 kịch bản

| Kịch bản | Chất lượng | Vấn đề |
|----------|-----------|--------|
| Câu hỏi mơ hồ ("hooks là gì") | Tốt — đầy đủ, tiếng Việt | Information overload (~1500 từ) |
| Câu hỏi cụ thể ("tạo hook PostToolUse") | Tốt — code hoàn chỉnh | OK |
| Best practices ("CLAUDE.md cho team") | Trộn nguồn | Trộn official docs + third-party blogs + opinion, không phân biệt rõ |

### Phân tích tin cậy

| Loại câu hỏi | Độ tin cậy | Lý do |
|---|---|---|
| Feature docs | Cao | Fetch từ official docs |
| Syntax/config | Cao-Trung | Có thể sai chi tiết nhỏ |
| Best practices | **Thấp-Trung** | Trộn nguồn, opinion = fact |
| Architecture decisions | **Thấp** | Suy luận, không có SOT |

### 3 vấn đề khi kỹ sư PNX dùng agent

1. **Information overload** — agent dump all-in-one, không progressive disclosure
2. **Circular dependency** — cần biết cách hỏi (prompting) để dùng agent dạy prompting
3. **Unknown unknowns** — agent chỉ reactive, không chủ động giới thiệu concepts mới

### Bản đồ thay thế

| Nội dung | Agent thay được? |
|---|---|
| Feature docs, specs, config | Thay hoàn toàn |
| Setup guides, tutorials | Thay hoàn toàn |
| Cheatsheets | Thay phần lớn |
| Prompt methodology | Không thay được |
| Anti-patterns từ kinh nghiệm | Không thay được |
| PNX domain examples | Không thay được |
| Best practices (verified) | Không nên tin agent |
| .claude/ infrastructure | Không thay được (configs thực) |

---

## 13. Phản biện toàn diện — 8 chiều (Session 5)

### C1: Sunk cost
Guide Claude đã hoàn thành vai trò pilot (học cách dùng Claude). Giá trị nằm ở quá trình xây (kinh nghiệm Đạt) + infrastructure (.claude/), không phải 20 file markdown.

### C2: Người ta có đọc guide không?
Đa số học tool bằng cách dùng → vấp → tìm hiểu (Cách 2). Guide phục vụ Cách 1 (đọc trước). Cần cách nhúng kiến thức vào lúc đang dùng.

### C3: Custom agent thay guide?
Có thể tạo PNX agent chứa methodology. Nhưng unknown unknowns vẫn chưa giải — agent chỉ trả lời khi được hỏi. Giải pháp: agent chủ động qua hooks (SessionStart gợi ý).

### C4: Best practices "đã verify"?
Test trên 1 người (Đạt), 1 loại task (documentation), do Claude viết + Đạt review. Sample size = 1. Infrastructure (.claude/) verify chắc hơn (automated, chạy nhiều lần).

### C5: Team scaling chưa validate
Đang thiết kế cho 15 người dựa trên kinh nghiệm 1 người, chưa feedback từ target audience.

### C6: Vòng lặp rebuild
v1→v7 rebuild, v7→v9 rebuild (33 sessions), đang cân nhắc rebuild lần nữa. Cần dừng phân tích và bắt đầu làm ở điểm phù hợp.

### C7: Giá trị thực đã tạo
Infrastructure (.claude/) + methodology ngầm trong đầu Đạt = giá trị cao. Guide content chưa ai ngoài Đạt đọc. Scaffold thử 1 lần (AMR-T800) thất bại.

### C8: Đang giải bài toán nào?
Bài toán gốc: số hóa kiến thức PNX. Guide Claude đang dạy tool (Claude Code) thay vì dạy dùng tool để giải bài toán domain. Hai cái liên quan nhưng khác nhau.

---

## 14. Hướng đi đã chốt — Guide Claude = Bộ lọc PNX (Session 5)

### Phương án

Guide Claude chuyển từ **"dạy Claude Code"** sang **"lọc Claude Code qua lăng kính PNX"**:
- Feature docs → để `claude-code-guide` trả lời realtime
- Guide chỉ giữ: awareness (có gì), methodology (cách tư duy), PNX evaluation (nên/không nên), anti-patterns (tránh gì)
- Mỗi chủ đề: 15-25 dòng thay vì 2-3 trang

### Kiến trúc 4 lớp

```
Lớp 1: Infrastructure (.claude/)    ← Core deliverable cho team
Lớp 2: Guide content (guide/)       ← Bộ lọc PNX (gọn, unique)
Lớp 3: claude-code-guide (built-in) ← Feature depth on-demand
Lớp 4: Scaffold (templates)         ← Delivery cho team mới
```

### Quyết định bổ sung

| # | Quyết định | Chốt |
|:-:|-----------|------|
| Q6 | Vai trò guide | Bộ lọc PNX, không phải sách giáo khoa. Cắt feature docs, giữ methodology + evaluation |
| Q7 | `claude-code-guide` | Dùng làm depth layer cho features. KHÔNG tin cho best practices/methodology |
| Q8 | Rebuild hay trim? | Session sau brainstorm chi tiết: có thể bắt đầu lại nếu cần |

---

## 15. Handoff cho session tiếp — Brainstorm chi tiết cách xây dựng lại

### Câu hỏi cần trả lời

1. **Bắt đầu lại từ đầu hay trim v9.1?** — đánh giá effort, rủi ro, kết quả
2. **Kiến trúc mới cụ thể:** bao nhiêu modules, tên gì, thứ tự nào
3. **Format mỗi module:** template chi tiết cho "bộ lọc PNX"
4. **Quy trình xây:** làm 1 module pilot → đánh giá → roll out
5. **Infrastructure giữ/đổi gì:** .claude/ rules, hooks, skills cần adjust?
6. **Scaffold v2:** thiết kế lại cho mô hình mới
7. **Workspace plan:** adjust hay viết lại?

### Context cần đọc

- File này (brainstorm-2026-03.md) — sections 12-15
- workspace-plan.md — 7 milestones hiện tại
- v10-decisions.md — decisions Q1-Q8
- guide/ folder structure hiện tại — để đánh giá giữ/bỏ

### Chuỗi kế thừa PNX → Robotics → Solution → Personal

Phân tích kỹ thuật Claude Code cho thấy @import chain (max 5 cấp) + repo `pnx-claude-standards` (Q2) hỗ trợ đủ.

**Mapping tổ chức → Claude Code:**

```
Phenikaa-X  → Managed CLAUDE.md hoặc shared repo /pnx/
Robotics    → Shared repo /robotics/ + @import
Solution    → Shared repo /solution/ + @import
Personal    → ~/.claude/CLAUDE.md
```

**Cấu trúc repo `pnx-claude-standards`:**

```
pnx-claude-standards/
├── pnx/           claude.md + rules/ + hooks/  (conventions chung)
├── robotics/      claude.md + rules/           (ROS2, AMR, hardware)
├── solution/      claude.md + rules/           (doc workflows, orchestration)
└── templates/     developer/ + doc-writer/ + solution-lead/
```

**Hệ quả cho session sau:**
- Guide content cần tách theo tầng kế thừa (PNX chung / Robotics / Solution)
- Infrastructure (.claude/) hiện tại trộn lẫn tất cả — cần tách
- Scaffold redesign cho mô hình @import + shared repo
- Windows: symlink cần admin, ưu tiên @import; path chuẩn hóa `C:\PNX-Standards\`

### Nguyên tắc cho session sau

- Đánh giá khách quan: bắt đầu lại có thể tốt hơn nếu v9.1 architecture không phù hợp
- Tránh vòng lặp analysis paralysis — session sau ra được phương án cụ thể, actionable
- Pilot 1 module trước khi quyết định toàn bộ
- Thiết kế phải tương thích chuỗi kế thừa PNX → Robotics → Solution → Personal

---

> [!NOTE]
> Đây là tài liệu brainstorm — không phải kế hoạch thực thi.
