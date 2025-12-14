# 1.
`𐒌(2)`
The standard system allocator `glibc` (hereafter — `Gᨀ`), used in Linux by default, prioritizes execution speed over memory efficiency during the multi-threaded operation of `Vᨀ`.

# 2.
`𐒌(3)`
This leads to external heap fragmentation, where available memory is split into small non-contiguous blocks that cannot be effectively reused.

# 3.
`𐒌(1)`
On multi-core processors, e.g. your AWS Graviton, `Gᨀ` uses multiple memory arenas to reduce lock contention, which significantly increases the process RSS.