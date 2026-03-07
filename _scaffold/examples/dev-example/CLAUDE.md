# CLAUDE.md — My Dev Project

## Project context
Backend API service — Python FastAPI.
- **Version:** xem file `VERSION` (SSOT)
- **Phase:** Development
- **Stack:** Python 3.12, FastAPI, PostgreSQL, Docker

## Folder structure
```
my-dev-project/
├── src/                    Application code
│   ├── api/                Route handlers
│   ├── models/             Database models
│   └── services/           Business logic
├── tests/                  Test files
├── .claude/                Infrastructure
│   ├── CLAUDE.md           File này
│   ├── settings.json       Hooks
│   └── commands/           /start, /checkpoint
├── VERSION                 Version SSOT
└── docker-compose.yml      Local dev environment
```

## Code conventions
- **Style:** PEP 8, type hints bắt buộc
- **Naming:** snake_case cho functions/variables, PascalCase cho classes
- **Imports:** stdlib → third-party → local (isort order)
- **Tests:** pytest, mỗi module có test file tương ứng (`src/api/users.py` → `tests/test_api_users.py`)

## Rules
1. **Git-first:** `/checkpoint` trước refactor lớn
2. **Tests:** chạy `pytest` trước khi commit — fix nếu fail
3. **No destructive git:** KHÔNG force push, reset --hard
4. **Dependencies:** thêm package → update `requirements.txt`
5. **Secrets:** KHÔNG commit `.env`, credentials, API keys

## Git workflow
- **Branch naming:** `feat/<topic>`, `fix/<topic>`
- **Commit message:** English, imperative mood ("Add user endpoint", "Fix auth bug")
- **Main branch:** `main`

## Commands
| Command | Trigger |
|---------|---------|
| `/start` | Đầu mỗi session |
| `/checkpoint` | Quick commit |

## Common tasks
```bash
# Run tests
pytest -v

# Run dev server
uvicorn src.main:app --reload

# Run linter
ruff check src/

# Build Docker
docker-compose up --build
```
