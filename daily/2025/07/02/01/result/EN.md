PostgREST is set up as follows:
1) Create a dedicated schema for the API (e.g., `api`) and place only objects that should be accessible externally there.
As such, `VIEW` and `FUNCTION` should be used, rather than the tables themselves.
The main data tables must be located in a separate, private schema (e.g., `private`), which is not specified in the PostgREST configuration and, therefore, remains invisible to HTTP clients.
1.1) A more robust variant of point 1 is to use versioning for the public schema. 
The first version can be named `api_1`. 
When a new version of the API is released, create another schema for it: `api_2`.
This stronger solution enables the simultaneous support of multiple API versions: a modern version for new clients and a legacy version for existing clients (giving them time to migrate).
2) The PostgREST authentication and authorization system is entirely based on the PostgreSQL role model.
For correct operation, it is necessary to create at least 3 types of roles:
2.1) `authenticator`: used for connecting PostgREST to the database.
2.2) `anonymous`: used for processing requests from anonymous users.
2.3) Roles representing authenticated users with different access levels.
3) Authorization in PostgREST is controlled by the standard PostgreSQL `GRANT` and `REVOKE` commands.
Each role must be precisely defined in terms of the operations it can perform on the objects in the `api` schema.
4) Configuring `postgrest.conf`:
4.1) `db-uri`: a value like `postgres://authenticator:<password>@localhost:5432/<database_name>`
4.2) `db-schemas`: specifies a comma-separated list of database schemas to be exposed through the API (point 1 above).
4.3) `db-anon-role`: the name of the database role to be used for processing unauthenticated requests (point 2.2 above).
4.4) `jwt-secret`: a secret key used to verify the cryptographic signature of a JSON Web Token (JWT).
4.5) `server-port`: The TCP port on which PostgREST will listen for HTTP requests.
By default, port `3000` is used.
4.6) `admin-server-port`: the port for the administrative server, which provides endpoints for the health check.
5) PostgREST uses a stateless authentication mechanism.
Each protected request must contain an `Authorization: Bearer <token>` header, where `<token>` is a valid JSON Web Token.
6) PostgREST only verifies tokens, but does not create them.
The `pgjwt` extension can be used to create tokens: this allows creating a simple SQL login function that accepts credentials, verifies them against a user table, and upon success, returns a signed JWT.
7) Row-Level Security (RLS) enables granular access control.
The combination of claims in the JWT and RLS policies creates an extremely flexible system.
PostgREST passes the claims from the token to the PostgreSQL session, where they are accessible via the function `current_setting('request.jwt.claims', true)`.
This allows RLS policies to make decisions based on token data, such as `user_id` or `tenant_id`.
8) Running the PostgREST process directly from the terminal command line is not suitable for a production environment because the process will not automatically restart in case of a failure or after a server reboot.
`systemd` manages the application lifecycle on most modern Linux distributions.
9) PostgREST does not implement HTTPS, delegating this function to external components.
In a production environment, transferring data, especially credentials or confidential information, over the insecure HTTP protocol is unacceptable.
Therefore, it is necessary to configure a reverse proxy server (for example, Nginx) to terminate SSL/TLS connections.
10) Enabling HTTPS requires a certificate.
It is best configured through Certbot and Let's Encrypt.
11) PostgREST automatically creates a standard RESTful interface for the tables and views specified in the API schema.
For the `table` table, the following main endpoints will be available:
11.1) `GET /table`
11.2) `POST /table`
11.3) `PATCH /table?id=eq.<id>`
11.4) `DELETE /table?id=eq.<id>`
12) To perform a POST (point 11.2 above), it is necessary first to obtain a JWT and then use it for authentication.
13) PostgREST returns error messages in JSON format with the following fields:
- `message`: The main text of the error message.
- `details`: Additional details.
- `hint`: A hint about a possible solution.
- `code`: either a 5-digit PostgreSQL error code (e.g.: `23505`), or a PostgREST code (e.g.: `PGRST100`).