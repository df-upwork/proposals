1) Problem #1 does not result from an opaque or unpredictable mechanism.
The calculation of a summary metric, such as «Net Income», is the terminal node in a directed acyclic graph (DAG) of computations.
E.g., «Net Income» depends on «Gross Profit» and «Operating Expenses»; in turn, «Operating Expenses» depend on the sum of «Administrative Expenses» and «Sales Expenses».
This tree-like dependency structure requires special processing approaches, such as recursion, which creates the illusion of «nonlinearity».
2) Complex report structures in Sage Intacct are designed in Excel before being implemented in the system.
This means that the system's logic directly reflects the business rules established by users.
The main obstacle is not technical uncertainty, but the need to formalize and document these business processes.
3) The proper solution to Problem #1 must be based on a dynamic, metadata-driven approach, rather than hard-coding a single, specific report.
This ensures the solution is resilient to changes that financial users may make to the report structure in Sage Intacct.
4) The metric «technician sales» is ambiguous because it does not represent a single field in the database.
It is a calculated metric (KPI) that results from the complex interaction of multiple underlying entities (estimates, invoices), business rules (percentage-based distribution among technicians, sales thresholds for job types), and context (the fundamental distinction between the concepts of «Sales» and «Revenue»).
The root cause of Problem #2 is the absence of a predefined formula; replication requires not just extracting a value, but recreating the calculation logic itself.
5) The correct way to solve Problem #1:
5.1) Using the `query` method of the `GLACCOUNTGROUP` object via the Sage Intacct API, extract the complete information for all account groups.
The result must contain:
- `id`
- `title`
- `groupType`
- composition: a list of accounts or other groups.
- computation parameters
5.2) Obtain all detailed `GLDETAIL` entries for the required reporting period.
The most reliable method is to use a data export from a specially created custom report in Sage Intacct, which will contain all the necessary fields.
5.3) Obtain a list of all used dimensions and their values to enable subsequent filtering.
5.4) Create a model in the target database that describes the report structure:
5.4.1) Create the metadata table `dim_account_groups`.
This table will store all information about account groups: their ID, title, type, computation formula (if applicable), normal balance, etc.
5.4.2) Create the bridge table `bridge_account_group_hierarchy`.
This is a key element for working with hierarchies.
The table will have a simple structure, for example, (`parent_group_id`, `child_group_id`, `order`), and describe the tree-like relationships between account groups.
This structure is ideal for processing with recursive queries.
5.5) Report Assembly:
5.5.1) Use a recursive SQL query (e.g., with a Recursive Common Table Expression or CTE) to traverse the hierarchy defined in `bridge_account_group_hierarchy`.
At the lowest level (where the child elements are GL accounts), transactions from the `GLDETAIL` table are summed.
Then, the results are rolled up the hierarchy, aggregating at each level.
5.5.2) Inside the aggregate function (e.g., `SUM()`), apply a condition that multiplies the sum by `1` or `-1` depending on the normal balance of the account/group, to correctly account for revenues and expenses.
5.5.3) Apply the logic for groups of type `Computation` as a separate step after the base aggregation.
At this step, formulas stored in the `dim_account_groups` metadata table are applied to the already calculated group totals.
6) The correct way to solve Problem #2:
6.1) It is necessary to understand the fundamental distinction between «Sales» and «Revenue» in ServiceTitan terminology.
The critical difference lies in the timing of recognition: an estimate can be sold in January (appearing in the sales report for January), while the work for it might be completed and invoiced only in February (appearing in the revenue report for February).
Therefore, for accurate replication, it is necessary to extract and process data from both estimates and invoices, and to never use these metrics interchangeably.
6.2) Problem #2 is, at its core, a data modeling and ETL/ELT logic task.
The source data exists, but the final KPI is created during the transformation stage.
6.3) Solving Problem #2 requires a systematic approach to extracting all necessary components and their subsequent assembly in accordance with the business logic:
6.3.1) Extracting all necessary data (e.g., via the Transactional API)
6.3.2) All data extracted from the API must first be loaded in its «raw» form into staging tables (staging area) in the target data platform.
6.3.3) Implement the business logic and calculated views.