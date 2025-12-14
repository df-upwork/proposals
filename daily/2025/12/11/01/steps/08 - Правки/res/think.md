1. `𐒌(2)`
В пункте 4 замени предложение «The configuration parameter `-s malloc,SIZE` limits only the memory volume for object bodies but does not account for the overhead on their metadata.» на:
`The configuration parameter `-s malloc,SIZE` limits the memory volume for object bodies and HTTP headers but does not account for the overhead on their metadata.`

2. `𐒌(4)`
В пункте 4 замени предложение «Each object in the cache requires approximately 1 KB of RAM for internal structures (`struct obj`, `objcore`) allocated outside the capped area.» на:
`Each object in the cache requires approximately 1 KB of RAM for internal structures (`objhead`, `objcore`) allocated outside the capped area.`

3. `𐒌(3)`
В пункте 4 замени предложение «Due to `⋇1`, the number of objects can reach tens of millions, which results in the consumption of tens of gigabytes of memory solely for metadata.» на:
`Due to `⋇1`, the number of objects can reach millions, which results in the consumption of gigabytes of memory solely for metadata.`