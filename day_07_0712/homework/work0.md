1. wykorzystaj moduły: dumper / json do wyświtlania informacji w naszej aplikacji

2. napisz prosty skrypt wykorzystujący moduły: pickle i json do wczytania danych z bazy i zapisu w human readable format ;-)

3. Wykorzystaj kod:
```
with open("nazwa_pliku") as f:
    w = f.readlines()

oraz:

from pathlib import Path
q = Path("nazwa_pliku").read_text()
```

do wczytania danych z pliku tekstowego - zobacz różnice.

