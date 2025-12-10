Для устранения 𐒌(4):

Заменить абзац в §3.1:

```
Frequent or inefficient queries to Windows Management Instrumentation (WMI) can cause a memory or handle leak in the WMI service (Winmgmt) or the WmiPrvse.exe process.
```

На абзац:

```
Frequent or inefficient queries to Windows Management Instrumentation (WMI) can cause a memory or handle leak, primarily within the WMI Provider Host process (WmiPrvse.exe), where WMI providers execute the queries.
```

Для устранения 𐒌(2) и 𐒌(3):

Заменить абзац в §3.1:

```
When the handle count reaches the system limit or the WMI service becomes unstable, the application and the server slow down and hang.
```

На следующие абзацы:

```
When the handle count grows excessively, it can exhaust the kernel memory (Paged Pool or Non-Paged Pool) used to store these objects, leading to a system-wide slowdown and hang.
Alternatively, if a process reaches its specific handle quota (e.g., for GDI or USER objects), or if the WMI service becomes unstable, the application may become unresponsive without necessarily affecting the entire server.
```