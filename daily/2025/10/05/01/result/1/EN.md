The most likely causes of your issue:
1) Incorrect configuration of the DNS servers in «Client VPN endpoint» (`E`)
https://archive.is/dzXYE#selection-2645.11-2645.62
1.1) Perhaps, old, inaccessible Akamai DNS servers are specified.
1.2) Perhaps, no DNS servers are specified at all (the field is left empty). 
In this case, the DNS configuration is not passed to the client, and it attempts to use its local DNS settings.
The subsequent behavior depends on the tunneling mode of `E` (split-tunnel or full-tunnel).
1.2.1) If split-tunnel mode is enabled, the client will be able to use local DNS servers to resolve public names, but will not be able to resolve internal names in the VPC.
In this mode, AWS VPN Client on Windows does not set Windows Filtering Platform (`WFP`) rules to block local DNS traffic.
1.2.2) If full-tunnel mode is used, all client traffic is directed into the VPN tunnel through the default route (`0.0.0.0/0`).
This route intercepts traffic, including DNS queries, to local and public DNS servers.
Additionally, when using the AWS VPN Client on Windows in full-tunnel mode, `WFP` rules are applied.
These rules force all DNS traffic into the tunnel and block access to local DNS servers to prevent DNS leaks.
If the DNS servers are not specified in the `E` configuration or are unavailable through the tunnel, this leads to a complete failure of DNS resolution.
2) Lack of required authorization rules.
https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rules.html
3) Incorrect configuration of Routes.
Routing issues depend on whether the split-tunnel mode is enabled on `E`.
3.1) Split-tunnel mode is enabled.
The `E` route table must contain a route to the network where the DNS servers are located.
In this mode, only the routes defined in the `E` route table are added to the client device's route table.
If a route to the DNS servers (e.g., `AmazonProvidedDNS` or Custom DNS) is missing from this table, it will not be added to the client device.
As a result, DNS queries cannot be routed through the VPN tunnel.
Since the client's local network usually does not have routes to the internal IP addresses of the VPC, the queries will fail (time out).
3.2) split-tunnel mode is disabled (full-tunnel).
All client traffic, including DNS requests, is routed into the VPN tunnel via the default route (`0.0.0.0/0`).
In this case, a failure can occur if the traffic cannot reach the DNS servers after entering the VPC.
The traffic enters the subnets associated with `E`.
It is necessary to check the VPC Route Tables of these associated subnets.
These tables must contain the correct routes to the DNS servers being used.
E.g., if Custom DNS servers in a remote network are used (connected via VPC Peering or a Transit Gateway), the corresponding routes are required in the VPC Route Table.
Also, if public name resolution over the internet is required, the VPC Route Table must contain a route to a NAT Gateway or an Internet Gateway.
The absence of these routes at the VPC level will lead to the loss of DNS packets.
4) Traffic filtering by Security Groups (`SG`).
4.1) When `E` is associated with subnets, traffic is subject to an `SG`.
If Custom DNS servers are used (e.g., on EC2 instances or a `R` Inbound Endpoint), this `SG` must allow Outbound traffic on port 53 (UDP/TCP) to these servers.
Traffic to `R` is not filtered by `SG`.
4.2) If Custom DNS servers located inside the VPC (e.g., an EC2 instance or a `R` Inbound Endpoint) are used, it is necessary to check their own `SG`.
This `SG` must allow Inbound traffic on port 53 (UDP/TCP).
The Source for this Inbound rule must be the `SG` associated with `E`.
4.3) The network traffic flow has changed after the migration from Akamai.
New rules might not have been added or existing rules may be blocking traffic from the Client VPN network interfaces.
5) Traffic blocking by Network Access Control Lists (NACLs).
`E` is associated with specific subnets in the VPC.
Traffic passing through these subnets is filtered by Network Access Control Lists (NACLs).
However, traffic to `R` is not filtered by NACLs.
Therefore, NACLs configuration is required only when using custom DNS servers (e.g., located on EC2 instances or a `R` Inbound Endpoint).
In this case, it is necessary to consider that NACLs are stateless (they do not track connection state).
Unlike `SG`s, NACLs require explicit rules for both outbound and return traffic at the Subnet level.
It is necessary to check the NACLs for the subnets associated with `E` (the source subnets), and the NACL for the Subnet where the Custom DNS servers are located (the destination Subnet), if they are different.
Outbound NACL rules for the source subnets must allow traffic on port 53 (UDP/TCP) to the target subnet.
Inbound NACL rules for the source subnets must allow return traffic from the target Subnet to the ephemeral ports (typically the range `1024-65535`).
Inbound NACL rules for the target Subnet must allow traffic on port 53 (UDP/TCP) from the source subnets.
Outbound NACL rules for the target Subnet must allow return traffic to the ephemeral ports (`1024-65535`) to the source subnets.
The absence of any of these rules will result in DNS failures when using Custom DNS servers.