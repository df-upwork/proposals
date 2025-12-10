1\.
Правка для устранения `𐒌(1)` в `Aᨀ` §7.1.

Заменить:

```markdown
7.1) It is necessary to implement strict technical access controls by blocking the ability to edit or delete any transactions created by `Fᨀ` in `Qᨀ`.
This is the primary and mandatory defense against `С1ᛡ`.
This directly neutralizes the behavioral root cause of `D-COGS†` by physically preventing errors at the user interface level.
This control is especially critical for Purchase transactions (Bills), which must remain detailed in `Qᨀ` (see point 7.3).
```

На:

```markdown
7.1) It is necessary to implement strict technical access controls by blocking the ability to edit or delete any transactions created by `Fᨀ` in `Qᨀ`.
This is the primary and mandatory defense against `С1ᛡ`.
This directly neutralizes the behavioral root cause of `D-COGS†` by physically preventing errors at the user interface level.
This control is especially critical for Sales transactions (Invoices or Sales Receipts), as these are the transactions where COGS is generated and where manual edits (`С1ᛡ`) occur.
```

2\.
Правка для устранения `𐒌(1)` в `Aᨀ` §7.3.

Заменить:

```markdown
7.3) It is necessary to reconfigure `Fᨀ` to export Sales transactions (Invoices or Sales Receipts) as summary `GJE` instead of detailed individual transactions.
These summary `GJE` will periodically (e.g., daily) update only the account balances in `Qᨀ` (COGS, Revenue, `IA`).
This architecture provides significant advantages: increased synchronization stability and speed, which is critical for your high transaction volume.
It also provides a secondary layer of defense against `С1ᛡ` on the Sales side, as the object for incorrect editing physically disappears for users.
However, this configuration cannot be applied to Purchase transactions (Bills).
Detailed Bills must be exported to `Qᨀ` to enable the AP payment workflow via `Bᨀ` described in point 5.4.
Therefore, the technical blocking described in point 7.1 remains the essential control mechanism for the Purchase side.
```

На:

```markdown
7.3) It is necessary to reconfigure `Fᨀ` to export Sales transactions (Invoices or Sales Receipts) as summary `GJE` instead of detailed individual transactions.
These summary `GJE` will periodically (e.g., daily) update only the account balances in `Qᨀ` (COGS, Revenue, `IA`).
This architecture provides significant advantages: increased synchronization stability and speed, which is critical for your high transaction volume.
It provides the most effective layer of defense against `С1ᛡ` on the Sales side, as the object for incorrect editing physically disappears for users.
Even with this configuration, the technical blocking described in point 7.1 remains essential to prevent manual `GJE` entries on the COGS account (`С4ᛡ`).
```