# Example: Minimal Dev Project

**Loại:** Development project (Python/Node.js/etc.)

Ví dụ config tối thiểu cho một dev project dùng Claude Code. Chỉ gồm những thành phần thiết yếu — thêm dần khi cần.

---

## Cấu trúc

```
my-dev-project/
├── src/                        # Code chính
├── tests/                      # Tests
├── VERSION                     # Version number
├── .claude/
│   ├── CLAUDE.md               # Project instructions
│   ├── settings.json           # SessionStart hook
│   └── commands/
│       ├── start.md            # /start — session orientation
│       └── checkpoint.md       # /checkpoint — quick commit
└── ...
```

## Thành phần tối thiểu

| File | Vai trò | Bắt buộc? |
|------|---------|:---------:|
| `.claude/CLAUDE.md` | Project context, rules, conventions | ✅ |
| `.claude/settings.json` | SessionStart hook | ✅ |
| `.claude/commands/start.md` | Orientation đầu session | ✅ |
| `.claude/commands/checkpoint.md` | Quick commit workflow | Khuyến nghị |
| `VERSION` | Version SSOT | Khuyến nghị |

## Mở rộng khi cần

Khi project phức tạp hơn, thêm dần:

1. **Rules** (`.claude/rules/`) — auto-load theo path:
   ```
   rules/
   ├── code-standards.md      → src/**
   └── test-standards.md      → tests/**
   ```

2. **Hooks** — enforce tự động:
   ```json
   {
     "PostToolUse": [{
       "matcher": "Edit|Write",
       "hooks": [{ "type": "command", "command": "npm run lint --silent" }]
     }]
   }
   ```

3. **Skills** — on-demand workflows:
   ```
   skills/
   ├── code-review/SKILL.md
   └── release/SKILL.md
   ```

---

> [!NOTE]
> Ví dụ này dùng conventions chung. Customize `CLAUDE.md` cho tech stack và quy trình cụ thể của project.
