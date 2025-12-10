1) The most likely cause of your problem: the «retry mechanism» is attempting to use a file URI that is no longer valid.
1.1) `expo-image-picker` by default provides a URI not to the original image in the device's gallery, but to its temporary copy created in the application's isolated storage.
This copy is created so that the application can safely work with the file without requesting broad access permissions to the entire user storage.
However, the lifecycle of this copy and its URI is strictly limited.
This URI may not persist, especially after restarting the application or if the operating system clears the cache.
1.2) In particular:
- On Android, the temporary path (`response.uri`) can be deleted when the application is closed.
- On iOS, the application identifier (GUID), which is part of the file path, can change upon restart, making the saved absolute URI invalid.
1.3) On modern versions of Android, the problem is exacerbated by the use of the `content://` URI scheme.
Unlike a direct file path (`file://`), a `content://` URI is a pointer to a Content Provider: a system mechanism for secure data exchange between applications.
Access to a content URI is granted to an application temporarily, usually for the lifetime of the current activity.
As soon as the user closes the application or the system forcibly terminates it, this temporary permission is revoked.
When the application is subsequently launched and attempts to use the saved `content://` URI to access the file, the operating system will deny access because the permission is no longer valid.
1.4) The correct way to eliminate cause #1 is to immediately copy the file from the temporary location provided by `expo-image-picker` to a persistent directory in the application sandbox.
Expo provides 2 main directories:
- `FileSystem.cacheDirectory` for temporary files that the system can delete when storage is low
- `FileSystem.documentDirectory` for persistent files that are only deleted by the application itself

The task is to use a function such as `FileSystem.copyAsync()` or `file.move()` to move the file to `FileSystem.documentDirectory` immediately after receiving the temporary URI.
It is the URI of this persistent copy that must be saved in the retry queue.
Even if the `copyToCacheDirectory` option in the picker is used, the file still ends up in the temporary cache, which can be cleared by the system, making this approach unreliable for deferred tasks.
1.5) Specifically, how cause #1 leads to the "undefined values" failure:
1.5.1) The retry logic retrieves an outdated, invalid URI from the queue.
1.5.2) An attempt to read the file at this URI using the file system fails (for example, an exception is thrown or `null` is returned).
1.5.3) If the `catch` block or subsequent error-handling logic is not robust enough, the variable that was supposed to contain the file's binary data or the file object receives the value `undefined.`
1.5.4) This undefined variable is then passed to the upload function (for example, into the body of a fetch request), resulting in the «undefined values» error recorded in the logs.
This is a fundamental data integrity problem at the «first mile».
If the reference to the source data is fragile, no retry or queue management logic can correct the situation, no matter how sophisticated.
The failure occurs at the very beginning of the offline process.
The recent fix that worked in the laboratory likely did not include a full application restart cycle.
Within a single application session, the temporary URI remains valid, creating the false impression that the problem has been resolved.
However, this fix does not account for the full application lifecycle, which regularly occurs in field conditions, and is therefore incomplete.
2) 3 more potential causes of your problem are evident to me.
Upwork limits the length of a proposal to ~5,500 characters, so I will list these causes briefly:
2.1) Expiration of the Azure Blob storage SAS token on a delayed retry attempt.
2.2) Incorrect serialization of the upload task state.
2.3) In-memory state loss due to OS process termination.
---
My GitHub profile: https://github.com/dmitrii-fediuk