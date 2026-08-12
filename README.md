# codex-efficiency-skills

`codex-efficiency-skills` provides focused Agent Skills for improving execution and verification efficiency in long-running Codex workflows without weakening task reliability.

The project targets avoidable agent turns, redundant tool calls, repeated inference, and low-value verification. It does not treat fewer tokens or fewer checks as goals by themselves.

## Why it exists

Agent workflows can waste resources in two common ways:

- waking repeatedly to learn only that a non-interactive process is still running; and
- expanding routine validation into checks that do not address a concrete, credible failure mode.

Reducing those patterns can lower unnecessary agent-loop iterations and inference workload. Raw token volume is not the same as billing, rate-limit consumption, energy consumption, or monetary cost, and this project makes no universal savings claim. Reducing unnecessary inference cycles may also improve computational resource efficiency, but environmental effects require workload-specific measurement.

## Skills

The repository contains two independent Skills. They remain separate so each can match only the tasks where it is relevant.

### `long-task-polling`

Use this Skill for asynchronous waiting on long-running, non-interactive processes such as simulations, solvers, test suites, compilation, data processing, training, or batch jobs.

Its governing state is:

```text
process still running
-> no new actionable information
-> keep waiting efficiently
```

It does not apply to interactive input, approval waits, safety-sensitive live observation, short jobs, or cases where intermediate output determines the next action. Runtime-specific wait values in the Skill are practical heuristics, not fixed OpenAI guarantees.

### `risk-calibrated-validation`

Use this Skill to match verification effort to credible task risk:

```text
validation effort ~ probability of a credible error x consequence of that error
```

Routine tasks receive direct or targeted checks. High-risk work can and should use hashes, exact diffs, regression tests, provenance, datachecks, or identity verification when those checks address a real failure mode. Security validation, user-required checks, formal release evidence, and other high-risk controls are never weakened by default.

## Installation and usage

Codex currently discovers repository-scoped Skills under `.agents/skills` from the current working directory up to the repository root. Each Skill directory contains a required `SKILL.md` with `name` and `description` frontmatter. This layout follows the [official OpenAI Skill documentation](https://learn.chatgpt.com/docs/build-skills).

To explore the Skills in this repository:

```bash
git clone https://github.com/soarinsky1/codex-efficiency-skills.git
cd codex-efficiency-skills
```

Start Codex in the repository and invoke a Skill explicitly, for example `$long-task-polling`, or let Codex match the task against the Skill description.

To use a Skill in another repository, copy its complete directory into that repository's `.agents/skills/` directory. For user-scoped discovery across repositories, Codex also supports `$HOME/.agents/skills/`. Keep references next to the corresponding `SKILL.md` so progressive disclosure remains intact.

Official OpenAI documentation currently prefers plugin packaging when distributing multiple reusable Skills broadly. Version 0.1.0 intentionally keeps the canonical standalone, repo-scoped Skill directories simple; plugin packaging can be added separately without merging the Skills.

## Skill vs. `AGENTS.md`

A Skill is a task-specific reusable workflow. `AGENTS.md` is a persistent instruction mechanism loaded for every applicable task.

You can use only the Skills, or copy a compact policy from [`snippets/`](snippets/) into `~/.codex/AGENTS.md` when you want the behavior to apply by default. A global `~/.codex/AGENTS.override.md`, when present and non-empty, takes precedence over the ordinary global `AGENTS.md`; see the [official OpenAI AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

This repository does not modify global Codex instructions.

## Design principles

- Preserve task correctness and reliability.
- Keep each Skill focused on one job.
- Prefer instructions over runtime-specific automation.
- Treat runtime values as bounded heuristics, not portable guarantees.
- Add validation only when it addresses a concrete, credible error.
- Avoid unsupported performance, cost, energy, or environmental claims.
- Fix execution-layer failures at the smallest sufficient scope.

## Benchmarks

The [`benchmarks/`](benchmarks/) directory defines a reproducible comparison framework. It tracks agent wake-ups, empty polling turns, tool calls, token categories, wall-clock completion, validation calls, redundant checks avoided, and task correctness.

Version 0.1.0 publishes methodology only. It does not present local observations as universal benchmark results or equate raw tokens with cost.

## Trigger behavior

[`tests/trigger-cases.md`](tests/trigger-cases.md) documents positive, negative, high-risk, and combined matching cases for the two Skills. These cases define intended activation boundaries and help prevent efficiency guidance from overriding interactive, security-sensitive, release-critical, or scientific validation requirements.

## Limitations

- Tool contracts and maximum wait behavior vary by Codex version and runtime.
- A longer polling interval does not help when a process is interactive or intermediate output is actionable.
- Risk classification requires task context and does not replace security, integrity, scientific, or release requirements.
- Efficiency effects must be measured on representative workloads; no fixed percentage improvement is claimed.

## Contributing

Keep changes instruction-first and scoped to one of the two responsibilities. Use official OpenAI documentation as the format authority, update runtime examples when contracts change, and run:

```bash
python scripts/validate_skills.py
```

Do not add benchmark claims without reproducible data and clearly stated measurement boundaries.

## License

MIT. See [`LICENSE`](LICENSE).
