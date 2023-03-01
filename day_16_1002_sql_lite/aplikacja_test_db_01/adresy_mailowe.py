import sqlite3
from pathlib import Path
import sys

# tworzy bazę, jeśli ona nie istnieje
_data_base = "adresy_mailowe.db"

# zabezpieczamy się na to aby poinformować gdy baza nie istnieje i zakończyć działanie kodu
if not Path(_data_base).exists():
    print("Baza nie istnieje! Koniec.")
    sys.exit(2)

# kod błędu '2' - file not found

print(f"OK dla pliku {Path(_data_base)}")
connection_sql = sqlite3.connect(_data_base)

result = connection_sql.execute(f"SELECT * FROM address")
print(result.fetchall())