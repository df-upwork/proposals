# 1. Point 3 (`⋇2`)
`Vᨀ` uses the special `Transient` storage for objects with a TTL shorter than the `shortlived` parameter and for buffering uncacheable response bodies.
By default, this storage uses the system allocator `malloc` and has no limit on the maximum amount of consumed memory.
During an influx of traffic resulting in uncacheable responses (e.g. containing `Set-Cookie` headers or `Cache-Control: private` directives), `Vᨀ` uncontrollably fills RAM with buffered data until the server crashes completely (OOM).

# 2. Point 8.2 (`Rationale`)
In the standard configuration, `Vᨀ` uses an unbounded storage for short-lived objects and uncacheable response buffers, which occupies all available memory during attacks or failures.
Setting a hard limit forces `Vᨀ` to apply the eviction algorithm (LRU) to transient objects when the threshold is reached, instead of allocating new memory pages.
This creates a guaranteed safety barrier preventing a server crash (OOM) even during a flood of uncacheable responses.
`R2` compensates for the architectural vulnerability of `Vᨀ` related to the `unbounded` nature of the transient storage by default.