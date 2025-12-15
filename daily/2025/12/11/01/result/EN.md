1) In points 2-5, I describe 4 main causes of your problem (hereafter — `P†`).
In points 7-10, I outline my 4 main recommendations.
2) `⋇1`
Your website `runrepeat.com` uses faceted search (color, size) and advertising tags (`gclid`, `utm`).
This creates a combinatorial explosion of URLs (cache bloat).
If aggressive normalization (cleaning and sorting of parameters) is not performed before caching, the metadata overhead from duplicate objects consumes system memory outside the storage limit, leading to exhaustion regardless of eviction policies.
3) `⋇2`
Varnish (hereafter — `Vᨀ`) uses the special `Transient` storage for objects with a TTL shorter than the `shortlived` parameter and for buffering uncacheable response bodies.
By default, this storage uses the system allocator `malloc` and has no limit on the maximum amount of consumed memory.
During an influx of traffic resulting in uncacheable responses (e.g. containing `Set-Cookie` headers or `Cache-Control: private` directives), `Vᨀ` uncontrollably fills RAM with buffered data until the server crashes completely (OOM).
4) `⋇3`
The configuration parameter `-s malloc,SIZE` limits the memory volume for object bodies and HTTP headers but does not account for the overhead on their metadata.
Each object in the cache requires approximately 1 KB of RAM for internal structures (`objhead`, `objcore`) allocated outside the capped area.
Due to `⋇1`, the number of objects can reach millions, which results in the consumption of gigabytes of memory solely for metadata.`
5) `⋇4`
The standard system allocator `glibc` (hereafter — `Gᨀ`), used in Linux by default, prioritizes execution speed over memory efficiency during the multi-threaded operation of `Vᨀ`.
This leads to external heap fragmentation, where available memory is split into small non-contiguous blocks that cannot be effectively reused.
On multi-core processors, e.g. your AWS Graviton, `Gᨀ` uses multiple memory arenas to reduce lock contention, which significantly increases the process RSS.
6) In points 7-10, I outline my 4 main recommendations for eliminating `P†`.
7) `R1`
To prevent `⋇1` and eliminate the root cause of `⋇3`, implement strict logic for stripping marketing tags (`gclid`, `fbclid`, `utm_`) from `req.url` and normalizing HTTP headers in the `vcl_recv` procedure before hash calculation:
7.1) Use the `regsuball` function to remove tracking parameters or the `vmod_querystring` module to filter and sort parameters alphabetically, which brings them to a canonical form.
7.2) Normalize the `User-Agent` header to a limited set of groups (e.g. mobile/desktop).
7.3) Remove the `Cookie` header for all requests that do not require server-side personalization.
8) `R2`
To compensate for the architectural vulnerability of `Vᨀ` related to `⋇2`, add the flag `-s Transient=malloc,SIZE` (e.g. `-s Transient=malloc,2G`) to the startup parameters of the `varnishd` daemon (hereafter — `VDᨀ`).
9) `R3`
To solve `⋇4`, switch `VDᨀ` to using the `jemalloc` library (hereafter — `Jᨀ`) instead of `Gᨀ`.
`Jᨀ` uses efficient memory management algorithms (arenas, size classes), minimizing external heap fragmentation in multithreaded applications.
`R3` is especially critical for the ARM64 architecture (AWS Graviton), where `Gᨀ` demonstrates low memory utilization efficiency.
10) `R4`
As a temporary solution for stabilization, reduce the value of the `-s malloc,SIZE` parameter of `VDᨀ` to a level that reserves sufficient headroom for fragmentation, thread memory, and metadata.
For a server with 32 GB RAM, a safe value is 14-16 GB, rather than 25-28 GB.
The calculation must account for the OS reserve, the Transient storage limit, heap fragmentation, thread stacks, and object metadata overhead.