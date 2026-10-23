# tuntun-auntie

An accountability tasks app that roasts you into getting things done. You commit to **five tasks a day**. Finish them and your streak grows. Miss them and the app roasts you, in the tone you picked.

**Live demo:** _coming soon_  
**Status:** In development (v1)

## Why I built this
Most task apps let you pile up endless lists and never finish anything. This one limits you to five tasks per day and holds you accountable with humor. I built it to learn full-stack design end to end: data modeling, API design, authentication, business rules and deployment.

## Features (v1)
- [ ] Signup and login (JWT auth)
- [ ] Daily board with a hard limit of 5 tasks
- [ ] Waitlist for extra and carried-over tasks
- [ ] Midnight rollover in the user's time zone (unfinished tasks go to the waitlist)
- [ ] Streaks for days where every task is done
- [ ] Roasts in three tones: sarcastic, loving, angry
- [ ] In-app notifications and reminders
- [ ] Task history and stats

**Planned later:** email notifications, scheduled background jobs, LLM-personalized roasts, voice and image input.

## Tech stack
| Layer | Tech | Why |
|---|---|---|
| Frontend | Next.js, TypeScript | Widely used; typed UI code |
| Backend | FastAPI (Python) | Typed validation with Pydantic, auto API docs |
| Database | PostgreSQL | Relational data with strict rules and constraints |
| ORM / migrations | SQLAlchemy 2.0, Alembic | Versioned schema changes |
| Auth | JWT, bcrypt-hashed passwords | Stateless API auth |
| Tests | pytest | Business rules need automated checks |
| Deploy | Docker, Vercel, Render/Railway | Live link, reproducible setup |

## Architecture
See [`docs/04-architecture.md`](./docs/04-architecture.md) for diagrams and the request flow.

## Getting started
### Prerequisites
- Node.js 20+
- Python 3.11+
- Docker (for PostgreSQL)

### Setup
1. Clone the repo.
2. Copy `.env.example` to `.env` in `backend/` and `frontend/`, then fill in the values.
3. Start the database: `docker compose up -d db`
4. Backend: `cd backend && pip install -r requirements.txt && alembic upgrade head && uvicorn app.main:app --reload`
5. Frontend: `cd frontend && npm install && npm run dev`

_(Commands will be finalized as the project is built.)_

## Running tests
`cd backend && pytest`

## Project structure
```
.
├── backend/    # FastAPI app
├── frontend/   # Next.js app
├── docs/       # design documents
└── docker-compose.yml
```

## Design docs
1. [Requirements](./docs/01-requirements.md)
2. [Data model](./docs/02-data-model.md)
3. [API design](./docs/03-api-design.md)
4. [Architecture](./docs/04-architecture.md)
5. [Decision log](./docs/05-decisions.md)