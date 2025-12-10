# 1.
## 1.1.
`Aᨀ` ≔ (мой ответ `ꆜ`)

## 1.2.
Содержание `Aᨀ`:
~~~markdown
1) The root cause of your problem is not technical, but incorrect business processes of your company: a violation of the «Master/Ledger» architecture caused by employees systematically bypassing Fishbowl (hereafter — `Fᨀ`) by entering data directly into QuickBooks Online (hereafter — `Qᨀ`) or Bill.com (hereafter — `Bᨀ`).
A surgeon-style engagement is absolutely meaningless if your employees immediately return to harmful behavior.
Surgery will eliminate the symptoms, but not the cause.
If the staff's behavior and business processes do not change, the problems will inevitably return.
Success depends on change management, training, and the implementation of strict discipline—this is a long-term process that requires monitoring, not a one-off engagement.
Adults are difficult to retrain.
And it is especially difficult to retrain people working at a low rate of $16.54/hr (the average rate of your past projects on Upwork): such employees usually have neither the ability nor the motivation for change management.
Below, in the answers to your specific questions, I explain the reasons for your problems in detail.

2) «Have you personally worked on Fishbowl → QuickBooks cleanup projects? Describe the LAST one.»
Yes, working for the last 15 years in e-Commerce, I have completed many such projects.
Since Upwork severely limits the maximum text size in a proposal, it will be much more productive if I detail here in the proposal not extraneous projects, but the specific causes of your specific problems — they are obvious to me.

3) Reasons for duplicated COGS (hereafter — `D-COGS†`) specifically in your case
3.1) The main reason (hereafter — `С1ᛡ`)
Your employees most likely manually edit invoices created by `Fᨀ` in `Qᨀ`, replacing the `Fᨀ` service item with the `Qᨀ` inventory item.
In doing so, `Qᨀ` activates its internal logic and creates its own COGS transaction.
This transaction is created in addition to the correct General Journal Entry (hereafter — `GJE`) for COGS, which `Fᨀ` has already sent.
This leads to `D-COGS†`.
3.2) Secondary reasons:
3.2.1) `С2ᛡ`
It is very likely that `Fᨀ` items are incorrectly mapped to the «Inventory» type in `Qᨀ` and/or the inventory tracking function in `Qᨀ` was not disabled.
In this case, `Qᨀ` tries to independently calculate COGS upon sale.
This creates a systemic conflict, forcing `Qᨀ` to generate its own COGS entries parallel to the `GJE` from `Fᨀ`. 
3.2.2) `С3ᛡ`
It is possible that your employees sometimes bypass `Fᨀ` and erroneously create sales transactions (Invoices or Sales Receipts) directly in `Qᨀ`.
3.2.3) `С4ᛡ`
It is possible that your employees manually create `GJE` on the COGS account in `Qᨀ` or incorrectly code vendor bills in `Bᨀ`, posting them directly to COGS.

4) Reasons for negative inventory (hereafter — NI†) specifically in your case:
4.1) The main reason — `С1ᛡ` (point 3.1 above).
`С1ᛡ` causes `Qᨀ` to activate its internal logic and write off an item that, in its opinion, is not in stock (as the receipt was registered via `Fᨀ`), which leads to `NI†`.
4.2) Secondary reasons:
4.2.1) `С5ᛡ`
It is very likely that the dispatch transaction (shipping goods to the customer) is registered in `Fᨀ` before the corresponding receipt transaction (receiving goods from the supplier) is registered.
`С5ᛡ` explains the `NI†` within `Fᨀ`, but it does not explain `D-COGS†` as strongly as `С1ᛡ` does.
4.2.2) `С2ᛡ` (point 3.2.1 above)
`С2ᛡ` creates an environment in which `Qᨀ` tries to independently manage inventory quantities in parallel with `Fᨀ`, which leads to `NI†`.
This is an enabling (environmental) factor, and not a direct trigger event (`С1ᛡ`).
4.2.3) `С6ᛡ`
It is likely that the «Allow Negative Inventory» option is activated in `Fᨀ`.
In my experience, companies often deliberately allow negative inventory to ensure operational flexibility and not to stop shipments due to temporary data entry delays.
Of course, this is erroneous.
However, `С6ᛡ` itself does not create `NI†`, but only allows other causes (specifically, `С5ᛡ`) to lead to `NI†`.

5) «Explain how Bill.com AP bills should map if they relate to landed cost versus non-inventory expenses»
5.1) The correct solution briefly:
5.1.1) Non-inventory expenses must be entered into `Bᨀ` and mapped to the corresponding expense accounts in `Qᨀ`.=
5.1.2) `LC` (hereafter — `LC`) must not be entered into `Bᨀ`.
It is impossible to correctly map them from `Bᨀ`, as they require capitalization and allocation at the SKU level, which only `Fᨀ` can perform.
These bills must be entered exclusively through the `Fᨀ` module «Reconcile» (hereafter — `R`).
5.2) Explanations:
`Fᨀ` and `Bᨀ` have conflicting roles in accounts payable (`AP`) management when integrated with `Qᨀ`.
`LC` must be capitalized — that is, added to the value of the inventory asset (hereafter — `IA`).
`Fᨀ` has the only correct mechanism for this — `R`.
After receiving the goods, at the «Landed Cost step», these costs must be added.
5.3) Your mistake:
When you receive a bill for `LC`, you, following your usual process, enter it directly into `Bᨀ`.
`Bᨀ`, having no connection with `Fᨀ`, sends this bill to `Qᨀ` as a regular expense.
Result:
- The `IA` value on the balance sheet is understated.
- COGS on sale is understated.
- Gross Profit is artificially inflated.
- Operating Expenses (Opex) are overstated.
- Margin analysis at the SKU level becomes impossible.

5.4) The correct solution in detail
5.4.1) Non-inventory expenses are entered into `Bᨀ` and mapped to the corresponding expense accounts in `Qᨀ`.
5.4.2) Inventory expenses and all related `LC` are completely excluded from the entry process in `Bᨀ`.
These bills are entered exclusively manually into `R`.
`Fᨀ` performs `LC` allocation and the 3-Way Match, and then exports the finished bill to `Qᨀ`.
`Bᨀ` can be used at the final stage only for the payment of this bill, which already exists in `Qᨀ`.
5.4.3) This is the only method that guarantees 100% accuracy of COGS accounting and inventory valuation.
`LC` are correctly capitalized and allocated at the SKU level using the native mechanisms of `Fᨀ`.
Correct operation of the 3-Way Match (PO, Receipt, Bill reconciliation) is ensured inside `Fᨀ`.
The accumulation of errors on the «Holding Account» (hereafter — `HC`) is prevented.
This Method corresponds to the architectural requirements of `Fᨀ` as a master system.

6) «What should Fishbowl push into QuickBooks — and what should never be pushed?»
6.1) `Fᨀ` must become the single master system for all inventory operations.
6.2) `Qᨀ` must become a passive financial ledger.
6.3) `Fᨀ` must send to `Qᨀ` all financial consequences of operations (Invoices, Bills, GJE).
6.4) The inventory tracking function in `Qᨀ` must be disabled.
6.5) User access rights in `Qᨀ` must be strictly limited to physically prevent manual entry or editing of transactions on accounts managed by `Fᨀ` (`IA`, COGS, `HC`).
6.6) This is the only method that guarantees long-term data integrity and the accuracy of financial reporting in conditions of low procedural discipline.
It physically eliminates the root causes of critical `D-COGS†` and `NI†` by blocking the possibility of incorrect manual edits in `Qᨀ`.
The method enforces the use of `R`, which ensures the correct capitalization of `LC` and the clearing of the `HC`.
The method corresponds to the best practices for implementing ERP/IMS, minimizing the risks of the human factor.

7) «How do you prevent duplicate COGS entries between Fishbowl and QuickBooks?»
7.1) It is necessary to block the ability to edit or delete transactions created by `Fᨀ` in `Qᨀ`.
This eliminates the possibility of making an error at the user interface level.
This directly neutralizes `С1ᛡ`: the behavioral root cause of `D-COGS†`.
7.2) It is necessary to deactivate Inventory Tracking in `Qᨀ`.
7.3) It is necessary to reconfigure `Fᨀ` to export `GJE` instead of detailed individual transactions.
These `GJE` will periodically (e.g., daily) update only the account balances in `Qᨀ` (COGS, Revenue, `IA`).
Since detailed invoices with items are not present in `Qᨀ`, the object for incorrect editing physically disappears for users.
This prevents `С1ᛡ` by eliminating the object of editing itself.

8) «What’s your approach to resolving negative inventory and timing mismatches?»
8.1) All bills related to inventory and `LC` are processed exclusively through `R`: see point 5.1 above.
`R` synchronizes the moment of physical receiving of goods (Receiving) with the moment of financial recognition of costs and clearing of the transit account `HA`.
This ensures correct and timely recognition of COGS and capitalization of additional expenses, eliminating gaps between operational and financial accounting.
This is the only method to correctly capitalize `LC`, which is critical for accurate margin calculation.
8.2) Point 7.1 above.
This is the only reliable way to stop `D-COGS†` and `NI†`.
8.3) Timeliness and accuracy of data entry.
The key requirement is the immediate registration of goods receipt (Receiving) in `Fᨀ` upon their physical arrival at the warehouse.
This prevents the situation where goods are sold (Shipping) before they are posted in the system.
The method includes the optimization of warehouse processes, e.g., using mobile scanners (Fishbowl Mobile) to speed up registration and minimize data entry errors.
Strict SOPs are implemented, prohibiting the shipment of goods not present in the system, even if they are physically in the warehouse.
This directly eliminates the operational cause of `NI†`, ensuring that the receipt always precedes the shipment.
8.4) Correction of already existing `NI†` and accumulated timing mismatches (hereafter — `TM†`) to restore accounting accuracy.
8.4.1) This requires a full forensic audit of the transaction history using the Fishbowl report «Inventory Event History».
8.4.2) To fix `NI†`, a physical inventory is performed, and discrepancies are corrected in Fishbowl via «Cycle Count» (to correct quantity) or «Add Inventory» (to add missing receipts with the correct cost).
8.4.3) To fix `TM†`, a detailed audit and clearing of `HC` in `Qᨀ` is required, which has accumulated errors due to the incorrect `AP` process.
8.4.4) The final step is creating a clearing `GJE` in `Qᨀ` to bring the `IA` balance in line with `Fᨀ`.
8.4.5) This is the only way to eliminate the `TM†` and restore trust in the system data.
The method allows establishing a clean baseline («Source of Truth»), necessary for further correct operation.
8.4.6) Of course, this quality work completely contradicts your erroneous expectations of a «light touch».
8.5) Continuous monitoring: implementing a mandatory daily procedure for reconciling key data between `Fᨀ` and `Qᨀ`.
It is necessary to daily reconcile the `Fᨀ` report «Asset Valuation By Account» and the `IA` balance in `Qᨀ`.
It is also necessary to monitor negative inventory using specialized reports or dashboards.
Any discrepancies must be immediately investigated and resolved.
Of course, this quality work completely contradicts your erroneous expectations of a «one-time “surgeon-style” engagement».
~~~

# 2.
## 2.1.
`Fⰳ(§p)` ≔ (Пункт `§p` из `Aᨀ`)

## 2.2.
`Fⰳ(§a-§b)` ≔ (Фрагмент `Aᨀ` с пункта `§a` по пункт `§b` включительно)

# 3.
`Fᨀ` ≔ `Fⰳ(1-8)`

# 4. `᛭T`
Проанализируй `Fᨀ`:
1) Есть ли там логические ошибки?
2) Есть ли там фактические ошибки?

# 5. Требования к твоему ответу
## 5.0.
Обязательно используй свой режим «Deep Research».
Твой ответ без режима «Deep Research» — гарантированно неверный.
## 5.1.
Отвечай на русском языке.
## 5.2.
Мой вопрос не пересказывай.
## 5.3.
Уже сформулированную мной информацию не пересказывай.
## 5.4.
Писать свою версию `Fᨀ` не нужно: просто укажи свои замечания по пунктам.
## 5.5.
До и после списка замечаний ничего не пиши.
## 5.6.
Нумерация замечаний должна быть сквозной.
## 5.7.
Для каждого своего замечания указывай свою степень уверенности в нём по шкале от 0 до 100:
- 0 означает, что твоё замечание безосновательно (ошибочно).
- 100 означает, что ты полностью уверен в правоте своего замечания.

# 6. К чему не надо придираться
## 6.1.
Если большая часть `Fᨀ` — на русском языке, то не придирайся к смешению в `Fᨀ` русского и английского языков.
Это смешение — временное и будет устранено позже.

## 6.2.
Не придирайся, что в моей отнологии (`O.md`) я использую обозначения, отличные от письма клиенту.
Онтология предназначения для моего внутреннего анализа, а не для клиента.
Клиент не видит онтологию и он не знает о моих внутренних обозначениях.