## 1

1, 2, 3, 4
1)
Viewport and layout coordinates become desynchronized after keyboard interaction or orientation changes.
Fixed interface elements shift upward.
This gap exposes the white `WKWebView` backing store.
Chrome on iOS inherits this bug without the possibility of a fix at the browser level.

Viewport and layout coordinates become desynchronized during initialization, keyboard interaction, or orientation changes.
Consequently, the system renders an opaque protective mask over the bottom area of the webpage.
This layer (the color depends on the system theme) visually blocks the content.
Chrome on iOS inherits this bug, and the current application version fails to mitigate it via native workarounds.