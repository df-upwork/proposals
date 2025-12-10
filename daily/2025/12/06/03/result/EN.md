1) In points 2-7, I outline your misconceptions.
In point 8, I outline the correct method to solve your problem.
2) You mistakenly believe that Google Datastream (hereafter — `Dᨀ`) is compatible with a MongoDB Replica Set accessed via Private Service Connect endpoints (hereafter — `PSC`).
In fact, this configuration is non-functional due to the combination of API restrictions and fundamental networking constraints.
The `Dᨀ` API prevents the use of the `directConnection` parameter (hereafter — `DC`), which is mandatory for private topologies where the discovered cluster nodes are not directly routable.
Without `DC`, the driver attempts to connect to the discovered backend nodes, which fails because they are unreachable in this network topology.
Furthermore, even with `DC`, the VPC Network Peering connection does not support transitive access to `PSC` endpoints.
3) You mistakenly believe that `Dᨀ` should have access to the Private DNS Zone of your network, and that the current behavior of `Dᨀ` (hereafter — `B𐏐`) is a failure.
In fact, `B𐏐` is explicitly stated in the official documentation of `Dᨀ` (hereafter — `D⸙`): «Datastream doesn't support Domain Name System (DNS) resolution in private connections»
https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration
4) You mistakenly attribute the routing of traffic destined for public IPs to «ignored» routes.
In fact, routing (Layer 3) occurs after DNS resolution.
Since DNS (due to `B𐏐`) resolved the hostname of Atlas (hereafter — `Aᨀ`) to a public IP, `Dᨀ` directed traffic to that destination.
The VPC Network Peering connection (hereafter — `P`) exchanges routes for the standard subnets containing `PSC`.
These routes were not «ignored» but were inapplicable to the public IP.
5) You mistakenly believe that the successful «VM Connectivity Test» proves the infrastructure is configured correctly.
In fact, the VM resides inside the VPC network and queries the local metadata server for DNS.
`Dᨀ` operates in the service producer network and uses independent Google internal DNS resolvers.
These resolvers have no access to your Private DNS Zone because `P` shares IP routes but not DNS records.
The VM has direct intra-VPC access to `PSC`.
Since `Dᨀ` resolves the hostname to a public IP, `Dᨀ` attempts to route traffic via the public internet instead of `P`.
Your test proves backend availability but not reachability via `P`.
6) You mistakenly believe that your «`Dᨀ` → `P` → `PSC`» topology is valid.
In fact, `D⸙` states: «The VPC Network Peering connection between your VPC network and the Datastream VPC network doesn't let Datastream connect to: Private Service Connect endpoints located in your VPC network»:
https://cloud.google.com/datastream/docs/private-connectivity
Traffic from `Dᨀ` cannot reach `PSC` in `datastream-net` because `P` does not support transitive access to `PSC` endpoints.
Even if you bypass the DNS problem by entering the IP manually, the Google SDN controller will drop the packets.
7) You might assume that using an intermediate TCP proxy or the «Forward SSH tunnel» connectivity method could resolve the connectivity issue.
In fact, these configurations are rendered ineffective by the API limitation described in point 2.
Since you cannot inject `DC`, the `Dᨀ` driver performs topology discovery and attempts to establish direct connections to the inaccessible internal backend nodes.
This results in a `ServerSelectionTimeoutError` distinct from the current DNS failures, yet the replication remains blocked.
8) `R`: the correct method to solve your task
8.1) Use Google Cloud Dataflow (hereafter — `DFᨀ`) instead of `Dᨀ`.
8.2) Develop a custom `DFᨀ` pipeline (hereafter — `PL`) using the Apache Beam `DebeziumIO` connector within your `datastream-net` VPC.
`PL` will read the change stream directly and write to your desired destination (e.g. GCS, BigQuery).
Note that the standard Apache Beam `MongoDbIO` connector currently supports only bounded (batch) reads and is unsuitable for real-time CDC.
8.3) Use the `mongodb://` connection string scheme because your Private DNS Zone lacks the SRV records required for the `mongodb+srv://` scheme.
Append the `tls=true` parameter to enforce encrypted communication, as `Aᨀ` requires TLS but the standard scheme does not enable it by default.
Set the `DC` parameter to `true` to force the driver to treat the `PSC` endpoint as the single entry point.
This configuration prevents connection failures caused by the driver attempting to access internal cluster nodes that are not directly routable behind the load balancer.
8.4) Enable «Private Google Access» on the `datastream-net` subnet to allow `DFᨀ` workers to reach Google Cloud APIs.
The workers will utilize your Private DNS Zone to resolve the `Aᨀ` hostname because they reside within the VPC network.
8.5) Connecting via the domain name ensures the successful validation of the `Aᨀ` TLS certificate.
8.6) `R` ensures that all replication traffic remains within the private network backbone.
---
My GitHub profile: https://github.com/dmitrii-fediuk