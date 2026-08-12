---
name: long-task-polling
description: Use for asynchronous waiting and polling of a long-running non-interactive process when repeated status checks yield no actionable information. Covers solvers, long tests, compilation, simulation, data processing, training, and batch jobs. Do not use for interactive input, approvals, safety-sensitive live monitoring, short tasks, stalled prompts, or intermediate output that determines the next action.
---

# Long-task polling

Reduce unnecessary agent wake-ups and repeated inference while waiting for long-running, non-interactive processes.

## Apply the decision rule

Continue waiting efficiently when all of these are true:

1. The process is still running.
2. The process is expected to take minutes or longer.
3. No user input or approval is pending.
4. No new output requires interpretation or action.
5. The process is not plausibly blocked on an interactive prompt.
6. Live observation is not required for safety or control.

Use this state transition:

```text
process still running
-> no new actionable information
-> keep waiting efficiently
```

Do not wake the agent only to report that the process is still running.

## Choose the wait mechanism

1. Inspect the active tool contract before choosing parameters.
2. Use the longest reasonable bounded wait supported by the current runtime for a pure, non-interactive completion wait.
3. When the active runtime supports `yield_time_ms`, treat `>=180000 ms` as a practical target for long pure waits and about `300000 ms` as a useful default when intermediate output is not needed.
4. Treat those values as engineering heuristics and runtime workarounds, not fixed OpenAI recommendations or guarantees.
5. If the tool contract does not expose such parameters, do not invent them. Use the runtime's actual longest reasonable wait mechanism while preserving the higher-level rule.
6. Rely on early-return behavior when supported: if the process completes before the interval, return immediately instead of artificially waiting out the interval.

## Handle nested waits

When a wait runs inside a JavaScript or tool-execution wrapper that has its own yield window:

1. Confirm that both inner and outer timing controls exist in the active runtime.
2. Set the outer window longer than the longest nested wait or timeout.
3. A margin of about 30 seconds is a practical engineering heuristic.
4. Do not copy historical wrapper syntax into a runtime that does not support it.

## Preserve interactive behavior

Do not apply long polling to a non-empty `write_stdin` call or equivalent operation that sends:

- interactive input;
- a confirmation;
- a password or prompt response; or
- required control input.

Send required input promptly using the runtime's normal interactive mechanism.

## Do not apply this Skill when

- waiting for user approval or authorization;
- output must be watched in real time to make a safety decision;
- debugging is interactive;
- the task is short;
- the process may be stopped at a prompt;
- intermediate results determine the next operation; or
- the process state is unknown and a targeted status check is needed to diagnose it.

## Report progress proportionally

Provide an update when new actionable information appears, the process completes, the process fails, user input becomes necessary, or the agreed monitoring boundary is reached. Do not create repeated empty status turns.

## References

Read [`references/runtime-notes.md`](references/runtime-notes.md) when adapting the policy to a concrete wait API or wrapper. Read [`references/rationale.md`](references/rationale.md) when explaining measurement boundaries or designing an evaluation.
