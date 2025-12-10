I. The root cause of your issue lies in how Azure Database for PostgreSQL Flexible Server resolves Entra ID group memberships.
Successful group-based authentication requires the server to be able to resolve a user's membership in Entra ID groups.
This resolution can occur either at sign-in (Just-In-Time, JIT) or via background synchronization.
Background synchronization always requires interaction with the Microsoft Graph API, while JIT requires it only in specific scenarios (e.g., Group Claim Overage).
Regardless of the method used, the server requires authorization to read data from the client's tenant.
The service principal representing the Azure PostgreSQL service in the client's Entra ID must have the appropriate Microsoft Graph API permissions.
Typically, `GroupMember.Read.All` or `Directory.Read.All` permissions are required.
The absence of these permissions or the lack of Admin Consent for them is a common root cause of failures in resolving group membership.
Therefore, the most likely root causes are insufficient Microsoft Graph API permissions, lack of network access to the API, or misconfiguration of the group resolution method.
The choice of this group resolution method is determined by the `pgaadauth.enable_group_sync` server parameter.
II.
1) Mode 1: Group synchronization is disabled (default mode)
The `pgaadauth.enable_group_sync` parameter is disabled.
In this mode, PostgreSQL does not perform background synchronization of group membership.
Group membership verification occurs at sign-in time (JIT) and is primarily based on the analysis of claims in the user's access token.
1.1) Scenario 1.1: Using a UPN instead of the group name
1.1.1) Essence
Group authentication in this mode requires users to use the Entra ID group name as the username.
Authentication via the group fails if users attempt to sign in using their User Principal Name (UPN, e.g., `user@company.com`) while expecting to inherit group permissions.
1.1.2) Rationale
The system expects the group name as the username (in psql or DBeaver) and the user's personal access token as the password.
If users use their UPN, the system attempts to authenticate them based on their individual UPN role (direct mapping).
If the individual UPN role exists on the server (which explains why your direct mappings succeed), the login will be successful, but the user will not inherit the group's permissions.
If the individual UPN role does not exist (and only the group role is configured), authentication will fail (e.g., «role not found»).
1.2) Scenario 1.2: Group Claim Overage
1.2.1) Essence
This scenario occurs when a user is a member of too many Entra ID groups.
In this case, Entra ID does not include the full list of groups in the user's access token, but instead adds an overage claim.
Even if the user correctly specifies the group name upon sign-in (as per Scenario 1.1), authentication fails.
1.2.2) Rationale
When an overage occurs, the server must perform a JIT request to the Microsoft Graph API to retrieve the user's complete list of groups.
The request fails if the Azure PostgreSQL service principal lacks the required Microsoft Graph API permissions (e.g., `GroupMember.Read.All`) in the client's tenant, or if the server cannot establish an outbound connection to the Microsoft Graph API.
This connection failure can occur due to network issues (e.g., blocked traffic to the `AzureActiveDirectory` Service Tag in Network Security Groups (NSG) or issues with Custom DNS).
If the request is not successful, the server cannot confirm the user's membership in the target group, which leads to an authentication failure.
2) Mode 2: Group synchronization enabled
The `pgaadauth.enable_group_sync` parameter is enabled.
This mode is designed to enable UPN-based sign-in while inheriting group permissions.
The server performs a periodic background synchronization (usually every 30 minutes) of group membership via the Microsoft Graph API.
Authentication relies on pre-synchronized data, so a Group Claim Overage in the user's access token does not cause an authentication failure in this mode.
2.1) Scenario 2.1: Issues with accessing the Microsoft Graph API (permissions and network)
2.1.1) Essence
For background synchronization, the server requires access to the Microsoft Graph API (e.g., `graph.microsoft.com`).
Synchronization fails if the necessary Microsoft Graph API permissions are missing or if outbound network access is blocked.
Blocked network access is common in configurations with Private access / VNet integration, using NSG or Custom DNS.
2.1.2) Rationale
The background synchronization process involves making requests to the Microsoft Graph API.
First, the Azure PostgreSQL service principal must have the necessary permissions (e.g., `GroupMember.Read.All`) to read group memberships.
Second, these requests must pass through the client's network infrastructure.
Background synchronization fails if the permissions are missing, if outbound traffic to the `AzureActiveDirectory` Service Tag is blocked (e.g., in NSGs or User Defined Routes (UDRs)), or if DNS does not correctly resolve the Microsoft Graph API addresses.
Users cannot sign in via UPN when relying on group roles, as the server does not have up-to-date data about their membership.
2.2) Scenario 2.2: Synchronization latency
2.2.1) Essence
Group membership synchronization occurs periodically (30 minutes by default).
If a user was recently added to a group, the server may not yet have this information.
2.2.2) Rationale
Authentication in this mode relies on pre-synchronized data.
If the data is outdated, user authentication relying on new group permissions will fail, even if the configuration in Entra ID is correct.
Direct user authentication (if an individual role is configured) works because it is based on the user's Object ID (OID) in the access token and does not depend on the background group synchronization.