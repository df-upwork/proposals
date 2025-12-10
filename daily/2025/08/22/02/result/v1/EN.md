1) The most probable cause of your «wrong format» problem is the use of the «timestamp without time zone» data type in PostgreSQL instead of the recommended «timestamp with time zone» type: https://www.postgresql.org/docs/current/datatype-datetime.html
The most probable reason that this problem was hidden when using Node.js is that the Node.js application was running on a different server than the Python application.
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