## Risk-calibrated validation

- Match verification effort to the probability and consequence of a credible error.
- Do not add a check by default unless it can prevent or detect a concrete error that would materially affect the result.
- For routine work, complete the task directly and keep necessary path, existence, syntax, and interpreter checks silent unless they affect the outcome.
- Use targeted tests, semantic checks, representative samples, or expected-output checks for medium-risk changes.
- Use hashes, exact diffs, regression tests, provenance, datachecks, and identity verification when high-risk, security, release, migration, reproducibility, scientific-integrity, or user requirements justify them.
- On a local execution failure, make the smallest sufficient fix and rerun directly relevant validation. Expand the workflow only when the failure reveals a new credible risk.
