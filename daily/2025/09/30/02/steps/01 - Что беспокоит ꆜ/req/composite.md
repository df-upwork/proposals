# 1. `B.md`
~~~~~~markdown
# 1. `᛭MDi`
## 1.1.
Каждый отдельный (произвольный, неопределённый) документ в формате Markdown, прикреплённый мной к этому запросу, буду обозначать `᛭Di`.
## 1.2.
Имя файла `᛭Di` всегда имеет расширение `.md`.
## 1.3.
Множество всех `᛭Di` буду обозначать `᛭Ds`.

# 2. `L.md`
### 2.1.
`L.md` ∈ `᛭Ds`.
## 2.2.
`L.md` описывает полуформальный язык: `᛭L`.
## 2.3.
Большинство `᛭Di` написаны на `᛭L`.
## 2.4.
Множество всех `᛭Di`, написанных на `᛭L`, буду обозначать `᛭DLs`.
Таким образом, `᛭DLs` ⊆ `᛭Ds`. 

# 3. `O.md`
## 3.1.
`O.md` ∈ `᛭DLs`
## 3.2.
`O.md` описывает некую **онтологию** (`᛭O`)  — модель предметной области, в которой тебе предстоит решать задачу.
«An **ontology** encompasses a representation, formal naming, and definitions of the categories, properties, and relations between the concepts, data, or entities»: https://en.wikipedia.org/wiki/Ontology_(information_science)

# 4. `T.md`
## 4.1.
`T.md` ∈ `᛭DLs`
## 4.2.
`T.md` описывает задачу (`᛭T`), которую ты должен решить.

# 5. Порядок твоих действий
Действуй пошагово:
## 5.1.
Сначала внимательно и полностью прочитай `L.md`.
В точности запомни его содержание.

## 5.2.
Затем внимательно и полностью прочитай `O.md`. 
В точности запомни его содержание.

## 5.3.
Затем внимательно и полностью прочитай `T.md`. 
Выполни `᛭T`.

~~~~~~

# 2. `L.md`
~~~~~~markdown
# 1. `≔`
## 1.1.
- `≔` — это бинарный оператор.
## 1.2.
`A ≔ B` means that `A` **denotes** `B`.
## 1.3.
Я использую `≔` для сокращения записи.
В выражении `A ≔ B` `B` обычно — это длинный текст, а `A` — это более короткое обозначение.  
## 1.4.
~~~code
A ≔
```
B
```
~~~
равнозначно `A ≔ B` и используется, когда `B` — многострочный текст.

# 2. `→`
~~~code
A → B
~~~
denotes a material conditional (https://en.wikipedia.org/wiki/Material_conditional)

# 3. `⊢`
~~~code
A ⊢ B
~~~
denotes a logical consequence (https://en.wikipedia.org/wiki/Logical_consequence)

# 4. `⊤`
## 4.1.
~~~code
⊤ B
~~~
means that `B` is true (is a fact).

## 4.2.
~~~code
⊤⟦Rs⟧ B
~~~
means:
```
(⊤ `B`) AND (`Rs` are the reasons why `B` is true)
```

## 4.3.
~~~code
A ≔⊤
```
B
```
~~~
means:
```code
(`A` ≔ `B`) AND (⊤ `B`).
```

## 4.4.
~~~code
A ≔⊤⟦Rs⟧
```
B
```
~~~
means:
```code
(`A` ≔ `B`) AND (⊤⟦Rs⟧ B).
```

# 5. `≔!`
## 5.1.
~~~code
A ≔! B
~~~
means:
```code
(`A` ≔⊤ `B`) AND (`B` is surprising).
```

## 5.2.
~~~code
A ≔!⟦Rs⟧ B
~~~
means:
```code
(`A` ≔⊤⟦Rs⟧ `B`) AND (`B` is surprising).
```

# 6. `?`
## 6.1.
~~~code
? B
~~~
means that `B` is a hypothesis.

## 6.2.
~~~code
?⟦Rs⟧ B
~~~
means:
```code
(? `B`) AND (`Rs` are the reasons for the hypothesis)
```

## 6.3.
~~~code
A ≔? B
~~~
means:
```code
(? `B`) AND (`A` ≔ `B`)
```

## 6.4.
~~~code
A ≔?⟦Rs⟧ B
~~~
means:
```code
(?⟦Rs⟧ `B`) AND (`A` ≔ `B`)
```

# 7.
## 7.1.
~~~code
A : S ≔ B
~~~
means:
```code
(`A` ≔ `B`) AND (`A` ∈ `S`).
```

## 7.2.
~~~code
A : S
~~~
means:
```code
`A` : `S` ≔ (an arbitrary element of `S`)
```

# 8. `⠿{…}`
## 8.1. `⠿{I₁, I₂, …, Iₙ}`
`⠿{I₁, I₂, …, Iₙ}` обозначает множество, заданное точным перечислением всех его элементов: {`I₁`, `I₂`, …, `Iₙ`}.

## 8.2. `⠿{I₁-Iₙ}` 
`⠿{I₁-Iₙ}` обозначает множество, заданное интервалом (диапазоном) его значений.
Это множество, в числе прочего, включает границы указанного интервала: `I₁` и `Iₙ`.

# 9. `⠿~`
## 9.1. `⠿~ (D)`
`⠿~ (D)` обозначает множество, заданное неформальным (словесным) описанием его элементов (`D`).

## 9.2.
~~~code
⠿~
```
D
```	
~~~
равнозначно `⠿~ (D)` и используется, когда `D` — многострочный текст.

## 9.3.
~~~code
S ≔ ⠿~ (D)
```yaml
- I₁
- I₂
- …
- Iₙ
```	
~~~
означает: (`S ≔ ⠿~ (D)`) AND (⠿{`I₁`, `I₂`, …, `Iₙ`} ⊆ `S`) .

# 10.
## 10.1.
`᛭DLi` : `᛭DLs`
## 10.2.
### 10.2.1.
`᛭Dc` — это обозначение `᛭DLi` самого себя.
Другими словами, если текст `᛭DLi` содержит упоминание `᛭Dс` — это значит, что `᛭Di` упоминает сам себя. 
### 10.2.2.
Например: если имя файла `᛭Di` — `sample.md`, и текст `sample.md` использует обозначение `᛭Dc`, это значит, что `᛭Dc` в данном случае обозначает документ `sample.md`.  

# 11. `§`
## 11.1.
~~~code
§P
~~~
означает ссылку на пункт `P` `᛭Dc`.
Например, §8.2.2 означает ссылку на пункт 8.2.2 `᛭Dc`.
## 11.2.
~~~code
`᛭DLi`::§P
~~~
означает ссылку на пункт `P` `᛭DLi`.
  
# 12. Local Definitions
## 12.1.
~~~code
A[§P] ≔ B
~~~
Означает:
- Для понятия `B` я **временно**, **только в рамках** §`P`, использую обозначение `A`.
- Вне §`P` это правило не применяется: в частности, если до §`P` обозначение `A` имело другой смысл, то после §`P` обозначение `A` снова будет иметь этот смысл.
- По сути, `A[§P] ≔ B` объявляет **локальную переменную** `A` с **областью действия** §`P`.
- В отличие от `A[§P] ≔ B`, `A ≔ B` объявляет **глобальную переменную** `A`.

## 12.2.
~~~code
A[§P₁, §P₂, …, §Pₙ] ≔ B
~~~
Означает, что обозначение `A` имеет значение `B` в контексте ⠿{§`P₁`, §`P₂`, …, §`Pₙ`}.
По сути, это правило аналогично §12.1, но область действия локальной переменной `A` ограничивается не одним пунктом, а множеством пунктов.

## 12.3.
~~~code
A[§P₁-§Pₙ] ≔ B
~~~
Означает, что обозначение `A` имеет значение `B` в контексте ⠿{§P₁-§Pₙ}.
По сути, это правило аналогично §12.1 и §12.2.

# 13. `≔†`
~~~code
A ≔† B
~~~
means:
```code
(`A` ≔ `B`) AND (`B` is a **problem** to me).
```

# 14. `▶`
```code
▶ A
```
означает, что в описываемой мной ситуации я использую `A`.

# 15. `ⰳ`
```code
Aⰳ(a, b, …) ≔ B
```
means:
- `A` — это функция с параметрами ⠿{`a`, `b`, …}.
- `B` — семантика `A`

# 16. `߷`
## 16.1.
```
߷⠿ ≔ ⠿~ (приложеные к этому запросу файлы)
```

## 16.2.
```code
߷ⰳ(ID, Name) ≔ Desc
```
means:
```code
- `ID` : `߷⠿` ≔ `Desc`
- `Name` — имя файла
```


~~~~~~

# 3. `O.md`
~~~~~~markdown
# 0.
Сегодня 2025-09-30.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021973080903566247101

## 2.2. Title
Magento Website Update: Theme & Version Upgrade

## 2.3. Description
`PD` ≔ 
```text
We are seeking an experienced Magento developer to update our existing Magento website with a new theme and ensure it runs on the latest stable version of Magento. 
Additionally, we require the implementation of a one-page checkout (fire checkout) feature to enhance user experience. 
The ideal candidate should have a strong understanding of Magento architecture and customization.  
I would like to utilize the Breeze Business Theme.  (https://swissuplabs.com/blog/get-ready-to-level-up-with-the-new-argento-breeze-business-theme/) 
The current website has only 30 products and is running on magento 2.4.5 and has 7 extensions installed on it currently:
- Amasty Product Feed M2
- Mageplaza SMTP Email
- MagePrince Product Attachments
- BSS Commerce HTML Sitemap Extension
- Xtento Customer Carriers Trackers
- MageMart Order Editor/Grid Manager M2
- Paradox Labs M2 Authorize.net CIM Payment Module
  
The goal of this project is to give the website a face lift with better graphic design images and banners, make it more user friendly, more professional looking, and have a better order flow/checkout.  
We will select a candidate within the next 10 days to begin the project.
```

# 5. Информация о `ꆜ`
## 5.1. Местоположение

United States
West Chester

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Mar 3, 2012
### 5.3.2. Hire rate (%)
70
### 5.3.3. Количество опубликованных проектов (jobs posted)
40 
### 5.3.4. Total spent (USD)
47K
### 5.3.5. Количество оплаченных часов в почасовых проектах
1158 
### 5.3.6. Средняя почасовая ставка (USD)
12.73 

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

## 6.1.1. URL
https://www.upwork.com/jobs/~01099a26f0b53e8311

## 6.1.2. Title
SEO On Page Specialist for Magento 2 with Hyva Them

## 6.1.3. Description
`P1D` ≔ 
```text
I own and manage a Magento 2.4.5 website that has the Hyva theme as the frontend.  
This new site design went live about a year ago.  
Since then my organic rankings have suffered. 
I do not currently use any SEO extension in my magento backend to optimize the SEO.  
I have just recently signed up with Semrush and have found many on page issue with the site.  
I am looking for a Magento 2 on page SEO expert to optimize the settings.  
The issues that Semrush found are the following:

## Errors:
- 12 duplicate title tags
- 10 pages with duplicate content
- 8 pages with duplicate meta descriptions
- 4 incorrect pages found in the sitemap.xml

## Warnings:
- 207 URLs with a temporary redirect
- 68 pages have low text-HTML ratio
- 25 images don't have alt attributes
- 17 pages have too much text within the title tags
- 11 pages don't have meta descriptions

## Notices:
- 416 URLs with a permanent redirect
- 74 orphaned pages in Google Analytics
- 62 links have non-descriptive anchor text
- 29 orphaned pages in sitemaps
- 18 pages have only one incoming internal link
- 12 pages are blocked from crawling
- 10 links have no anchor text
- 2 subdomains don't support HSTS
- 1 page has more than one h1 tag
- 10 pages don't have an h1 heading
- 4 external links are broken
- 2 links on HTTPS pages lead to HTTP page
- 1 page has an underscore in the URL

Please respond with your relevant experience in fixing magento 2 on page seo issues such as these.
Thank you for your time and interest.
Ben
```

## 6.1.4. Publication Date
last year

## 6.1.5. Payment Terms (USD) 
### 6.1.5.1. Expected by `ꆜ`  
500 (Fixed Price)
### 6.1.5.2. Actual
18515

## 6.1.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.1.7. Duration (expected by `ꆜ`)
Not specified

## 6.1.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.2. `P2⁎`

## 6.2.1. URL
https://www.upwork.com/jobs/~01d78afe347375724a

## 6.2.3. Title
Magento Upgrade from 2.3.3 to 2.4.5 Plus Extension Updates

## 6.2.3. Description
`P2D` ≔ 
```text
I have a live site running Magento 2.3.3 and the Porto theme on Nexcess Hosting.  
It is a simple site with only 30 products.  
This job is very straightforward. 
I have already purchased the needed additional Nexcess Hosting package that has an updated server (PHP) for Magento 2.4.5.  
This job requires a Magento expert to do the following:
- Update the live site from Magento 2.3.3 to Magento 2.4.5 (on new server)
- Update and install patches for the Porto theme to the latest version
- Update/Install 6 third party extensions

I would expect the developer to use a staging site to test the upgrade before doing it on the live site.  We need to retain all customers/orders/transactions.  

Please let me know your relevant experience with projects like this, the expected timeframe, and your best price to complete this job.  
Given that the existing live site, the staging site, and the new server location are all located in my single Nexcess Hosting account the migration should be relatively simple.
Thank you for your interest.
Regards,
Ben
```

## 6.2.4. Publication Date
2 years ago

## 6.2.5. Payment Terms  (USD) 
### 6.2.5.1. Expected by `ꆜ`
500 (Fixed Price)
### 6.2.5.2. Actual 
460

## 6.2.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.2.7. Duration (expected by `ꆜ`)
Not specified

## 6.2.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.3. `P3⁎`

## 6.3.1. URL
https://www.upwork.com/jobs/~0166809038a1d466f9

## 6.3.2. Title
Install New Magento 2 Theme and Upgrade Magento from 2.3.3 to 2.4.3

## 6.3.3. Description
`P3D` ≔ 
```text
I currently have a live magento 2 multidomain store (3 domains).  

These domains are currently all using the ultimo theme (99% the same).  
I am getting a lot of Google Pagespeed issues with the current setup. 
I am hosting the sites at Nexcess Magento 2 Cloud Hosting which has an easy testing environment for the development site.

I would like to transition over to one of the SwissUpLabs Argento themes because of how fast it is with google pagespeed using the Breeze module. 
There are several backend extensions that I must use for this business.

- (Extension is Magemart "AheadGroups" Order Editor/Advanced Grid Manager M2)
- (Extension is Mirasvit M2 Follow Up Email)
- (Extension is Paradox Labs M2 Authorize.net CIM Payment Module)
- (Extension is Fooman Magento 2 PDF Customizer)

I am looking for find a Magento 2 developer that has worked with the Argento theme before, is well versed in quality graphic design and SEO best practices for Magento 2, and is experienced with how to upgrade a site from Magento 2.3.3 to 2.4.3.  
It should be noted that I am not looking to really redesign the site.  
The general content will remain the same.  
I would like to give it a facelift (especially on the homepage) where we can, but 95% of the content will be copy and pasted over to the new themed site.

If you look at the google pagespeed scores for mobile and desktop on the following theme: https://breeze.swissupdemo.com/breeze_blank/

This is kind of performance I am looking for (97M and 100D).
My site is simple with only 8 products.  
CMS pages: Homepage, Product Pages, About Us, Rates, Contact Us, Guarantee, FAQ, BLOG, T&C.

I need to convey professionalism and simplicity while most focused on SPEED, SEO, and easy future upgrades.

If you want the job and think it is a good fit for your skill set, please send me a message with why this job is a good fit for you and why you think you will be able to deliver.  
I will respond to thoughtful messages with the current primary domain for this project.

Best Regards,
Ben
```

## 6.3.4. Publication Date
4 years ago

## 6.3.5. Payment Terms (USD) 
### 6.3.5.1. Expected by `ꆜ`  
4000 (Fixed Price)
### 6.3.5.2. Actual
23 hrs @ $100.00/hr
Billed: $2,333.33

## 6.3.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.3.7. Duration (expected by `ꆜ`)
Not specified

## 6.3.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.4. `P4⁎`

## 6.4.1. URL
https://www.upwork.com/jobs/~0109439fea38cbf252

## 6.4.2. Title
Upgrade Site from Magento 1.9 to 2.3.2. Freshen Design and Transfer All Data.

## 6.4.3. Description
`P4D` ≔ 
```text
Current live Site:  www.metalshipper.com

This site is currently hosted on Nexcess.net Shared Hosting and is running on Magento 1.9.3.1.  
This job is to upgrade the site to Magento 2.3.2 and in the process freshen the design using the Ultimo Magento 2 theme.  
I want the site to look cleaner, more professional, run faster, and be easier to navigate.  
Also in the process of the update we need to transfer all the product, order, and customer data.
The site uses the stock magento admin with no critical extensions. 
We will need to install a free BLOG extension of some kind.  
We also need to make sure to do all the needed SEO work in terms of url's, google shopping feed, etc....
```

## 6.4.4. Publication Date
6 years ago

## 6.4.5. Payment Terms (USD) 
### 6.4.5.1. Expected by `ꆜ`  
2000 (Fixed Price)
### 6.4.5.2. Actual
3275

## 6.4.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.4.7. Duration (expected by `ꆜ`)
Not specified

## 6.4.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.5. `P5⁎`

## 6.5.1. URL
https://www.upwork.com/jobs/~0116f3fde70b8327ab

## 6.5.2. Title
Magento Multi Site - Need Theme Structure / Products / Static Blocks / CSS / Pages Migrated to 2.3

## 6.5.3. Description
`P5D` ≔ 
```text
Currently have a 3 site Magento Community 1.9.3.1 Multi Site hosted on Nexcess.net:  
- https://www.urgentpassport.com
- www.uspassportservice.com
- www.hcexp.com 

I need to migrate this multi site to Magento 2.3.  
It is critical that the migration be done in a way that sets up child sub themes in the new file structure to allow for easy updating as magento updates come out (see pages 70 - 75 of attached user guide).  
The primary theme I will be using for the new sites will be "Ultimo".  
I want to keep the code as clean and fast as possible while allowing for 3 distinct looking sites that can be easily updated to new magento versions as they come out.  
For this job I need the following:
1) Create the multi site structure on the development server ( already have the dev account setup)
2) Create the correct file structure and magento settings for the 3 custom child themes of Ultimo Theme
3) Transfer the needed CSS, CMS Page, and static block content from 3 current sites to 3 new sites (it is critical that the needed content items render properly on the new setup so testing and resolving any CSS or JS conflicts will be needed)
4) Transfer the product information for the 3 current sites to the 3 new sites
5) Install new versions of 4 needed extensions that are compatible with magento 2.3

This will then allow me to go into the admin and finish customizing the multi site content.

I am looking for a magento 2 expert that has had direct experience with the Ultimo Theme and is very comfortable creating the correct directory structure and transferring the old site elements to the new site.  
Please explain why you would be a good fit for this job.  I will also need more work done in the future relating to Magento 2.

The the required extensions needed are the following:

1) https://marketplace.magento.com/aheadgroups-ordereditor.html (M2)
2) https://marketplace.magento.com/aheadgroups-authorizenetcim.html (M2)
3) https://www.micosolutions.com/product-ordered-emails (Shown as M1 on site but I have spoken to company and they have the updated software for M2 extension that is working)
4) Basic Blog and Testimonial extension to allow for migration of existing blog and testimonial content.

MILESTONE PAYMENTS FOR COMPLETED WORK:

1) design of all 3 sites completed as JPG screenshots and approved by client $500.00
2) 1st site launched on clients' test server on Magento 2.3 with new Theme $1,500.00
3) 2nd and 3rd websites launched on clients' test server on Magento 2   $800.00
4) final tweaks, SEO redirects - All 3 sites working 100% fully byy Apr 30, 2019 $400.00
```

## 6.5.4. Publication Date
6 years ago

## 6.5.5. Payment Terms (USD) 
### 6.5.5.1. Expected by `ꆜ`  
3000 (Fixed Price)
### 6.5.5.2. Actual
4950

## 6.5.6. Contractor Level (expected by `ꆜ`)
Intermediate

## 6.5.7. Duration (expected by `ꆜ`)
Not specified

## 6.5.8. Contractor Location (expected by `ꆜ`)
Not specified

# 7.
`M` ≔ Magento

# 8.
## 8.1.
`W1⁎` ≔ (https://metalshipper.com)

## 8.2.
⊤ (`W1⁎` работает на `M` 2.4: https://www.metalshipper.com/magento_version)

## 8.3.
⊤ (`W1⁎` использует design theme Ultimo (`Infortis/ultimo_child`))


# 9.
## 9.1.
`W1⁎` ≔ (https://urgentpassport.com)

## 9.2.
⊤ (`W2⁎` работает на `M` 2.4: https://www.urgentpassport.com/magento_version)

## 9.3.
⊤ (`W1⁎` использует design theme `Paspartoo/urgentpassport`)

# 10.
## 10.1.
`P-W1⠿` ≔⠿ {`P⁎`, `P1⁎`, `P2⁎`, `P4⁎`}

## 10.2.
⊤ (`P-W1⠿` related to `W1⁎`)

# 11.
## 11.1.
`P-W2⠿` ≔⠿ {`P3⁎`, `P5⁎`}

## 11.2.
⊤ (`P-W2⠿` related to `W2⁎`)



 
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1. `᛭T`
1) Выяви все проблемы, которые беспокоят `ꆜ` в `P⁎`.
2) Проанализируй обоснованность каждой из выявленных проблем.

# 2. Источники информации
В своём анализе используй авторитетные источники информации на английском языке.

# 3. Требования к ответу
Свой ответ дай на русском языке. 
~~~~~~