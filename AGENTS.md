# Repository maintenance

- Keep each Skill focused on one job; do not merge the two Skills into a general efficiency or token-saving Skill.
- Use current official OpenAI Skill documentation as the format authority.
- Do not make unsupported performance, cost, energy, carbon, or environmental claims.
- Treat runtime-specific syntax and wait values as conditional examples and update them when tool contracts change.
- Run `python scripts/validate_skills.py` after changing Skill metadata or structure.
- Avoid unnecessary repository-wide validation, dependencies, scripts, and defensive gates.
