# Notification system contract

The caller sends semantic content, priority, optional dedupe key, and lifetime. The core decides admission and ordering; a UI adapter renders and disposes views.

- Set an explicit queue capacity and overflow rule, including whether a high-priority message may evict a low-priority one. Avoid unbounded memory growth during event bursts.
- Define whether matching dedupe keys suppress, replace, or coalesce pending and visible messages; bound the dedupe window and clear it when appropriate.
- Associate every display timer with a generation token or handle. A timer from an old notification must not dismiss a replacement or a newly mounted UI.
- Make `Dismiss`, `Clear`, and teardown idempotent. Disconnect listeners, cancel owned tasks when possible, and ignore callbacks after disposal.
- Keep server-originated notices behind server-side validation and per-player rate limits; the client can manage purely local presentation. Never allow client-controlled text to become a global broadcast unchecked.
- Adapter contract covers show/update/hide, duration, safe areas, motion preferences, input, and screen-reader-friendly text as needed. The core should be testable without an actual ScreenGui.

Exercise overflow, same-key bursts, priority changes, stale timers, respawn/remount, and disconnect in a real client session.
