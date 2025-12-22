## 1

### Замечания

𐒌₂

### Пункт документа

### Исходный текст

This gap exposes the `WKWebView` backing store (the color depends on the system theme).

### Предлагаемый текст

This gap exposes the `WKWebView` backing store.

## 2

### Замечания

𐒌₁

### Пункт документа

### Исходный текст

The problem stems from the root cause `C`, exacerbated by factors `S1` and `S2`

### Предлагаемый текст

The problem stems from the root cause `C`, while factors `S1` and `S2` determine the visual appearance of the artifact

## 3

### Замечания

𐒌₁, 𐒌₂

### Пункт документа

4.2)

### Исходный текст

In Chrome, the System UI Backdrop renders as a solid opaque block (the color depends on the system theme).
This opaque layer visually occludes the underlying content.

### Предлагаемый текст

In Chrome, the System UI Backdrop renders as a solid white block.
This opaque layer visually fills the exposed gap.

## 4

### Замечания

𐒌₁

### Пункт документа

### Исходный текст

Consequently, the system enforces a protective mask that visually occludes the content.

### Предлагаемый текст

Consequently, the system enforces a protective mask that visually fills the exposed gap.

## 5

### Замечания

𐒌₃

### Пункт документа

7.1)

### Исходный текст

Create an isolated stacking context for fixed elements and lock the root container height.

### Предлагаемый текст

Create an isolated stacking context for fixed elements.

## 6

### Замечания

𐒌₄

### Пункт документа

8.1)

### Исходный текст

The script listens for `focusout` and `resize` events to trigger a layout reset via a non-destructive micro-scroll (e.g. 1 pixel).

### Предлагаемый текст

The script listens for `focusout` and `resize` events to trigger a layout reset via a forced scroll position reset (`window.scrollTo(0, 0)`).