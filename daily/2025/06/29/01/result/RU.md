Правильное решение вашей задачи:
1) Разработать главную программу (`P1`), которая будет управлять всем процессом миграции.
Я рекомендую сделать её на языке Python.
2) Разработать набор низкоуровневых программ (`P2s`) на языке сценариев FileMaker.
3) `P1` будет взаимодействовать с `P2s` посредством стандартной для FileMaker технологии `fmurlscript` (через URL вида `fmp://`).
Вызов `P2s` из `P1` на Python:
3.1) в Windows:
```python
subprocess.run(['start', '', fmp_url])
``` 
3.2) В macOS:
```python
subprocess.run(['open', fmp_url])
``` 
4) `P1` будет читать cхему (структуру) базы данных из FileMaker посредством библиотеки `pyfilemaker2`:  https://github.com/jeremie-borel/pyfilemaker2
5) Основные скрипты `P2s` будут экспортировать данные из FileMaker:
5.1) В CSV (для простых схем).
5.2) В XML (для сложных схем).
6) `P1` будет загружать данные в PostgreSQL посредством библиотеки `psycopg`: https://github.com/psycopg/psycopg
 