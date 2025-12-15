# 1\.

В пункте 2 название сайта написано со строчной буквы, хотя в онтологии (`O.md`, §6.2) используется написание `RunRepeat.com`.
Также термин «advertising tags» (рекламные теги) технически некорректен применительно к URL-параметрам; лучше использовать «tracking parameters».
Степень уверенности: 95
Предложение по устранению:

```
Faceted search and tracking parameters on `RunRepeat.com` create a combinatorial explosion of URLs.
```

# 2\.

В пункте 2 фраза «leads to exhaustion» является неполной, так как не уточняет, какой именно ресурс исчерпывается.
Степень уверенности: 95
Предложение по устранению:

```
This leads to memory exhaustion regardless of eviction policies.
```

# 3\.

В пункте 3 фраза «shorter than `shortlived`» грамматически неточна, так как сравнивает время жизни (число) с именем параметра.
Также фраза «until the server crashes» технически неверна: механизм OOM Killer в Linux завершает конкретный процесс, а не обрушивает операционную систему.
Степень уверенности: 98
Предложение по устранению:

```
Varnish (hereafter — `Vᨀ`) uses `Transient` storage for objects with a TTL shorter than the `shortlived` parameter and for buffering uncacheable response bodies.
Traffic with uncacheable responses (e.g. containing `Set-Cookie`) causes `Vᨀ` to uncontrollably fill RAM with buffered data until the system OOM killer terminates the process.
```

# 4\.

В пункте 5 использование «e.g.» сразу после существительного без скобок стилистически делает предложение менее связным.
Конструкция «such as» подходит лучше.
Степень уверенности: 85
Предложение по устранению:

```
On multi-core processors, such as your AWS Graviton, `Gᨀ` uses multiple memory arenas to reduce lock contention, significantly increasing process RSS.
```

# 5\.

В пункте 7 вводная фраза упоминает только нормализацию HTTP-заголовков, но подпункт 7.1 описывает действия с `req.url`, который является частью строки запроса, а не заголовком.
Также стоит унифицировать терминологию с пунктом 2.
Степень уверенности: 100
Предложение по устранению:

```
To prevent `⋇1` and eliminate the root cause of `⋇3`, strip tracking parameters (`gclid`, `fbclid`, `utm_`) from `req.url` and normalize the request URL and HTTP headers in `vcl_recv` before hashing:
```

# 6\.

В пункте 9 фраза «switch ... instead of» содержит плеоназм (избыточность).
Глагол «configure ... to use» звучит профессиональнее.
Степень уверенности: 90
Предложение по устранению:

```
To solve `⋇4`, configure `VDᨀ` to use `jemalloc` (hereafter — `Jᨀ`) instead of `Gᨀ`.
```

# 7\.

В пункте 9 упоминание «arenas» как преимущества `Jᨀ` может запутать читателя, так как в пункте 5 «arenas» в `Gᨀ` были названы причиной проблем.
Эффективность `Jᨀ` лучше объяснить через классы размеров.
Также следует унифицировать написание «multi-threaded» (с дефисом), как в пункте 5.
Степень уверенности: 90
Предложение по устранению:

```
`Jᨀ` minimizes external heap fragmentation in multi-threaded applications via size classes and efficient memory recycling.
```

# 8\.

В пункте 10 фраза «reserve headroom» содержит тавтологию («headroom» — это уже запас).
Естественнее звучит «leave headroom».
Степень уверенности: 80
Предложение по устранению:

```
As a temporary stabilization measure, reduce the `VDᨀ` parameter `-s malloc,SIZE` to leave headroom for overhead.
```