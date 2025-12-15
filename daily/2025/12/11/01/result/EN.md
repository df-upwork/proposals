In points 1-4, I describe the 4 main causes of your problem.
In points 5-8, I explain how to eliminate them.
1) `⋇1`
Faceted search, tracking parameters, and `User-Agent` variations on `RunRepeat.com` create a combinatorial explosion of cache objects.
Without normalization, metadata overhead from duplicate objects consumes memory outside the storage limit.
This leads to memory exhaustion regardless of eviction policies.
2) `⋇2`
Varnish (hereafter — `Vᨀ`) uses `Transient` storage for objects with a TTL shorter than the `shortlived` threshold and for storing `hit-for-miss` objects.
By default, this storage uses `malloc` and has no memory limit.
Traffic with uncacheable responses (e.g. containing `Set-Cookie`) generates millions of `hit-for-miss` objects.
The accumulated metadata overhead for these objects uncontrollably consumes RAM until the system OOM killer terminates the process.
3) `⋇3`
The configuration parameter `-s malloc,SIZE` limits memory for bodies and HTTP headers but excludes metadata overhead.
Each object requires approximately 1 KB of RAM for internal structures (`objhead`, `objcore`) allocated outside this limit.
Due to `⋇1`, millions of objects consume gigabytes of memory solely for metadata.
4) `⋇4`
The default allocator `glibc` (hereafter — `Gᨀ`) prioritizes execution speed over memory efficiency during multi-threaded `Vᨀ` operations.
This leads to external heap fragmentation, where non-contiguous memory blocks cannot be effectively reused.
On multi-core processors, such as your AWS Graviton, `Gᨀ` uses multiple memory arenas to reduce lock contention, significantly increasing the process Resident Set Size.
5) `R1`
To prevent `⋇1` and eliminate the root cause of `⋇3`, strip tracking parameters (`gclid`, `fbclid`, `utm_*`) from `req.url` and normalize the request URL and HTTP headers:
5.1) Use `regsuball` to remove tracking parameters and `vmod_querystring` to filter and sort parameters alphabetically.
5.2) Normalize the `User-Agent` header to limited groups (e.g. mobile/desktop).
5.3) Remove the `Cookie` header in `vcl_recv` and the `Set-Cookie` header in `vcl_backend_response` for requests not requiring server-side personalization.
6) `R2`
To compensate for the architectural vulnerability of `Vᨀ` related to `⋇2`, add the flag `-s Transient=malloc,SIZE` (e.g. `-s Transient=malloc,2G`) to the startup parameters of the `varnishd` daemon (hereafter — `VDᨀ`).
7) `R3`
To solve `⋇4`, configure `VDᨀ` to use `jemalloc` instead of `Gᨀ`.
`jemalloc` minimizes external heap fragmentation in multi-threaded applications via size classes and efficient memory recycling.
`R3` is critical for ARM64 (your AWS Graviton), where `Gᨀ` demonstrates low memory efficiency.
8) `R4`
As a temporary stabilization measure, reduce the `VDᨀ` parameter `-s malloc,SIZE` to reserve memory for operational overhead.
For a server with 32 GB RAM, a safe value is 14-16 GB rather than 25-28 GB.
The calculation must account for the OS reserve, `Transient` storage limit, heap fragmentation, thread stacks, and metadata overhead.
---
My GitHub profile: https://github.com/dmitrii-fediuk