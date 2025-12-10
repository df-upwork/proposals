# 1.
## 2.1.
`Dᨀ` ≔ (мой ответ `ꆜ`)

## 2.2.
Содержание `Dᨀ`:
~~~markdown
The problem of modeling a ragged hierarchy in Alteryx One Platform is solved as follows:
1) Data Preparation (Main Workflow)
Before starting the iterative processing, it is necessary to consolidate the data from all source tables into a single structure.
1.1) Import data.
Use the «Input Data» tool to load all Excel tables describing the hierarchy.
1.2) Consolidate and normalize the structure.
Combine the data from the various tables into a single data stream with an adjacency list structure (Adjacency List), that is, in a Parent-Child format.
This stage may require complex logic to join the tables representing different levels or sub-hierarchies (ragged hierarchy).
If the logic analogous to the SQL Conditional Outer Join (as specified in the project description) is required to connect the source tables, where the conditions are included in the `ON` predicate (e.g., `... ON L.Key = R.Key AND [Condition]`), it is necessary to implement it at this stage using the reliable method described in point 2.2.
This method requires a combination of several tools (e.g., «Record ID», «Join», «Filter», «Union») to accurately replicate the SQL logic and ensure the correct number of rows.
The resulting data set (hereinafter `Hierarchy_Data`) must contain at least the parent identifier field (e.g., `ParentID`), the child identifier field (e.g., `ChildID`), and all fields required for the conditional join logic (hereinafter `ConditionFields`).
A unified Parent-Child structure is necessary for the universal implementation of the iterative hierarchy traversal logic.
1.3) Define the initial nodes.
Define the nodes where the hierarchy traversal will start (e.g., the root nodes where `ParentID` is `Null`). Use the «Filter» tool.
1.4) Prepare data for iteration.
To implement the hierarchy traversal (e.g., to expand it into a flat list of Ancestor-Descendant relationships), it is necessary to add auxiliary fields to the initial nodes.
Use the «Formula» tool to add fields:
- `AncestorID`: The ancestor identifier (initially equal to the identifier of the node itself).
- `CurrentID`: The current node identifier (initially equal to the identifier of the node itself).
- `Level`: The hierarchy level (initially 0 or 1).
- `PathHistory`: The path from the root of the hierarchy to the current node to detect cyclical references (initially a string containing the node identifier with delimiters, e.g., the formula `'|' + ToString([CurrentID]) + '|'`).
This data set (hereinafter `Initial_Nodes`) initiates the process.
2) Implementation of Conditional Join in Alteryx
The «Join» tool in Alteryx supports only equality-based joins (equi-joins).
Therefore, to replicate the conditional logic, it is necessary to use a combination of tools after the «Join» tool.
2.1) Conditional Inner Join Implementation.
If it is required to include in the result only those records for which the keys match and the condition is met:
2.1.1) Use the «Join» tool to join by keys.
2.1.2) Connect the «Filter» tool to the «J» (Joined) output of the «Join» tool.
2.1.3) Configure the «Filter» tool to check the additional conditions (`ConditionFields`).
2.1.4) The «T» (True) output of the «Filter» tool contains the result of the Conditional Inner Join.
2.2) Implementation of the Conditional Outer Join (e.g., Left Outer Join).
If it is required to replicate the logic of the SQL `LEFT OUTER JOIN`, where additional conditions are included in the `ON` predicate (e.g., `... ON L.Key = R.Key AND [Condition]`), it is necessary to use an approach that determines the very fact of a successful join based on all conditions.
The rationale for this method (the «Double Join» pattern) is based on the difference between the conditions specified in the `ON` predicate and the `WHERE` predicate in SQL.
In a `LEFT OUTER JOIN`, the conditions in the `ON` predicate determine whether a join occurs but do not filter records from the left table if the condition is false (the fields from the right table are populated with `Null`).
The conditions in the `WHERE` predicate are applied after the join and filter the resulting data set.
The standard approach in Alteryx (combining the «L» and «J» outputs of the «Join» tool via the «Union» tool) with the subsequent application of the «Filter» tool is equivalent to the logic of the `WHERE` predicate.
This approach incorrectly handles the conditional join on the `ON` predicate, as it may filter out records from the left table that must be preserved.
The «Double Join» pattern accurately replicates the logic of the `ON` predicate, which is critical for preserving data integrity, especially in N-to-M (Many-to-Many) relationships.
2.2.1) Ensure the uniqueness of the records in the left data stream.
To uniquely identify the records, it is necessary to ensure that the left data stream has a unique identifier.
If one does not exist, use the «Record ID» tool to create a new field (e.g., `L_ID`).
2.2.2) Perform the Conditional Inner Join.
Implement the logic described in point 2.1, using the prepared left stream (step 2.2.1) and the right stream.
The result (the «T» output of the «Filter» tool, hereinafter `Joined_Conditional`) contains successfully joined records, including the unique identifier (`L_ID`).
2.2.3) Identify the truly unjoined records (Left Unjoined).
It is necessary to find the records from the left stream for which not a single match was found for the full join condition.
2.2.3.1) Add a second «Join» tool.
Join the prepared left stream (step 2.2.1, «L» input) and `Joined_Conditional` (step 2.2.2, «R» input).
2.2.3.2) Configure the join by the unique identifier (e.g., `L_ID`).
2.2.3.3) The «L» (Left Unjoined) output of this tool contains the target unjoined records (hereinafter `Unjoined_L`).
2.2.4) Final union.
Use the «Union» tool to union `Joined_Conditional` (step 2.2.2) and `Unjoined_L` (step 2.2.3.3).
The «Union» tool automatically reconciles the data schemas, populating the fields from the right table with Null values for the `Unjoined_L` stream (with the appropriate configuration, e.g., «Auto Configure by Name»).
2.2.5) Completion.
If necessary, use the «Select» tool to remove the auxiliary unique identifier (e.g., `L_ID`) and order the fields.
3) Creating an Iterative Macro
It is necessary to create a separate Workflow to implement the recursive logic.
In most cases, to traverse the hierarchy in the recursive step, the Inner Join logic is used (finding existing connections).
3.1) Set the Workflow type.
In a new Workflow, open the «Workflow Configuration» pane.
On the «Workflow» tab, in the «Type» section, select «Macro», then «Iterative Macro».
The «Iterative Macro» executes a process iteratively, passing the results of one iteration to the input of the next, which allows data to be processed recursively or until a certain condition is met.
3.2) Define the macro inputs.
Add two «Macro Input» tools from the «Interface» category.
3.2.1) Iterative input (e.g., `Input_I`).
Accepts data for the current iteration.
The schema must match `Initial_Nodes` (fields `AncestorID`, `CurrentID`, `Level`).
3.2.2) Fixed input (e.g., `Input_H`).
Accepts the complete hierarchy data set (`Hierarchy_Data`).
3.3) Implement the iteration and conditional join logic.
It is necessary to find the next level of the hierarchy.
For the recursive traversal of the hierarchy, the Conditional Inner Join logic is applied (see point 2.1).
The purpose of the iterative process is to detect existing relationships (descendants) that satisfy the specified conditions, to continue the traversal along these branches.
The Conditional Outer Join logic (mentioned in the problem description) is applied when it is necessary to preserve records for which the condition is not met (e.g., at the data consolidation stage in point 1.2), but it is not suitable for the recursive traversal mechanism inside the «Iterative Macro».
The use of an Outer Join will make it impossible for the macro to complete, as the data stream passed to the iterative output (`Output_I`) will never become empty (the standard stopping condition will not be met).
3.3.1) Add a «Join» tool. Join `Input_I` (the «L» input) and `Input_H` (the «R» input).
3.3.2) Configure the join: `L.CurrentID` = `R.ParentID`.
3.3.3) Add a «Filter» tool, connected to the «J» output.
3.3.4) Configure the «Filter» based on `ConditionFields` from `Input_H` (and, possibly, data from `Input_I`).
The «T» (True) output contains potential candidates for the next iteration (hereinafter `Candidates`).
3.3.5) Implement a cyclic reference detection mechanism.
To prevent infinite loops, it is necessary to check whether the new node (`ChildID` from `Input_H`) has already been visited in the current branch of the hierarchy.
Add a second «Filter» tool connected to the `Candidates` stream.
3.3.6) Configure the cycle check.
Use a function to search for the child identifier (`R.ChildID`) inside the `PathHistory` field (from `Input_I`).
E.g., the formula `Contains([L.PathHistory], "|" + ToString([R.ChildID]) + "|")`.
The use of delimiters (as defined in point 1.4) ensures the reliability of the check, preventing false positives on partial identifier matches (e.g., ID 12 and ID 123).
3.3.7) Process the check results.
The «F» (False) output contains the valid connections without cycles (hereinafter `Valid_Next_Level`).
The «T» (True) output contains the detected cyclical references (hereinafter `Cyclic_Records`).
3.4) Prepare data for the next iteration.
The `Valid_Next_Level` stream (step 3.3.7) contains the successful joins. It is necessary to update the data for the next step.
3.4.1) Add the «Formula» tool connected to the `Valid_Next_Level` stream.
3.4.2) Update the fields:
- `AncestorID`: leave the value from `Input_I` (carried over through iterations).
- `CurrentID`: set the value to `ChildID` from `Input_H` (the new current node).
- `Level`: increase the value by 1 (use the formula `[Level] + 1`).
- `PathHistory`: add the new node (`CurrentID`) to the existing path (use the formula `[PathHistory] + ToString([CurrentID]) + "|"`).
The system variable `[Engine.IterationNumber]` (which starts at 0) can also be used to calculate the level.
However, this requires taking into account the initial level set in point 1.4 (e.g., the formula `[Initial_Level] + [Engine.IterationNumber] + 1`).
Explicitly passing and incrementing the `Level` field provides greater flexibility if different branches of the hierarchy start at different levels.
3.4.3) Use the «Select» tool to ensure the data schema matches the `Input_I` schema.
The required strictness of the match depends on the selected «Output Mode» in the macro configuration (see point 4.3).
3.5) Define the macro outputs.
Add two «Macro Output» tools.
3.5.1) Result output (e.g., `Output_R`).
Connect the output of the «Select» tool (step 3.4.3).
The data (Ancestor-Descendant relationships), generated only within the current iteration (the delta), is sent to this output.
The Alteryx Engine automatically performs the «Union» operation to accumulate the results of all iterations in the final output stream of the macro.
3.5.2) Iterative output (e.g., `Output_I`).
Also connect the output of the «Select» tool (step 3.4.3).
This data is passed back to `Input_I`.
The macro will stop when this output is empty.
3.5.3) Cyclical data output (e.g., `Output_C`).
Connect the `Cyclic_Records` stream (step 3.3.7).
This output allows to isolate and analyze the records that form cyclical references in the hierarchy, without including them in the main result of the iterative process.
4) Configuring Macro Parameters
4.1) Open the Interface Designer.
Go to «View» → «Interface Designer».
4.2) Configure the iteration properties.
Go to the «Properties» section (the wrench or gear icon).
4.2.1) In the «Iteration Input» field, select `Input_I`.
4.2.2) In the «Iteration Output» field, select `Output_I`.
4.2.3) In the «Maximum Number of Iterations» field, set a sufficiently large value (e.g., 100).
This value serves as a fail-safe mechanism to prevent the unexpected infinite execution of the Workflow, although the main logic for detecting cyclical references is implemented inside the macro (step 3.3.5).
Rationale: These settings determine how the Alteryx Engine manages the data flow between iterations.
4.3) Configure the output mode.
Go to the «Properties» section in the «Interface Designer».
In the «Output Mode» field, select the mode for combining the results of the iterations.
It is recommended to use «Auto Configure by Name (Wait until all Iterations run)».
It is recommended to use «Auto Configure by Name (Wait until all Iterations run)».
When using this mode, a match of field names and data types is required; a strict order of fields is not mandatory.
When using the «Auto Configure by Position» mode, an exact match of field types and order is required.
4.4) Save the macro (e.g., as the file `ProcessHierarchy.yxmc`).
5) Execution (Main Workflow)
5.1) Insert the macro.
In the main Workflow, right-click on the canvas → «Insert» → «Macro...» and select the file `ProcessHierarchy.yxmc`.
5.2) Connect the data.
5.2.1) Connect `Hierarchy_Data` (step 1.2) to the `Input_H` input of the macro.
5.2.2) Connect `Initial_Nodes` (step 1.4) to the `Input_I` input of the macro.
5.3) Process the results.
The `Output_R` output of the macro contains the expanded hierarchy (all Ancestor-Descendant relationships, starting from level 1).
The described «Iterative Macro» logic does not include the initial nodes (level 0) in this output stream.
To obtain the complete hierarchy data set, it is necessary to use the «Union» tool to union the initial nodes (`Initial_Nodes`) with the macro result (`Output_R`).
~~~

# 2. `᛭T`
Я хочу опубликовать `Dᨀ` в виде статьи на своём сайте и в виде документа PDF.
Для этих целей мне нужно озаглавить `Dᨀ`.
Твоя задача: предложить 10 вариантов заголовка (`T๏`) для `Dᨀ`.

# 2. Требования к `T๏`
1) `T๏` должен быть на английском языке
2) Для каждого `T๏` укажи своё обоснование
3) Не пиши каждое слово заголовко с заглавной буквы. Вместо этого пиши нормальным образом, как обычное предложение.

# 3. Пожелания к `T๏`
1) Желательно использовать профессиональный язык предметных областей `P⁎` и `Dᨀ`.

