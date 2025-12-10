From my analysis of all 3 of your Upwork projects, 2 main reasons for your performance issue are clear to me:
1) Inappropriate data model.
1.1) Consider, e.g., the «real-time draft» in your fantasy sports application.
If each user's picks are stored in a single large document for their team, and 12 users in a league are making picks every 30 seconds, this document will be constantly updated.
This can lead to write conflicts and performance degradation, as MongoDB has to rewrite the entire document on every update.
This is the classic «bloated document» or «unbounded array» problem.
1.2) The explanation is perfectly straightforward: startups like yours almost always prioritize development speed over optimal schema design at the initial stage.
The quickest data model to implement might be the creation of large, deeply nested documents (e.g., a league document containing an array of teams, which in turn contain an array of players).
Such a model is easy to reason about in code.
It works perfectly for a few users, as reads are fast (a single document query), and write conflicts are rare.
However, when 100+ users attempt to update this single league document simultaneously during the draft, they create massive write contention and locking.
This perfectly explains why the system «slows significantly when more users join».
2) Inefficient data access logic (the «N+1» queries problem).
2.1) E.g., your fantasy sports application may make a query to get all the teams in a user's league, and then in a loop N queries (one for each team) to get their player rosters.
2.2) The «N+1» problem is a direct and compelling explanation for all the observed symptoms:
- high latency (~5s)
- degradation under load
- spikes in the number of requests («Opcounters»).
2.3) Causal relationship.
Let us assume the request to get the league draft status includes the «N+1» pattern.
2.3.1) For a 12-team league, this means 1 + 12 = 13 queries per API call.
If each query has a modest latency of 50 ms for a roundtrip to Atlas, the total time is already 13×50ms=650ms from network overhead alone, not counting execution time.
2.3.2) Now, consider 10 concurrent users making this request.
This generates 130 requests arriving at the database in a short period, which explains the spike in «Opcounters».
The database must handle 130 concurrent operations, which leads to context switching and possible queues, increasing the execution time of each individual request.
The application server (especially if it is a single-threaded Node.js) may be blocked while waiting for these 130 database responses, which will lead to the queuing of other incoming API requests.
The combination of network overhead, database resource contention, and application-level queueing can easily explain the observed latency of ~5 seconds under load.
---
My GitHub profile: https://github.com/dmitrii-fediuk