1) Действие «Reauthorize» и вообще экран «Integrations» не имеют никакого отношения к вашей проблеме: вы тратите время и силы впустую.
2) Контекст проблемы — Digital Markets Act (DMA) Европейского союза.
Исполняя DMA, Google перекладывает обязательство по сбору согласия на вас как владельца сайта, используя свой протокол «Consent Mode».
3) В мае 2025 года Google обновила свой протокол «Consent Mode», изменив формат cookie («GS2 Cookie»).
Именно это поломало ваш модуль (WeltPixel Google Analytics 4 PRO).
4) WeltPixel в курсе проблемы и описывает её в changelog модуля на своём сайте:
«Important adjustment (PRO): Implemented the use of the updated GS2 Cookie, a potentially integration-breakning change Google introduced in May 2025 without prior notice. 
If your tracking implementation is experiencing attribution or issues surrounding data tracking, please update to this version ASAP.»
5) Правильное решение вашей проблемы:
5.1) Убедиться, что модуль WeltPixel действительно качественно обновлён.
5.2) Убедиться, что новая версия модуля не конфликтует с другими установленными модулями и оформительской темой Magento.
5.3) Убедиться, что в Magento установлен и правильно работает модуль для управления согласием.
В частности, сам WeltPixel предлагает такой модуль: https://www.weltpixel.com/google-consent-mode-v2.html


 