# Reusable system boundaries

A reusable system owns one coherent behavior and exposes a small contract. It may span client, shared, and server modules, but that split is driven by authority and execution context, not a required folder pattern.

## Discovery

- Find existing services, module loaders, remotes, data access, UI composition, lifecycle, test runner, and dependency injection conventions.
- Write down the public operations, emitted events, configuration, ownership of state, and cleanup semantics before implementation.
- Keep game-specific rewards, copy, sounds, assets, UI layout, economy values, and progression definitions in adapters or configuration supplied by the host game.
- Keep the internal graph deep enough to hide meaningful complexity behind its public operations; avoid one-file-per-trivial-function fragmentation.

## Authority and runtime

- The server validates and commits consequential state. Treat client messages as requests, never proof that a purchase, tutorial step, reward, or inventory change occurred.
- Replicate only the state clients need; local signals and tables do not cross the network by themselves. Define the remote payload, sender, rate limit, and error behavior explicitly.
- Put server-only source in nonreplicated containers at authoring/build time. Do not rely on moving initially replicated code at server startup as a secrecy boundary.
- Keep client presentation and input separate from server rules. Shared code may define types and pure transformations, but shared runtime tables are separate copies on client and server.
- Choose direct module calls, attributes, signals, remotes, or tags according to the project; none is mandatory. Dispose event connections, timers, and observers when their owner ends.

## Portability check

Replace the host game's adapters with fakes or with another project's adapters. The core should still behave without referencing a named GUI, experience-specific service, currency, or asset. Document the minimum integration contract and error outcomes.
