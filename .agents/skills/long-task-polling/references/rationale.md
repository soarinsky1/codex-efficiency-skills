# Rationale and claim boundaries

Repeated empty polling can create avoidable agent-loop iterations and inference workload, particularly for long-running non-interactive jobs. Each wake-up may cause the agent to re-read context, interpret an unchanged status, and choose the same wait action again.

The intended optimization is narrow: eliminate agent turns that add no actionable information while preserving completion detection, failure handling, required interaction, and safety monitoring.

## Measurement boundaries

Keep these quantities distinct:

```text
raw token volume
!= billing
!= rate-limit consumption
!= energy consumption
!= monetary cost
```

Caching, model behavior, product accounting, tool implementation, and workload shape can change the relationship between these quantities. Do not claim a universal token-saving percentage.

Environmental claims require direct measurement and an explicit system boundary. A conservative statement is acceptable: reducing unnecessary inference cycles may improve computational resource efficiency. Do not quantify energy or carbon reduction without evidence.

## Reliability boundary

The Skill changes how an agent waits, not what successful completion means. It must not suppress actionable errors, interactive prompts, safety signals, or intermediate results required for the next decision.
