1\.
Относительно `𐒌(1)`.
Заменить пункты 4.2–4.3.2 `Aᨀ` следующим текстом:

```markdown
4.2) The architecture risks cascading failures due to the «thundering herd» effect.
4.2.1) During failover, if segments are not already cached, `M` generates a sudden request spike towards the backup `O`.
Without request collapsing (request coalescing), this load can cause the backup `O` to fail shortly after the primary `O`.
4.2.2) If `M` restarts, it faces a reconnection storm from clients.
If the cache is cold after restart, this storm propagates to the `O`, which can cause both `M` and `O` to fail again.
4.3) While you propose «maintain segment cache» (hereafter — `R2`) and «prefetch segments» (hereafter — `R3`) to mitigate the failover scenario (4.2.1), these mechanisms introduce significant negative trade-offs.
4.3.1) `R3` doubles specific infrastructure loads (e.g. `O` egress and `M` ingress traffic) and significantly increases operational costs by continuously pulling segments from both `O`.
4.3.2) `R2` and `R3` introduce latency via a store-and-forward mechanism.
This conflicts with low latency HLS requirements crucial for live sports and breaks partial segment delivery.
```