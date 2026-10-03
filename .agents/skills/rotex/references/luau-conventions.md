# Luau implementation conventions

- Prefer `--!strict` on maintained modules and type the public surface, payloads, callbacks, and state boundaries. Let straightforward local values infer their types. Narrow untrusted data at runtime; static types cannot validate remote input.
- `const name = value` prevents rebinding in Luau versions that support it. It does not freeze a table or Instance; use `table.freeze` for a table whose contents must be immutable, when appropriate. Check the project's installed Luau analyzer and Studio compatibility before adding newer syntax broadly.
- Use `task.wait`, `task.spawn`, `task.defer`, and `task.delay` instead of legacy scheduler globals when scheduling is needed. Prefer events over polling; hold and cancel owned threads where possible and guard callbacks with lifecycle state.
- Use relative string `require("./Module")` only where the project's Roblox/Studio and external toolchain support that resolution. Otherwise use the project's established Instance paths. Avoid claiming that a path syntax is universally portable.
- Place sensitive modules in server-only source containers before runtime. Validate all RemoteEvent/RemoteFunction arguments, permissions, frequency, and state transitions on the server.
- Keep module initialization side effects controlled. Give long-lived systems explicit start/stop or equivalent lifecycle and disconnect event listeners on teardown.
- Use existing formatter, analyzer, and package manager settings. Check type solver behavior in the target environment rather than demanding a particular rollout state.

Reference: [Luau syntax](https://luau.org/syntax), [Luau types](https://luau.org/types/), [Roblox scheduling](https://create.roblox.com/docs/scripting/scheduler), and [Roblox type checking](https://create.roblox.com/docs/luau/type-checking). Recheck platform documentation when updating these conventions.
