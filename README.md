# Rotex Skills

Framework-neutral agent guidance for Roblox development and reusable Luau systems.

The [`rotex` skill](.agents/skills/rotex/SKILL.md) guides agents through Roblox game construction, portable system contracts, Luau conventions, and safe CLI/Studio workflows. It adapts to an existing project and does not install a framework or copy a fixed project template.

To use it from an agent terminal, make this repository available to the agent and point it at `.agents/skills/rotex/SKILL.md`. For Studio MCP work, connect a Studio-capable tool separately; the skill discovers its available operations at run time. The skill itself contains guidance, not an MCP server or executable Roblox package.

Run `python3 scripts/validate_skills.py` and `python3 -m unittest discover -s tests` to check the Markdown contract. Playtesting and client installation must be verified separately in Roblox Studio.
