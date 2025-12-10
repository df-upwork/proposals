https://gemini.google.com/share/c660de97257c

## **1. Введение: Технический парадокс «чистой этикетки» и срока годности**

В современной пищевой промышленности Канады наблюдается острая дихотомия между потребительским спросом на продукты с «чистой этикеткой» (clean label) и логистической необходимостью в длительных сроках годности. Клиент ꆜ ставит задачу разработки чизкейка со сроком хранения 40 дней в охлажденном виде, исключая при этом синтетические консерванты. Для категории молочных десертов с высокой влажностью это представляет собой сложнейшую инженерную и микробиологическую задачу. Чизкейк как матрица уникален: он сочетает в себе фазу с высокой активностью воды (творожная начинка, `a_w > 0.95`) и фазу с низкой активностью воды (песочная основа, `a_w < 0.60`), что создает термодинамический драйвер для миграции влаги, помимо рисков микробиологической порчи и окисления липидов.

Традиционные методы решения этой задачи опираются на химические ингибиторы, такие как сорбат калия или бензоат натрия, которые эффективно подавляют рост дрожжей и плесени. Отказ от них требует внедрения альтернативных технологий барьерного типа (hurdle technology). В данном отчете проводится глубокий анализ трех основных технологических векторов: обработки высоким давлением (HPP), модифицированной газовой среды (MAP) и биопрезервации, с особым акцентом на нормативную базу Канады, которая существенно отличается от американской и европейской в вопросах маркировки «натуральных» консервантов.

### **1.1 Канадский регуляторный контекст и заблуждения индустрии**

Одним из критических аспектов данного проекта является необходимость развеять распространенные в индустрии заблуждения относительно того, что считается «чистой этикеткой» в Канаде. Многие производители, оглядываясь на рынок США, полагают, что использование ферментированных ингредиентов, таких как «культивированная декстроза» (cultured dextrose) или «культивированное обезжиренное молоко», позволяет декларировать продукт как «без консервантов». Однако анализ нормативных актов Канадского агентства инспекции пищевых продуктов (CFIA) и Министерства здравоохранения Канады (Health Canada) выявляет иную реальность.

Согласно разъяснениям CFIA, если ингредиент, такой как культивированная декстроза (коммерчески известная как MicroGARD и др.), добавляется в продукт с целью продления срока годности за счет содержания пропионовой, масляной и молочной кислот или бактериоцинов, он классифицируется как консервант.1 Это имеет фундаментальные последствия для маркировки: хотя в составе ингредиент может быть указан под своим обычным названием (например, «культивированная декстроза»), производитель **не имеет права** выносить на лицевую сторону упаковки клеймы «Без консервантов» (No Preservatives) или «Не содержит консервантов».2 Использование таких заявлений при наличии функциональных ферментатов считается введением потребителя в заблуждение согласно Разделу 5 Закона о пищевых продуктах и лекарствах. Это ставит Клиента ꆜ перед стратегическим выбором: либо отказаться от клейма «Без консервантов», либо искать физические методы обработки, не требующие декларирования добавок.

Более того, нормативный ландшафт Канады динамичен. Важным событием мая 2024 года стало расширение списка разрешенных консервантов, включившее **Натамицин** для использования в стандартизированных и нестандартизированных сливочных сырах и продуктах на их основе.4 Ранее натамицин был разрешен только для поверхностной обработки твердых сыров. Это изменение открывает новые возможности для биопрезервации, позволяя использовать натуральный антимикотик непосредственно в массе чизкейка, что ранее было невозможно. Это создает легальный путь для использования высокоэффективного натурального консерванта, который, хотя и должен быть задекларирован, воспринимается потребителями более лояльно, чем синтетические сорбаты.

Таким образом, «чистая этикетка» в контексте Канады — это не просто список ингредиентов, но и сложная система допустимых заявлений. В отчете мы рассмотрим, как технологии HPP и MAP могут позволить полностью избежать использования консервантов, обеспечивая истинную чистоту этикетки, или как биопрезервация может быть интегрирована с минимальными репутационными рисками.

---

## **2. Микробиологические и физико-химические вызовы срока в 40 дней**

Для достижения 40-дневного срока годности необходимо понимание механизмов деградации чизкейка. Основными векторами порчи являются рост патогенов (безопасность), рост плесени и дрожжей (коммерческая порча) и физическая деградация (текстура и синерезис).

### **2.1 Listeria monocytogenes: Угроза нулевой толерантности**

В категории мягких сыров и готовых к употреблению (RTE) продуктов *Listeria monocytogenes* является главной биологической угрозой. В отличие от многих других патогенов, листерия является психротрофом, то есть способна размножаться при температурах холодильного хранения (4°C).7 Для чизкейка с pH выше 4.6 и высокой активностью воды, отсутствие термической обработки после фасовки создает риск. Даже если выпечка убивает патогены, процессы нарезки и упаковки представляют собой точки реконтаминации.

Политика «нулевой толерантности» к *Listeria* в США и строгие нормы в Канаде требуют, чтобы любой продукт со сроком годности 40 дней имел надежный барьер против этого патогена. Исследования показывают, что без вмешательства листерия может достичь опасных уровней концентрации за время длительного хранения.9 Это делает технологии, обеспечивающие инактивацию *после упаковки* (post-lethality treatment), такие как HPP, особенно привлекательными, так как они устраняют риск перекрестного загрязнения.

### **2.2 Плесени и дрожжи: Визуальный враг**

Если листерия невидима, то плесень является основным фактором возврата продукции из торговых сетей. Плесени являются облигатными аэробами, требующими кислорода для роста, тогда как некоторые дрожжи могут быть факультативными анаэробами. В условиях «чистой этикетки» удаление сорбатов лишает продукт химической защиты от грибков. Физическое удаление кислорода (вакуум или MAP) эффективно против плесени, но может создать условия для роста анаэробных бактерий или брожения дрожжей, если не сбалансировано правильно.11

### **2.3 Физическая нестабильность: Синерезис и миграция влаги**

Третий, часто недооцениваемый аспект — это физическая стабильность. Чизкейк — это, по сути, белковый гель. Со временем, особенно под воздействием колебаний температуры при транспортировке или циклов заморозки-разморозки, происходит ретроградация крахмалов и сжатие белковой матрицы, что приводит к синерезису — выделению сыворотки.12 В контексте 40-дневного срока годности это проявляется в виде скопления жидкости на дне упаковки («лужа») и размокания песочной основы («soggy crust»).

Проблема «мокрой корки» усугубляется при использовании технологий высокого давления (HPP), которые интенсифицируют миграцию воды. Без решения этой физической проблемы микробиологическая стабильность не имеет смысла, так как продукт потеряет товарный вид. Решение требует применения функциональных ингредиентов нового поколения, таких как цитрусовые волокна, которые обладают высокой водоудерживающей способностью и устойчивостью к заморозке.14

---

## **3. Альтернатива A1: Обработка высоким давлением (HPP)**

Технология High Pressure Processing (HPP) представляет собой наиболее продвинутый нетермический метод консервации, доступный сегодня. Она заключается в воздействии на упакованный продукт изостатическим давлением воды от 300 до 600 МПа (до 87 000 psi) в течение нескольких минут.16 Для Клиента ꆜ HPP предлагает уникальное ценностное предложение: возможность обеспечить безопасность продукта непосредственно в финальной упаковке, полностью исключая риск пост-процессинговой контаминации.

### **3.1 Механизм действия и эффективность против патогенов**

Принцип действия HPP основан на разрушении слабых нековалентных связей (водородных, ионных, гидрофобных) в биологических макромолекулах микроорганизмов. Это приводит к денатурации критически важных ферментов и повреждению клеточных мембран бактерий, дрожжей и плесени, вызывая их гибель.17 При этом ковалентные связи, отвечающие за вкус, аромат и витаминный состав продукта, остаются нетронутыми.

Исследования на матрицах мягких сыров (таких как *Queso Fresco* и *Serra da Estrela*) демонстрируют впечатляющую эффективность HPP. Обработка при 600 МПа в течение 3-5 минут обеспечивает снижение популяции *Listeria monocytogenes* более чем на 5 логарифмических порядков (>5 log reduction), что является золотым стандартом пищевой безопасности.10 Срок годности таких сыров увеличивается с стандартных 7-14 дней до 60-100 дней при хранении в холодильнике.18 Важно отметить, что HPP не уничтожает бактериальные споры (например, *Clostridium botulinum*), поэтому продукт должен оставаться в холодовой цепи, что соответствует модели дистрибуции чизкейков.

В Канаде HPP не требует специального уведомления как «новый продукт питания» (Novel Food), если процесс не вызывает существенных изменений в составе или питательной ценности.19 Однако производитель обязан провести валидационные исследования, подтверждающие, что выбранные параметры давления и времени обеспечивают необходимую инактивацию целевых патогенов в конкретной матрице продукта.

### **3.2 Влияние на текстуру и структуру чизкейка**

Главный технический риск внедрения HPP для чизкейка связан с его влиянием на структуру. Давление в 600 МПа приводит к мгновенному сжатию продукта примерно на 15%. Для продуктов, содержащих включения воздуха (аэрацию), это может быть фатальным.

| Тип чизкейка | Влияние HPP на структуру | Прогноз качества |
| :---- | :---- | :---- |
| **Нью-Йорк (Плотный)** | Минимальное изменение объема. Возможно легкое уплотнение белковой матрицы, делающее текстуру более "творожистой" или плотной. | **Высокий.** HPP подходит идеально. Текстура воспринимается как премиальная и насыщенная. |
| **Суфле / Мусс (Аэрированный)** | Полный коллапс воздушных пузырьков. После декомпрессии структура не восстанавливается. Продукт превращается в плотную массу, теряя объем. | **Низкий.** HPP категорически не рекомендуется без полной переформуляции. |
| **No-Bake (Желатиновый)** | Потенциальное изменение силы геля. Некоторые гидроколлоиды могут ослабевать или менять структуру геля под давлением. | **Средний.** Требует тестирования стабилизационной системы. |

Исследования показывают, что HPP может вызывать легкое пожелтение сырной массы и увеличение твердости.18 Однако в сенсорных тестах сыров *Serra da Estrela*, обработанных давлением, значимых различий во вкусе по сравнению с необработанными образцами выявлено не было, даже после 15 месяцев хранения.22 Это подтверждает, что органолептика сохраняется лучше, чем при любой термической пастеризации.

### **3.3 Проблема миграции влаги и «мокрой корки»**

Специфическая проблема многослойных десертов при HPP — это ускоренная миграция влаги. Во время цикла сжатия вода под давлением стремится выровнять градиент активности воды между влажной начинкой и сухой коркой. Адиабатический нагрев (повышение температуры продукта примерно на 3°C на каждые 100 МПа давления) приводит к кратковременному разогреву продукта на ~18°C при 600 МПа.17 Этот скачок температуры снижает вязкость жиров в корке и увеличивает растворимость сахаров, делая корку гигроскопичной губкой.

Результатом часто становится полная потеря хрусткости основы — так называемый дефект "soggy bottom".23 Для успешного применения HPP в чизкейках требуется **инженерная защита интерфейса**:

1. **Гидрофобный барьер:** Нанесение спреем слоя какао-масла или белого шоколада на выпеченную основу перед заполнением сырной массой. Жировой слой физически блокирует проникновение воды под давлением.25  
2. **Инкапсуляция крошки:** Использование крошки печенья, предварительно покрытой тугоплавким жиром.  
3. **Раздельная упаковка:** Радикальное решение, при котором сырная часть подвергается HPP, а крошка (крамбл) прилагается в отдельном саше в крышке (топпер), что гарантирует 100% хрусткость, но меняет формат потребления.

### **3.4 Экономика толлинга (Tolling) для стартапов**

Для Клиента ꆜ закупка собственного оборудования HPP (стоимостью от 1 до 4 млн долларов США) на начальном этапе нецелесообразна.26 Оптимальной стратегией является использование услуг толлинга (tolling) — контрактной обработки на мощностях сторонних операторов.

* **Стоимость услуг:** Рыночные ставки на толлинг варьируются от **`0.25 до `0.60 CAD за фунт** (`0.50 - `1.20 за кг) в зависимости от объема партии и коэффициента заполнения корзины реактора (filling ratio).26  
* **Логистика:** Толлинг требует транспортировки упакованного продукта к оператору и обратно, что добавляет логистические расходы, но исключает капитальные затраты (CapEx) и расходы на обслуживание сложного оборудования высокого давления.  
* **Доступность:** В Канаде и приграничных зонах США существует развитая сеть толлинговых центров (например, Preshafood, Texas Food Solutions и др.), готовых работать с партиями от нескольких паллет.30 Это позволяет гибко масштабировать производство и проводить рыночные тесты с минимальными рисками.

---

## **4. Альтернатива A2: Модифицированная газовая среда (MAP)**

Если ограничения по текстуре (необходимость аэрации) или логистике делают HPP неприемлемым, технология упаковки в модифицированной газовой среде (Modified Atmosphere Packaging, MAP) становится основным инструментом продления срока годности. MAP замещает воздух в упаковке специально подобранной смесью газов.

### **4.1 Оптимизация газовой смеси для чизкейков**

Выбор газовой смеси для чизкейка критически важен, так как продукт является композитным (молочная начинка + выпечная основа). Использование чистого углекислого газа (`CO_2`), который является основным бактериостатическим агентом, неприемлемо для мягких сыров.

* **Проблема растворимости `CO_2`:** Углекислый газ обладает высокой растворимостью в воде и жирах сырной массы. Если использовать 100% `CO_2`, газ со временем растворится в продукте, создавая вакуум внутри упаковки. Это приведет к коллапсу упаковки (эффект "snug down"), деформации десерта и, что хуже, к закислению вкуса из-за образования угольной кислоты, придающей продукту резкий, газированный привкус.32  
* **Рекомендуемая формула:** Исследования и практика индустрии указывают на оптимальное соотношение: **30% `CO_2` / 70% Азота (`N_2`)**.32  
  * **30% `CO_2`:** Этой концентрации достаточно для подавления роста плесени и аэробных бактерий (напр., *Pseudomonas*), не вызывая при этом сенсорных дефектов или коллапса упаковки.  
  * **70% `N_2`:** Азот выступает в роли инертного наполнителя. Он не растворяется в продукте, поддерживая объем упаковки («подушку»), что защищает деликатную поверхность чизкейка от механических повреждений пленкой. Кроме того, вытеснение кислорода азотом предотвращает окисление жиров (прогоркание масла в основе).37

С применением такой смеси срок хранения чизкейков при температуре 4-8°C может быть увеличен с 7-14 дней (в воздухе) до **4-8 недель**, что покрывает целевой показатель в 40 дней.11

### **4.2 Требования к упаковочным материалам**

Эффективность MAP напрямую зависит от барьерных свойств упаковки. Обычные картонные коробки или простые полиэтиленовые пленки проницаемы для газов, и нужная атмосфера исчезнет за считанные часы.

* **Барьерные пленки:** Необходимо использовать многослойные ламинаты с высоким барьером газопроницаемости (High Barrier Films), содержащие слои EVOH (этиленвиниловый спирт) или PVdC (поливинилиденхлорид). Показатель проницаемости кислорода (OTR) должен быть минимальным (обычно < 10 cc/`m^2`/24ч).  
* **Герметичность:** Качество сварных швов должно быть безупречным. Использование газоанализаторов на линии (on-line gas analysis) обязательно для контроля состава среды в каждой партии.32

### **4.3 Ограничения MAP по сравнению с HPP**

Важно понимать принципиальное отличие: **MAP не убивает патогены**, он лишь замедляет их рост.

* **Риск листерии:** Если продукт был контаминирован *Listeria monocytogenes* в процессе нарезки перед упаковкой, MAP не гарантирует безопасность. Листерия является факультативным анаэробом и может расти (хоть и медленнее) даже при пониженном содержании кислорода. Поэтому MAP требует стерильных условий фасовки («чистые комнаты») и строжайшего санитарного контроля, тогда как HPP обеспечивает страховку в виде финальной стерилизации.  
* **Рост плесени:** Хотя `CO_2` подавляет многие плесени, некоторые психротрофные виды способны развиваться при низких концентрациях кислорода (менее 1%). Поэтому MAP рекомендуется комбинировать с биопрезервантами (натамицином) для создания надежного барьера.

---

## **5. Биопрезервация и Инженерная Рецептура**

Независимо от выбора между HPP и MAP, сама рецептура чизкейка должна быть адаптирована («инженерно укреплена») для выживания в течение 40 дней без потери качества.

### **5.1 Стратегическое использование Натамицина и Низина**

Как было отмечено в разделе 1, изменения в канадском законодательстве от мая 2024 года 5 делают **Натамицин** ключевым элементом стратегии.

* **Применение:** Добавление натамицина (до 10-20 ppm) непосредственно в сырную массу или поверхностное орошение готового продукта создает мощный щит против дрожжей и плесени. Это натуральный метаболит бактерий *Streptomyces natalensis*, который не влияет на бактериальную флору (стартовые культуры) и вкус продукта.  
* **Низин:** Для контроля грамположительных бактерий, включая *Listeria*, целесообразно использование **Низина** (пептид, вырабатываемый *Lactococcus lactis*). Комбинация Низина и Натамицина создает синергетический эффект, закрывая как бактериальные, так и грибковые риски.4  
* **Маркировка:** Эти компоненты должны быть указаны в составе как «Натамицин» и «Низин» (или «Препарат низина»). Хотя это лишает права на клеймо «Без консервантов» (Preservative Free), это позволяет использовать клейма «Натуральные ингредиенты» и избегать пугающих химических названий.

### **5.2 Контроль синерезиса: Цитрусовые волокна**

Синерезис («плачущий» чизкейк) — главная физическая проблема длительного хранения. Традиционные стабилизаторы (камедь рожкового дерева, ксантановая камедь) могут восприниматься как «не чистые».

* **Цитрусовое волокно (Citrus Fiber):** Это инновационный ингредиент «чистой этикетки», получаемый из выжимок цитрусовых. Оно обладает гигантской площадью поверхности и способностью удерживать воду, в разы превышающей собственный вес.14  
* **Механизм:** Цитрусовое волокно связывает свободную воду механически, а не химически, предотвращая её миграцию при температурных колебаниях и циклах заморозки-разморозки. Оно также придает кремовость и может частично заменять жир, улучшая текстуру замороженных десертов после оттаивания.15 Включение 0.5-1.0% цитрусового волокна в рецептуру является обязательным для 40-дневного продукта.

### **5.3 «Чистые» крахмалы и барьеры для корок**

* **Функциональные нативные крахмалы:** Для предотвращения ретроградации (огрубения) текстуры используются крахмалы восковой кукурузы или тапиоки, обработанные физическими методами. Они маркируются просто как «Крахмал» или «Крахмал тапиоки», но обеспечивают стабильность, сравнимую с модифицированными крахмалами.42  
* **Crust Dust:** Техника посыпания дна формы смесью муки и сахара («crust dust») перед выпечкой создает абсорбирующий буфер, который впитывает первые капли влаги, защищая хрусткость корки.45  
* **Жировые барьеры:** Нанесение тонкого слоя растопленного какао-масла на выпеченную основу является наиболее эффективным методом защиты от влаги при длительном хранении, полностью соответствующим концепции clean label.25

---

## **6. Сценарии Интегрированных Решений (Aᚖ⠿)**

На основе анализа предлагается три стратегических сценария для Клиента ꆜ.

### **Сценарий А: «Неуязвимый Плотный» (Фокус на HPP)**

* **Концепция:** Премиальный, плотный чизкейк в стиле «Нью-Йорк».  
* **Процесс:** Выпечка `rightarrow` Охлаждение `rightarrow` Упаковка в скин-пленку (VSP) `rightarrow` Толлинг HPP (600 МПа, 3 мин).  
* **Формуляция:** Усиленная защита корки какао-маслом. Плотная текстура без аэрации. Использование цитрусовых волокон.  
* **Преимущества:** Максимальная безопасность (*Listeria* kill step), реальный срок 60+ дней. Отсутствие необходимости в консервантах (при успешной валидации).  
* **Недостатки:** Высокая себестоимость (из-за толлинга), ограничение по текстуре (только плотные виды).  
* **Маркировка:** Чистая этикетка, возможен клейм «Обработано холодным давлением» (опционально).

### **Сценарий B: «Атмосферный Инженер» (Фокус на MAP + Биопрезервация)**

* **Концепция:** Чизкейк с классической, более воздушной текстурой.  
* **Процесс:** Выпечка `rightarrow` Охлаждение `rightarrow` Нарезка в «чистой комнате» `rightarrow` Флоу-пак с газом (30% `CO_2` / 70% `N_2`) `rightarrow` Холодная дистрибуция.  
* **Формуляция:** Включает **Натамицин** (против плесени) и **Низин** (против листерии).  
* **Преимущества:** Сохранение воздушной текстуры, ниже затраты чем у HPP, стандартная упаковка.  
* **Недостатки:** Нет финальной стерилизации (риск листерии зависит от гигиены), наличие консервантов (натуральных) в составе.  
* **Маркировка:** В составе указаны «Натамицин», «Низин». Нельзя писать «Без консервантов».

### **Сценарий C: «Гибрид Заморозки» (Freeze-Thaw)**

* **Концепция:** Замороженная дистрибуция, дефростация (slacking out) в ритейле с датировкой 40 дней.  
* **Процесс:** Шоковая заморозка сразу после выпечки.  
* **Формуляция:** Высокая доза функциональных крахмалов и цитрусовых волокон для криопротекции.  
* **Преимущества:** Бесконечный срок хранения на складе, гибкость логистики. 40 дней отсчитываются только с момента разморозки в магазине.  
* **Недостатки:** Риск потери текстуры при оттаивании (синерезис), возможна необходимость указания «Ранее заморожен».

---

## **7. Операционная дорожная карта и Рекомендации**

Для реализации проекта Клиенту ꆜ рекомендуется следующий план действий:

1. **Фаза R&D (Формуляция):** Внедрить в базовую рецептуру **цитрусовое волокно** (0.5-0.8%) и **Натамицин** (10 ppm). Это фундамент для любого сценария. Разработать процесс нанесения **барьера из какао-масла** на песочную основу.  
2. **Фаза Выбора Технологии:** Произвести опытную партию. Часть отправить на тест HPP (через толлингового партнера), часть упаковать в MAP.  
   * Если после HPP текстура приемлема (не слишком резиновая) — **выбирать Сценарий А (HPP)** как самый безопасный и инновационный.  
   * Если HPP убивает текстуру — **выбирать Сценарий B (MAP + Биопрезервация)**, но усилить санитарный контроль зоны нарезки.  
3. **Фаза Легализации:** Провести челлендж-тест (Challenge Study) на *Listeria monocytogenes* для подтверждения безопасности на 40-й день. Согласовать макет этикетки с юристами, избегая ловушки «Без консервантов» при использовании био-ингибиторов.

**Итоговый вывод:** Технически задача выполнима. Ключ к успеху лежит не в поиске одного «волшебного ингредиента», а в комбинации физических барьеров (HPP/MAP), биологической защиты (Натамицин) и структурной инженерии матрицы (Волокна/Крахмалы). Использование толлинга HPP позволяет стартапу получить доступ к технологиям крупных игроков без капитальных вложений, создавая продукт премиального качества с истинно чистой этикеткой.

---

### **Таблица 1: Сравнительный анализ технологий сохранения (Aᚖ⠿)**

| Характеристика | HPP (Высокое Давление) | MAP (Газовая Среда) | Биопрезервация (Натамицин/Низин) |
| :---- | :---- | :---- | :---- |
| **Механизм** | Разрушение клеточных мембран давлением (600 МПа). | Ингибирование роста составом газа (`CO_2`). | Метаболическое ингибирование. |
| **Уничтожение патогенов** | **Да** (>5 log *Listeria*). Kill Step. | Нет (Бактериостатик). | Нет (Ингибирование). |
| **Потенциал срока** | **60-120 Дней** | 30-50 Дней | 30-45 Дней (в комбинации с холодом). |
| **Влияние на текстуру** | **Высокое:** Уплотняет, убивает аэрацию. | Низкое: Сохраняет объем при балансе `N_2`. | Отсутствует. |
| **Риск для корки** | **Высокий:** Вгоняет влагу внутрь (Soggy). | Средний: Естественная миграция. | Низкий. |
| **Маркировка (Канада)** | Не требует указания на этикетке. | Не требует указания газа. | **Обязательно указание в составе.** Считается консервантом. |
| **Стоимость** | Высокая (Толлинг + VSP упаковка). | Средняя (Газ + Барьерная пленка). | Низкая (Стоимость ингредиента). |
| **Идеально для** | **Плотных чизкейков (NY Style).** | **Воздушных десертов.** | **Доп. барьер для всех типов.** |

### **Таблица 2: Рекомендуемые газовые смеси для MAP (Сырные десерты)**

| Категория продукта | CO2​ % | N2​ % | O2​ % | Обоснование |
| :---- | :---- | :---- | :---- | :---- |
| **Твердый сыр** | 100% | 0% | 0% | Максимальная защита от плесени; твердая структура не сжимается. |
| **Мягкий сыр / Чизкейк** | **30%** | **70%** | **0%** | **Предотвращает коллапс упаковки; избегает кислого вкуса; давит плесень.** |
| **Аэрированный мусс** | 0% | 100% | 0% | Азот сохраняет объем пузырьков; `CO_2` исключен для защиты вкуса. |
| **Бисквит (Кекс)** | 50% | 50% | 0% | Баланс между защитой от черствения и плесени. |

#### **Works cited**

1. Labelling requirements for dairy products - Canada.ca, accessed November 25, 2025, [https://inspection.canada.ca/en/food-labels/labelling/industry/dairy](https://inspection.canada.ca/en/food-labels/labelling/industry/dairy)  
2. Canadian Food Inspection Agency - Guide to Food Labelling and Advertising - Decision - Milk and Dairy Products, accessed November 25, 2025, [https://epe.lac-bac.gc.ca/100/206/301/cfia-acia/2011-09-21/inspection.gc.ca/english/fssa/labeti/decisions/dailaie.shtml](https://epe.lac-bac.gc.ca/100/206/301/cfia-acia/2011-09-21/inspection.gc.ca/english/fssa/labeti/decisions/dailaie.shtml)  
3. Guide to Food Labelling and Advertising - Food - Canadian Food Inspection Agency, accessed November 25, 2025, [http://www.alimentheque.com/divers/GuideFoodLabellingAdvertising_CFIA_dec2011.pdf](http://www.alimentheque.com/divers/GuideFoodLabellingAdvertising_CFIA_dec2011.pdf)  
4. Canada leads way with “natural” preservatives | Leatherhead - Sagentia, accessed November 25, 2025, [https://sagentia.com/blog/canada-leading-the-way-with-natural-preservatives/](https://sagentia.com/blog/canada-leading-the-way-with-natural-preservatives/)  
5. Modification to the List of permitted preservatives to extend the use of natamycin, accessed November 25, 2025, [https://www.canada.ca/en/health-canada/services/food-nutrition/public-involvement-partnerships/modification-list-permitted-preservatives-extend-use-natamycin.html](https://www.canada.ca/en/health-canada/services/food-nutrition/public-involvement-partnerships/modification-list-permitted-preservatives-extend-use-natamycin.html)  
6. Canada Approves Natamycin as a Preservative for Certain Cheeses - ECHEMI.com, accessed November 25, 2025, [https://www.echemi.com/cms/1915657.html](https://www.echemi.com/cms/1915657.html)  
7. The efficacy and safety of high‐pressure processing of food - PMC - PubMed Central, accessed November 25, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8902661/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8902661/)  
8. Inhibition of Listeria monocytogenes on cheese using lactic acid bacteria as a biocontrol system intervention | National Agricultural Library, accessed November 25, 2025, [https://www.nal.usda.gov/research-tools/food-safety-research-projects/inhibition-listeria-monocytogenes-cheese-using-lactic-acid-bacteria-biocontrol-system-intervention](https://www.nal.usda.gov/research-tools/food-safety-research-projects/inhibition-listeria-monocytogenes-cheese-using-lactic-acid-bacteria-biocontrol-system-intervention)  
9. Bioprotective Strategies to Control Listeria monocytogenes in Food Products and Processing Environments - MDPI, accessed November 25, 2025, [https://www.mdpi.com/1422-0067/26/21/10481](https://www.mdpi.com/1422-0067/26/21/10481)  
10. Clean Label Approaches in Cheese Production: Where Are We? - PMC - NIH, accessed November 25, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11899541/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11899541/)  
11. Bakery Products - Freshline® Guide to MAP — Air Products and Chemicals, Inc., accessed November 25, 2025, [https://microsites.airproducts.com/com/map_selector/results/BakeryProducts.htm](https://microsites.airproducts.com/com/map_selector/results/BakeryProducts.htm)  
12. Why my cake leaks water during the freeze/thaw cycle? Let's talk about syneresis, accessed November 25, 2025, [https://jordibordas.com/en/blog/por-que-mi-pastel-pierde-agua-durante-la-descongelacion-hablemos-de-sineresis/](https://jordibordas.com/en/blog/por-que-mi-pastel-pierde-agua-durante-la-descongelacion-hablemos-de-sineresis/)  
13. Syneresis: All you ever wanted to know – MASTERCLASS - YouTube, accessed November 25, 2025, [https://www.youtube.com/watch?v=Fqd7VqUiYuc](https://www.youtube.com/watch?v=Fqd7VqUiYuc)  
14. Citri-Fi® Citrus Fiber in Freezer Meals & Frozen Foods - Fiberstar, Inc., accessed November 25, 2025, [https://www.fiberstar.net/citrus-fiber-frozen-foods/](https://www.fiberstar.net/citrus-fiber-frozen-foods/)  
15. Top Frequently Asked Questions (FAQ) Citrus Fiber - Fiberstar, Inc., accessed November 25, 2025, [https://www.fiberstar.net/2019/10/14/citrus-fiber-top-frequently-asked-questions-faq/](https://www.fiberstar.net/2019/10/14/citrus-fiber-top-frequently-asked-questions-faq/)  
16. High Pressure Processing (HPP) Advantages - Hiperbaric, accessed November 25, 2025, [https://www.hiperbaric.com/en/hpp-technology/what-is-hpp/](https://www.hiperbaric.com/en/hpp-technology/what-is-hpp/)  
17. Application of High-Pressure-Based Technologies in the Food Industry - Ohioline, accessed November 25, 2025, [https://ohioline.osu.edu/factsheet/fst-fabe-1001](https://ohioline.osu.edu/factsheet/fst-fabe-1001)  
18. Effect of high pressure on fresh cheese shelf-life | Request PDF - ResearchGate, accessed November 25, 2025, [https://www.researchgate.net/publication/251539831_Effect_of_high_pressure_on_fresh_cheese_shelf-life](https://www.researchgate.net/publication/251539831_Effect_of_high_pressure_on_fresh_cheese_shelf-life)  
19. Foods treated with high pressure processing (HPP) - inspection.canada.ca, accessed November 25, 2025, [https://inspection.canada.ca/en/preventive-controls/high-pressure-processing](https://inspection.canada.ca/en/preventive-controls/high-pressure-processing)  
20. Novel Food Information - High Pressure Processing (HPP)-Treated Fruit and Vegetable-Based Juices - Canada.ca, accessed November 25, 2025, [https://www.canada.ca/en/health-canada/services/food-nutrition/genetically-modified-foods-other-novel-foods/approved-products/novel-food-information-high-pressure-processing-treated-fruit-vegetable-based-juices.html](https://www.canada.ca/en/health-canada/services/food-nutrition/genetically-modified-foods-other-novel-foods/approved-products/novel-food-information-high-pressure-processing-treated-fruit-vegetable-based-juices.html)  
21. Effect of high pressure processing on batters and cakes properties - Aarhus University - Pure, accessed November 25, 2025, [https://pure.au.dk/portal/en/publications/effect-of-high-pressure-processing-on-batters-and-cakes-propertie](https://pure.au.dk/portal/en/publications/effect-of-high-pressure-processing-on-batters-and-cakes-propertie)  
22. Effect of High-Pressure Processing on Proteolysis, Texture and Sensorial Attributes of Raw Ewe's Cheeses Throughout Storage - MDPI, accessed November 25, 2025, [https://www.mdpi.com/2076-3417/15/12/6562](https://www.mdpi.com/2076-3417/15/12/6562)  
23. Use of high-pressure processing and low-temperature storage to extend the performance shelf life of 2 types of string cheese - PubMed, accessed November 25, 2025, [https://pubmed.ncbi.nlm.nih.gov/38762114/](https://pubmed.ncbi.nlm.nih.gov/38762114/)  
24. Soggy Cheesecake Crust - Ronnie Fein, accessed November 25, 2025, [https://www.ronniefein.com/recipes/soggy-cheesecake-crust](https://www.ronniefein.com/recipes/soggy-cheesecake-crust)  
25. How to stop cheesecake crust from going soggy in the fridge? : r/Baking - Reddit, accessed November 25, 2025, [https://www.reddit.com/r/Baking/comments/1463ayj/how_to_stop_cheesecake_crust_from_going_soggy_in/](https://www.reddit.com/r/Baking/comments/1463ayj/how_to_stop_cheesecake_crust_from_going_soggy_in/)  
26. High-Pressure Processing Atlantic Blue Crab Meat | North Carolina Sea Grant, accessed November 25, 2025, [https://ncseagrant.ncsu.edu/high-pressure-processing/](https://ncseagrant.ncsu.edu/high-pressure-processing/)  
27. FAQ - Wear Parts and Processing Equipment for the HPP Food Industry, accessed November 25, 2025, [https://hppadvisors.com/faq/](https://hppadvisors.com/faq/)  
28. Juice Manufacturing Contractor, HPP High Pressure Toll Processing - Preshafood, Australia, accessed November 25, 2025, [https://www.preshafood.com.au/hpp-toll-processing](https://www.preshafood.com.au/hpp-toll-processing)  
29. High Pressure Processing Machine (HPP): Costs, Capacity, And ROI For U.S. Brands | 2025, accessed November 25, 2025, [https://agristuff.com/food-industry/high-pressure-processing-machine-hpp-costs-capacity-and-roi-for-u-s-brands/](https://agristuff.com/food-industry/high-pressure-processing-machine-hpp-costs-capacity-and-roi-for-u-s-brands/)  
30. HPP Toll Processing - Hiperbaric, accessed November 25, 2025, [https://www.hiperbaric.com/en/hpp-technology/hpp-tolling/](https://www.hiperbaric.com/en/hpp-technology/hpp-tolling/)  
31. HPP meets the pressure for fresher | ProFood World, accessed November 25, 2025, [https://www.profoodworld.com/home/article/15634956/hpp-meets-the-pressure-for-fresher](https://www.profoodworld.com/home/article/15634956/hpp-meets-the-pressure-for-fresher)  
32. GET A CONSISTENT AND ACCURATE GAS MIX FOR MODIFIED ATMOSPHERE PACKAGING - AMETEK MOCON, accessed November 25, 2025, [https://www.ametekmocon.com/-/media/ametekmocon/mediapreview/dk-market-segment-brochures/master-your-gas-mix-guide.pdf?la=en&revision=54ad7fd8-2611-4a03-9e4e-5498c1d43301?download=1](https://www.ametekmocon.com/-/media/ametekmocon/mediapreview/dk-market-segment-brochures/master-your-gas-mix-guide.pdf?la=en&revision=54ad7fd8-2611-4a03-9e4e-5498c1d43301?download%3D1)  
33. Modified Atmosphere Packaging for Baked Goods and Confectionary - Linde Gas, accessed November 25, 2025, [https://www.linde-gas.com/industries/food-and-beverage/bakery/packaging](https://www.linde-gas.com/industries/food-and-beverage/bakery/packaging)  
34. Recommended MAP Gas Mixtures - Sorbent Systems, accessed November 25, 2025, [https://www.sorbentsystems.com/map-gas-guide.html](https://www.sorbentsystems.com/map-gas-guide.html)  
35. Dairy Products - Modified Atmosphere Packaging (MAP) - Air Products, accessed November 25, 2025, [https://www.airproducts.com/applications/modified-atmosphere-packaging/dairy-products](https://www.airproducts.com/applications/modified-atmosphere-packaging/dairy-products)  
36. Recommended Gas Mixtures for Food and Beverage Packaging - matheson, accessed November 25, 2025, [https://www.mathesongas.com/pdfs/litcenter/Gas-Mixes-for-Food-Bev.pdf](https://www.mathesongas.com/pdfs/litcenter/Gas-Mixes-for-Food-Bev.pdf)  
37. Modified Atmosphere Packaging - Baked Goods - Linde, accessed November 25, 2025, [https://assets.linde.com/-/media/global/usa/linde-us/literature/food-and-beverage/p-40-4609-extendapak-for-baking---x.pdf](https://assets.linde.com/-/media/global/usa/linde-us/literature/food-and-beverage/p-40-4609-extendapak-for-baking---x.pdf)  
38. Your in-depth guide to Modified Atmosphere Packaging - Air Products, accessed November 25, 2025, [https://www.airproducts.me/-/media/files/en/332/332-15-121-en-your-in-depth-guide-to-modified-atmosphere-packaging.pdf](https://www.airproducts.me/-/media/files/en/332/332-15-121-en-your-in-depth-guide-to-modified-atmosphere-packaging.pdf)  
39. Modification to the List of permitted preservatives to extend the use of nisin - Canada.ca, accessed November 25, 2025, [https://www.canada.ca/en/health-canada/services/food-nutrition/public-involvement-partnerships/modification-list-permitted-preservatives-extend-use-nisin.html](https://www.canada.ca/en/health-canada/services/food-nutrition/public-involvement-partnerships/modification-list-permitted-preservatives-extend-use-nisin.html)  
40. Citrus Fiber: A Natural Way to Improve Moisture Retention, Texture & the Freshness of Baked Products, accessed November 25, 2025, [https://foodspecialities.com/industry-news/citrus-fiber-a-natural-way-to-improve-moisture-retention-texture-the-freshness-of-baked-products/](https://foodspecialities.com/industry-news/citrus-fiber-a-natural-way-to-improve-moisture-retention-texture-the-freshness-of-baked-products/)  
41. Optimization of citrus fiber-enriched vegan cream cheese alternative and its influence on chemical, physical, and sensory properties - PubMed, accessed November 25, 2025, [https://pubmed.ncbi.nlm.nih.gov/39139951/](https://pubmed.ncbi.nlm.nih.gov/39139951/)  
42. NOVATION® clean label starch range - Ingredion, accessed November 25, 2025, [https://www.ingredion.com/apac/en-au/ingredients/ingredient-product-families/novation-clean-label-starch-range.html](https://www.ingredion.com/apac/en-au/ingredients/ingredient-product-families/novation-clean-label-starch-range.html)  
43. CLARIA® Functional Clean-Label Starch - Tate & Lyle, accessed November 25, 2025, [https://www.tateandlyle.com/ingredient/claria-functional-clean-label-starch](https://www.tateandlyle.com/ingredient/claria-functional-clean-label-starch)  
44. LABEL-FRIENDLY STARCH OFFERINGS - Gillco Ingredients, accessed November 25, 2025, [https://gillco.com/2019/08/26/label-friendly-starch-offerings/](https://gillco.com/2019/08/26/label-friendly-starch-offerings/)  
45. Things bakers know: “Crust dust” is the secret ingredient to preventing a soggy bottom, accessed November 25, 2025, [https://www.kingarthurbaking.com/blog/2022/11/16/prevent-soggy-pie-bottoms-crust-dust](https://www.kingarthurbaking.com/blog/2022/11/16/prevent-soggy-pie-bottoms-crust-dust)