Вот конкретные правки к `Aᨀ` для устранения `𐒌⠿`:

## 1.
В пункте 3 замени первые два абзаца:
«The correct way to resolve your problem is to use the `pip-system-certs` (`SC`) package to integrate Azure CLI with the Windows system certificate store.
`SC` dynamically substitutes the validation mechanisms of the `requests` module, redirecting checks from OpenSSL to the Windows System Cryptographic API (CAPI).»
На следующий текст:
«The correct way to resolve your problem is to use the `truststore` package to integrate Azure CLI with the Windows system certificate store.
`truststore` dynamically substitutes the validation mechanisms of the `requests` module, redirecting checks from OpenSSL to the Windows System Cryptographic API (CAPI).»

## 2.
В пункте 3 замени третий абзац:
«Unlike Python 3.13 in strict mode, Windows correctly processes corporate certificates without the `KeyUsage` extension if they are in the trusted store.»
На следующий текст:
«Unlike Python 3.13 in strict mode, Windows permissively accepts corporate certificates without the `KeyUsage` extension if they are in the trusted store.»