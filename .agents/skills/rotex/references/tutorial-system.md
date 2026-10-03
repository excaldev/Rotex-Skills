# Tutorial system contract

Expose operations such as `Register(definition)`, `Start(player, id)`, `Observe(player)`, and `Stop(player, reason)` as appropriate to the host project. Do not prescribe these exact names.

- Each tutorial has a stable ID and version, ordered or explicitly linked steps, and a definition of what server-observable event completes each step. Presentation metadata can be provided separately.
- Server owns active step, transition rules, rewards, and persisted completion. A client may request an action, but a claimed `CompleteStep` is not sufficient evidence.
- For each event, check player identity, current tutorial ID/version, expected step, prerequisites, event provenance, and idempotency. Duplicate or late events must not advance twice or grant a reward twice.
- Resume uses validated persisted progress. Define migration/reset behavior for removed or reordered steps and loading failure behavior; never silently treat missing data as completion.
- Replicate a compact current snapshot and transitions. A late-joining client can render from the snapshot without replaying historical local signals.
- The client adapter handles prompts, highlights, input cues, accessibility, and cleanup on death, respawn, UI replacement, exit, or disconnect. Tutorial core does not depend on a particular GUI framework.
- Define entry, exit, skip, and abandonment policies in the host game. Validate a multiplayer and reconnect scenario in Studio before declaring runtime readiness.
