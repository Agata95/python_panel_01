from tinydb import TinyDB
import time

baza = TinyDB("baza_maili.json")

# clear database
baza.drop_tables()
table_log = baza.table("logs")

# od Python 3.8 - walrus operator
while(data := input("Podaj treść")) != "QUIT":
    table_log.insert({"message": data, "timestamp": time.time()})