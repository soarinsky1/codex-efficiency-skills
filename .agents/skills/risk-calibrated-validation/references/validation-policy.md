# Validation policy

Validation should prevent or detect a defined failure that could materially change the result. Start from the task's output contract and credible failure modes, then choose the smallest evidence set that covers them.

## Decision questions

For each proposed check, ask:

1. What concrete error could this check detect or prevent?
2. Is that error credible in the current task and environment?
3. Would the error materially affect the result or downstream action?
4. Is this the least costly reliable check for that error?
5. Has the same fact already been confirmed without a relevant environment change?

If the first three answers are not clear, omit the check by default.

## Evidence by risk

| Risk level | Typical evidence |
| --- | --- |
| Low | Direct completion plus silent path, syntax, or existence checks when needed |
| Medium | Relevant test, semantic check, representative sample, expected-output check |
| High | Regression suite, semantic or exact diff, checksum, provenance, datacheck, artifact identity verification |

The table is a starting point, not a rigid checklist. A checksum is high-value for cross-stage artifact identity but low-value for ordinary text reading. A representative sample can be sufficient for a reversible batch transform, while an irreversible migration may require complete reconciliation.

## Escalation and de-escalation

Escalate when new evidence reveals a credible failure mode, the consequence grows, or the task enters a formal identity or release boundary. De-escalate repeated checks when the environment and relevant facts are unchanged.
