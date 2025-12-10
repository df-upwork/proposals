1) Firebase provides a native mechanism for implementing broadcast messaging: FCM Topic Messaging.
2) My proposed architecture:
2.1) The server-side (`S`) uses the Firebase Admin SDK to perform privileged operations, such as managing device subscriptions to topics and sending messages to them. 
`S` is responsible for all the server-side logic.
2.2) Client-side (`C`):
- requests permission from the user (`U`) to receive notifications
- receives a unique device registration token (`T`) from FCM and sends `T` to `S` for subsequent subscription.
3) High-level interaction flow:
3.1) `C` obtains `T` and sends it to `S`.
3.2) `S` subscribes the device with this `T` to a common topic.
3.3) Subsequently, to send a broadcast notification, an authorized administrator (`A`) sends a single message to FCM via the secure API endpoint `/api/broadcast` (`E1`), specifying this common topic as the recipient.
3.4) FCM, in turn, delivers this message to all subscribed devices.
4) A key architectural limitation of FCM for web clients is that they cannot subscribe to topics independently.
This operation must be performed by `S`.
Consequently, it is necessary to create a server-side API endpoint `/api/subscribe` (`E2`) that will accept the registration `T` from `C` and perform the subscription on its behalf.
5) Access to `E1` and `E2` must be strictly restricted.
Unprotected endpoints for broadcast messaging are vulnerable to spam and attacks.
I recommend implementing this protection in 2 steps:
5.1) Authentication: ensure that the request comes from a known, logged-in `A` (in the case of `E1`) and `U` (in the case of `E2`).
For `E1` I recommend using Firebase ID tokens (`AT`), which `A` will send with each request.
5.2) Authorization: ensure that `A` / `U` has the necessary permissions to perform this action.
5.2.1) I recommend adding a custom claim (`AC`) to `A`, e.g. `{admin: true}`, and verifying it on `S`.
5.2.2) The assignment of `AC` must be performed via a separate, highly secure mechanism, e.g., via a Cloud Function available only to existing `A`s, or via a server-side script.
6) To work with FCM in `C`, it is necessary to install the client SDK and configure a Service Worker.
7) The browser will not provide `T` until `U` explicitly grants the website permission to display notifications. 
Therefore, permission must be requested from `U` to receive notifications.
8) It is crucial to remember that `T` can change.
I recommend obtaining it on each load of `C` and sending it to `S` if it differs from the previously saved one.
9) For `S` to authenticate and execute Firebase API calls, it requires an identity.
This role is performed by a service account (`SA`): a special type of Google account intended for non-human interactions, such as server-to-server communication.
Including the `SA` key file in the Docker image is a serious security violation.
I recommend injecting the credentials into the container at runtime.
10) Full `U` subscription process:
10.1) `U` opens `C` in the browser.
10.2) `C` initiates the request for permission to display notifications.
10.3) `U` clicks «Allow».
10.4) `C` requests `T` from FCM.
10.5) `C` sends the token to `S` at `E2`.
10.6) `S` subscribes `T` to the common topic `all_users`.
10.7) `U`'s device is ready to receive broadcast notifications.
11) Procedure for initiating a broadcast notification:
11.1) `A` logs into their account in a special administrative panel.
11.2) `A` obtains from Firebase an `AT` containing the `AC`.
11.3) `A` composes the message (title and body) and clicks «Send».
11.4) The admin application makes a `POST` request to `E1`, attaching the `AT` in the `Authorization: Bearer <AT>` header.
11.5) `E1` verifies the validity of the token and the presence of the `AC`.
If the check passes, `S` constructs the message object for FCM and calls the send method.
11.6) FCM receives the request and delivers the notification to all devices subscribed to the `all_users` topic.