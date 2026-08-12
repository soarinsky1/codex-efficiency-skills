# Benchmarks

This directory defines reproducible experiments for evaluating the Skills without publishing unsupported performance claims.

Version 0.1.0 contains methodology only. Add results only when the workload, runtime, model, tool contracts, raw observations, and correctness criteria can be documented well enough for another contributor to reproduce the comparison.

## Evaluation tracks

### Long-task polling

Compare a short-polling agent loop with bounded long polling on the same non-interactive job. Hold the job, environment, completion criterion, and required user communication constant.

### Risk-calibrated validation

Compare a workflow with redundant validation against a risk-calibrated workflow on the same task. Define the credible failure modes and correctness criteria before running either condition.

## Required principle

Efficiency is acceptable only when task correctness and required controls do not decline. Do not remove security, integrity, release, or user-required checks to improve an efficiency metric.

See [`methodology.md`](methodology.md) for metrics and experiment design.
