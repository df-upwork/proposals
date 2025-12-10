1) Federated Learning (`FL`) enables joint training of a single global model while keeping training data decentralized, eliminating the need to transfer source data to a central repository.
Rather than moving the data to the model, the model moves to the data.
2) In your Health & Fitness sector, data is highly sensitive.
`FL` ensures that user data remains local.
This is critically important for complying with regulatory requirements (e.g., HIPAA) and increasing user trust.
3) While the data remains decentralized, the orchestration of the training process can be either centralized or decentralized.
3.1) Centralized (`T1`)
A central server (Orchestrator) coordinates the entire process: distributes the model, collects updates, and aggregates them.
Its advantages include simplicity of implementation and management, and fast model convergence.
Its main disadvantage is that the central server is a single point of failure and a potential bottleneck.
3.2) Decentralized (`T2`)
There is no server; clients exchange updates directly.
Its advantage is increased fault tolerance.
Its disadvantages include the complexity of coordination and security, and slow convergence.
4) Given your company size (2-9 people), I recommend `T1`, as it is significantly easier to manage.
The Databricks platform will act as the central orchestrator.
5) The training process for `T1`:
5.1) The central server creates a baseline global model.
5.2) The model is sent to selected participants (clients), who then train it on their local data.
5.3) Clients send only the model updates (weights or gradients) to the server.
5.4) The server aggregates these updates to improve the global model.
5.5) The cycle is repeated until the required model accuracy is achieved.
6) Databricks does not provide its own built-in framework for the `FL` process.
7) Databricks Lakehouse is an infrastructure for orchestrating, managing, and scaling `FL`.
8) It is necessary to distinguish `FL` from Databricks Lakehouse Federation. 
The latter allows executing SQL queries against external sources without data movement.
These are different technologies.
9) Data in Health & Fitness varies greatly between users (different demographic groups, activity levels).
This is called statistical heterogeneity.
Standard aggregation may perform poorly or converge slowly under these conditions.
10) It is necessary to use specialized open-source frameworks to implement the `FL` logic on top of the Databricks infrastructure.
The server-side of the framework is deployed on the Databricks cluster, and the client-side is deployed on devices or in silos.
---
My GitHub profile: https://github.com/dmitrii-fediuk