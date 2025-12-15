1. Исправление `𐒌(5)` в пункте 2 (`⋇1`):
Faceted search, advertising tags, and `User-Agent` variations on `runrepeat.com` create a combinatorial explosion of cache objects.
Without normalization, metadata overhead from duplicate objects consumes memory outside the storage limit.
This leads to exhaustion regardless of eviction policies.

2. Исправление `𐒌(1)` в пункте 3 (`⋇2`):
`Vᨀ` uses `Transient` storage for objects with a TTL shorter than `shortlived` and for tracking `hit-for-miss` states.
By default, this storage uses `malloc` and has no memory limit.
Traffic with uncacheable responses (e.g. containing `Set-Cookie`) generates millions of `hit-for-miss` objects.
The accumulated metadata overhead for these technical markers uncontrollably consumes RAM until the server crashes (OOM).

3. Исправление `𐒌(4)` в пункте 7.3 (`R1`):
7.3) Remove the `Cookie` header in `vcl_recv` and the `Set-Cookie` header in `vcl_backend_response` for requests not requiring server-side personalization.