1) Your problem is almost surely caused by a violation of canonical JSON serialization: https://github.com/Polymarket/py-clob-client/issues/164
2) Short explanation:
The Polymarket server requires that the JSON request body be serialized in a compact format (without spaces between keys and values) for HMAC signature verification (L2).
The standard `json` library in Python adds spaces by default during serialization (e.g. `{"key": "value"}` instead of `{"key":"value"}`).
If the byte representation of the request body sent over the network differs from the one used to generate the signature, the server rejects the request with code 401.
3) Detailed explanation:
3.1) The standard `json` library in Python, specifically the `json.dumps()` method, defaults to a serialization format that adds spaces after separators to improve human readability.
3.2) The default separators used in Python are defined as `separators=(', ', ': ')`.
This means that the object `{'a': 1}` is converted into the string `'{"a": 1}'` (with a space after the colon).
3.3) However, high-performance APIs, such as Polymarket CLOB, often require (or imply) a «canonical» or «compact» JSON form for calculating signatures to minimize traffic and eliminate ambiguity.
The compact form does not contain spaces: `'{"a":1}'`.
3.4) The `requests` library, which is used by the vast majority of Python bots, implicitly calls `json.dumps()` with default settings when a dictionary is passed to the `json=` parameter.
Thus, formatted JSON (containing extra whitespace) is sent over the network.
3.5) If the signing logic inside the bot (or the `py-clob-client` library used by it) calculates the signature based on the compact JSON form (which is the standard for crypto-signatures), a critical mismatch occurs:
- Client Sign: `Hmac(Secret, Timestamp + POST + /order + {"price":10})`
- Network Payload: `{"price": 10}`
- Server Verify: `Hmac(Secret, Timestamp + POST + /order + {"price": 10})`
3.6) As a result, the hashes do not match.
The server will return `401 Unauthorized`, because the signature does not correspond to the transmitted body.
---
My GitHub profile: https://github.com/dmitrii-fediuk