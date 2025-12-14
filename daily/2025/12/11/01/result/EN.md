1) In points 2-5, I describe 4 main causes of your problem (hereafter — `P†`).
In points 7-10, I outline my 4 main recommendations.
2) `⋇1`: cache bloat
Your website `RunRepeat.com` (hereafter — `Rᨀ`) uses faceted search (color, size) and advertising tags (`gclid`, `utm`).
This creates a combinatorial explosion of URLs (cache bloat).
Varnish (hereafter — `Vᨀ`) by default considers `/shoe?color=red` and `/shoe?gclid=123` as different objects.
If aggressive normalization (cleaning and sorting of parameters) is not performed before caching, memory will be clogged with garbage faster than any eviction policies can free it.
3) `⋇2`: Unbounded transient storage
`Vᨀ` uses the special `Transient` storage for short-lived objects and technical `hit-for-miss` records created when caching is impossible.
By default, this storage uses the system allocator `malloc` and has no limit on the maximum amount of consumed memory.
During an influx of traffic with unique tags or Cookies that the backend marks as `private`, `Vᨀ` uncontrollably fills RAM with these temporary records until the server crashes completely (OOM).
4) `⋇3`: metadata overhead
The configuration parameter `-s malloc,SIZE` limits only the memory volume for object bodies but does not account for the overhead on their metadata.
Each object in the cache requires approximately 1 KB of RAM for internal structures (`struct obj`, `objcore`) allocated outside the capped area.
Due to `⋇1`, the number of objects can reach tens of millions, which results in the consumption of tens of gigabytes of memory solely for metadata.
5) `⋇4`: heap fragmentation
The standard system allocator `glibc` (hereafter — `Gᨀ`), used in Linux by default, is inefficient for the multi-threaded operation of `Vᨀ` with frequent memory allocation.
This leads to external heap fragmentation, when the operating system considers memory occupied by the process, although internally it is free but broken into small chunks.
On the AWS Graviton (ARM64) architecture, the problem of `Gᨀ` fragmentation manifests itself particularly acutely, causing an increase in the process RSS.
6) In points 7-10, I outline my 4 main recommendations for eliminating `P†`.
7) `R1`
7.1) Essence
Implement strict logic for cleaning `req.url` from marketing tags (`gclid`, `fbclid`, `utm_`) and unique session identifiers in the `vcl_recv` procedure before hash calculation.
7.2) Implementation
7.2.1) Use the `vmod_std` module (function `std.querysort`) or `vmod_querystring` for alphabetical sorting of query parameters, which brings them to a canonical form.
7.2.2) Normalize the `User-Agent` header to a limited set of groups (e.g. mobile/desktop)
7.2.3) Remove the `Cookie` header for static resources.
7.3) Result
7.3.1) Prevention of `⋇1` by converting potential duplicates into single instances of objects in memory.
7.3.2) Elimination of the root cause of `⋇3`.
8) `R2`
8.1) Essence
Add the flag `-s Transient=malloc,SIZE` (e.g. `-s Transient=malloc,2G`) to the startup parameters of the `varnishd` daemon (hereafter — `VDᨀ`).
8.2) Rationale
In the standard configuration, `Vᨀ` uses an unbounded storage for transient objects (hit-for-miss, shortlived), which occupies all available memory during attacks or failures.
Setting a hard limit forces `Vᨀ` to apply the eviction algorithm (LRU) to transient objects when the threshold is reached, instead of allocating new memory pages.
This creates a guaranteed safety barrier preventing a server crash (OOM) even during a flood of requests with `Set-Cookie` or unique parameters.
`R2` compensates for the architectural vulnerability of `Vᨀ` related to the `unbounded` nature of the transient storage by default.
9) `R3`
9.1) Essence
Switch `VDᨀ` to using the `jemalloc` library (hereafter — `Jᨀ`) instead of `Gᨀ`.
9.2) Implementation
Install the `Gᨀ` package.
Configure the `LD_PRELOAD` environment variable or linking parameters in the `systemd` unit file.
9.3) Rationale
`Jᨀ` uses efficient memory management algorithms (arenas, size classes), minimizing external heap fragmentation in multithreaded applications.
This solution is especially critical for the ARM64 architecture (AWS Graviton), where `Gᨀ` demonstrates low memory utilization efficiency.
9.4) Result
`R3` solves `⋇4`, eliminating the gap between the memory consumption recorded by `Vᨀ` and the actual resident set size (RSS) of the process.
10) `R4`
10.1) Essence
Reducing the value of the `-s malloc,SIZE` parameter of `VDᨀ` to a level that leaves sufficient headroom for metadata and operational overhead.
For a server with 32 GB RAM, a safe value is 18-20 GB, rather than 25-28 GB, as administrators often mistakenly set.
The calculation must take into account the formula: RAM minus OS reserve, minus Transient limit, minus memory for metadata (1 KB per object).
10.2) Advantages
10.2.1) `R4` prevents the OOM Killer from triggering in normal operating mode due to accurate accounting of all memory consumers within the process.
10.2.2) `R4` allows the system to operate stably even during moments of peak object count loads, absorbing the increase in overhead.
10.2.3) `R4` provides room for maneuver during a temporary increase in memory consumption by workspaces.
10.2.4) Simplicity of implementation allows applying `R4` quickly as a temporary solution for stabilization.