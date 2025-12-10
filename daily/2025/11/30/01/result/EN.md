1) In points 2-4, I describe 3 main causes of your problem (hereafter — `P†`).
In points 5-12, I outline my recommendations.
2) `⋇1`: fail-safe mechanism (hereafter — `FSM`).
This is the most probable cause of `P†`.
The NetSuite connector (hereafter — `Cᨀ`) automatically creates the «inventory adjustments» (hereafter — `IA`) you mentioned to ensure order processing from Shopify (hereafter — `Sᨀ`) when an insufficient inventory level is recorded in NetSuite (hereafter — `Nᨀ`).
`Nᨀ`, as a strict ERP system, prohibits transactions that reduce inventory below zero (e.g., «Cash Sale» or «Item Fulfillment»).
When `Cᨀ` detects insufficient stock before importing an order, `FSM` proactively creates an `IA` to increase the inventory balance.
This prevents the transaction blockage and ensures the order can be successfully imported and fulfilled.
Enabling overselling in `Sᨀ` or temporary inventory synchronization delays between `Nᨀ` and `Sᨀ` can serve as a trigger.
3) `⋇2`: item configuration conflict (data model mismatch)
Mismatches between `Sᨀ` models (e.g., Bundles) and `Nᨀ` models (Assembly Items (hereafter — `AI`), Kits/Package Items (hereafter — `KPI`), Inventory Items (hereafter — `II`)) cause availability errors.
This occurs when the mapped `Nᨀ` configuration results in 0 inventory for fulfillment, e.g.:
- an `AI` lacking an Assembly Build (`Quantity Built = 0`)
- a Bundle mapped to an `II` where stock is held at the component level
- `Cᨀ` incorrectly expecting stock on a parent `KPI` SKU.

Detecting these shortages, `Cᨀ` activates `FSM` (`⋇1`) and creates an `IA`.
4) `⋇3`: impact of internal customizations (SuiteScripts and Workflows)
Your other Upwork project «NetSuite SDF configuration» indicates customizations are active in `Nᨀ`, increasing the risk of unintended interactions.
Directly, customizations might independently create `IA` based on internal logic.
Indirectly, they might alter inventory data (e.g., Quantity Available or Inventory Commitment).
If availability is reduced, `Cᨀ` detects a shortage during proactive checks.
Consequently, `Cᨀ` activates the `FSM` (`⋇1`) and creates the `IA`.
5) In points 6-8, I outline my main recommendations for eliminating `⋇1`.
6) `R1`: disable `FSM` in `Cᨀ`.
6.1) Advantages
It prevents the distortion of financial data integrity and the accuracy of the COGS calculation specifically caused by the `FSM`.
It forces identifying and eliminating the root causes of inventory discrepancies, rather than masking them.
It corresponds to best practices for mature ERP systems, where accounting accuracy has priority.
6.2) Key challenges
The outcome depends on the transaction type and the interaction of `Nᨀ` configurations and customizations:
6.2.1) If `Nᨀ` prevents the transaction (Negative Inventory (hereafter — `NI`) disallowed), the import of inventory-impacting records (e.g., Item Fulfillment) fails.
This typically occurs via API rejection (e.g., `INSUFFICIENT_INVENTORY` error).
The impact depends on the integration flow.
Sales Order imports (impacting Quantity Committed) usually succeed.
However, subsequent Item Fulfillment (impacting Quantity On Hand) is blocked until stock is available.
Cash Sale or Invoice imports (impacting Quantity On Hand) will fail.
Prompt intervention is required to analyze errors and resolve the discrepancy.
Resolution involves stock replenishment or order management (e.g., cancellation).
Automatic retries by `Cᨀ` may resolve temporary discrepancies.
Inefficient resolution risks delays in customer service and revenue recognition.
6.2.2) If `Nᨀ` permits the transaction (`NI` allowed), transactions proceed, but the primary challenge is the formation of negative balances in the ERP.
This requires rigorous Backorder Management and timely reconciliation to align `Nᨀ` data with physical reality.
It increases administrative burden and OPEX by requiring continuous monitoring and discrepancy resolution.
7) `R2`: change the frequency and speed of inventory synchronization `Nᨀ` → `Sᨀ`
7.1) Essence
Minimize latency between `Nᨀ` and `Sᨀ` via Near Real-Time (hereafter — `NRT`) synchronization.
Methods include optimized batch polling (delta syncs) or event-driven updates (`User Event Scripts` in `Nᨀ`).
7.2) Advantages
The risk of overselling due to outdated inventory data is significantly reduced, decreasing `FSM` activation.
Availability information accuracy on the `Sᨀ` storefront increases.
7.3) Key challenges
Latency cannot be completely eliminated.
Increased frequency heightens the risk of exceeding API limitations on both platforms, potentially halting integration flows.
High frequency can degrade performance.
`R2` does not resolve fundamental configuration problems or business process errors.
8) `R3`: implementation of Inventory Buffer (hereafter — `IB`)
8.1) Essence
Configure `Cᨀ` to subtract an `IB` from the `Nᨀ` Quantity Available before syncing data to `Sᨀ`.
E.g., if 5 units are available in `Nᨀ` and the `IB` equals 2, then a balance of 3 will be sent to `Sᨀ`.
This reserves inventory to prevent overselling caused by synchronization latency (race conditions).
8.2) Advantages
`R3` effectively mitigates overselling risks and reduces out of stock errors during order import.
Implementation is flexible, supporting static buffers via `Cᨀ` or dynamic strategies utilizing `Nᨀ` customization (e.g., Saved Searches).
8.3) Key challenges
`R3` may lead to lost revenue by artificially reducing available quantity and masks the root causes of discrepancies.
Dynamic strategies introduce complexity and require careful implementation regarding `Nᨀ` performance.
Utilizing synchronous calculations significantly degrades performance.
The best practice is utilizing asynchronously updated Stored Custom Fields.
Optimal buffer size requires continuous analysis and adjustment.
9) In points 10-12 I outline my main recommendations for eliminating `⋇2`.
10) `R4`: restructuring composite items (`KPI`/`AI`)
10.1) Essence
`R4` aligns `Nᨀ`/`Sᨀ` models to resolve `⋇2` via 3 actions:
10.1.1) `R4.1`: addressing `AI` conflicts.
If assembly is not required, `AI` must be replaced with `KPI`.
Because `Nᨀ` prohibits changing item types post-transaction, this requires SKU migration.
10.1.2) `R4.2`: addressing `II` conflicts.
If a `Sᨀ` Bundle maps to an unstocked `Nᨀ` `II`, it must be remapped to a `KPI` or `AI`, or the `II` must be migrated to a `KPI`.
10.1.3) `R4.3`: addressing `KPI` conflicts.
If `Cᨀ` incorrectly expects stock on the parent `KPI` SKU, its settings must be adjusted.
`Cᨀ` must calculate availability based on the components.
10.2) Advantages
It eliminates `⋇2` root causes and shortages.
It ensures accurate COGS and component consumption.
It prevents asset inflation from `IA` creation when components remain stocked.
10.3) Key challenges
A comprehensive audit of the catalog and `Cᨀ` configuration is required.
SKU migration is complex and requires careful planning.
Implementation demands deep expertise in `Nᨀ` architecture and `Cᨀ` configuration.
11) `R5`: synchronization of «Buildable Quantity» (hereafter — `BQ`) for `AI`
11.1) Essence
Reconfigure `Cᨀ` to synchronize `BQ` instead of the «Quantity on Hand» (hereafter — `QH`) for `AI`.
`R5` applies if `AI` is mandatory (`R4` impossible) for virtual or just-in-time (hereafter — `JIT`) assembly.
This recognizes component-based availability, preventing false shortages and `FSM` activation when `QH` = 0.
11.2) Advantages
`R5` resolves `⋇2` via standard `Cᨀ` configuration, avoiding SKU migration (`R4`) or scripting (`R6`).
It retains `AI` and advanced costing models (e.g., Standard Costing) unsupported by `KPI`.
11.3) Key challenges
`R5` requires accurate Bill of Materials (BOM) configuration and efficient `Cᨀ` performance.
It mandates prompt «Assembly Build» execution (manual or via `R6`) post-import for component consumption.
12) `R6`: Auto-Build Assemblies via scripting
12.1) Essence
Automate `Assembly Build` creation via SuiteScript when `R4`/`R5` are not viable or `JIT` automation is required.
It balances accounting integrity (`NI` settings) against performance, depending on `R1` status.
12.1.1) Strategy `R6.1`: synchronous `JIT` build.
It executes during import (e.g., User Event Script) if `R1` is active and `NI` is prevented.
12.1.2) Strategy `R6.2`: asynchronous replenishment.
It executes post-import (e.g., map/reduce) if `R1` is active and `NI` is allowed for the `AI`.
12.2) Advantages
`R6` retains `AI` usage when native options fail.
`R6.1` ensures accounting integrity (prevents `NI`).
`R6.2` optimizes performance by minimizing import impact.
12.3) Key challenges
`R6` increases complexity, TCO, and demands robust error handling.
`R6.1` severely impacts performance, risking timeouts, locking, and governance breaches.
`R6.2` requires allowing `NI` (contradicting best practices), mandates backorder management, and causes latency.