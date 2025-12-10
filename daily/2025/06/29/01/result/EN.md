The correct solution to your problem:
1) Implement a main program (`P1`) that will manage the entire migration process.
I recommend doing it in Python.
2) Implement a set of low-level programs (`P2s`) in the FileMaker scripting language.
3) `P1` will interact with `P2s` using the standard FileMaker `fmurlscript` technology (the `fmp://` URL scheme).
Calling `P2s` from `P1` in Python:
3.1) Windows:
```python
subprocess.run(['start', '', fmp_url])
```
3.2) macOS:
```python
subprocess.run(['open', fmp_url])
```
4) `P1` will read the database schema (structure) from FileMaker via `pyfilemaker2`: https://github.com/jeremie-borel/pyfilemaker2
5) The main `P2s` scripts will export data from FileMaker:
5.1) To CSV (for simple schemas).
5.2) To XML (for complex schemas).
6) `P1` will load the data into PostgreSQL using `psycopg`: https://github.com/psycopg/psycopg