1) Both options you are considering are suboptimal.
I outline their disadvantages in points 4 and 5 below.
In points 6 and 7, I outline 2 high-quality ways to solve your problem.

2) Key definitions used in my analysis:
- Data replication: `R᛭`
- Your «Option 1» (use of `R᛭`): `⌖1`
- Your «Option 2» («a scheduled backend job»): `⌖2`
- «a naive scheduled job could be intensive and create heavy IO load on production if it scans across all entities»: `P1†`
- «our current setup may limit built in replication support»: `P2†`
- Your information system as a whole: `S༄`
- Bubble.io: `Bᨀ`
- React: `Rᨀ`
- PostgreSQL: `Pᨀ`
- Supabase: `Sᨀ`
- Tinybird: `Tᨀ`
- Write-Ahead Log: `WAL`

3) My assumptions about `S༄` based on the analysis of your projects on Upwork
3.1) The assumed essence of `S༄`
Most likely, `S༄` represents a B2C platform for the algorithmic distribution of short gaming videos (clips), aggregated via the Twitch API.
The system implements an infinite feed mechanic («TikTok for gamers»), where AI (OpenAI) ranks content based on user preferences.
Viewers consume content via a high-performance web interface (`Rᨀ`), generating a stream of events: «views», «skips», and «saves».
Platform owners provide analytics to content creators (streamers), monetizing the service via subscription or advertising.
3.2) The assumed architecture of `S༄`
The `S༄` system is based on the `Bᨀ` backend, which creates the current architectural limitations regarding replication and IO, and uses a modern frontend on `Rᨀ` for interaction with users.

4) Disadvantages of `⌖1`
4.1) In classical database architecture, the gold standard for building data warehouses is `R᛭`.
`Bᨀ` uses `Pᨀ`.
However, the platform architecture is multi-tenant.
Thousands of applications may share a single database cluster.
Granting direct access to `WAL` or replication slots is impossible for security reasons, as this would give access to the data of other clients (noisy neighbors).
Therefore, you are physically denied access to low-level synchronization mechanisms.

4.2) API Polling
Since direct `R᛭` is impossible, the option of periodic API Polling is often considered for exporting new data.
Source analysis reveals critical disadvantages of this method for the task:
4.2.1) Algorithmic complexity of pagination.
The `Bᨀ` Data API uses standard pagination (limit/offset or cursor).
For exporting 100,000 events accumulated over a day, the system will require executing a series of requests.
Offset Problem: In `Pᨀ` (and other RDBMS), the query `OFFSET 50000 LIMIT 100` requires the database to read 50,100 rows, discard the first 50,000, and return the last 100.
The "deeper" we go into the event history, the slower each subsequent request works.
This creates an `O(N^2)` load during a full table export, which catastrophically affects performance with large data volumes.
4.2.2) According to the documentation, `Bᨀ` imposes strict limits on the number of requests to the API.
Starter Plan: 15,000 requests per minute (aggregated for Workflow API and Data API).
Growth Plan: 25,000 requests.
Although these figures seem large, the real throughput is limited by the server-side processing time.
Heavy requests for reading data with filtering can consume a significant share of "Capacity", which will lead to timeouts (code 503) long before reaching the limit on the number of requests.
4.2.3) When downloading data in pages via the API (especially if the process takes minutes or hours), it is impossible to guarantee snapshot isolation.
If, during the download of the 50th page, a user adds a new event that should have fallen onto the 1st page (due to sorting), this event may be skipped or lead to an offset shift, causing data duplication.
This directly contradicts your requirement «the job must be accurate».
The native export function in `Bᨀ` has serious limitations:
Row limits: Users report failures and timeouts when attempting to export more than 10,000 - 50,000 rows at a time.
Lack of automation: Native export often requires manual triggering from the editor, which violates the "low maintenance" requirement.
Plugins: Using plugins (e.g., "1T CSV Creator") shifts the file generation load to the client browser or the application server capacity (Server-Side Actions), which brings us back to the issue of resource consumption (Capacity) and `P2†` risks.

5) Disadvantages of `⌖2`
5.1) The Workload Units (WU) economy and the cost of computing
Since 2023 `Bᨀ` has switched to a pricing model based on Workload Units.
Every database operation (creation, search, modification) has its own "price" in WU.
The cost of Search: A search in the database is one of the most expensive operations, especially if it includes complex filters ("Constraint") or sorting.
The cost of aggregation: Operations like "Count", "Sum", performed on a list of search results, consume WU proportionally to the number of processed records.
Client scenario: A daily job that must scan, e.g., 100,000 events for 5,000 users, will cause an avalanche-like consumption of WU.
If the cost of processing one entity is, say, 0.5 WU (an optimistic estimate), then daily processing will cost 50,000 WU.
Per month this is 1.5 million WU, which may require upgrading to expensive pricing plans (from $300-$500/month and higher), making analytics disproportionately expensive compared to the direct income from the client ($1300 total spent).
5.2) The `O(N)` algorithmic trap and Recursive Workflows
To process large lists in `Bᨀ`, the "Recursive Backend Workflows" pattern is used, since the Schedule API Workflow on a list loop has a limit of 100,000 elements and can function unstably on large volumes.
The recursive process handles one record (or a batch of records) and then calls itself for the next.
Such a process creates `P2†`.
If the processing takes 3 hours, then during these 3 hours the database is under constant pressure of read/write operations.
Blocking: Sources confirm that at high Capacity utilization ("app too busy"), requests from real users start to slow down.
This is a classic problem of Resource Contention, when an analytical task (low priority) interferes with a transactional task (high priority).
5.3) Source analysis reveals another fundamental problem that renders option O⌖2 technically untenable, even if resources were sufficient.
10,000 items limit: A field of type List in `Bᨀ` cannot reliably store more than 10,000 items.
Scenario: If we attempt to store a list of "Views" directly inside the "Article" object for calculation convenience, a popular article will exhaust this limit in a few days or weeks.
Consequences: Upon exceeding the limit, operations to add to the list begin to fail or slow down to unacceptable levels.
This forces the developer to create separate join tables, which brings us back to the problem of slow search across millions of rows.

6) `R1⁂`: a high-quality way to solve your task No. 1
6.1) Essence
Dual-Write architecture into a relational DBMS (`Sᨀ` / Neon).
Modifying the frontend to send events (clicks, views) via a parallel asynchronous request directly to the external `Pᨀ` (`Sᨀ`) database, completely bypassing the `Bᨀ` backend.
The external database ingests the «raw» stream of events and aggregates them in the background via materialized views or incremental SQL procedures.
The main `Bᨀ` application requests pre-calculated metrics from the external database via API only at the moment they are displayed to the user.
6.2) Advantages
This approach physically isolates the event write stream from the main transactional database, which mathematically guarantees the absence of input/output blocking (`P2†`) in the `S༄` system.
Using standard `Pᨀ` in an external environment eliminates the problem of lack of access to the Write-Ahead Log (`P1†`), as the client gains full administrative control over the new database.
The economic efficiency of the solution is maximal because external SQL services (`Sᨀ`, Neon) provide generous free limits and do not charge for operations based on the Workload Units model.
The `INSERT ON CONFLICT` (Upsert) mechanism ensures strict write idempotency, guaranteeing data accuracy even during network failures or repeated submissions.

7) `R2⁂`: a high-quality method of solving your task #2
7.1) Essence
Use a specialized columnar database (`Tᨀ`), designed for ingesting high-frequency data streams via HTTP endpoints.
The client application sends events to the `Tᨀ` API, where they are immediately stored and become available for analytical SQL queries with sub-second latency.
Integration with `Bᨀ` is reduced to a simple call of API endpoints («Pipes») to retrieve ready-made JSON statistics for each entity.
7.2) Advantages
Columnar architecture ensures phenomenal aggregation performance at any data volumes, completely eliminating the risk of system slowdown with audience growth.
The service automatically handles peak loads («thundering herd»), protecting the client infrastructure from overload.
There is no need for complex database schema and index design, as the engine is optimized for arbitrary analytical queries.