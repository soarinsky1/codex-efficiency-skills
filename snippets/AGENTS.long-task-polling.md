## Long-running asynchronous work

- For a long-running, non-interactive process, avoid repeated wake-ups that only confirm it is still running.
- When no intermediate output, approval, or input is needed, use the longest reasonable bounded wait supported by the active runtime and return early when the process completes.
- If `yield_time_ms` is supported, `>=180000 ms` is a practical target and about `300000 ms` is often useful for pure waits; treat these as heuristics, not fixed OpenAI guarantees.
- If a wait is nested in a wrapper with its own yield window, make the outer window longer than the inner wait when the runtime supports both controls; about 30 seconds of margin is a practical heuristic.
- Do not invent unsupported parameters or apply long polling to interactive input, approvals, safety-sensitive monitoring, short jobs, stalled prompts, or actionable intermediate output.
