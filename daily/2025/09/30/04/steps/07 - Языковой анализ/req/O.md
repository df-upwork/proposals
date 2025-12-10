# 0.
Сегодня 2025-10-01.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021973162834964667109

## 2.2. Title
Urgent: WordPress/LearnDash Developer Needed to Fix Login Redirection Issue

## 2.3. Description
`PD` ≔ 
```text
Users are being redirected back to the login page when trying to access courses or lessons, even though they are already logged in.

This creates daily frustration for users and a massive support burden for our staff.

We’ve tried numerous solutions with different developers, and even LearnDash support has pointed out it’s likely tied to WordPress sessions, cookies, or permalink handling. 
Our current developer has been investigating, but we need someone who can come in quickly, isolate the root cause, and implement a permanent fix.

# What’s Happening:
- Users log in successfully, but when they click into a course/lesson, they are redirected back to the login page.
- Clearing cache or logging in via an incognito/private browser often “fixes” the issue temporarily.
- We’ve tested staging, but staging doesn’t replicate live user sessions (problem only shows with real user activity).

# Environment Details:
- Platform: WordPress &#43; LearnDash LMS
- Hosting: cPanel/WHM (Apache, PHP-FPM, MariaDB), with Google Cloud storage integration in progress

# Logs we have:
- Custom MU plugin logging logins, cookies, and referrers
- login-audit.log tracking user logins in real time
- Apache/domlogs

# What We’ve Already Tried:
- Clearing and resetting server/session caches
- Restarting Apache/PHP-FPM
- Flushing OPcache, deleting /tmp session files
- Creating custom logging MU plugin to track login/session cookies
- Testing staging (problem does not reproduce there — only live with active users)

# What We Need From You:
- Diagnose and fix the root cause of the login redirection issue
- Audit session/cookie handling (WordPress core &#43; LearnDash &#43; any custom plugins)
- Ensure the fix works across all courses and lessons without having to manually update permalinks
- Provide a clear report of the root cause and implemented solution so we can maintain it long term

# Bonus Points if You Can:
- Suggest and implement hardening for session handling, caching, and redirects
- Audit our LearnDash &#43; WordPress setup for other performance or stability issues
- Set up better logging so future issues can be quickly diagnosed

# Requirements:
- Proven experience with WordPress core session/auth systems
- Deep knowledge of LearnDash (courses, lessons, redirects, logins)
- Strong debugging skills (server logs, PHP logs, WordPress hooks/filters)
- Able to start immediately and work directly on our live system during peak hours (with our oversight)

# Deliverables
1. Permanent fix to the login redirection issue
2. Documentation of root cause + steps taken
3. Recommendations for long-term maintenance
```

## 2.4. Tags
WordPress core debugging (authentication, sessions, redirects)
LearnDash LMS deep experience (courses, lessons, login/session flows)
PHP (advanced debugging and plugin development)
Apache/Nginx server configuration (cPanel/WHM environments
Cookie/session handling in WordPress
MySQL query troubleshooting
BuddyBoss
Redis, Memcached, Opcache
sign-on (SSO
Google Cloud Storage

## 2.5. Questions
### 2.5.1.
Have you fixed login redirection/session loop issues in WordPress or LearnDash before? 
If yes, please describe the root cause and solution.

### 2.5.2.
How would you approach debugging this issue without disrupting live students?

### 2.5.3.
What’s your process for isolating a plugin conflict vs. WordPress core issue?

### 2.5.4.
Do you have experience with multi-server environments or caching conflicts

### 2.5.5.
How quickly could you start and provide an initial root cause analysis?

# 5. Информация о `ꆜ`
## 5.1. Местоположение

United States
Lake Mary

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
10-99

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Oct 11, 2017
### 5.3.2. Hire rate (%)
81
### 5.3.3. Количество опубликованных проектов (jobs posted)
77
### 5.3.4. Total spent (USD)
$162K
### 5.3.5. Количество оплаченных часов в почасовых проектах
11996
### 5.3.6. Средняя почасовая ставка (USD)
12.95

# 6.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
Users are being redirected back to the login page when trying to access courses or lessons, even though they are already logged in.
~~~
```

# 7.
## 7.1.
`Aᨀ` ≔ (мой потенциальный ответ `ꆜ`)

## 7.2.
Содержание `Aᨀ`:
~~~markdown
I have identified the 2 most likely causes, which can cause this problem independently or in combination.
I outline them in points 1 and 2 below.
The «WordPress sessions» cause, to which LearnDash support pointed you, is far less likely.
I discuss it in point 3.
1) Cause #1: Incorrect configuration of caching or intermediary layers (Proxy/CDN).
1.1) Essence:
This cause most likely manifests under scenario 1.1.1.
Scenario 1.1.2 is much less likely for the reason in point 1.2.3.
1.1.1) Incorrect operation of Page Caching and Redirect Caching.
This is the most common mechanism.
WordPress authentication is based on cookies (names start with `wordpress_logged_in_`).
Page Caching systems (e.g., at the web server level, such as Apache, Proxy, CDN, or caching plugins) must be configured to bypass cache when these cookies are present.
Using the vary cache mechanism is incorrect in this case.
The value of authentication cookies is unique for each user session.
Varying the cache based on a unique value will create a separate cache entry for each session.
This completely negates the effectiveness of Page Caching (Cache Hit Rate).
If the configuration is incorrect, the caching system ignores these cookies and processes the request as an anonymous one.
When an authorized user requests a protected URL (e.g., a course or a lesson), the caching system may return a response previously saved for a guest (Cache HIT).
If a redirection response (an HTTP 302 to the login page, which is generated for guests) has been cached for this URL, the user is immediately redirected back to the login page.
In this scenario, the request is served by the caching system.
PHP may not execute at all (if the cache is served by the Apache web server, a Proxy, or a CDN).
Alternatively, PHP execution may be interrupted at an early stage (e.g., via the `advanced-cache.php` Drop-in mechanism when using WordPress caching plugins).
1.1.2) Improper Cookie Stripping.
An intermediate layer (e.g., a CDN, Proxy, Load Balancer, or the Apache web server configuration) may be incorrectly configured to strip authentication cookies before the request reaches the WordPress application.
In this scenario, the request reaches the WordPress core.
However, since the authentication cookies are absent, the `is_user_logged_in()` function returns `false`.
To protect the content, WordPress (often via the `auth_redirect()` function) or LearnDash immediately initiates a redirection to the login page.
1.2) Rationale:
1.2.1) You write that clearing the cache or logging in via an incognito/private browser often «fixes» the issue temporarily.
1.2.2) This indicates that the user is receiving a stale state.
This is a strong indicator of receiving a cached redirect (Scenario 1.1.1).
Client-side actions cannot fix the server configuration, but they can temporarily bypass the issue by changing the state of the request or the local cache.
This occurs through 2 mechanisms:
1.2.2.1) Interaction with browser cache.
In Scenario 1.1.1, the server-side caching system incorrectly returns a cached redirect response (e.g., HTTP 302).
If this response contains cache control headers (e.g., `Cache-Control` or `Expires`) added by the caching layer, the browser may store it locally.
In this case, the browser performs the redirection locally without contacting the server again.
Clearing the browser cache or using incognito mode forces the browser to discard the locally stored response and send a new request to the server.
1.2.2.2) Temporary bypass of server-side cache.
Incognito mode or clearing cookies require re-login.
The login process changes the session characteristics.
E.g., the `wp-login.php` response contains the `Set-Cookie` header.
Some caching systems may interpret this as a signal to temporarily disable the cache for this session (e.g., the Hit-for-Pass mechanism).
Also, the request immediately following login may contain a specific `Referer` header.
These factors may allow the first request after login to successfully reach WordPress, bypassing the incorrect cached response.
However, on subsequent requests, when these conditions are no longer met, the problem returns.
1.2.3) Symptom 1.2.1 makes Scenario 1.1.2 much less likely than Scenario 1.1.1.
If the infrastructure configuration were homogeneous, a persistent cookie stripping rule would be applied to every request, and client-side actions would not result in a temporary solution.
However, in a non-homogeneous environment with multiple servers (e.g., behind a load balancer), where the configuration might not be identical, it is possible that only some of the nodes incorrectly strip cookies.
In such a case, starting a new session might direct the user to a correctly functioning node, which would create the appearance of a temporary fix for the problem.
2) Cause #2: Incorrect operation of object caching.
2.1) Essence:
In the project tags, you have specified Redis and Memcached.
If your system uses these technologies for object caching, critical data for authentication are cached in memory.
WordPress uses session tokens (stored in `wp_usermeta`) to track the user's login state.
Under high load, the state of these tokens in the object cache can become inconsistent with the current state of the MariaDB database.
When a user navigates to a protected page, WordPress performs an authentication check using the `wp_validate_auth_cookie()` function.
With a persistent object cache, this function uses it as the primary data source to retrieve session tokens (e.g., via `get_user_meta()`).
If WordPress reads an incorrect (stale or corrupted) session token from the cache (cache hit), the authentication check fails.
As a result, WordPress considers the user unauthenticated (the `is_user_logged_in()` function returns `false`) and initiates a redirection to the login page.
This can occur in two scenarios.
2.1.1) Stale Cache
When session tokens are updated in the database (e.g., upon login, logout, or automatic session extension), the corresponding data in the object cache must be invalidated or updated.
If the invalidation mechanism works incorrectly (e.g., due to a configuration error, a plugin conflict, or database replication issues), subsequent requests may receive stale data from the cache.
Using a stale token leads to an authentication failure.
2.1.2) Race Condition
Under high load and concurrent requests (e.g., AJAX), a race condition can occur when updating Session Tokens in the cache.
Although the basic operations (e.g., GET, SET) in Redis and Memcached are atomic, the race condition occurs at the application Logic level in the read-modify-write cycle.
This cycle (the application reads the token array from the cache, modifies it in PHP, and writes it back) is not atomic.
If multiple processes simultaneously modify this array, it can lead to a lost update and an inconsistent state in the cache.
Reading the incorrect state of session tokens leads to an authentication failure.
2.2) Rationale:
2.2.1) The combination of high user activity (which is present on production but not on staging) and the use of an external object cache creates the conditions for stale cache and race condition.
2.2.2) This mechanism explains why users are redirected, «even though they are already logged in».
The authentication cookie is present in the browser, but the authentication xheck fails due to a temporary inconsistency of the session tokens in the object cache during a specific request.
3) Cause #3: Problems with PHP native sessions.
3.1) Essence:
This cause is far less likely (rationale in point 3.2), but it should be considered, as there are signs of the use of PHP native sessions (`$_SESSION`) in your system.
Although WordPress core does not use `$_SESSION` for authentication, some plugins (e.g., BuddyBoss, mentioned in the tags) can activate them.
Your actions of deleting `/tmp` session files also suggest their use.
If `$_SESSION` are active, this creates concurrency challenges under high load (which exists on production but not on staging).
Specific problems depend on the PHP `session.save_handler` configuration and manifest in 2 main scenarios:
3.1.1) Session Locking.
If the standard handler (`session.save_handler = files`) is used, parallel requests (e.g., AJAX) block each other when calling `session_start()`.
This leads to resource contention and significant delays.
3.1.2) Race Conditions.
If an external handler (e.g., Redis or Memcached, mentioned in the tags) is used with disabled or ineffective locking, parallel requests can corrupt session data.
3.2) Rationale for low probability.
These scenarios are unlikely to be the direct cause of the redirection loop due to a symptom mismatch.
3.2.1) Session Locking (point 3.1.1) leads to performance bottlenecks.
Symptoms typically include server errors (e.g., HTTP `504 Gateway Timeout` or HTTP `500 Internal Server Error`), rather than a pure redirect (HTTP `302`) to the login page.
3.2.2) Race Conditions (point 3.1.2) cause data corruption in `$_SESSION`.
This can affect the logic of the plugins (LearnDash/BuddyBoss), but it does not affect the standard WordPress core authentication mechanism.
WordPress core authentication is based on cookies and session tokens, and not on `$_SESSION`.
3.2.3) Overall, these mechanisms contribute to the general instability of the system under load, and not specifically to this problem with the redirection loop.
4) «How would you approach debugging this issue without disrupting live students?»
4.1) Passive Diagnostics
The goal of this stage is to identify the layer generating the redirection (CDN, Proxy, Apache, or WordPress/PHP) without making changes to the production code or configuration.
4.1.1) Analysis of configuration and HTTP Headers (diagnosing Cause #1).
4.1.1.1) Analyze the configuration of all page caching layers (CDN, Proxy, Apache modules, WordPress plugins) for authentication cookie handling rules.
4.2.2.2) Analyze HTTP Response headers (e.g., `X-Cache`, `Cache-Control`, `Age`) for requests to protected URLs.
The presence of headers indicating a cache hit in the HTTP 302 response will confirm Scenario 1.1.1.
4.1.2) Object Cache Analysis (diagnosing Cause #2).
4.1.2.1) Analyze the Redis/Memcached integration configuration.
4.1.2.2) Analyze cache operations (GET/SET/DELETE) related to session tokens during test login attempts using real-time monitoring tools (e.g., `redis-cli monitor`).
This allows for observing potential inconsistencies (stale cache or race conditions) without flushing the global cache, which would cause a forced logout of all students.
4.1.3) Analysis of existing logs.
Perform a correlation analysis of the Apache `domlogs`, `login-audit.log`, and the logs from your MU plugin to identify redirection patterns.
4.2) Conditional Debugging
If passive diagnostics do not provide a definitive answer, proceed to active debugging methods.
4.2.1) Enhanced Logging.
Modify the MU plugin for detailed logging of the authentication process (e.g., the result of `wp_validate_auth_cookie()`) and the state of cookies.
This logging will be activated only with a special debug cookie or for a specific test `user_id`.
4.2.2) Controlled Cache Bypass.
Temporarily configure rules to force a page cache bypass only for test requests.
Use the `wp_using_ext_object_cache` filter to temporarily disable the object cache only for my test session.
4.3) Staging Reproduction
Since the problem depends on the load, conduct Load Testing on the Staging environment.
Using tools (e.g., Apache JMeter or k6), simulate parallel authenticated sessions to artificially create race conditions (Cause 2.1.2).
This will allow to safely reproduce the problem and test the fixes before deployment to production.
5) «What’s your process for isolating a plugin conflict vs. WordPress core issue?»
5.1) General principle: systematic isolation.
Systematically simplifying the Runtime Environment to a minimal configuration (vanilla WordPress).
This makes it possible to determine whether the failure is caused by the code of third-party components (plugins or the theme) or by the base platform (WordPress Core or infrastructure).
5.2) Isolation procedure on production.
5.2.1) Creating a clean environment. 
Using the conditional deactivation technique.
This is implemented via a Must-Use Plugin (`mu-plugin`) or specialized tools (e.g., the «Health Check & Troubleshooting» plugin).
This method creates a clean environment (deactivates plugins and switches the theme to a default one, e.g., Twenty Twenty-Five) only for my admin session.
Other users continue to use the website without any changes.
5.2.2) Baseline Check.
Attempt to reproduce the problem in the isolated clean environment (point 5.2.1).
5.2.2.1) If the problem is reproduced — this indicates a problem in WordPress core, Must-Use Plugins (including your custom MU plugin for logging) or the infrastructure configuration (server configuration, caching layers).
In this case, proceed to the analysis of the infrastructure and WordPress core (point 5.2.4).
5.3.2.2) If the problem is not reproduced - this confirms a plugin conflict or a theme conflict.
In this case, proceed to the isolation of the conflicting component (point 5.2.3).
5.2.3) Isolating the conflicting component.
5.2.3.1) Activate components while maintaining the isolated session.
5.2.3.2) First, activate the current theme. 
If the problem returns, the source of the conflict is in the theme.
5.2.3.3) If not, activate the critical plugins (LearnDash, BuddyBoss). 
Then use the Binary Search Method: activate half of the remaining plugins and check if the problem reproduces. 
Repeat the process, narrowing the search to identify the specific plugin or combination of plugins causing the conflict.
5.2.4) Differentiating between WordPress core and infrastructure.
5.2.4.1) Check the integrity of WordPress core files for modifications.
5.2.4.2) Analyze the infrastructure configuration (Apache, PHP-FPM, Redis/Memcached, Caching rules), as these are the most likely causes for production-only problems (as described in points 1-3).
5.3.4.3) If the previous steps do not reveal the cause, consider the possibility of an error in WordPress core.
In this case, perform deep debugging using Xdebug to analyze the authentication flow and search for known issues in WordPress Trac.
~~~
 