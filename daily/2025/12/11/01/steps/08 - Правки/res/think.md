1. `𐒌(1)`, `𐒌(2)`, `𐒌(3)`
10.1) Essence
Reducing the value of the `-s malloc,SIZE` parameter of `VDᨀ` to a level that reserves sufficient headroom for fragmentation, thread memory, and metadata.
For a server with 32 GB RAM, a safe value is 14-16 GB, rather than 25-28 GB.
The calculation must account for the OS reserve, the Transient storage limit, heap fragmentation, thread stacks, and object metadata overhead.

2. `𐒌(4)`
10.2.1) `R4` significantly reduces the risk of the OOM Killer triggering by reserving physical memory for overheads that are not tracked by the `-s` parameter.