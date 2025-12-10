In my experience, your problem is most likely caused by one of the following 3 reasons:
1) Java Heap Leak
1.1) Essence
Infor Lawson often runs on Java application servers, such as IBM WebSphere.
A heap memory leak occurs when the application retains references to objects that are no longer in use.
The Garbage Collector (`GC`) cannot free this memory because the objects are considered active.
Over 2-3 weeks, these objects accumulate, filling up the available heap.
This leads to frequent and prolonged `GC` thrashing, which consumes CPU resources and makes the application extremely slow or completely unresponsive.
1.2) Rationale
Symptoms of gradual performance degradation culminating in unresponsiveness are a classic sign of a Java memory leak.
The 2-3 week periodicity indicates a slow leak, which is characteristic of complex enterprise systems.
Even if an `OutOfMemoryError` does not occur, continuous `GC` activity can completely paralyze the application.
There are known cases of leaks in WebSphere components (e.g., during the processing of EJB calls) that have led to memory exhaustion.
2) Connection Pool Exhaustion
2.1) Essence
The application uses a connection pool on the application server to interact with SQL Server.
A connection leak occurs when the application retrieves a connection from the pool but fails to return it after use.
Over time, all available connections in the pool become exhausted.
New requests to the application hang while waiting for an available connection, which makes the application unresponsive.
2.2) Rationale
Connection pool exhaustion is a common cause of application unresponsiveness when the application itself and the database appear to be functioning correctly.
This issue occurs on the application server side, which is why your SQL DBA, who only checked the SQL Server, might have missed it.
In WebSphere, this problem often manifests as the `J2CA0045E` error (`ConnectionWaitTimeoutException`).
This occurs when the connection pool is exhausted, and a new connection request times out while waiting for an available connection.
3) Windows handle leak or WMI resource exhaustion
3.1) Essence
Handles are Windows resources used for tracking open objects, such as files, threads, registry keys, and network connections.
If a process (the Lawson application or monitoring services) does not close handles after use, a leak occurs.
Frequent or inefficient queries to Windows Management Instrumentation (`WMI`) can cause a memory or handle leak, primarily within the WMI Provider Host process (`WmiPrvse.exe`), where WMI providers execute the queries.
When the handle count grows excessively, it can exhaust the kernel memory (paged pool or non-paged pool) used to store these objects, leading to system-wide performance degradation and unresponsiveness.
Alternatively, if a process reaches its specific handle quota (e.g., for GDI or USER objects), or if the WMI service becomes unstable, the application may become unresponsive without necessarily affecting the entire server.
3.2) Rationale
Handle leaks accumulate slowly, which aligns with the observed 2-3 week timeframe.
WMI issues caused by problematic or frequent queries from monitoring systems are a common cause of performance degradation on Windows servers.
---
My GitHub profile: https://github.com/dmitrii-fediuk