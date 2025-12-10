Your misconceptions:
1) Elastic Query (hereinafter `EQ`) does not support Azure Managed Identity (hereinafter `AMI`).
This is the most fatal technical flaw that makes your proposed architecture dead on arrival.
The official Microsoft documentation for `EQ` contains an unambiguous and fatal limitation: «Elastic queries are only supported when connecting with SQL Server Authentication».
This limitation directly contradicts all modern security best practices in Azure, which mandate the use of Microsoft Entra ID (hereinafter `EID`) and `AMI` precisely to avoid using and storing passwords.
2) You are asking Eccovia (hereinafter `E`) for direct SQL access.
Because of point 1, you are forced to request SQL Authentication credentials (a login and password) from `E`, rather than being able to utilize secure authentication methods like `EID` or `AMI`.
In 2025, no competent SaaS vendor, especially in the HIPAA-compliant healthcare sector, will ever provide an external entity with a SQL login and password to its production multi-tenant database.
This would be equivalent to handing over the administrative keys to their entire production database.
3) Your architecture is a point-to-point integration: <Your own Azure SQL DB> ⟷ <`E`'s database>.
`EQ` is intended for a one-to-many architecture within your own environment: <Main DB> ⟷ <Shard 1, Shard 2,..., Shard N>.
This is a fundamental mismatch.
`EQ` is not a universal replacement for linked servers.
It is not designed for connecting to arbitrary external SQL databases.
This is especially true for an isolated, secure PaaS database managed by a third-party SaaS provider.
4) Microsoft still marks `EQ` as «in preview».
`EQ` has been in preview status for several years.
The «Preview» status has specific and serious consequences: it lacks both a Service Level Agreement (SLA) and full production support.
You work in the healthcare sector, processing Protected Health Information (`PHI`).
This is an environment with the highest requirements for stability, security, and support.
Building the primary production analytical platform on a technology that lacks an SLA and remains in a state of perpetual preview is a gross violation of fundamental technical risk management principles.
5) `E`'s «hesitance» is not a subjective obstacle, but an objective requirement driven by HIPAA compliance and technical security imperatives.
`E`, as an EHR system provider that processes mental health data, is legally classified as a «Business Associate» under HIPAA.
In this capacity, `E` bears direct legal responsibility for ensuring the confidentiality, integrity, and availability of `PHI`.
This responsibility is fundamentally undermined by direct SQL access because it bypasses the application-level Role-Based Access Control (`RBAC`) required by HIPAA.
Consequently, even read-only access exposes confidential data by circumventing these controls.
When dealing with confidential data, particularly in the healthcare sector, unauthorized reading (disclosure) is often a more serious violation than unauthorized writing (modification).
6) Misconception about «viewer-level access» (hereinafter `VLA`)
6.1) In the context of SQL Server, `VLA` corresponds to the built-in database role `db_datareader`.
This role grants only the `SELECT` permission on all user tables. 
It does not grant any Data Definition Language (`DDL`) permissions.
6.2) Implementing `EQ` requires executing the T-SQL command `CREATE EXTERNAL DATA SOURCE` (hereinafter `CEDS`).
Executing `CEDS` requires the permission `ALTER ANY EXTERNAL DATA SOURCE` (hereinafter `AAEDS`).
6.3)
`AAEDS` is a highly privileged DDL permission. 
Attempting to execute `CEDS` with `db_datareader` rights will fail with the «PERMISSION DENIED» error.
6.4) `AAEDS` grants the ability to access all database scoped credentials.
The official Microsoft documentation states: «this permission should be considered highly privileged and should only be granted to trusted principals in the system». 
6.5) Essentially, `E` politely refused you by offering you only `VLA`, and you mistook this refusal for a working compromise.
7) Overall, `EQ` in your context is not only non-viable, but also the worst of all available options.
The correct solutions for your task:
7.1) The best strategic long-term solution is Fast Healthcare Interoperability Resources+ Azure Health Data Services.
7.2) The immediate tactical solution for batch integration is ADF + Async Export via the `E` User-Specific Storage Container.