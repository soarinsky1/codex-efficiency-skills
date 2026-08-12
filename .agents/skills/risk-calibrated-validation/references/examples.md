# Examples

## Routine file and code work

Reading a control document or extracting a result normally needs a path and existence check plus correct interpretation. It does not normally need a SHA-256, file-size report, byte comparison, and repeated path check.

A small code change with an explicit behavior should receive the relevant focused test. A full repository audit is justified only if the change or failure creates repository-wide risk.

## Batch data conversion

For a reversible conversion, inspect the schema, run the transform, check expected row or record behavior, and review a representative sample. Use full reconciliation when omissions would be materially harmful or when the output is the authoritative migration artifact.

## Abaqus and finite-element work

For a formal solve, high-value validation commonly follows:

```text
model semantic change
-> datacheck
-> solver completion
-> key numerical outputs
-> relevant physical and result checks
```

That sequence validates model meaning, execution, numerical output, and the relevant physical interpretation. It does not imply that every ordinary step also needs:

```text
SHA
-> file-size check
-> byte comparison
-> repeated path verification
-> another SHA
-> another gate
```

For a formal baseline freeze, parameter migration, reproducibility package, or proof of minimal change, hashes and exact or semantic diffs become appropriate evidence again. The objective is less unnecessary work, not less reliable scientific work.

## Local execution failure

If a command fails because one path is wrong, correct the path and rerun the directly affected command or test. Do not automatically redesign the workflow or re-check every previously confirmed dependency. If the failure instead reveals ambiguous artifact identity, raise the validation level and verify the relevant provenance or checksum.
