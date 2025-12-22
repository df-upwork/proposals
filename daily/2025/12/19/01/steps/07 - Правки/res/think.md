## 1

### Замечания

`𐒌₁`

### Пункт документа

3

### Исходный текст

The problem results from `C`, `S1`, `S2`, or a combination thereof.

### Предлагаемый текст

The problem stems from the root cause `C`, exacerbated by factors `S1` and `S2`.

## 2

### Замечания

`𐒌₂`

### Пункт документа

5

### Исходный текст

The system subsequently enforces Safe Area constraints, but the layout fails to extend the content.
Consequently, the unfilled area exposes the underlying background.

### Предлагаемый текст

The system subsequently enforces Safe Area constraints by rendering an opaque protective overlay.
Consequently, this system layer visually occludes the content layer.

## 3

### Замечания

`𐒌₃`

### Пункт документа

7.1

### Исходный текст

Set `html` and `body` height to `100dvh` with `overflow: hidden`.
Move the content to an internal wrapper with `height: 100%` and `overflow-y: auto`.

### Предлагаемый текст

Set `html` and `body` height to `100dvh`.

## 4

### Замечания

`𐒌₃`

### Пункт документа

7.2

### Исходный текст

The internal scrolling architecture eliminates layout shifts caused by dynamic browser panels.

### Предлагаемый текст

The usage of `100dvh` units prevents layout shifts caused by dynamic browser panels.

## 5

### Замечания

`𐒌₄`

### Пункт документа

7.3.2

### Исходный текст

Moving scrolling to an internal container preserves native inertia automatically on iOS 26.

### Предлагаемый текст

(Удалить этот пункт).