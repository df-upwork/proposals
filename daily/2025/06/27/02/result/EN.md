1) The most robust solution for this task is to develop a custom backup script specifically for the database rather than using SQL-aware agents.
This can best be accomplished using `dbatools`: https://github.com/dataplat/dbatools
Since your organization is large (with 1,000+ people), your databases likely have many specific characteristics that generic SQL-aware agents (for example, those from Veeam) may not take into account.
These agents perform backups in a generic way, which is unlikely to be optimal for your specific situation.
2) Of course, the task can also be solved using SQL-aware agents.
The specifics of the solution depend on the backup system used: Veeam, Acronis, Commvault, etc.