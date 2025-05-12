Start projeto:
pip install -r requiments.txt
py -m app/main.py

Caso postgre apite erro de COLLATION VERSION execute:
ALTER DATABASE template1 REFRESH COLLATION VERSION
