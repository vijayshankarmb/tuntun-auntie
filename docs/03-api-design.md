# API design (draft)

Base path: `/api/v1`. JSON requests and responses. Protected routes need `Authorization: Bearer <JWT>`.
Validation errors return `422`. Accessing another user's resource returns `404` (not `403`, so IDs are not leaked).

## Auth and user
| Method | Path | Auth | Request body | Success | Errors |
|---|---|---|---|---|---|
| POST | /auth/signup | no | name, email, password, timezone | 201 user | 409 email exists, 422 |
| POST | /auth/login | no | email, password | 200 access_token | 401 bad credentials |
| GET | /users/me | yes | n/a | 200 user + streaks | 401 |
| PATCH | /users/me | yes | roast_tone?, timezone?, name? | 200 user | 401, 422 |

## Tasks
| Method | Path | Auth | Request body | Success | Errors |
|---|---|---|---|---|---|
| GET | /tasks/today | yes | n/a | 200 today's board (runs rollover first) | 401 |
| GET | /tasks/waitlist | yes | n/a | 200 list | 401 |
| GET | /tasks/history?date=YYYY-MM-DD | yes | n/a | 200 summaries / tasks of that day | 401 |
| POST | /tasks | yes | title | 201 task (`pending`, or `waitlisted` if the board is full) + roast | 401, 422 |
| PATCH | /tasks/{id} | yes | title | 200 task | 404, 409 (task is done) |
| DELETE | /tasks/{id} | yes | n/a | 204 | 404, 409 (task is done) |
| POST | /tasks/{id}/complete | yes | n/a | 200 task + roast | 404, 409 (not pending) |
| POST | /tasks/{id}/move-to-today | yes | n/a | 200 task | 404, 409 (board full or not waitlisted) |

## Notifications
| Method | Path | Auth | Request body | Success | Errors |
|---|---|---|---|---|---|
| GET | /notifications?unread=true | yes | n/a | 200 list | 401 |
| PATCH | /notifications/{id}/read | yes | n/a | 200 | 404 |
| POST | /notifications/read-all | yes | n/a | 204 | 401 |

## Stats
| Method | Path | Auth | Success |
|---|---|---|---|
| GET | /stats | yes | 200 current streak, longest streak, completion rate, recent summaries |

## Other
| Method | Path | Auth | Success |
|---|---|---|---|
| GET | /health | no | 200 `{ "status": "ok" }` |

## Notes
- **Rollover** runs at the start of any task or stats request for the logged-in user (a shared dependency). See `04-architecture.md`.
- Roasts are returned in the response *and* saved as notifications.
- This is a draft. Update it as the real code is written.