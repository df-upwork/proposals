1.  Замени пункт 12.1 следующим текстом:

<!-- end list -->

```markdown
12.1) Essence
`R6` automates `Assembly Build` creation via SuiteScript when `R4`/`R5` are unviable.
It balances accounting integrity (`NI` settings) against performance, depending on `R1` status.
```

2.  Замени пункт 12.1.1 следующим текстом:

<!-- end list -->

```markdown
12.1.1) Strategy `R6.1`: synchronous `JIT` build.
It executes during import (e.g., User Event Script) if `R1` is active and `NI` is prevented.
```

3.  Замени пункт 12.1.2 следующим текстом:

<!-- end list -->

```markdown
12.1.2) Strategy `R6.2`: asynchronous replenishment.
It executes post-import (e.g., Map/Reduce) if `R1` is active and `NI` is allowed for the `AI`.
```

4.  Замени пункт 12.2 следующим текстом:

<!-- end list -->

```markdown
12.2) Advantages
`R6` retains `AI` usage when native options fail.
`R6.1` ensures accounting integrity (prevents `NI`).
`R6.2` optimizes performance by minimizing import impact.
```

5.  Замени пункт 12.3 следующим текстом:

<!-- end list -->

```markdown
12.3) Key challenges
`R6` increases complexity, TCO, and demands robust error handling.
`R6.1` severely impacts performance, risking timeouts, locking, and governance breaches.
`R6.2` requires allowing `NI` (contradicting best practices), mandates Backorder Management (see 6.3.2), and causes latency.
```