1) In points 2-5, I describe 4 main causes of your problem.
In points 7-10, I outline my 4 main recommendations.
2) `⋇1`
Faceted search and advertising tags on `runrepeat.com` create a combinatorial explosion of URLs.
Without normalization, metadata overhead from duplicate objects consumes memory outside the storage limit.
This leads to exhaustion regardless of eviction policies.
3) `⋇2`
Varnish (hereafter — `Vᨀ`) uses `Transient` storage for objects with a TTL shorter than `shortlived` and for buffering uncacheable response bodies.
By default, this storage uses `malloc` and has no memory limit.
Traffic with uncacheable responses (e.g. containing `Set-Cookie`) causes `Vᨀ` to uncontrollably fill RAM with buffered data until the server crashes (OOM).
4) `⋇3`
The configuration parameter `-s malloc,SIZE` limits memory for bodies and HTTP headers but excludes metadata overhead.
Each object requires approximately 1 KB of RAM for internal structures (`objhead`, `objcore`) allocated outside this limit.
Due to `⋇1`, millions of objects consume gigabytes of memory solely for metadata.
5) `⋇4`
The default allocator `glibc` (hereafter — `Gᨀ`) prioritizes execution speed over memory efficiency during multi-threaded `Vᨀ` operations.
This leads to external heap fragmentation, where non-contiguous memory blocks cannot be effectively reused.
On multi-core processors, e.g. your AWS Graviton, `Gᨀ` uses multiple memory arenas to reduce lock contention, significantly increasing process RSS.
6) In points 7-10, I outline my 4 main recommendations for eliminating your problem.
7) `R1`
To prevent `⋇1` and eliminate the root cause of `⋇3`, strip marketing tags (`gclid`, `fbclid`, `utm_`) from `req.url` and normalize HTTP headers in `vcl_recv` before hashing:
7.1) Use `regsuball` to remove tracking parameters and `vmod_querystring` to filter and sort parameters alphabetically.
7.2) Normalize the `User-Agent` header to limited groups (e.g. mobile/desktop).
7.3) Remove the `Cookie` header for requests not requiring server-side personalization.
8) `R2`
To compensate for the architectural vulnerability of `Vᨀ` related to `⋇2`, add the flag `-s Transient=malloc,SIZE` (e.g. `-s Transient=malloc,2G`) to the startup parameters of the `varnishd` daemon (hereafter — `VDᨀ`).
9) `R3`
To solve `⋇4`, switch `VDᨀ` to `jemalloc` (hereafter — `Jᨀ`) instead of `Gᨀ`.
`Jᨀ` minimizes external heap fragmentation in multithreaded applications via arenas and size classes.
`R3` is critical for ARM64 (your AWS Graviton), where `Gᨀ` demonstrates low memory efficiency.
10) `R4`
As a temporary stabilization measure, reduce the `VDᨀ` parameter `-s malloc,SIZE` to reserve headroom for overhead.
For a server with 32 GB RAM, a safe value is 14-16 GB rather than 25-28 GB.
The calculation must account for the OS reserve, `Transient` storage limit, heap fragmentation, thread stacks, and metadata overhead.