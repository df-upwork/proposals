Для устранения 𐒌(1), 𐒌(2), 𐒌(3), 𐒌(4):

1.  Заменить пункт 11 (включая подпункты 11.1, 11.2, 11.3) следующим текстом:

<!-- end list -->

```
11) `R5`: synchronization of Buildable Quantity for `AI`
11.1) Essence
`R5` is applicable if the use of `AI` is a business requirement (making `R4` impossible) and the assembly process is virtual or occurs just-in-time.
`R5` involves reconfiguring `Cᨀ` to synchronize the Buildable Quantity instead of the Quantity on Hand for `AI`.
The Buildable Quantity represents the maximum number of assemblies that can be built based on the current availability of components.
By synchronizing this value (e.g., enabling the setting «For Assembly Items, Include Buildable Quantity When Syncing Total»), `Cᨀ` recognizes the item as available if components are in stock, even if the assembly is not pre-built (Quantity on Hand = 0).
This prevents `Cᨀ` from detecting a false shortage and activating the `FSM`.
11.2) Advantages
`R5` eliminates `⋇2` without requiring SKU migration (`R4`) or complex scripting (`R6`).
`R5` allows retaining the use of `AI` and their associated costing models (e.g., Standard Costing), which `KPI` do not support.
`R5` utilizes standard configuration options within `Cᨀ`.
11.3) Key challenges
`R5` relies on the capability of `Cᨀ` to calculate and synchronize the Buildable Quantity efficiently.
The accuracy of the Buildable Quantity depends on the precise configuration of the Bill of Materials (BOM) in `Nᨀ`.
If the calculation is complex (e.g., multi-level BOMs), it may impact synchronization performance.
`R5` requires that a process (manual or automated, like `R6`) exists to execute the `Assembly Build` transactions in `Nᨀ` promptly after the order is imported to consume the components.
```

2.  Заменить пункт 12.1 следующим текстом для обеспечения логической связи с обновленным пунктом 11:

<!-- end list -->

```
12.1) Essence
`R6` is an alternative if `R4` is not applicable and `R5` cannot be implemented (e.g., `Cᨀ` lacks the capability to synchronize Buildable Quantity) or if Just-In-Time automation of the `Assembly Build` transaction is required.
Automating the creation of `Assembly Build` transactions just-in-time via customization.
To adhere to NetSuite Best Practices, avoid performance degradation, and ensure data integrity, this automation must be implemented asynchronously (e.g., using `afterSubmit` User Event Scripts triggering Map/Reduce or Scheduled Scripts).
```