1) The root cause of your problems is not technical, but procedural: it stems from incorrect business processes within your company.
Specifically, employees systematically violate the «Master/Ledger» architecture by bypassing Fishbowl (hereafter — `Fᨀ`) and entering data directly into QuickBooks Online (hereafter — `Qᨀ`) or Bill.com (hereafter — `Bᨀ`).
The benefits of a «surgeon-style» engagement will be short-lived if your employees return to counterproductive practices.
Surgery will eliminate the symptoms, but not the cause.
If the staff's behavior and business processes do not change, the problems will inevitably return.
Success depends on change management, training, and the implementation of strict discipline.
Sustaining these improvements is not a one-off event, but a long-term process that requires continuous monitoring.
Changing established organizational behaviors and workflows is inherently challenging.
It is especially difficult to drive change among staff working at a low rate of $16.54/hr (the average rate of your past projects on Upwork): such employees usually lack the motivation or incentive for change management.
Below, in the answers to your specific questions, I explain the reasons for your problems in detail.

2) «Have you personally worked on Fishbowl → QuickBooks cleanup projects? Describe the LAST one.»
Yes, I have completed many such projects during my 17 years of experience in e-Commerce.
Since Upwork severely limits the maximum text size in a proposal, it will be much more productive if I focus this proposal not on past projects, but on the specific causes of your problems — they are obvious to me.

3) Reasons for duplicated COGS (hereafter — `D-COGS†`) specifically in your case
3.1) The main reason (hereafter — `С1ᛡ`)
Most likely, your employees manually edit invoices created by `Fᨀ` in `Qᨀ`, replacing the `Fᨀ` service item with the `Qᨀ` inventory item.
Consequently, `Qᨀ` activates its internal logic and creates its own COGS transaction.
This transaction duplicates the correct General Journal Entry (hereafter — `GJE`) for COGS, which `Fᨀ` has already sent.
This leads to `D-COGS†`.
3.2) Secondary reasons:
3.2.1) `С2ᛡ`
It is very likely that `Fᨀ` items are incorrectly mapped to the «Inventory» type in `Qᨀ` and/or the inventory tracking function in `Qᨀ` is enabled.
In this case, `Qᨀ` independently calculates COGS upon sale.
This creates a systemic conflict.
This configuration error either forces `Qᨀ` to automatically generate its own COGS entries alongside the `GJE` entries from `Fᨀ`, or it enables duplication when employees manually edit transactions (`С1ᛡ`).
3.2.2) `С3ᛡ`
It is possible that your employees sometimes bypass `Fᨀ` and erroneously create sales transactions (Invoices or Sales Receipts) directly in `Qᨀ`.
This leads to `D-COGS†` if the same sale is also registered in `Fᨀ`.
3.2.3) `С4ᛡ`
Your employees might manually create `GJE` entries on the COGS account in `Qᨀ` or incorrectly code vendor bills in `Bᨀ`, posting them directly to COGS.

4) Reasons for negative inventory (hereafter — NI†) specifically in your case:
4.1) The main reason is `С1ᛡ` (point 3.1 above).
`С1ᛡ` causes `Qᨀ` to activate its internal logic and deduct an item that, according to its records, is not in stock (as the receipt was registered via `Fᨀ`), which leads to `NI†`.
4.2) Secondary reasons:
4.2.1) `С5ᛡ`
It is very likely that the dispatch transaction (shipping goods to the customer) is registered in `Fᨀ` before the corresponding receipt transaction (receiving goods from the supplier).
`С5ᛡ` explains the `NI†` within `Fᨀ`, but unlike `С1ᛡ`, it is not a direct cause of `D-COGS†`.
4.2.2) `С2ᛡ` (point 3.2.1 above)
`С2ᛡ` creates an environment in which `Qᨀ` attempts to manage inventory quantities in parallel with `Fᨀ`, which leads to `NI†`.
This is an enabling factor, rather than a direct trigger event (`С1ᛡ`).
4.2.3) `С6ᛡ`
It is likely that the «Allow Negative Inventory» option is enabled in `Fᨀ`.
In my experience, companies often deliberately allow negative inventory to ensure operational flexibility and avoid stopping shipments due to temporary data entry delays.
Of course, this practice is erroneous.
However, `С6ᛡ` itself does not create `NI†`, but only allows other causes (specifically, `С5ᛡ`) to lead to `NI†`.

5) «Explain how Bill.com AP bills should map if they relate to landed cost versus non-inventory expenses»
5.1) The correct solution briefly:
5.1.1) Non-inventory expenses must be entered into `Bᨀ` and mapped to the corresponding expense accounts in `Qᨀ`.
5.1.2) Landed Costs (hereafter — `LC`) must not be entered into `Bᨀ`.
It is impossible to correctly map them from `Bᨀ`, as they require capitalization and allocation at the SKU level, which only `Fᨀ` can perform.
The bills associated with `LC` must be entered exclusively through the `Fᨀ` module «Reconcile» (hereafter — `R`).
5.2) Explanations:
`Fᨀ` and `Bᨀ` have incompatible processes for managing inventory-related accounts payable (`AP`) when integrated with `Qᨀ`.
`LC` must be capitalized — that is, added to the value of the inventory asset (hereafter — `IA`).
`Fᨀ` has the only correct mechanism for this — `R`.
After receiving the goods, these costs must be added within `R` at the «Landed Cost step».
5.3) The likely process flaw:
When you receive a bill for `LC` or inventory, you likely follow your usual process and enter it directly into `Bᨀ`
`Bᨀ`, lacking integration with `Fᨀ`'s inventory processes, sends this bill to `Qᨀ`, bypassing `R`.
This causes 2 critical financial consequences:
5.3.1) Incorrect capitalization.
`LC` are recorded as regular expenses instead of being capitalized into `IA`.
Result:
- The `IA` value on the balance sheet is understated.
- COGS on sale is understated.
- Gross Profit is artificially inflated.
- Operating Expenses (Opex) are overstated.
- Margin analysis at the SKU level becomes impossible.
5.3.2) Failure of the Holding Account (hereafter — `HA`).
When `Fᨀ` registers the receipt of goods, it automatically credits `HA`.
Because the corresponding bill is entered via `Bᨀ` instead of `R`, the required debit transaction to clear `HA` is never created.
Result:
- `HA` accumulates a significant, uncleared credit balance.
- Your liabilities are systematically doubled on the balance sheet (once in `HA` and again in Accounts Payable).

5.4) The correct solution in detail
5.4.1) Non-inventory expenses must be entered into `Bᨀ` and mapped to the corresponding expense accounts in `Qᨀ`.
5.4.2) Inventory bills and all related `LC` must be completely excluded from the entry process in `Bᨀ`.
These bills must be entered exclusively into `R`.
These bills are entered exclusively manually into `R`.
`Fᨀ` performs `LC` allocation and the 3-Way Match, and then exports the finished bill to `Qᨀ`.
`Bᨀ` may still be used at the final stage, strictly for the payment of this bill, which already exists in `Qᨀ`.
5.4.3) This is the most balanced method that ensures maximum accuracy of COGS accounting and inventory valuation while preserving the value of `Bᨀ` for non-inventory expenses.
This method ensures `LC` are correctly capitalized and allocated at the SKU level using the native mechanisms of `Fᨀ`.
It ensures correct operation of the 3-Way Match (PO, Receipt, Bill reconciliation) inside `Fᨀ`.
It prevents the accumulation of errors on `HA`.
This method corresponds to the architectural requirements of `Fᨀ` as a master system.

6) «What should Fishbowl push into QuickBooks — and what should never be pushed?»
6.1) `Fᨀ` must become the single master system for all inventory operations.
6.2) `Qᨀ` must become a passive financial ledger.
6.3) `Fᨀ` must send to `Qᨀ` the full financial impact of operations by specifically pushing the following data:
6.3.1) Sales transactions (Invoices or Sales Receipts) after completion of Shipping.
These should preferably be sent as summary `GJE` to prevent manual editing (see point 7.3).
6.3.2) Vendor Bills after completion of the 3-Way Match and capitalization of Landed Cost in `R`.
These must be sent as detailed Bills to enable the `AP` workflow (see point 5.4).
6.3.3) Customer Payments (if accepted in `Fᨀ`).
6.3.4) `GJE` for inventory asset valuation (e.g., upon Receiving: Debit `IA`, Credit `HA`).
6.3.5) `GJE` for Cost of Goods Sold (e.g., upon Shipping: Debit COGS, Credit `IA`).
6.3.6) `GJE` for all inventory adjustments (e.g., results of Cycle Counts, Scrap).
6.3.7) New Contacts (Customers and Vendors).
6.4) The inventory tracking function in `Qᨀ` must be disabled.
6.5) User access rights in `Qᨀ` must be strictly limited, technically prohibiting manual entry or editing of transactions on accounts managed by `Fᨀ` (`IA`, COGS, `HA`, Revenue, and Accounts Payable).
6.6) This is the only method that guarantees long-term data integrity and the accuracy of financial reporting when procedural discipline is low.
It technically neutralizes the impact of the primary behavioral root causes of critical `D-COGS†` and `NI†` by blocking the possibility of incorrect manual edits in `Qᨀ`.
This method, combined with the strict procedural segregation described in point 5, ensures the correct capitalization of `LC` and the clearing of `HA`.
This method aligns with the best practices for implementing ERP/IMS, minimizing the risks associated with human error.
6.7) Conversely, the following actions must never occur in `Qᨀ` or `Bᨀ`:
6.7.1) Creation of Purchase Orders (PO) in `Qᨀ`.
All POs must be managed exclusively in `Fᨀ`.
6.7.2) Manual inventory quantity adjustments in `Qᨀ`.
These must be technically blocked (see point 6.5).
6.7.3) Entry of inventory bills or Landed Costs via `Bᨀ` or `Qᨀ`.
These must be procedurally prohibited (see point 5).
6.7.4) Editing or deletion of transactions created by `Fᨀ` in `Qᨀ`.
These must be technically blocked (see point 6.5).

7) «How do you prevent duplicate COGS entries between Fishbowl and QuickBooks?»
7.1) It is necessary to implement strict technical access controls by blocking the ability to edit or delete any transactions created by `Fᨀ` in `Qᨀ`.
This is the primary and mandatory defense against `С1ᛡ`.
This directly neutralizes the behavioral root cause of `D-COGS†` by physically preventing errors at the user interface level.
This control is especially critical for Sales transactions (Invoices or Sales Receipts), as these are the transactions where COGS is generated and where manual edits (`С1ᛡ`) occur.
7.2) It is necessary to deactivate Inventory Tracking in `Qᨀ`.
7.3) It is necessary to reconfigure `Fᨀ` to export Sales transactions (Invoices or Sales Receipts) as summary `GJE` instead of detailed individual transactions.
These summary `GJE` will periodically (e.g., daily) update only the account balances in `Qᨀ` (COGS, Revenue, `IA`).
This architecture provides significant advantages: increased synchronization stability and speed, which is critical for your high transaction volume.
It provides the most effective layer of defense against `С1ᛡ` on the Sales side, as the object for incorrect editing physically disappears for users.
Even with this configuration, the technical blocking described in point 7.1 remains essential to prevent manual `GJE` entries on the COGS account (`С4ᛡ`).

8) «What’s your approach to resolving negative inventory and timing mismatches?»
8.1) All bills related to inventory and `LC` must be processed exclusively through `R`: see point 5.4 above.
`R` synchronizes the physical receiving of goods with the financial recognition of costs and clearing of the transit account `HA`.
This ensures correct and timely recognition of COGS and capitalization of additional expenses, eliminating gaps between operational and financial accounting.
This is the only method to correctly capitalize `LC`, which is critical for accurate margin calculation.
8.2) Technical access control.
8.2.1) Point 7.1 above.
This is the only reliable way to stop `D-COGS†` and `NI†`.
8.2.2) It is necessary to mandate the setting and strict enforcement of a «Closing Date» in `Qᨀ` and the corresponding period closing mechanism in `Fᨀ`.
This technically prohibits entering transactions retroactively (Back-Dating) into already closed and reconciled financial periods.
This stabilizes financial reporting and prevents the distortion of historical data, eliminating a key cause of timing mismatches (hereafter — `TM†`).
8.3) Optimization of operational processes.
The key requirement is the immediate registration of goods receipt (Receiving) in `Fᨀ` upon their physical arrival at the warehouse.
This prevents the situation where goods are sold before they are posted in `Fᨀ`.
The method includes the optimization of warehouse processes, e.g., using mobile scanners (Fishbowl Mobile) to speed up registration and minimize data entry errors.
Strict SOPs must be implemented, prohibiting the shipment of goods not present in the system, even if they are physically in the warehouse.
These SOPs must be enforced technically, not just procedurally.
The «Allow Negative Inventory» option in `Fᨀ` (mentioned in point 4.2.3) must be deactivated.
This technically prevents the system from completing the Shipping process if the stock level is insufficient, eliminating reliance on employee discipline alone.
This directly eliminates the operational cause of `NI†`, ensuring that the receipt always precedes the shipment.
8.4) Correction of already existing `NI†` and accumulated `TM†` to restore accounting accuracy.
8.4.1) This requires a full forensic audit of the transaction history using the Fishbowl report «Inventory Event History».
8.4.2) To fix `NI†`, it is necessary to correct errors in both `Qᨀ` and `Fᨀ`.
8.4.2.1) First, negative balances for inventory items within `Qᨀ` (caused by `С1ᛡ` and `С2ᛡ`) must be identified and corrected using the «Inventory Quantity Adjustment» function, typically by zeroing them out.
8.4.2.2) This step must be completed before deactivating inventory tracking or inventory items in `Qᨀ` (see point 7.2) to prevent `Qᨀ` from creating incorrect automatic General Ledger adjustments.
8.4.2.3) A physical inventory must be performed, and discrepancies in `Fᨀ` must be corrected via «Cycle Count» (to correct quantity) or «Add Inventory» (to add missing receipts with the correct cost).
8.4.3) To fix `TM†` and, more critically, the systematic doubling of liabilities on your balance sheet, a detailed audit and clearing of `HA` in `Qᨀ` is required.
This account has accumulated substantial uncleared credits due to the incorrect `AP` process.
8.4.4) The final step is creating a clearing `GJE` in `Qᨀ` to bring the `IA` balance in line with `Fᨀ`.
8.4.5) This is the only way to eliminate the accumulated `TM†` and restore trust in the system data.
The method allows establishing a clean baseline («Source of Truth»), necessary for further correct operation.
8.4.6) Of course, this quality work completely contradicts your erroneous expectations of a «light touch».
8.5) Continuous monitoring: implementing a mandatory daily procedure for reconciling key data between `Fᨀ` and `Qᨀ`.
It is necessary to reconcile daily the `Fᨀ` report «Asset Valuation By Account» and the `IA` balance in `Qᨀ`.
It is also necessary to monitor negative inventory using specialized reports or dashboards.
Any discrepancies must be immediately investigated and resolved.
Of course, this quality work completely contradicts your erroneous expectations of a «one-time “surgeon-style” engagement».