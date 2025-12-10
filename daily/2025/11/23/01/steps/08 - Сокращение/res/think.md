1.  Пункт 9, предложение 1.
    Было:

<!-- end list -->

```
9) Use the modern HLS Content Steering specification (RFC 8216bis) for dynamic server-side CDN selection management without proxying video traffic.
```

Стало:

```
9) Use HLS Content Steering (RFC 8216bis) for dynamic server-side CDN management without proxying traffic.
```

2.  Пункт 9, предложение 2.
    Было:

<!-- end list -->

```
Control is performed via an external steering server which provides `P` with lightweight JSON manifests containing pathway priorities.
```

Стало:

```
An external steering server provides `P` with JSON manifests containing pathway priorities.
```

3.  Пункт 10, предложение 1.
    Было:

<!-- end list -->

```
10) Use managed `O` services (e.g. AWS Elemental MediaPackage or Unified Streaming Platform) for packaging and ensuring content availability at the `O` level.
```

Стало:

```
10) Use managed `O` services (e.g. AWS Elemental MediaPackage) for packaging and availability.
```

4.  Пункт 10, предложение 2.
    Было:

<!-- end list -->

```
They simplify the ingestion of synchronized streams (point 7) and can automatically generate the `RS` manifests required for client-side failover (point 8).
```

Стало:

```
They simplify synchronized stream ingestion (point 7) and automatically generate `RS` manifests for client-side failover (point 8).
```

5.  Пункт 10, предложение 3.
    Было:

<!-- end list -->

```
These services enhance the overall resilience of the `O` layer through built-in high availability and input redundancy mechanisms.
```

Стало:

```
These services enhance resilience via built-in high availability and input redundancy.
```