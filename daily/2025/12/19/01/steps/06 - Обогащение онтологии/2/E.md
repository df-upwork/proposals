# `ⵣ⧛1⧚`
`ⵣ⧛1⧚` ≔
```markdown
1) The root cause (`C`): https://bugs.webkit.org/show_bug.cgi?id=297779
Viewport and layout coordinates become desynchronized after keyboard interaction or orientation changes.
Fixed interface elements shift upward.
This gap exposes the white `WKWebView` backing store.
Chrome on iOS inherits this bug without the possibility of a fix at the browser level.
2) Key definitions used in my analysis:
Liquid Glass: `LG`
3) `C` manifests in 2 scenarios (`S1` and `S2`).
4) `S1`: activation of the system setting «Reduce Transparency»
4.1) Example
https://discussions.apple.com/thread/256149325?answerId=256149325021
4.2) The essence
This setting replaces semi-transparent `LG` backdrops with opaque fills.
In Chrome, the bottom navigation bar becomes a solid white block.
This block is rendered above the webpage layer and blocks the content.
5) `S2`: architectural conflict between `LG` and Safe Area
Dynamic floating layers create a race condition during Safe Area initialization.
Chrome initially receives 0-value insets and extends the content to the full screen.
The system subsequently applies an opaque protective mask under the panels.
Consequently, the system overlay covers the content.
6) Below are 2 high-quality strategies to mitigate the effects of `C`.
In some cases, it is necessary to apply them in combination.
7) `R1⁂`
7.1) Essence
Create an isolated stacking context for fixed elements and lock the root container height.
Apply `transform: translateZ(0)` to `position: fixed` elements to bypass the WebKit bug.
Set `html` and `body` height to `100dvh` to handle the dynamic address bar.
Set the `body` `background-color` to match the bottom panel for visual masking.
7.2) Advantages
It circumvents the layer compositing error in `LG`.
`dvh` units ensure correct area calculation accounting for floating browser panels.
`R1⁂` applies instantly without burdening the JavaScript thread.
Background masking conceals the problem even if physical displacement persists.
7.3) Key challenges
7.3.1) Changing the stacking context affects `z-index`, requiring verification of modal windows.
7.3.2) In rare cases, the combination of `100dvh` and `translateZ` conflicts with native inertial scrolling.
8) `R2⁂`
8.1) Essence
Implement a script to synchronize layout coordinates with the visual viewport upon interface state changes.
The script listens for `focusout` and `resize` events to trigger a layout reset via `window.scrollTo(0, 0)`.
This action resets the WebKit internal offset flag.
8.2) Advantages
It resolves interface displacement caused by interactions with the virtual keyboard.
It works reactively when the engine fails to apply CSS rules correctly.
It does not require layout restructuring and serves as a targeted «hotfix».
8.3) Key challenges
8.3.1) Frequent event handling increases CPU load and may cause interface «jitter».
8.3.2) A delay between the event and execution may cause a visible content jump.
8.3.3) Reliance on JavaScript reduces reliability under high system load.
```

# `𐒌ⵣ⠿⧛1⧚`
`𐒌ⵣ⠿⧛1⧚` ≔ 
```markdown
# 1.

**Логическая ошибка в классификации причинно-следственных связей (Пункты 1, 3, 4, 5).**
В тексте утверждается, что корневая причина `C` (баг WebKit #297779 — десинхронизация координат) проявляется в виде сценариев `S1` и `S2`. Это утверждение некорректно:

1. Сценарий `S1` (настройка «Reduce Transparency») — это штатная функция системы доступности, изменяющая прозрачность слоев. Она не вызывается багом координат.
2. Сценарий `S2` (архитектурный конфликт Safe Area / гонка инициализации) — это проблема начального рендеринга и передачи переменных окружения (`env()`). Она технически независима от бага смещения вьюпорта при взаимодействии, описанного в `C`.
Эти явления (`C`, `S1`, `S2`) являются тремя разными факторами, а не следствиями одного бага.
Степень уверенности: 95

# 2.

**Логическое противоречие в описании механизма проблемы (Пункты 1 и 4.2).**
— В пункте 1 утверждается, что проблема заключается в смещении элементов вверх, из-за чего *обнажается* подложка снизу («exposes the white `WKWebView` backing store»). То есть визуальный артефакт находится *под* или *за* контентом.
— В пункте 4.2 утверждается, что системный блок рендерится *поверх* слоя веб-страницы («rendered above the webpage layer and blocks the content»).
Один и тот же артефакт не может быть одновременно «дырой» под контентом и «наложением» поверх него.
Степень уверенности: 100

# 3.

**Критическая логическая ошибка (UX) в стратегии `R2⁂` (Пункт 8.1).**
Предложение вызывать `window.scrollTo(0, 0)` при событии `resize` является недопустимым для мобильных браузеров. Событие `resize` штатно срабатывает при вертикальной прокрутке страницы, когда скрывается или появляется адресная строка браузера. Реализация этого совета приведет к тому, что при любой попытке пользователя прокрутить страницу его будет принудительно возвращать в начало документа, делая сайт неработоспособным.
Степень уверенности: 100

# 4.

**Техническая ошибка в стратегии `R1⁂` (Пункт 7.1).**
Инструкция установить `html` и `body` height в `100dvh` («Set `html` and `body` height to `100dvh`») технически неполна. Без явного указания на создание внутреннего контейнера с прокруткой (свойства `overflow-y: auto` и т.д.) такая фиксация высоты на корневых элементах приведет к блокировке прокрутки страницы. Весь контент, выходящий за пределы первого экрана, станет недоступным.
Степень уверенности: 95

# 5.

**Фактическая ошибка в описании `S1` (Пункт 4.2).**
Утверждение, что при включении настройки «Reduce Transparency» навигационная панель становится «сплошным *белым* блоком» («solid white block»), является неточным. Цвет непрозрачной подложки зависит от системной темы оформления (Light/Dark Mode) и CSS-стилей браузера. В темной теме этот блок будет черным или темно-серым.
Степень уверенности: 90

# 6.

**Фактическая ошибка в атрибуции проблем (Пункт 7.3.2).**
Утверждается, что комбинация `100dvh` и `translateZ` конфликтует с нативным инерционным скроллом («conflicts with native inertial scrolling»). Это технически неверно. Потеря инерции скролла в iOS (momentum scrolling) вызывается использованием свойств `overflow: hidden` / `auto` на контейнерах без добавления `-webkit-overflow-scrolling: touch` (в старых версиях) или особенностями реализации `body scroll lock`. Сами по себе единицы измерения высоты или 3D-трансформации инерцию не отключают.
Степень уверенности: 85
```

# `ⵣ⧛2⧚`
`ⵣ⧛2⧚` ≔
```markdown
1) The root cause (`C`): https://bugs.webkit.org/show_bug.cgi?id=297779
Viewport and layout coordinates become desynchronized after keyboard interaction or orientation changes.
Fixed interface elements shift upward.
This gap exposes the white `WKWebView` backing store.
Chrome on iOS inherits this bug without the possibility of a fix at the browser level.
2) Key definitions used in my analysis:
Liquid Glass: `LG`
3) The problem results from the interaction of 3 distinct factors (`C`, `S1`, and `S2`).
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
The system subsequently applies an opaque protective mask under the panels.
Consequently, the system overlay covers the content.
6) Below are 2 high-quality strategies to mitigate the effects of `C`.
In some cases, it is necessary to apply them in combination.
7) `R1⁂`
7.1) Essence
Create an isolated stacking context for fixed elements and lock the root container height.
Apply `transform: translateZ(0)` to `position: fixed` elements to bypass the WebKit bug.
Set `html` and `body` height to `100dvh` with `overflow: hidden`.
Move the content to an internal wrapper with `height: 100%` and `overflow-y: auto`.
Set the `body` `background-color` to match the bottom panel for visual masking.
7.2) Advantages
It circumvents the layer compositing error in `LG`.
`dvh` units ensure correct area calculation accounting for floating browser panels.
`R1⁂` applies instantly without burdening the JavaScript thread.
Background masking conceals the problem even if physical displacement persists.
7.3) Key challenges
7.3.1) Changing the stacking context affects `z-index`, requiring verification of modal windows.
7.3.2) Moving scrolling to an internal container requires explicit `-webkit-overflow-scrolling: touch` to preserve native inertia.
8) `R2⁂`
8.1) Essence
Implement a script to synchronize layout coordinates with the visual viewport upon interface state changes.
The script listens for `focusout` events to trigger a layout reset via `window.scrollTo(0, 0)`.
This action resets the WebKit internal offset flag.
8.2) Advantages
It resolves interface displacement caused by interactions with the virtual keyboard.
It works reactively when the engine fails to apply CSS rules correctly.
It does not require layout restructuring and serves as a targeted «hotfix».
8.3) Key challenges
8.3.1) Frequent event handling increases CPU load and may cause interface «jitter».
8.3.2) A delay between the event and execution may cause a visible content jump.
8.3.3) Reliance on JavaScript reduces reliability under high system load.
```

# `𐒌ⵣ⠿⧛2⧚`
`𐒌ⵣ⠿⧛2⧚` ≔ 
```markdown
# 1.

**Логическая ошибка (Противоречие между механизмом и симптомом).**
В тексте утверждается, что механизм проблемы — это образование «зазора» («gap»), который «обнажает подложку» («exposes... backing store») в результате смещения элементов вверх. Однако в описании проблемы `P†` указано, что белая полоса **блокирует** контент («blocks content»). «Зазор» или «подложка» физически находятся *позади* слоя веб-контента и не могут перекрывать (блокировать) элементы интерфейса. Описанный механизм логически не соответствует наблюдаемому симптому наложения.
Степень уверенности: 95

# 2.

**Фактическая ошибка (Техническая возможность исправления).**
Утверждение, что Chrome на iOS наследует баг «без возможности исправления на уровне браузера» («without the possibility of a fix at the browser level»), ложно. Разработчики приложения Chrome имеют доступ к нативному API iOS и могут внедрять обходные пути (workarounds) на уровне приложения — например, через принудительное изменение размеров фрейма `WKWebView`, использование нативных оверлеев или автоматическую инъекцию компенсирующих JavaScript-сценариев.
Степень уверенности: 95

# 3.

**Фактическая ошибка (Цвет подложки).**
Утверждение «exposes the *white* `WKWebView` backing store» содержит фактическую неточность. Цвет подложки (`backing store`) не является фиксированно белым, а зависит от системной темы оформления (Light/Dark Mode). В тёмном режиме подложка будет чёрной или тёмно-серой. Безусловное определение её как белой ошибочно.
Степень уверенности: 90

# 4.

**Фактическая неполнота (Триггеры возникновения).**
В тексте возникновение рассинхронизации привязывается исключительно к «взаимодействию с клавиатурой или смене ориентации» («after keyboard interaction or orientation changes»). Это противоречит данным онтологии (`O.md`), согласно которым проблема также может возникать сразу при загрузке страницы из-за состояния гонки (Race Condition) при инициализации метрик Safe Area и Liquid Glass, без активных действий пользователя.
Степень уверенности: 85
```

# `ⵣ⧛3⧚`
`ⵣ⧛3⧚` ≔
```markdown
1) The root cause (`C`): https://bugs.webkit.org/show_bug.cgi?id=297779
Viewport and layout coordinates become desynchronized during initialization, keyboard interaction, or orientation changes.
Consequently, the system renders an opaque protective mask over the bottom area of the webpage.
This layer (the color depends on the system theme) visually blocks the content.
Chrome on iOS inherits this bug, and the current application version fails to mitigate it via native workarounds.
2) Key definitions used in my analysis:
Liquid Glass: `LG`
3) The problem results from the interaction of 3 distinct factors (`C`, `S1`, and `S2`).
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
The system subsequently applies an opaque protective mask under the panels.
Consequently, the system overlay covers the content.
6) Below are 2 high-quality strategies to mitigate the effects of `C`.
In some cases, it is necessary to apply them in combination.
7) `R1⁂`
7.1) Essence
Create an isolated stacking context for fixed elements and lock the root container height.
Apply `transform: translateZ(0)` to `position: fixed` elements to bypass the WebKit bug.
Set `html` and `body` height to `100dvh` with `overflow: hidden`.
Move the content to an internal wrapper with `height: 100%` and `overflow-y: auto`.
Set the `body` `background-color` to match the bottom panel for visual masking.
7.2) Advantages
It circumvents the layer compositing error in `LG`.
`dvh` units ensure correct area calculation accounting for floating browser panels.
`R1⁂` applies instantly without burdening the JavaScript thread.
Background masking conceals the problem even if physical displacement persists.
7.3) Key challenges
7.3.1) Changing the stacking context affects `z-index`, requiring verification of modal windows.
7.3.2) Moving scrolling to an internal container requires explicit `-webkit-overflow-scrolling: touch` to preserve native inertia.
8) `R2⁂`
8.1) Essence
Implement a script to synchronize layout coordinates with the visual viewport upon interface state changes.
The script listens for `focusout` events to trigger a layout reset via `window.scrollTo(0, 0)`.
This action resets the WebKit internal offset flag.
8.2) Advantages
It resolves interface displacement caused by interactions with the virtual keyboard.
It works reactively when the engine fails to apply CSS rules correctly.
It does not require layout restructuring and serves as a targeted «hotfix».
8.3) Key challenges
8.3.1) Frequent event handling increases CPU load and may cause interface «jitter».
8.3.2) A delay between the event and execution may cause a visible content jump.
8.3.3) Reliance on JavaScript reduces reliability under high system load.
```

# `𐒌ⵣ⠿⧛3⧚`
`𐒌ⵣ⠿⧛3⧚` ≔ 
```markdown
## Замечание №1
### Перечень пунктов, к которым относится замечение
1, 5, 7.1
### Конкретные цитаты, к которым относится замечение
Пункт 1: «Consequently, the system renders an opaque protective mask over the bottom area of the webpage... visually blocks the content.»
Пункт 5: «The system subsequently applies an opaque protective mask under the panels. Consequently, the system overlay covers the content.»
Пункт 7.1: «Set the `body` `background-color` to match the bottom panel for visual masking.»
### Суть замечания
**Логическое противоречие (Диагноз vs Лечение).**
В пунктах 1 и 5 утверждается, что механизм проблемы заключается в рендеринге системной маски *поверх* («over», «covers») веб-страницы. В стратегии `R1⁂` (пункт 7.1) предлагается решение через изменение цвета фона (`background-color`) элемента `body`.
Фон `body` находится на самом нижнем уровне стека отрисовки документа. Если проблема вызвана наложением непрозрачного слоя *поверх* контента, то изменение цвета фона, находящегося *под* контентом, физически не может скрыть или замаскировать наложенный сверху элемент. Данная стратегия была бы эффективна, только если бы проблема заключалась в смещении контента (gap), обнажающем подложку, но это противоречит описанию механизма в пунктах 1 и 5.
### Степень уверенности в истинности замечания
100

## Замечание №2
### Перечень пунктов, к которым относится замечение
8.1
### Конкретные цитаты, к которым относится замечение
«The script listens for `focusout` events to trigger a layout reset via `window.scrollTo(0, 0)`.»
### Суть замечания
**Критическая логическая ошибка (UX).**
Инструкция выполнять `window.scrollTo(0, 0)` (мгновенный скролл в самый верх страницы) при событии `focusout` (потеря фокуса полем ввода / закрытие клавиатуры) является недопустимой с точки зрения юзабилити.
Это событие срабатывает, когда пользователь заканчивает ввод или переходит к следующему полю. Если пользователь заполняет форму в середине или внизу длинной страницы, выполнение этого скрипта приведёт к потере визуального контекста и принудительному возврату в начало страницы. Интерфейс станет непригодным для использования. Корректный метод сброса лэйаута не должен разрушать текущую позицию скролла пользователя (например, микро-скролл на 1px).
### Степень уверенности в истинности замечания
100

## Замечание №3
### Перечень пунктов, к которым относится замечение
1
### Конкретные цитаты, к которым относится замечение
«The root cause (`C`): ... Consequently, the system renders an opaque protective mask over the bottom area of the webpage.»
### Суть замечания
**Фактическая ошибка (Атрибуция механизма).**
Баг WebKit #297779 вызывает рассинхронизацию координат (`VisualViewport` vs `LayoutViewport`), что приводит к смещению контента и образованию пустого пространства (gap/displacement), через которое видна подложка. Этот программный баг *не инициирует* активный рендеринг системой специальной «защитной маски» («protective mask»). Механизм защитных масок относится к штатной работе подсистемы Liquid Glass / Safe Area (описанной в `S2`), но не является прямым следствием бага координат. Текст ошибочно приписывает багу смещения свойства защитного оверлея.
### Степень уверенности в истинности замечания
95

## Замечание №4
### Перечень пунктов, к которым относится замечение
3
### Конкретные цитаты, к которым относится замечение
«The problem results from the interaction of 3 distinct factors (`C`, `S1`, and `S2`).»
### Суть замечания
**Логическая ошибка (Неверное обобщение условий).**
Формулировка подразумевает, что для возникновения проблемы необходимо одновременное взаимодействие всех трёх факторов. Это неверно:

1. `S1` (настройка «Reduce Transparency») и `S2` (гонка инициализации прозрачности Liquid Glass) являются взаимоисключающими или альтернативными сценариями. Если активно `S1`, динамическая прозрачность отключена.
2. Баг `C` может проявляться независимо от `S1` и `S2`.
Проблема `P†` может возникать при наличии только `C`, только `S2` или их парной комбинации, но не требует одновременного участия всех трёх факторов.
### Степень уверенности в истинности замечания
90

## Замечание №5
### Перечень пунктов, к которым относится замечение
7.3.2
### Конкретные цитаты, к которым относится замечение
«Moving scrolling to an internal container requires explicit `-webkit-overflow-scrolling: touch` to preserve native inertia.»
### Суть замечания
**Фактическая ошибка (Устаревшие технические данные).**
Утверждение, что для сохранения инерции скролла во внутренних контейнерах *требуется* («requires») явное указание свойства `-webkit-overflow-scrolling: touch`, неактуально для iPadOS 26 (2025 год). Начиная с iOS 13, инерционный скролл включен по умолчанию для всех контейнеров с `overflow: auto` или `scroll`. В современном контексте данное свойство поддерживается только для обратной совместимости и не является обязательным требованием.
### Степень уверенности в истинности замечания
95
```

# `ⵣ⧛4⧚`
`ⵣ⧛4⧚` ≔
```markdown
1) The root cause (`C`): https://bugs.webkit.org/show_bug.cgi?id=297779
Viewport and layout coordinates become desynchronized during initialization, keyboard interaction, or orientation changes.
Consequently, the system renders an opaque protective mask over the bottom area of the webpage.
Consequently, fixed interface elements shift upward, creating a gap between the content and the screen edge.
This gap exposes the `WKWebView` backing store (the color depends on the system theme).
2) Key definitions used in my analysis:
Liquid Glass: `LG`
3) The problem results from `C`, `S1`, `S2`, or a combination thereof.
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
The system subsequently enforces Safe Area constraints, but the layout fails to extend the content.
Consequently, the unfilled area exposes the underlying background.
6) Below are 2 high-quality strategies to mitigate the effects of `C`.
In some cases, it is necessary to apply them in combination.
7) `R1⁂`
7.1) Essence
Create an isolated stacking context for fixed elements and lock the root container height.
Apply `transform: translateZ(0)` to `position: fixed` elements to bypass the WebKit bug.
Set `html` and `body` height to `100dvh` with `overflow: hidden`.
Move the content to an internal wrapper with `height: 100%` and `overflow-y: auto`.
Set the `body` `background-color` to match the bottom panel for visual masking.
7.2) Advantages
It circumvents the layer compositing error in `LG`.
`dvh` units ensure correct area calculation accounting for floating browser panels.
`R1⁂` applies instantly without burdening the JavaScript thread.
Background masking conceals the problem even if physical displacement persists.
7.3) Key challenges
7.3.1) Changing the stacking context affects `z-index`, requiring verification of modal windows.
7.3.2) Moving scrolling to an internal container preserves native inertia automatically on iOS 26.
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
8.3.1) Frequent event handling increases CPU load and may cause interface «jitter».
8.3.2) A delay between the event and execution may cause a visible content jump.
8.3.3) Reliance on JavaScript reduces reliability under high system load.
```

# `𐒌ⵣ⠿⧛4⧚`
`𐒌ⵣ⠿⧛4⧚` ≔ 
```markdown
## Замечание №1

### Перечень пунктов, к которым относится замечение

1

### Конкретные цитаты, к которым относится замечение

«Consequently, the system renders an opaque protective mask over the bottom area of the webpage.»
«Consequently, fixed interface elements shift upward, creating a gap... This gap exposes the `WKWebView` backing store...»

### Суть замечания

**Логическое противоречие (Взаимоисключающие механизмы).**
В пункте 1 одновременно утверждается наличие двух взаимоисключающих физических явлений как следствие одной причины:

1. Система рендерит непрозрачную маску *поверх* («over») нижней части веб-страницы.
2. Элементы смещаются вверх, создавая разрыв («gap»), через который видна подложка *под* («backing store») веб-страницей.
Визуальный артефакт не может быть одновременно слоем, перекрывающим контент сверху, и пустотой, открывающей вид на фон снизу. Если присутствует непрозрачная маска сверху, она перекрывает собой и контент, и любой гипотетический зазор под ним.

### Степень уверенности в истинности замечания

100

## Замечание №2

### Перечень пунктов, к которым относится замечение

1, 7.1

### Конкретные цитаты, к которым относится замечение

Пункт 1: «Consequently, the system renders an opaque protective mask over the bottom area of the webpage.»
Пункт 7.1: «Set the `body` `background-color` to match the bottom panel for visual masking.»

### Суть замечания

**Логическое несоответствие стратегии лечения заявленному диагнозу.**
В пункте 1 утверждается, что проблема вызвана наложением маски *поверх* контента. В стратегии `R1⁂` (пункт 7.1) предлагается решение через изменение цвета фона элемента `body`. Элемент `body` находится на самом нижнем уровне стека отрисовки. Изменение его цвета технически не может скрыть или замаскировать элемент, наложенный *поверх* веб-страницы. Данная стратегия валидна только для сценария с «разрывом» (gap), но противоречит описанию механизма «маски» (mask over).

### Степень уверенности в истинности замечания

100

## Замечание №3

### Перечень пунктов, к которым относится замечение

1

### Конкретные цитаты, к которым относится замечение

«The root cause (`C`): ... Consequently, the system renders an opaque protective mask over the bottom area of the webpage.»

### Суть замечания

**Фактическая ошибка (Неверная атрибуция механизма).**
В тексте утверждается, что баг WebKit #297779 (рассинхронизация координат) приводит к активному рендерингу «защитной маски» («protective mask»). Это технически неверно.
Баг #297779 вызывает ошибки смещения (`layout shift`), но не инициирует создание системных оверлеев. Механизм защитных масок относится к работе подсистемы Safe Area / Liquid Glass (описанной в пункте 5 как `S2`), но не является прямым следствием программного сбоя координат, описанного в пункте 1.

### Степень уверенности в истинности замечания

95

## Замечание №4

### Перечень пунктов, к которым относится замечение

7.1, 7.2

### Конкретные цитаты, к которым относится замечение

Пункт 7.1: «Set `html` and `body` height to `100dvh` with `overflow: hidden`. Move the content to an internal wrapper...»
Пункт 7.2: «`dvh` units ensure correct area calculation accounting for floating browser panels.»

### Суть замечания

**Логико-техническая ошибка (Нивелирование преимущества).**
В пункте 7.1 предлагается архитектура с блокировкой прокрутки `body` и переносом скролла во внутренний контейнер. В мобильных браузерах (iOS Safari/Chrome) панели инструментов становятся плавающими (скрываются/появляются) *только* при прокрутке корневого элемента. Если прокрутка перенесена внутрь, панели браузера остаются статичными.
Следовательно, заявленное в пункте 7.2 преимущество единиц `dvh` (учёт *плавающих* панелей) теряет смысл, так как в данной конфигурации панели перестают быть плавающими.

### Степень уверенности в истинности замечания

90

## Замечание №5

### Перечень пунктов, к которым относится замечение

8.1, 8.3.1

### Конкретные цитаты, к которым относится замечение

Пункт 8.1: «The script listens for `focusout` events...»
Пункт 8.3.1: «Frequent event handling increases CPU load...»

### Суть замечания

**Логическая ошибка (Неверная оценка частоты событий).**
В пункте 8.1 указано, что скрипт реагирует на событие `focusout`. Это дискретное событие, происходящее редко (при завершении ввода). В пункте 8.3.1 в качестве недостатка указывается риск высокой нагрузки на CPU из-за «частой обработки событий» («Frequent event handling»). Это описание риска характерно для непрерывных событий (таких как `scroll` или `resize`), но фактологически неверно для события `focusout`.

### Степень уверенности в истинности замечания

90
```

# `Aᨀ`
`Aᨀ` ≔
```markdown
1) The root cause (`C`): https://bugs.webkit.org/show_bug.cgi?id=297779
Viewport and layout coordinates become desynchronized during initialization, keyboard interaction, or orientation changes.
Consequently, fixed interface elements shift upward, creating a gap between the content and the screen edge.
This gap exposes the `WKWebView` backing store (the color depends on the system theme).
2) Key definitions used in my analysis:
Liquid Glass: `LG`
3) The problem results from `C`, `S1`, `S2`, or a combination thereof.
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
The system subsequently enforces Safe Area constraints, but the layout fails to extend the content.
Consequently, the unfilled area exposes the underlying background.
6) Below are 2 high-quality strategies to mitigate the effects of `C`.
In some cases, it is necessary to apply them in combination.
7) `R1⁂`
7.1) Essence
Create an isolated stacking context for fixed elements and lock the root container height.
Apply `transform: translateZ(0)` to `position: fixed` elements to bypass the WebKit bug.
Set `html` and `body` height to `100dvh` with `overflow: hidden`.
Move the content to an internal wrapper with `height: 100%` and `overflow-y: auto`.
Set the `body` `background-color` to match the bottom panel for visual masking.
7.2) Advantages
It circumvents the layer compositing error in `LG`.
The internal scrolling architecture eliminates layout shifts caused by dynamic browser panels.
`R1⁂` applies instantly without burdening the JavaScript thread.
Background masking conceals the problem even if physical displacement persists.
7.3) Key challenges
7.3.1) Changing the stacking context affects `z-index`, requiring verification of modal windows.
7.3.2) Moving scrolling to an internal container preserves native inertia automatically on iOS 26.
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
```