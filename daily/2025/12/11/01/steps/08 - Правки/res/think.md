1. `𐒌3`
Пункт 7.1
Implement strict logic for stripping marketing tags (`gclid`, `fbclid`, `utm_`) from `req.url` and normalizing HTTP headers in the `vcl_recv` procedure before hash calculation.

2. `𐒌1`, `𐒌2`
Пункт 7.2.1
Use the `regsuball` function to remove tracking parameters or the `vmod_querystring` module to filter and sort parameters alphabetically, which brings them to a canonical form.

3. `𐒌4`
Пункт 7.2.3
Remove the `Cookie` header for all requests that do not require server-side personalization.

4. `𐒌5`
Пункт 7.3.1
Prevention of `⋇1` by eliminating unique marketing parameters and converting potential duplicates into single instances of objects in memory.