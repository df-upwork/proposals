Для устранения `𐒌(2)`, `𐒌(3)`, `𐒌(4)` и `𐒌(5)`:
Заменить пункт 3.1 в `Aᨀ` следующим текстом:
3.1) Essence
This method involves connecting the source contact data to the Outlook profile on the new computer and using the «Copy Folder» function to transfer the «Contacts» folder into the destination data store.
To be connected on the new computer, the source contacts must reside in a PST file.
The procedure varies depending on whether the source data is currently in a PST or an OST file.
Scenario A (Source data in PST, e.g., POP account): The PST file is copied from the old computer.
It is then connected to the new Outlook profile as an additional data store («File» → «Open & Export» → «Open Outlook Data File»).
Finally, the «Contacts» folder is copied from this connected PST file to the target folder in the new profile using the «Copy Folder» function.
Scenario B (Source data in OST, e.g., IMAP «This computer only» folders): The contacts must first be transferred to a temporary PST file on the source computer.
This OST to PST transfer can be performed using 2 high-fidelity methods.
Method B.1 (Copy Folder): Create a new PST file within the original Outlook profile and copy the «Contacts» folder directly from the OST storage to this new PST file using the «Copy Folder» function.
Method B.2 (Export Wizard): Use the standard Outlook «Import/Export Wizard» («File» → «Open & Export» → «Import/Export» → «Export to a file») to export the «Contacts» folder to a new PST file.
When exporting specifically to an «Outlook Data File (.pst)» (unlike CSV or Excel formats), the wizard preserves custom fields and groups.
The resulting temporary PST file (from B.1 or B.2) is then transferred to the new computer.
It is connected to the new profile, and the contacts are copied into the destination data store using the «Copy Folder» function.