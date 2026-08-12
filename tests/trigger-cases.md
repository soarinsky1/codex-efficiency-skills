# Skill trigger behavior cases

These cases document the intended matching boundaries for the repository's two Agent Skills.

They are behavioral specifications, not claims that every Codex version or model will produce an identical implicit-matching decision. The purpose is to make intended activation and non-activation boundaries explicit and reviewable.

## `long-task-polling`

### Should match

#### Case L1 — Long solver with no intermediate action

**Prompt**

> The Abaqus solve is still running and normally takes about 40 minutes. No intermediate output is needed. Wait for completion without repeatedly waking just to report that it is still running.

**Expected**

`long-task-polling` is relevant.

**Reason**

This is a long-running, non-interactive process and repeated status checks provide no actionable information.

---

#### Case L2 — Long test suite

**Prompt**

> The full regression suite usually runs for 25 minutes. Nothing needs to be inspected unless the process finishes or fails.

**Expected**

`long-task-polling` is relevant.

---

#### Case L3 — Batch data processing

**Prompt**

> This batch conversion job may take an hour. Continue waiting efficiently and only act when it completes or reports an error.

**Expected**

`long-task-polling` is relevant.

---

#### Case L4 — Long compilation

**Prompt**

> The build is expected to take several minutes and does not require interactive input. Avoid repeated empty polling while it runs.

**Expected**

`long-task-polling` is relevant.

---

### Should not match

#### Case L5 — Interactive prompt

**Prompt**

> The installer is asking whether to overwrite an existing file. What should be entered?

**Expected**

`long-task-polling` should not control the task.

**Reason**

User or agent input is required immediately.

---

#### Case L6 — Approval required

**Prompt**

> The deployment is waiting for my approval before continuing.

**Expected**

`long-task-polling` should not replace the approval interaction.

---

#### Case L7 — Intermediate output determines next action

**Prompt**

> Watch the solver log. If convergence warnings start increasing, stop the run and inspect the model.

**Expected**

`long-task-polling` should not apply as a blind long wait.

**Reason**

Intermediate output is actionable.

---

#### Case L8 — Short task

**Prompt**

> This command normally completes in five seconds. Run it and show me the result.

**Expected**

`long-task-polling` is unnecessary.

---

## `risk-calibrated-validation`

### Should match

#### Case R1 — Routine file edit

**Prompt**

> Make this small documentation change. Decide whether SHA-256, byte-level comparison, or a repository-wide audit is actually necessary.

**Expected**

`risk-calibrated-validation` is relevant.

**Reason**

Verification effort should be selected according to the credible risk of the change.

---

#### Case R2 — Small code fix

**Prompt**

> Fix this isolated parser bug and run the directly relevant test. Do not expand the task into unrelated repository auditing unless the failure reveals another real risk.

**Expected**

`risk-calibrated-validation` is relevant.

---

#### Case R3 — Routine result extraction

**Prompt**

> Read the existing result files and extract the requested values. Avoid redundant identity checks unless there is evidence that the files may have changed.

**Expected**

`risk-calibrated-validation` is relevant.

---

#### Case R4 — Batch transformation

**Prompt**

> Convert these files using the existing script and validate a representative output rather than adding unrelated defensive gates.

**Expected**

`risk-calibrated-validation` is relevant.

---

### Must preserve stronger validation

#### Case R5 — Release artifact

**Prompt**

> This is the final release artifact. Verify that it is byte-identical to the approved baseline and report its SHA-256.

**Expected**

The Skill must preserve the requested strong validation.

**Reason**

Formal release identity is a credible high-consequence requirement.

---

#### Case R6 — Baseline freeze

**Prompt**

> Freeze this model as the authoritative baseline. Record its identity so future parameter migrations can prove they started from the exact approved model.

**Expected**

Strong identity verification is appropriate.

---

#### Case R7 — Scientific model migration

**Prompt**

> Migrate only the specified FE parameters and prove that unrelated model topology and material definitions were unchanged.

**Expected**

Targeted semantic and/or exact-difference evidence is appropriate.

---

#### Case R8 — Security-sensitive change

**Prompt**

> Modify this authentication code and run all security checks required by the repository policy.

**Expected**

The Skill must not weaken required security validation.

---

## Combined cases

### Case C1 — Long high-risk computation

**Prompt**

> Run the formally approved simulation. It takes about an hour. Do not repeatedly poll while it is running, but after completion perform the required solver and result validation.

**Expected**

Both Skills may be relevant:

- `long-task-polling` governs the non-interactive waiting period.
- `risk-calibrated-validation` preserves the required post-run validation.

The efficiency policy must not remove required scientific verification.

---

### Case C2 — Long routine computation

**Prompt**

> Run this established batch script. It normally takes 30 minutes. No intermediate output is needed, and after completion just verify the expected output exists and is readable.

**Expected**

Both Skills may be relevant, with lightweight validation proportional to the routine task risk.

---

## Interpretation

These cases define intended behavioral boundaries:

```text
efficient waiting
!=
ignoring actionable intermediate state
```

and:

```text
risk-calibrated validation
!=
weak validation
```

The governing objective is to remove low-value agent activity while preserving the evidence required for correctness, integrity, security, release management, and scientific work.
