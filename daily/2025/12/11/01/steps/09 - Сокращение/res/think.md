1.
9) `R3`
To solve `⋇4`, switch `VDᨀ` to `jemalloc` (hereafter — `Jᨀ`) instead of `Gᨀ`.
`Jᨀ` minimizes external heap fragmentation in multithreaded applications via arenas and size classes.
`R3` is critical for ARM64 (AWS Graviton), where `Gᨀ` demonstrates low memory efficiency.