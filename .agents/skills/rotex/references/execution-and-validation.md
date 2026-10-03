# Execution and validation

## Choose the editing surface

- Inspect available tools and their supported operations before choosing a CLI, Roblox Studio MCP, or filesystem edit. Do not assume a particular MCP server or command name exists.
- For Rojo projects, identify the source tree, project mapping, and sync direction. For direct Studio edits, inspect the DataModel and script instances before mutation.
- Choose one authoritative source for each script during a task. If CLI/Rojo and MCP both can edit it, synchronize explicitly and verify the final content in Studio before changing surfaces.
- Scope edits to the user's place and branch. Preserve existing scripts and layout; propose a mapping only when the project has none.

## Evidence ladder

1. Static: links and frontmatter, syntax, type checks, formatting, deterministic contract tests.
2. Integration: remotes, data loading, reconnect, client/server timing, UI mount/unmount, and multiplayer in Studio.
3. Production: telemetry or guarded rollout where warranted.

Report each level actually completed. An instruction trial or a written contract is not a running Studio test. For a reusable system, test normal flow, duplicate messages, malformed client input, cancellation, late callbacks, and integration with a second host adapter.
