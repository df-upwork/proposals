I. «Which NetSuite connector do you recommend for our use case and why? List trade-offs and license costs.»
1) For the initial stage of the project, I recommend Celigo — it is the market leader in pre-built integrations between Magento and NetSuite: https://www.celigo.com/integrations/netsuite-magento 
2) Celigo fully meets and exceeds all the functional requirements outlined in your project description:
2.1) Celigo offers pre-built, bidirectional flows for all key entities: orders, customers, inventory, products (including images and attributes), prices, shipments, cancellations, and returns.
This fully covers your requirement for a «robust NetSuite connector».
2.2) Celigo allows synchronizing complex pricing policies, including NetSuite price levels as tier pricing in Magento.
2.3) Celigo also correctly handles promotions, cart-level and line-item discounts, as well as gift certificates..
2.4) Celigo is designed to handle high loads and millions of orders, and it also allows for the  connection of multiple Magento storefronts (websites, stores) to a single NetSuite account, which provides a foundation for future growth.
2.5) Celigo provides a dashboard for monitoring all integration flows, a real-time alerting system, and an AI-based error-handling system that, according to the company, automatically resolves over 95% of failures.
2.6) The subscription fee for Celigo for medium-sized companies is $12K-36K per year.
II. «Show one Magento project where you improved Core Web Vitals—before/after metrics and what you changed»
1) Of course, among my 500+ Magento projects on Upwork, I have had projects like that, but that was a long time ago, and the technologies used in them are no longer relevant in 2025.
In recent years, clients on Upwork have not hired me for that.
The reason why clients on Upwork have stopped paying for improving Core Web Vitals is obvious to me: it becomes too exensive for typical Upwork clients.
The standard Magento frontend is severely outdated: it uses long-outdated technologies (Knockout.js, jQuery, RequireJS), has a large DOM size, and an excessive amount of render-blocking JavaScript.
2) The correct solution to achieve high Core Web Vitals scores in 2025 is to replace the standard Magento frontend with either Hyvä or a PWA.
III. «Describe your 301 redirect and SEO migration process for 1,000+ URLs»
1) Managing these redirects at the Magento level (using the `url_rewrite` table) is inefficient.
2) It is significantly more efficient to handle this task at infrastructure levels upstream from Magento: the web server (Nginx), reverse proxy (Varnish), or CDN (Edge Redirects).
3) I recommend using Nginx — specifically, the `ngx_http_map_module`: https://nginx.org/en/docs/http/ngx_http_map_module.html#map.
This is a high-performance and highly scalable method due to the efficient in-memory hash table implementation in Nginx.
IV. «How do you structure category taxonomy for large catalogs to improve search and conversion?»
1) First and foremost, a well-designed system must separate the navigational hierarchy (the visible category tree for users and SEO) and the classification taxonomy (the internal structure for managing data, attributes, and faceted search).
2) Next, it is important to shift the focus from hierarchy to filtering: the main hierarchy should be shallow (a maximum of 2-3 levels) and serve only for initial grouping.
The main navigational load should be handled by robust faceted navigation.
For B2B, the ability to filter by technical specifications and compatibility is critical.
This ensures high-precision filtering by technical parameters — this is the primary method of navigation in complex B2B catalogs.
Regarding search accuracy, Magento (Elasticsearch/OpenSearch) uses attributes for ranking.
Configuring attribute weights (Search Weights) directly improves the accuracy of text search.
3) It is important to adapt the structure, category names, and attributes based on the analysis of real user search behavior (analysis of keywords, zero-result queries, industry jargon).
This ensures that the taxonomy uses the terms that buyers use, eliminating the gap between internal terminology and the market.
This analysis enables the configuration of synonym dictionaries in Elasticsearch to handle industry jargon, abbreviations, competitor part numbers, and common misspellings.
Analysis of failed searches helps to optimize the taxonomy structure.
4) It is important to structure the catalog based on the B2B purchasing context, implementing categorization by Use Case, Industry, or Compatibility, rather than just by product type.
This addresses the needs of buyers who are looking for a solution to a problem or a component for a system.
This helps users find related and compatible products.
V. «What’s your error-handling and alerting plan for connector failures (orders, inventory, pricing)?»
1) The cornerstone of reliable ERP integration is data idempotency: re-executing an operation (e.g., creating an order) must produce the same result as a single execution.
This is critically important for financial and operational integrity.
This prevents the duplication of orders, payments, or customer records in NetSuite.
This is a mandatory prerequisite for the safe implementation of automatic retries.
2) It is important to implement a dead-letter queue: to store transactions that could not be processed due to persistent errors after retry attempts have been exhausted.
This prevents the loss of critical data (orders).
Isolation of poison pill messages prevents head-of-line blocking of the main integration flow.
This enables the analysis and controlled reprocessing of messages after data or code corrections.
3) Automatic retry of operations is important for transient errors (network failures, NetSuite API timeouts, rate limits, record locks).
This provides protection against transient errors that are common in cloud APIs.
This significantly reduces the need for manual intervention and ensures eventual consistency.
4) It is important to have centralized logging and tracing: the collection, indexing, and analysis of logs from Magento, the connector, and NetSuite in a unified system (ELK, Datadog, etc.) using correlation identifiers (Correlation IDs).
This is a fundamental tool for Root Cause Analysis and debugging in a distributed architecture.
This ensures end-to-end visibility of transaction flows across all components.
5) Implement immediate alerting for responsible personnel regarding critical events.
6) It is important to validate data against business rules before synchronization.
7) It is important to perform reconciliation after synchronization: a comparison of data in Magento and NetSuite to identify discrepancies.
This process detects silent failures (when an error is not generated, but the data is incorrect or missing).
8) It is important to implement a Circuit Breaker in Magento: a mechanism that stops sending requests to an external service (NetSuite) if the failure rate exceeds a threshold, giving it time to recover.
This prevents cascading failures: it protects Magento and connector resources from exhaustion while waiting for a response from a failing system.
The fail-fast principle enables quick switching to a fallback mechanism (e.g., buffering) instead of waiting for a timeout.