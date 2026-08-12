---
name: risk-calibrated-validation
description: Use when choosing validation or verification effort and deciding whether hashes, repeated checks, exact comparisons, or defensive gates are justified. Match checks to credible risk and material consequence. Do not use this Skill to weaken security controls, high-risk or release validation, artifact identity requirements, scientific integrity checks, or validation explicitly required by the user.
---

# Risk-calibrated validation

Match verification effort to credible task risk while preserving high-value validation.

Use this model:

```text
validation effort should be proportional to
probability of a credible error x consequence of that error
```

Apply the governing rule:

> If an additional verification step cannot prevent a concrete, credible error that would materially affect the result, do not add that verification by default.

## Classify the task

### Routine, low-risk work

Examples include file reading, control-document searches, historical-view checks, ordinary code reading, small code changes, text extraction, routine data organization, and normal result retrieval.

Complete these tasks directly. Perform basic checks for paths, existence, syntax, and interpreters silently when needed. Report a check only when its result affects the task.

Do not add by default:

- SHA-256 or another checksum;
- file-size reporting;
- byte-for-byte comparison;
- repeated path verification;
- a gate without a defined failure mode; or
- fallback trees for unsupported low-probability anomalies.

### Medium-risk work

Examples include script behavior changes, batch file operations, data conversion, automated result extraction, and code changes with an explicit output contract.

Choose targeted validation such as:

- a semantic check;
- the relevant test;
- a representative sample; or
- an expected-output check.

Do not automatically expand a local change into a repository-wide audit, full hash inventory, or unrelated defensive gates.

### High-risk or formal-identity work

Use stronger evidence when the task involves a formal release, baseline freeze, critical model identity, parameter migration, proof that only specified changes occurred, a reproducibility package, security or integrity validation, cross-machine artifact identity, user-requested checksums, expensive computation, irreversible modification, or risk of a false scientific conclusion.

Select checks that address the risk, including as appropriate:

- SHA-256 or another approved hash;
- semantic and exact diffs;
- regression tests;
- targeted provenance;
- solver or datacheck execution; and
- artifact identity verification.

Hashes are evidence for identity and integrity when the risk requires them; they are not routine ceremony and are not prohibited.

## Handle execution-layer failures

When an execution problem occurs:

1. Identify the direct cause.
2. Apply the smallest sufficient fix.
3. Re-run validation directly related to that failure.
4. Do not use a local error as a reason to refactor the entire workflow.
5. Do not create a new audit project without a credible new risk.
6. Do not revalidate stable facts already confirmed in an unchanged environment.
7. Increase the validation level if the failure reveals a new credible risk.

## Preserve required controls

Never use this Skill to remove a user-required check or to weaken security, privacy, release, compliance, integrity, safety, or scientific validation. If the required validation appears excessive, explain the tradeoff but keep it unless the authorized decision-maker changes the requirement.

## References

Read [`references/validation-policy.md`](references/validation-policy.md) when selecting evidence for a risk tier. Read [`references/examples.md`](references/examples.md) for software, data, and scientific-computing examples.
