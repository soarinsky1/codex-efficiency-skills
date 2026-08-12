## Long-running asynchronous work

- For a long-running, non-interactive process, avoid repeated wake-ups that only confirm it is still running.
- When no intermediate output, approval, or input is needed, use the longest reasonable bounded wait supported by the active runtime and return early when the process completes.
- If `yield_time_ms` is supported, `>=180000 ms` is a practical target and about `300000 ms` is often useful for pure waits; treat these as heuristics, not fixed OpenAI guarantees.
- If a wait is nested in a wrapper with its own yield window, make the outer window longer than the inner wait when the runtime supports both controls; about 30 seconds of margin is a practical heuristic.
- Do not invent unsupported parameters or apply long polling to interactive input, approvals, safety-sensitive monitoring, short jobs, stalled prompts, or actionable intermediate output.

## Risk-calibrated validation

- Match verification effort to the probability and consequence of a credible error.
- Do not add a check by default unless it can prevent or detect a concrete error that would materially affect the result.
- For routine work, complete the task directly and keep necessary path, existence, syntax, and interpreter checks silent unless they affect the outcome.
- Use targeted tests, semantic checks, representative samples, or expected-output checks for medium-risk changes.
- Use hashes, exact diffs, regression tests, provenance, datachecks, and identity verification when high-risk, security, release, migration, reproducibility, scientific-integrity, or user requirements justify them.
- On a local execution failure, make the smallest sufficient fix and rerun directly relevant validation. Expand the workflow only when the failure reveals a new credible risk.
