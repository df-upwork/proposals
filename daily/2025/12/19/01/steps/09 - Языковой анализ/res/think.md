1) The root cause of your problem (`C1`): https://bugs.webkit.org/show_bug.cgi?id=297779
Desynchronization of the visual viewport and page layout coordinates occurring after interaction with the keyboard or changing the device orientation.
As a result of this failure, fixed interface elements shift upward by approximately 24 pixels.
The resulting gap exposes the system WebView rendering backing, which has a white color by default.
The Chrome browser on iOS is forced to use the system `WKWebView` component, so it inherits this bug without the possibility of correction at the application level.
2) `C1` often manifests in 2 scenarios (`S1` and `S2`), described in points 3 and 4 below.
3) `S1`: activation of the system setting «Reduce Transparency»
3.1) Example
https://discussions.apple.com/thread/256149325?answerId=256149325021
3.2) The essence
In the «Liquid Glass» design, this setting disables resource-intensive blur shaders and replaces semi-transparent backdrops with solid opaque fills.
In the Chrome browser, the bottom navigation bar or its backdrop turns into a solid white block.
This block is physically located above the webpage in the layer hierarchy, therefore it overlaps the bottom part of the content.
4) `S2`: architectural conflict between the «Liquid Glass» system and Safe Area
The new iPadOS 26 architecture introduces dynamic floating layers, which creates a race condition during the initialization of safe area environment variables.
At the moment of loading, Chrome may receive zero inset values, extending the content to the full screen.
Then the system applies a protective mask under the system panels, which renders as an opaque bar.
As a result, a visual conflict occurs, in which the content is covered by the system overlay.
5) Below are 2 high-quality ways to eliminate `C1`.
In some cases, it is necessary to apply them in combination.
6) `R1⁂`
6.1) Essence
Forcibly create an isolated stacking context for fixed interface elements and strictly fix the height of the root container.
It is necessary to apply the CSS property `transform: translateZ(0)` to elements with `position: fixed` to activate hardware acceleration and bypass the WebKit rendering bug.
For the root elements `html` and `body`, it is necessary to set the height to `100dvh` to compensate for the dynamic behavior of the Chrome address bar in iPadOS 26.
Additionally, it is required to set `background-color` for `body`, matching the color of the bottom panel, for visual masking of possible micro-shifts.
6.2) Advantages
`R1⁂` eliminates the most likely root cause of the visual artifact — a layer compositing error in the new Liquid Glass system.
Using `dvh` units ensures a mathematically correct calculation of the visible area, accounting for floating browser panels.
The solution is declarative, does not burden the main JavaScript execution thread, and applies instantly during page rendering.
Background color masking effectively conceals the problem even in those rare cases where the physical viewport displacement persists.
6.3) Key challenges
6.3.1) Changing the stacking context can affect the `z-index` of other popup elements, requiring verification of modal windows.
6.3.2) In rare cases, the combination of `100dvh` and `translateZ` may conflict with iOS native inertial scrolling.
7) `R2⁂`
7.1) Essence
Create an observer script that forcibly synchronizes the layout coordinates with the visual viewport when the interface state changes.
The script must track `focusout` (keyboard dismissal) and `resize` events, triggering a micro-scroll `window.scrollTo(0, 0)` or a style recalculation.
This action resets the internal offset flag in the WebKit engine, eliminating the «phantom» 24-pixel indentation remaining after the keyboard dismissal.
7.2) Advantages
`R2⁂` guarantees fixing the interface displacement in scenarios of active interaction with input forms and the virtual keyboard.
The script works reactively, eliminating the problem exactly at the moment of its occurrence, when CSS rules can be ignored by the engine.
`R2⁂` does not require a radical restructuring of the application layout and can be implemented as a targeted «hotfix».
7.3) Key challenges
7.3.1) Using `resize` and `scroll` event listeners creates additional CPU load and may cause interface «jitter».
7.3.2) There is a delay between the event occurrence and the script execution, due to which the user may notice a content jump.
7.3.3) Dependence on JavaScript makes the interface less stable under high system load conditions or script blocking.