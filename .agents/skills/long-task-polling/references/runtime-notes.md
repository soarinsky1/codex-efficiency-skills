# Runtime notes

Wait APIs change across products and versions. Inspect the active contract instead of assuming a historical parameter set.

## Supported bounded waits

For a runtime that explicitly supports a `yield_time_ms`-style option, a long non-interactive completion wait can use a practical target of at least 180 seconds, with roughly 300 seconds preferred when no intermediate output or interaction is needed. These values are heuristics, not API guarantees.

If the runtime caps the value, use the supported cap. If it returns early on completion, preserve that behavior.

## Nested execution wrappers

An outer execution cell or wrapper should not yield before the nested wait finishes. When both controls are documented by the active runtime, make the outer window longer than the longest nested wait; about 30 seconds of margin is a reasonable engineering allowance.

Example relationship, not portable syntax:

```text
outer yield window >= longest nested wait or timeout + approximately 30 seconds
```

## Interactive calls

Do not add a long pure-wait interval to calls carrying non-empty interactive input. Input delivery and polling are different operations and should remain separate.

## Fallback

If the active contract lacks configurable wait parameters, use its actual blocking, event-driven, callback, or longest bounded status mechanism. Never fabricate parameters to resemble another runtime.
