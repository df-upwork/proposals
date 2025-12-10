1) The cause for your «wrong format» problem is obvious to me — it is the differences in the interpretation of timestamps by the PostgreSQL drivers for Node.js (`node-postgres` or `pg`) and Python (`asyncpg`, `psycopg2`).
1.1) `node-postgres` by default converts `TIMESTAMP` (without time zone) values to the local time of the Node.js process (determined by the TZ environment variable). This often leads to confusion if the data is stored in UTC.
1.2) `asyncpg` (the standard asynchronous driver for FastAPI) always returns the time in UTC when working with `TIMESTAMPTZ`, ignoring the PostgreSQL session's `TimeZone` setting.
1.3) If the database schema uses `TIMESTAMP` instead of the recommended `TIMESTAMPTZ`.
`TIMESTAMP` stores the value as is, without any time zone information.
Combined with the behavior of the `node-postgres` driver, using this data type often leads to data intended as local time being saved without context.
When migrating to Python, which can interpret these «naive» values as UTC, a time shift occurs.
1.4) Python strictly distinguishes between «naive» and «aware» datetime objects. FastAPI/Pydantic serializes them differently: «aware» objects receive a timezone indicator (e.g., Z or +00:00), while «naive» ones do not.
If the Python application returns «aware» dates in UTC (which often happens when using asyncpg or `TIMESTAMPTZ`), the client side sees the UTC format.
If previously Node.js/Moment.js performed an explicit conversion to local time and returned it as a «naive» string, the client side will interpret the new format as an error.
Also, if Python returns naive dates (e.g., using `datetime.utcnow()`), timezone information is lost upon serialization.
2) The most probable cause for your «null» problem: storing problematic dates in a non-standard format.
The Python application probably uses the Pydantic library to process dates.
Moment.js can successfully parse a wide variety of and even incomplete string representations of dates.
Pydantic, in contrast, adheres to a strict «fail fast» philosophy and by default expects that date and time strings will conform to the ISO 8601 standard.
When FastAPI retrieves data from the database to create the API response, it apparently uses Pydantic models to validate and type this data.
If a field annotated as `datetime` receives a string from the database in a non-standard format (e.g., "10/27/2023", "27 Oct 2023" or even an empty string ""), Pydantic will not be able to parse it and will generate a `ValidationError` exception.
Then, this exception is caught by the `except` block of the application’s `try...except` statement, where the error is suppressed, and the value of the problematic field is forcibly set to `None`, which becomes `null` upon JSON serialization.
---
My GitHub profile: https://github.com/dmitrii-fediuk
My websites: https://df.tips?order=views and https://mage2.pro?order=views