# `᛭A`
`᛭A` ≔ ⟪ Мой proposal `ꆜ` для `P⁎` ⟫
~~~markdown
1) The root cause (`C`): https://bugs.webkit.org/show_bug.cgi?id=297779
Viewport and layout coordinates become desynchronized during initialization, keyboard interaction, or orientation changes.
Consequently, fixed interface elements shift upward, creating a gap between the content and the screen edge.
This gap exposes the `WKWebView` backing store (the color depends on the system theme).
2) Key definitions used in my analysis:
Liquid Glass: `LG`
3) The problem stems from the root cause `C`, exacerbated by factors `S1` and `S2`
4) `S1`: activation of the system setting «Reduce Transparency»
4.1) Example
https://discussions.apple.com/thread/256149325?answerId=256149325021
4.2) The essence
This setting replaces semi-transparent `LG` backdrops with opaque fills.
In Chrome, the bottom navigation bar becomes a solid opaque block (the color depends on the system theme).
This opaque layer visually occludes the webpage content layer.
5) `S2`: architectural conflict between `LG` and Safe Area
Dynamic floating layers create a race condition during Safe Area initialization.
Chrome initially receives 0-value insets and extends the content to the full screen.
The system subsequently enforces Safe Area constraints by rendering an opaque protective overlay.
Consequently, this system layer visually occludes the content layer.
6) Below are 2 high-quality strategies to mitigate the effects of `C`.
In some cases, it is necessary to apply them in combination.
7) `R1⁂`
7.1) Essence
Create an isolated stacking context for fixed elements and lock the root container height.
Apply `transform: translateZ(0)` to `position: fixed` elements to bypass the WebKit bug.
Set `html` and `body` height to `100dvh`.
Set the `body` `background-color` to match the bottom panel for visual masking.
7.2) Advantages
It circumvents the layer compositing error in `LG`.
The usage of `100dvh` units prevents layout shifts caused by dynamic browser panels.
`R1⁂` applies instantly without burdening the JavaScript thread.
Background masking conceals the problem even if physical displacement persists.
7.3) Key challenges
7.3.1) Changing the stacking context affects `z-index`, requiring verification of modal windows.
8) `R2⁂`
8.1) Essence
Implement a script to synchronize layout coordinates with the visual viewport upon interface state changes.
The script listens for `focusout` events to trigger a layout reset via a non-destructive micro-scroll (e.g. 1 pixel).
This action resets the WebKit internal offset flag.
8.2) Advantages
It resolves interface displacement caused by interactions with the virtual keyboard.
It works reactively when the engine fails to apply CSS rules correctly.
It does not require layout restructuring and serves as a targeted «hotfix».
8.3) Key challenges
8.3.1) The fix triggers only after the interaction concludes, potentially leaving the interface displaced during input.
8.3.2) A delay between the event and execution may cause a visible content jump.
8.3.3) Reliance on JavaScript reduces reliability under high system load.
~~~