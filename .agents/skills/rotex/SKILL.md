---
name: rotex
description: Plan, build, or review Roblox experiences and reusable Luau systems in an existing project, including tutorials, notifications, game loops, code architecture, and CLI or Studio MCP workflows. Use when the task concerns Roblox game construction or cross-project systems and should adapt to the project's own stack.
---

# Rotex

Inspect the project and the user's goal before choosing files, dependencies, or architecture. Preserve existing conventions where they work. Do not impose a loader, UI library, Rojo layout, starter project, or fixed template.

1. Identify the runtime surface: server, client, shared, Studio plugin, or external tooling. Find existing bootstrap code, package manifest, types, tests, and source-of-truth for the place.
2. For game design tasks, read [game-construction.md](references/game-construction.md). Define the player action, feedback, progress, and return loop before building supporting systems.
3. For reusable systems, read [system-boundaries.md](references/system-boundaries.md). For tutorials or notifications, also read the matching contract in `references/`.
4. Before editing Luau, read [luau-conventions.md](references/luau-conventions.md) and check the installed Studio/toolchain version for language features.
5. For CLI, Rojo, or Studio MCP work, read [execution-and-validation.md](references/execution-and-validation.md). Discover available capabilities. Identify the authoritative editor and avoid simultaneous unsynchronized edits of the same script.
6. Deliver a thin playable or callable slice, verify the invariants and failure paths, then iterate. Report what was exercised in a real Studio session separately from static checks or simulated instruction trials.

Keep the public contract small. Separate reusable rules from game-specific policy and presentation. Explain the integration seam to beginners with a concrete call site and where it belongs in their project; adapt names and paths to their actual tree.
