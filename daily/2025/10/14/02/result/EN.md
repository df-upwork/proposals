Correct methods for solving your task:
1) Synchronization via a server (Exchange / Microsoft 365 / Outlook.com)
1.1) Essence
When using a Microsoft Exchange, Microsoft 365, or Outlook.com account, all data (contacts, custom fields, groups) is stored on the server.
The server also stores the Master Category List (MCL), which defines the names and colors of the categories.
For the migration, it is sufficient to set up the same account in Classic Outlook on the new computer, and the data will synchronize automatically.
1.2) Advantages
This is the simplest and most straightforward method.
Manual effort is minimal, limited to the account setup.
Complete and accurate preservation of all data is guaranteed, including custom fields, groups, and category colors.
1.3) Disadvantages
This method is applicable only to Exchange, Microsoft 365, or Outlook.com accounts.
It is not applicable to POP accounts.
It is not applicable to IMAP accounts, as the IMAP protocol does not support the synchronization of contacts and categories.
2) Direct copying of the PST file (for local data)
2.1) Essence
If the contacts are stored locally in an Outlook Data File (.pst) (e.g., with a POP account or as a dedicated local data file alongside IMAP/Exchange), this method is applicable.
The method involves copying the entire PST file from the old computer to the new one while the Outlook application is closed on both computers.
On the new computer, Outlook is configured to use this copied file (either as the primary data store or connected as an additional data file).
2.2) Advantages
This is the most reliable method for local data, as the entire database is copied.
Preservation of custom fields and contact groups is guaranteed.
The MCL, which defines category colors, is stored only in the Default Data File of an Outlook profile.
Preservation of the MCL and colors is guaranteed only if the PST file was the Default Data File on the old computer and is configured as the Default Data File on the new computer.
2.3) Disadvantages
The method is applicable only if the source data is stored in a PST file.
It is not applicable if the contacts are stored in an OST file (used by Exchange, Microsoft 365, Outlook.com, and IMAP accounts for server-synchronized data and «This computer only» folders).
The entire file's contents are transferred (e.g., mail, calendar), meaning contacts cannot be migrated selectively.
If the PST file was not the Default Data File in the source profile, it does not contain the MCL.
If the PST file is connected as a secondary data store (not the Default Data File) in the new profile, the MCL from the PST file is ignored.
In these scenarios, the category colors will not be transferred automatically.
They must be migrated separately using specialized methods (e.g., specialized third-party tools or programmatic methods), just as required in method 3.
3) Folder-Level Transfer (via PST)
3.1) Essence
This method involves transferring the contacts via a temporary Outlook Data File (.pst).
It is used when methods 1 and 2 are not applicable (e.g., data stored locally in «This computer only» folders within an IMAP OST file) or when contacts need to be selectively merged into an existing profile.
The method consists of 2 main steps:
3.1.1) Step 1: Consolidate data into a PST file
If the source data is in an OST file, it must first be copied or exported to a PST file on the old computer.
This can be achieved using the Outlook «Import/Export Wizard» (exporting specifically to an «Outlook Data File (.pst)») or by using the «Copy Folder» function if a destination PST file is already connected to the profile.
Contrary to your belief, exporting to a PST file (unlike CSV) preserves all custom fields and groups.
If the data is already in a PST file, this consolidation step is skipped, and the file is used for the transfer.
3.1.2) Step 2: Transfer to the new computer
The PST file is copied or moved to the new computer and connected to the new Outlook profile.
Within Outlook on the new computer, the «Contacts» folder is then copied from this PST file to the main storage location using the «Copy Folder» function.
3.2) Advantages
This method ensures complete and accurate data copying, including custom fields and contact groups.
It allows for the integration of old contacts into a new profile without replacing it entirely.
It is a viable method for migrating data stored in OST files.
3.3) Disadvantages
This method is more complex than methods 1 and 2, requiring multiple steps and manual handling of data files.
The MCL, which stores category colors, is not transferred automatically.
While category names remain assigned to the contacts, their colors will be lost in the new profile.
Therefore, preserving the original colors requires a separate, specialized migration of the MCL (e.g., using programmatic methods or third-party tools) because Outlook lacks a built-in feature for this.