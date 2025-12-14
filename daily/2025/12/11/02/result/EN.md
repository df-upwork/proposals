1) In Python, starting from version 3.13 (which is built into Azure CLI ≥ 2.66.0), the `ssl.create_default_context` function sets the `VERIFY_X509_STRICT` and `VERIFY_X509_PARTIAL_CHAIN` flags by default:
1.1) https://docs.python.org/3/whatsnew/3.13.html
https://archive.is/BhVA3#selection-1787.0-1805.18
1.2) https://docs.python.org/3/library/ssl.html
https://archive.is/cow72#selection-2557.0-2575.29
2) `VERIFY_X509_STRICT` forces OpenSSL to perform certificate validation in strict compliance with IETF standards.
3) The correct way to resolve your problem is to use the `pip-system-certs` (`SC`) package to integrate Azure CLI with the Windows system certificate store.
`SC` dynamically substitutes the validation mechanisms of the `requests` module, redirecting checks from OpenSSL to the Windows System Cryptographic API (CAPI).
Windows, unlike Python 3.13 in strict mode, correctly processes corporate certificates without the `KeyUsage` extension if they are in the trusted store.