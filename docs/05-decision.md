# Decision log

## D1: Monorepo
- **Chosen:** one repo with `frontend/`, `backend/` and `docs/`.
- **Alternatives:** separate repos.
- **Why:** a solo project with one README, one CI pipeline, and atomic commits across API and UI.
- **Trade-offs:** deploy tools need a root-directory setting per service.

## D2: Next.js + FastAPI as separate services
- **Chosen:** a TypeScript frontend and a Python API.
- **Alternatives:** Next.js full-stack only; Node/Express backend.
- **Why:** it forces a clear API contract between client and server. FastAPI gives typed validation and auto docs, and Python leaves room for an LLM integration later.
- **Trade-offs:** two services to run and deploy.

## D3: PostgreSQL
- **Chosen:** a relational database.
- **Alternatives:** MongoDB, SQLite.
- **Why:** the data is relational (users, tasks, summaries) and has strict rules (uniqueness, foreign keys, enums).
- **Trade-offs:** migrations are needed (Alembic).

## D4: Lazy midnight rollover instead of a scheduler
- **Chosen:** when a logged-in user makes a request, the backend processes any days that have ended since the last rollover.
- **Alternatives:** a cron or background worker (Celery, APScheduler) that runs at midnight per time zone.
- **Why:** much simpler for v1. The user only sees notifications when they open the app anyway, and in-app notifications are all that v1 sends.
- **Trade-offs:** the roast is generated when the user returns, not at exactly 12:00am. A scheduler becomes necessary once emails or push notifications are added.

## D5: Calendar day in the user's time zone
- **Chosen:** a day runs midnight to midnight in the user's IANA time zone, stored on the user.
- **Alternatives:** a rolling 24 hours from task creation; server time.
- **Why:** it matches how people think about "today", and the rule is easy to explain and test.
- **Trade-offs:** time zone handling needs care (and tests around midnight).

## D6: Waitlist is a status, not a table, with manual promotion
- **Chosen:** `status = 'waitlisted'` and `board_date = NULL`. Tasks are moved to the board manually by the user.
- **Alternatives:** a separate waitlist table; automatic promotion when a slot frees.
- **Why:** one table keeps queries simple. Manual promotion matches the "commit to five" idea.
- **Trade-offs:** the user must take an action to move tasks.

## D7: Template-based roasts
- **Chosen:** pre-written messages per event and tone, with placeholders (task title, pending count).
- **Alternatives:** LLM-generated roasts.
- **Why:** free, fast, deterministic and testable, and it works offline.
- **Trade-offs:** less variety. The roast service interface leaves room to add an LLM later.

## D8: In-app notifications only in v1
- **Chosen:** a `notifications` table shown in the UI.
- **Alternatives:** email or push.
- **Why:** these need background jobs and external services, which are out of scope for v1.
- **Trade-offs:** users only see roasts when they open the app.

## D9: Enforce the 5-task limit in the service layer, in a transaction
- **Chosen:** lock the user row, count the board, then insert.
- **Alternatives:** a database trigger; trusting the frontend.
- **Why:** the backend must be the source of truth for the rules, and the logic stays visible and testable in Python.
- **Trade-offs:** the rule lives in code, not in the schema.

## D10: A `daily_summaries` table
- **Chosen:** one row per user per processed day.
- **Alternatives:** compute history from task rows only.
- **Why:** it makes history and stats cheap to query, and makes the rollover idempotent.
- **Trade-offs:** one more table to keep consistent.