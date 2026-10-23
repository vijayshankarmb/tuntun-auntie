# Requirements

## Goal
Help people actually finish their tasks. A user commits to at most five tasks per day. If they finish them, they build a streak. If they don't, the app roasts them in their chosen tone.

## User stories
**Account**
1. As a user, I can sign up with name, email and password so that I have my own account.
2. As a user, I can log in so that I can see my own tasks.
3. As a user, I can choose my roast tone (sarcastic, loving or angry) so that the feedback suits me.
4. As a user, I can set my time zone so that my day starts and ends at my local midnight.

**Tasks**
5. As a user, I can add a task so that it goes on today's board (max 5).
6. As a user, I can add a task when my board is full, and it goes to the waitlist so that I don't lose it.
7. As a user, I can edit or delete a pending task so that I can fix mistakes.
8. As a user, I can mark a task done so that I make progress and keep my streak alive.
9. As a user, I can see my waitlist so that I know what is waiting.
10. As a user, I can move a waitlisted task to today's board (if there is room) so that I can work on it.
11. As a user, I can edit or delete tasks in my waitlist so that it stays tidy.
12. As a user, I can view my past days (history) so that I can see how I did.

**Accountability**
13. As a user, I get a roast when I add a task, complete a task, complete a carried-over task, or miss tasks, so that the app keeps me honest.
14. As a user, I see in-app notifications so that I can read the roasts and reminders.
15. As a user, I can mark notifications as read so that my list stays clean.
16. As a user, I can see my current and longest streak so that I stay motivated.

## Rules and constraints
1. **Daily limit:** at most 5 tasks on a day's board.
2. **Day:** a calendar day, midnight to midnight, in the user's time zone.
3. **Midnight rollover:**
   - Tasks still pending when the day ends are **missed**. They can no longer be completed, edited or deleted *on that board*.
   - Missed tasks move to the **waitlist** (they carry over; nothing is deleted).
   - The user gets a roast for the missed tasks.
4. **Streak:**
   - +1 when every task on that day's board was completed.
   - Resets to 0 if the day had one or more missed tasks.
5. **Waitlist:**
   - Tasks added when the board is full go to the waitlist.
   - Waitlisted tasks never move to the board automatically. The user moves them manually, and only if the board has room.
   - In the waitlist, the user can edit, delete, or move tasks to the board.
6. **Completed tasks** are kept as history and can no longer be edited or deleted.
7. **Roast events:**
   - Task added
   - Task completed (a comment, e.g. sarcastic praise)
   - Carried-over task completed (a "finally" roast)
   - Day ended with missed tasks (midnight)
8. **Roast tone:** sarcastic, loving or angry. Roast messages are pre-written templates in v1.
9. **Notifications:** in-app only in v1.
10. **Reminders** (stretch goal for v1): when the user opens the app with pending tasks, show a nudge like "You still have 3 tasks pending, lazy human."

## Out of scope for v1
- LLM-personalized roasts
- Email notifications
- Scheduled background jobs (the midnight rollover is computed when the user next uses the app. See decision D4.)
- Voice input and image-to-task
- Social features, sharing, teams

## Open questions (to settle while building)
1. **"Late complete"** is interpreted as completing a task that was previously missed and carried over (`times_missed > 0`). Is this the right meaning?
2. **Streak with fewer than 5 tasks:** currently a day counts if all tasks on the board are done and the board had at least 1 task. Should the board need exactly 5?
3. **Empty days:** an empty board does not change the streak. Should it?
4. **Multi-day absence:** if the user is away for several days, each unprocessed day is rolled over when they return. Does an empty day break the streak?