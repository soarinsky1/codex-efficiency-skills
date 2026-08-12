# Benchmark methodology

## Objective

Measure whether the Skills reduce non-actionable agent activity while preserving correctness, required validation, and completion behavior.

## Experimental design

1. Select representative tasks and record their expected outputs and credible failure modes before execution.
2. Run a control condition using the existing polling or validation workflow.
3. Run a treatment condition using one Skill while holding the task, inputs, runtime, model, and tool contracts as constant as practical.
4. Repeat enough times to expose run-to-run variance. Report the number of runs and any order randomization.
5. Preserve raw event data needed to reproduce derived counts without publishing secrets or private session content.
6. Compare correctness first, then efficiency metrics.

## Metrics

Record, when available:

- agent wake-ups;
- empty polling turns;
- poll interval;
- tool calls;
- raw input tokens;
- cached input tokens;
- uncached input tokens;
- output tokens;
- wall-clock completion;
- validation tool calls;
- redundant checks avoided; and
- task correctness.

Define an empty polling turn as an agent iteration that observes no actionable state change and selects another wait. Define a redundant check as a verification step with no identified credible failure mode or one that repeats unchanged evidence without a relevant environment change.

## Long-task polling comparison

Use a deterministic or well-characterized non-interactive job long enough to span multiple short polling intervals. Compare:

- short polling with repeated agent wake-ups; and
- the longest reasonable bounded wait supported by the active runtime.

Confirm that both conditions detect completion and failure correctly. Record whether the wait API returns early when the process finishes.

## Risk-calibrated validation comparison

Use tasks across low, medium, and high risk. Before execution, list the checks required to cover credible failure modes. Compare:

- a workflow that performs repeated or unrelated validation; and
- a workflow that performs the defined risk-proportional checks.

Score both conditions against the same correctness and integrity criteria. High-risk and user-required controls must remain in both conditions.

## Reporting boundaries

- Separate cached and uncached input tokens when the runtime exposes them.
- Do not equate raw tokens with billing, rate-limit consumption, energy, or monetary cost.
- Do not infer energy or carbon reductions from token counts alone.
- Label non-reproducible numbers as `preliminary local observation`.
- Do not present a local percentage as a universal result.
- Publish no result when the underlying observations cannot be shared or reproduced sufficiently.
