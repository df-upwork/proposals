# 0.
Сегодня 2025-09-18.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021968450535897299150

## 2.2. Title
Data Scraping Expert Needed — Export Orders to CSV

## 2.3. Description
`PD` ≔ 
```text
I need a skilled scraper to extract historical order data from an old Magento backend. The goal is a clean, well-formatted CSV with the exact fields I’ll provide (video + list included).

What matters most:

Strong scraping / automation skills (Python, tools, or custom scripts)
Short Video Explanation: https://somup.com/cTQb3NPf9j

Ability to handle login, pagination, and large datasets

Clean data formatting and consistency

Magento knowledge is a plus but not required — as long as you can scrape it reliably.

Deliverable: one CSV with all orders in the requested column structure.
Please share your scraping approach, timeline, and cost in your proposal.
```

## 2.4. Tags
Data Scraping
Scrapy
Microsoft Excel
Data Extraction

# 3.
## 3.1.
`I⠿` ≔ ⠿~ (Файлы, которые `ꆜ` приложил к `P⁎`)

## 3.2.
⊤ (`I⠿` ⊆ `߷⠿`)

## 3.3.
```code
Iⰳ(ID, Name) ≔ Desc
```
means: 
```code
- ID : `I⠿`  
- ߷ⰳ(ID, Name) ≔ Desc
```

# 4.
## 4.1.
Iⰳ(`V߷`, `.mp4`) ≔ (`ꆜ` приводит его в `PD` как `https://somup.com/cTQb3NPf9j`)


# 5. Информация о `ꆜ`
## 5.1. Местоположение

United States
Guttenberg

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Nov 3, 2016
### 5.3.2. Hire rate (%)
54
### 5.3.3. Количество опубликованных проектов (jobs posted)
97 
### 5.3.4. Total spent (USD)
$97K
### 5.3.5. Количество оплаченных часов в почасовых проектах
456
### 5.3.6. Средняя почасовая ставка (USD)
20.28

# 6.
## 6.1.
`W᛭` ≔ (Веб-сайт, о которой `ꆜ` говорит в `PD` («old Magento backend»))
## 6.2.
`W᛭` работает на Magento 1.9.3.2.


# 6.
`T⁎` ≔ 
```
Задача, о которой `ꆜ` говорит в `PD`:
~~~
extract historical order data 
~~~
```

# 7. Содержание `V߷`
## 7.1. Содержание `V߷` (Язык оригинала: Английский)
 Okay, so what I need to do is basically scrap my old Magento back end with the data related to each order.
Okay, so I will tell you specifically what I need, like I need the customization notes, the customer information, billing, shipping, the item information, customer notes. 
 And then here I'll need, this pertaining to the order, 3D information if there is, diamonds information if there is, casting information if there is, and the employee comments information if there is. 
 Very simple like that. 
 The only challenge is that we have a lot of orders and it's going to need to go order by order and use Python or whatever it is to scrap it. 
 This is again, not something that there's a change in HTML or anything. 
 It's something my personal domain where I have my old back end that I just need to basically export all the data into CSV. 
 I prefer to do it this method because there's too many tables and too much complication with the database.
 So I think that this would be the easiest possible way to do it. 
 Okay? 
 So if you have experience, let me know, give me some examples maybe of stuff that you did. 
 And that's pretty much it.

# 7.2. Описание интерфейсов

The video displays the Magento Admin Panel. The version is identified in the footer as «Magento ver. 1.9.3.2». The demonstration takes place on the Order View page for «Order # 90921».

[00:00:00 - 00:00:10] Introduction and Overview
Screen: The video begins showing the middle section of the Order View page. Visible information blocks include «Payment Information» (showing "Pay By Phone"), «Shipping & Handling Information» (showing "Free Shipping"), «Order Special Note», «Edit Custom Shipping», «Delivery Date Information», and the «Items Ordered» grid. The items in the grid have a customized green background.
Action: The user scrolls up to the top of the page. This reveals the main navigation menu, which includes standard Magento items like «Sales», «Catalog», «Customers», and custom additions like «PrimeStyle Modules» and «Employee Message». At, the cursor briefly hovers over «Customers», displaying a dropdown menu.
Speech: The speaker states the objective: to "scrap my old Magento back end with the data related to each order".

[00:00:10 - 00:00:25] Identifying Data on the Information Tab
Screen: The user is viewing the main content area of the order (the «Information» tab).
Speech: The speaker enumerates specific data requirements: "customization notes, the customer information, billing, shipping, the item information, customer notes".
Action and Details: The user highlights these areas with the cursor.
1.  «Customization Notes»: The cursor highlights this block, which contains the text: "Shopify Order 120308, Added by: Jenny, On: 09-17-2025 09:19:44".
2.  Customer Information, Billing, Shipping: The cursor moves over the «Account Information» block (showing Customer Name: Armand Sabile, Customer Id: 36604), and the «Billing Address (print address)» and «Shipping Address (print address)» blocks. The addresses are located in North Highlands, California.
3.  Item Information: The user scrolls down to the «Items Ordered» grid. It displays one «Customize Product» with details including options («Choose Ring Size»: 7) and a «Comment» field with specifications and a URL. The «Subtotal» is $2,146.50.
4.  Customer Notes: The user scrolls down to the «Comments History» block. A section titled «Customer Note:» shows a history entry including «Employee Name» (Jeny123) and «Comment» (Order Placed From Admin panel). The «Order Status» column shows "DRDER INFECT".

[00:00:25 - 00:00:40] Identifying Data on Custom Tabs
Action: The user scrolls to the footer, then navigates to the Order View Navigation pane on the left. The user clicks through several tabs, which appear to be custom extensions.
Speech: The speaker lists additional data requirements, contingent on existence: "3D information..., diamonds information..., casting information..., and the employee comments information".

1.  3D Information: The user clicks a tab. The content area updates briefly before the next tab loads.
2.  Diamonds Information («Order Inventory»): The user opens the «Order Inventory» section. The grid is empty. Columns include: «RDEL», «Date Added», «Type», «Product», «Parcel ID», «CT Weight», «Stones», «Price Per CT», «Total Price», «MM», «Comments».
3.  Casting Information («Casting Receipt Order»): The user opens the «Casting Receipt Order» section. The grid is empty. Columns include: «#», «Supplier», «Date Added», «Invoice Number», «Metal Type», «Model Number», «Qty», «Weight», «Price». A checkbox «Wax Approved» is visible.
4.  Employee Comments Information («Employee Comments»): The user opens the «Employee Comments (View All)» section. The section is empty.

[00:00:40 - 00:01:31] Methodology Discussion
Screen: The view remains primarily on the «Employee Comments (View All)» section.
Action: The cursor moves along the left navigation pane. At, the cursor hovers over the top navigation menu item «Employee Message», revealing a dropdown menu (e.g., «My Messages»).
Speech: The speaker discusses the project approach. They mention the high volume of orders requires automated processing "order by order" using "Python". They confirm the HTML is static and the goal is to "export all the data into CSV". They justify this approach by stating the database is too complicated. The speaker concludes by requesting experience and examples.

# 8.
`Q1` ≔ (Почему `ꆜ` не рассматривает способ решения `T⁎` посредством стандартного экспорта данных из Magento?)
 