1) В Python, начиная с версии 3.13 (которая встроена в Azure CLI ≥ 2.66.0) функция `ssl.create_default_context` по умолчанию устанавливает флаги `VERIFY_X509_STRICT` и `VERIFY_X509_PARTIAL_CHAIN`:
1.1) https://docs.python.org/3/whatsnew/3.13.html
https://archive.is/BhVA3#selection-1787.0-1805.18
1.2) https://docs.python.org/3/library/ssl.html
https://archive.is/cow72#selection-2557.0-2575.29
2) `VERIFY_X509_STRICT` принуждает OpenSSL проводить валидацию сертификатов в строгом соответствии со стандартами IETF. 
3) Правильный способ устранения вашей проблемы — использовать пакет `pip-system-certs` (`SC`) для интеграции Azure CLI с системным хранилищем сертификатов Windows.
`SC` осуществляет динамическую подмену механизмов валидации модуля `requests`, перенаправляя проверки из OpenSSL в системный криптографический API Windows (CAPI).
Windows, в отличие от Python 3.13 в строгом режиме, корректно обрабатывает корпоративные сертификаты без расширения `KeyUsage`, если они находятся в доверенном хранилище.
