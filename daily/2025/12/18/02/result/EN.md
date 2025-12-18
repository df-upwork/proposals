1) Both your options are bad.
I outline their critical drawbacks in points 4 and 5.
In points 6 and 7, I outline 2 high-quality solutions.

2) Key definitions:
- Data replication: `R᛭`
- Your «Option 1» (use of `R᛭`): `⌖1`
- Your «Option 2» («a scheduled backend job»): `⌖2`
- «setup may limit built in replication support»: `P1†`
- «a naive scheduled job could be intensive»: `P2†`
- Your system as a whole: `S༄`
- The frontend of `S༄`: `F༄`
- Bubble.io: `Bᨀ`
- React: `Rᨀ`
- PostgreSQL: `Pᨀ`
- Supabase: `Sᨀ`
- Tinybird: `Tᨀ`
- `Bᨀ` Data API: `DA`
- `Bᨀ` Workload Units: `WU`
- Write-Ahead Log: `WAL`

3) `S༄` is likely a B2C platform for gaming clips, potentially designed for integration with the Twitch API.
Viewers generate a stream of events via a `Rᨀ` interface.
`S༄` likely utilizes `Rᨀ` as `F༄` and relies on a `Bᨀ` backend.

4) Disadvantages of `⌖1`
4.1) `Bᨀ` uses a multi-tenant `Pᨀ` architecture that prevents direct access to `WAL` or `R᛭` slots for security reasons.
Consequently, you are architecturally denied access to the low-level synchronization mechanisms required for standard `R᛭`.
4.2) Periodic API polling has critical scalability flaws in your case:
4.2.1) `DA` throughput is strictly constrained by application-layer serialization overhead and `Bᨀ` rate limits.
Attempting to accelerate extraction through concurrent requests rapidly hits strict rate limits.
This resource contention creates a bottleneck that makes daily extraction of large datasets slow and operationally fragile.
4.2.2) The real throughput in `Bᨀ` is strictly constrained by server-side processing time.
Complex read requests consume significant `WU` and trigger timeouts.
4.2.3)`DA` lacks transactional snapshot isolation across pages.
Maintaining data consistency during the prolonged export window necessitates implementing strict timestamp filtering logic.
The export action «Email a list of things as CSV» relies on asynchronous email delivery, preventing reliable programmatic ingestion.
Plugins shift the load to server-side actions, consuming `WU` and reintroducing `P2†` risks.

5) Disadvantages of `⌖2`
5.1) `⌖2` requires a normalized database structure to bypass the 10,000-item limit of `Bᨀ` on lists.
Although `Bᨀ` executes aggregations at the `Pᨀ` level, it consumes `WU` for every record scanned during the query.
This creates a scalability issue that persists even when utilizing efficient database-level grouping.
5.2) Generating daily statistics via `⌖2` creates a concentrated burst load.
The scheduler places tasks into a job queue where processing is subject to strict `Bᨀ` concurrency limits.
This activity spike creates heavy resource contention and risks triggering execution timeouts.
5.3) `Bᨀ` consumes `WU` for every database search and aggregation operation performed on the daily event delta.
Even this incremental processing strategy generates a recurring operational cost that scales linearly with user activity.
High-volume processing necessitates purchasing expensive workload tiers.

6) `R1⁂`
6.1) Essence
`F༄` transmits all interaction events to `Sᨀ` via a first-party server-side proxy to bypass client-side blockers.
The proxy authenticates its interaction with `Sᨀ` using a secure service key, eliminating the need for complex custom JWT generation in `Bᨀ.`
State-changing actions utilize a dual-write strategy: executing transactions in `Bᨀ` while concurrently logging events to `Sᨀ`.
This decoupled architecture mitigates race conditions by removing reliance on high-latency asynchronous synchronization.
`Sᨀ` aggregates data in the background, allowing `Bᨀ` to fetch final metrics via API.
6.2) Advantages
The direct data ingestion architecture operates independently of `WAL` access, effectively rendering `P1†` irrelevant.
Physical isolation of the write stream from the transactional database solves `P2†`.
Offloading the logging of high-frequency events to `Sᨀ` eliminates `WU` costs associated with both data ingestion and analytical processing.
The `INSERT ON CONFLICT` mechanism combined with client-generated deterministic IDs ensures strict write idempotency.

7) `R2⁂`
7.1) Essence
`F༄` generates a deterministic deduplication ID for each event and transmits data to `Tᨀ` via a custom domain to mitigate browser privacy restrictions.
The storage layer utilizes the `ReplacingMergeTree` engine to perform asynchronous deduplication in the background.
`Bᨀ` retrieves aggregated metrics via «Pipes» API endpoints.
7.2) Advantages
The serverless columnar architecture ensures high performance at scale and automatically handles peak loads.
Analytical queries utilize `argMax` at query time to compute accurate statistics directly from the raw data.
This approach minimizes query latency by leveraging columnar storage for user-facing statistics.