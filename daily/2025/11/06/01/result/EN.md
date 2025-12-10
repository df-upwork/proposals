Below is my analysis of 5 methods for solving your challenge.
I have ordered them from the worst (implied by you) to the best (recommended by me).
1) Custom development in Adobe Illustrator (hereinafter `AI`) using ExtendScript/UXP
This method is a strategic trap and is guaranteed to lead to failure.
`AI` does not have a built-in, reliable way to programmatically detect text overflow.
2) Esko Dynamic Content (hereinafter `EDC`)
`EDC` does not solve the text overflow problem: it detects overflow and generates a «Check Alert».
The designer must perform these actions manually.
Thus, this system (costing $25K/year) fails to achieve your operational goal of «minimal manual intervention», as it merely flags the issue rather than resolving it.
3) Migration to Adobe InDesign (hereinafter `AID`)
3.1) Advantages
`AID` is the correct tool for your challenge: it is designed for text layout and data integration.
`AID` natively manages overflow: it has the `.overflows` property and clearly displays the overflow.
More importantly, `AID` supports text frame threading, allowing text to automatically flow from one frame to another.
3.2) Disadvantages
The Data Merge function (hereinafter `DM`) cannot group or sort data: the generated output follows the order of the records in the CSV.
`DM` cannot handle complex logic (e.g., if the `allergen` field is not empty, then apply the `Bold` style).
`DM` cannot process hierarchical data (XML or JSON) and cannot connect to live data (API or Database): it is an import, not a link.
Using native `DM` relies entirely on static CSV files, which are not a reliable Single Source of Truth (hereinafter `SSOT`) for managing 480+ SKUs across 4+ languages.
4) The EasyCatalog plugin (hereinafter `EC`) for `AID`
4.1) Advantages
`EC` is specifically designed for creating catalogues, price lists, and packaging.
Unlike `DM`, `EC` (with modules) can connect to various sources, including XML, ODBC (databases), and «Combined Data Sources».
`EC` automatically solves the text overflow problem.
It has built-in, automated «Fitting» rules.
The «Frame Depth To Content Depth» rule automatically changes the height of the text frame to fit its text content.
The «Grow and Flow» rule does more: it automatically expands the text frame to the bottom of the page, adds a new page if necessary, and automatically links the text frames to continue the text flow.
`EC` also has a «check the integrity» function, which verifies the document against the data source.
4.2) Disadvantages
`EC` is a layout tool: it requires a clean, verified, and legally compliant data source.
If fed a garbage CSV, `EC` will perfectly automate the layout of garbage.
5) Implementation of PIM as an `SSOT`
This method is the only solution that eliminates the root cause of your problem, not its symptoms.
This approach requires shifting the perspective: moving from treating the project as an `AI` task to considering it a strategic corporate data management task.
PIM systems serve as an `SSOT`, ensuring legal compliance.
PIM systems are specifically designed to manage the critical data relevant to your needs: ingredients, allergen information, nutrition panels.
They natively support translation and localisation management.
Some PIMs have built-in modules for ensuring compliance with Regulation (EU) 1169/2011 and FDA rules.
PIM systems connect to `AID` via native connectors.
For example, the «Akeneo EasyCatalog InDesign Connector» enables configurable export from Akeneo PIM to XML, which `EC` can then read and use for print automation.