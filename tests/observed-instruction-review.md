# Observed instruction review — 3 October 2026

This is a same-agent, nonblind review of the recovered skill. The reviewer had
already read the handoff and references. It is evidence of the response below,
not an independent agent evaluation, implemented Roblox system, or Studio test.

## Task presented

“Add notifications to our existing Rojo game. We use Fusion for UI. Purchase
messages should appear before routine notices, duplicate messages should not
pile up, and respawning must not let old timers hide a new notice. Keep our
current bootstrap. Studio is not connected.”

No host project was supplied. The observed output is therefore an integration
proposal; inspection and implementation cannot honestly be marked complete.

## Observed response

Read `system-boundaries.md`, `notification-system.md`, and
`execution-and-validation.md`. Before writing Luau, also read
`luau-conventions.md` and check the host toolchain. Inspect the Rojo mapping,
existing client bootstrap, Fusion version, UI ownership, purchase handling,
and test runner. Ask for the host checkout because it is missing; do not ask
the user to choose a new framework or loader.

Keep synced scripts authoritative in the filesystem. Use the existing client
bootstrap to create a notification controller and pass a Fusion adapter into
it. The controller accepts semantic notices; the adapter owns Fusion views
and their cleanup. Actual filenames and Fusion calls depend on the host tree
and installed API, so do not invent those details.

For a first callable slice, propose a bounded pending queue of eight notices,
FIFO within each priority, and no interruption of the visible notice. Purchase
notices enter ahead of pending routine notices. At capacity, evict the oldest
pending routine notice; reject admission when no such notice exists. Return an
explicit admission result. Let the host override these defaults.

Coalesce matching pending notices; update a matching visible notice and renew
its lifetime. Deduplication covers only visible and pending entries, so its
memory is bounded. Each visible replacement and UI remount advances a
generation. A timer captures that generation and can dismiss only its own
display. Disposal disconnects listeners, cancels owned timers where possible,
and invalidates every callback. Define whether remount retains pending notices
in the host adapter rather than relying on an old GUI instance.

The server remains authoritative for purchases and rewards. Only server-verified
purchase outcomes produce purchase notices; notification text never grants an
entitlement. Validate and rate-limit any server broadcast request. Local routine
notices can stay entirely client-side.

Test admission, ordering, deduplication, stale callbacks, repeated disposal,
and adapter replacement with a fake clock and UI adapter using the host's test
runner. Test receipt integration, respawn, and two players in Studio when it is
available. With no host or Studio connection, report those checks as unrun.

## Review result

The response selected the relevant references, retained the existing stack,
defined the bootstrap/adapter seam, and gave explicit failure and cleanup
behavior. It correctly stopped short of invented implementation and runtime
claims. No instruction failure was observed in this limited review, so no skill
revision was made. A fresh agent trial with a real host checkout and Studio
integration remain outstanding.
