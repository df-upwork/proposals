I can handle 
1) In points 2-4 I describe your misconceptions.
In points 6-10 I describe my recommendations.
2) «Add #EXT-X-DISCONTINUITY on switch»
According to the HLS specification (RFC 8216, hereafter — `HLS`), `#EXT-X-DISCONTINUITY` (hereafter — `ED`) signals a discontinuity in stream characteristics to the player (hereafter — `P`).
When `P` encounters `ED`, it typically flushes decoder buffers and re-synchronizes the timeline.
This causes visible artifacts (freezing or buffering).
This contradicts your requirement «without buffering or interruptions» (hereafter — `R1`).
Using `ED` to ensure `R1` demonstrates a fundamental misunderstanding of `HLS`.
3) The focus solely on the failover microservice (hereafter — `M`) suggests you expect `M` to ensure `R1` independently.
`R1` requires frame-accurate, timestamp-identical streams synchronized at the encoder level (e.g. using timecode locking and epoch locking).
`M`, as a reverse proxy, cannot stitch unsynchronized streams seamlessly.
The required real-time media manipulation (transmuxing) is computationally intensive and therefore infeasible in a high-throughput proxy environment.
Thus, you are mistakenly attempting to achieve synchronization at the delivery stage rather than at the source.
4) Introducing `M` as a centralized component creates a critical architectural vulnerability: a Single Point of Failure.
Even if deployed as a high availability (hereafter — `HA`) cluster, any systemic failure in the `M` cluster impacts all `P` globally.
4.1) If deployed at the edge, `M` faces immense scalability challenges and DDoS vulnerabilities.
If deployed as an origin shield (behind the CDN, protecting the origin server, hereafter — `O`), it remains a centralized dependency, causing a total outage upon systemic failure.
4.2) The architecture is susceptible to cascading failures due to the «thundering herd» effect.
4.2.1) During failover, if segments are not already cached, `M` generates a sudden request spike towards the backup `O`.
Without request collapsing, this load can cause the backup `O` to fail shortly after the primary `O` fails.
4.2.2) If `M` restarts, it faces a reconnection storm from `P`.
If the cache is cold after restart, this storm propagates to the `O`, which can cause both `M` and `O` to fail again.
4.3) While you propose «maintain segment cache» (hereafter — `R2`) and «prefetch segments» (hereafter — `R3`) to mitigate the failover scenario (4.2.1), these mechanisms introduce significant negative trade-offs.
4.3.1) `R3` doubles the traffic volume in specific areas (e.g. `O` egress traffic and `M` ingress traffic) and significantly increases operational costs by continuously pulling segments from both `O`.
4.3.2) `R2` and `R3` introduce latency via a store-and-forward mechanism.
This conflicts with the requirements for low latency HLS, which are crucial for live sports.
It also breaks partial segment delivery mechanisms.
5) Points 6-10 outline my recommendations.
6) Abandon the development of `M`.
7) Shift the focus to achieving ideal encoder-level synchronization (frame-accurate alignment) of the primary and backup streams to ensure `R1`.
This involves input synchronization (e.g. SMPTE 2022-7) and output alignment (timecode and epoch locking).
These techniques can be implemented using platforms such as AWS Elemental MediaLive.
8) Utilize native `HLS` Redundant Streams (hereafter — `RS`) as the primary failover mechanism.
The master playlist specifies multiple URLs per quality, pointing to `O` or CDNs synchronized according to point 7.
This approach delegates «automatic failover» directly to `P`.
`P` reactively switches URLs upon encountering loading errors, such as HTTP 4xx/5xx or network timeouts.
This decentralized, reactive detection handles delivery failures, eliminating the need for the centralized, proactive «health checks» in the critical delivery path envisioned for `M`.
However, it cannot detect «stale playlist» («zombie stream») scenarios, where `O` returns HTTP 200 OK but the manifest is stale.
Therefore, proactive monitoring (deep health checks analyzing `#EXT-X-MEDIA-SEQUENCE` dynamics) remains necessary for resilience.
However, it must be performed by an external (out-of-band) system rather than an inline proxy like `M`.
9) Use HLS Content Steering (RFC 8216bis) for dynamic server-side multi-CDN traffic management without proxying traffic.
An external steering server provides `P` with JSON manifests containing pathway priorities.
10) Use managed `O` services (e.g. AWS Elemental MediaPackage or Unified Streaming Platform) for packaging and ensuring `HA` at the `O` level.
They simplify the ingestion of synchronized streams (point 7) and automatically generate `RS` manifests for client-side failover (point 8).
These services enhance resilience through built-in `HA` and input redundancy.
---
My GitHub profile: https://github.com/dmitrii-fediuk