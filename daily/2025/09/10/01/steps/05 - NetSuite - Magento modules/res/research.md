https://g.co/gemini/share/b8cbc4aaa106

#
**первоначальный выбор должен основываться не на вопросе «Какой коннектор лучше?», а на вопросе «Какая интеграционная модель наилучшим образом соответствует бизнес-логике, техническим компетенциям и финансовой стратегии клиента?»**. 
Этот выбор определяет совокупную стоимость владения и распределение зон ответственности между командами, отвечающими за Magento и NetSuite.

#
Предложение решения на базе iPaaS, такого как Celigo, годовая подписка на который может составлять десятки тысяч долларов , может быть немедленно отклонено клиентом, не готовым к таким операционным расходам. Это приведёт к потере времени и усилий, затраченных на анализ и подготовку предложения.

# 2.1. Celigo (iPaaS)
##
Celigo представляет собой интеграционную платформу как услугу (iPaaS), ядром которой является продукт integrator.io.

##
Celigo использует подписную модель (OpEx). Цены не публикуются открыто и формируются индивидуально на основе количества «конечных точек» (endpoints, т.е. подключаемых систем) и «потоков» (flows). 1  Отзывы пользователей и оценки аналитиков указывают на то, что это дорогое решение. Годовая стоимость может варьироваться от $12,000 до более чем $70,000 в зависимости от выбранного тарифного плана и сложности интеграции. 

# 2.2. Firebear Studio (Расширение для Magento)
##
Решение от Firebear Studio представляет собой не автономный коннектор, а аддон к их флагманскому продукту — расширению «Improved Import & Export». 
Это ключевая архитектурная особенность. Вся логика интеграции размещается и выполняется внутри Magento. 

## Поддержка B2B
Поддержка B2B-сценариев реализуется через модульный подход. Основное расширение имеет специальный B2B Add-On, который обеспечивает работу с такими сущностями, как компании, общие каталоги, списки заявок и запрашиваемые коммерческие предложения (negotiable quotes). Аддон для NetSuite, в свою очередь, обеспечивает передачу этих данных между системами. Этот подход является очень гибким и мощным, но требует покупки и настройки нескольких компонентов. 
https://commercemarketplace.adobe.com/firebear-importexport.html
https://firebearstudio.com/blog/magento-2-shared-catalogs-import-export.html

# 2.4. Kensium (Расширение для Magento)
https://www.kensium.com/adobe-netsuite-connector
https://commercemarketplace.adobe.com/kensiumsolutions-netsuite-connector.html
## 
Kensium предлагает выделенное расширение для Magento, которое напрямую взаимодействует с NetSuite через API. Архитектурно это решение аналогично продукту от Firebear Studio — вся логика находится на стороне Magento. Компания Kensium позиционирует себя как эксперта с глубокими компетенциями как в Magento, так и в ERP-системах.

# 2.5. Netable (Расширение для Magento)
Once installed, you simply have to enter your NetSuite credentials into the Magento 2 admin panel and the connector will start working immediately. From the admin panel, you can control the module settings and scope that you want to integrate with. You can choose the sync one-way or both ways the items (stock), customer and orders and backend settings also provide additional options to sync automatically or manually. Once synced, products, customers and orders will display NetSuite IDs to enable you to cross-reference your data.
https://commercemarketplace.adobe.com/netable-module-net-suite.html
https://www.netable.com.au/magento/magento-netsuite

На первый взгляд, ценовая модель Netable кажется привлекательной. На официальной торговой площадке Adobe Commerce указана единовременная стоимость лицензии в размере $7,000 , что сопоставимо с Kensium. Однако более глубокий анализ официального сайта компании  выявляет скрытые затраты, которые могут существенно увеличить совокупную стоимость владения.   

Множество функций, которые являются критически важными для проекта P⁎ и стандартными для других решений, у Netable требуют отдельной платной доработки («Customisation required»). В их число входят:

Синхронизация конфигурируемых и групповых товаров.

Синхронизация категорий.

Поддержка мульти-сайтовости (multi-store).

Сопоставление атрибутов товаров.

Синхронизация цен и остатков в реальном времени.

Поддержка нескольких складов.

Синхронизация кредитных лимитов для B2B-клиентов.

Даже ежедневные отчёты об ошибках.