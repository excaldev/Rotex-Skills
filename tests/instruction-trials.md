# Instruction trials

These are review prompts and expected behaviors, not Studio runtime test results.

## Reuse a tutorial in a second experience

Prompt: “Bring our obby tutorial into a racing game; change the steps and GUI but keep progress and resume.”

Expected: inspect both projects; keep trusted progress/resume in a reusable core; register racing-specific step definitions and UI adapter; server validates each event and handles duplicate/late signals; specify version migration; verify with a reconnecting player in Studio. Do not copy an entire obby project or grant progress from a client claim.

## Rojo and Studio MCP both present

Prompt: “Use the CLI and Studio MCP to add notifications to my Rojo project.”

Expected: discover actual tool capabilities and Rojo mapping; choose the filesystem as the authoritative source for synced scripts; use Studio MCP for inspection and runtime checks; avoid concurrent writes to the same script; verify synced content before playtesting. If Studio isn't connected, report that integration remains unverified.
