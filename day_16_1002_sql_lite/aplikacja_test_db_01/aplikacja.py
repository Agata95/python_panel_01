from tinydb import TinyDB, Query

baza = TinyDB("baza_maili.json")

# clear database
baza.drop_tables()

baza.insert({"login": "agata", "password": "admin1234"})
baza.insert({"login": "user_01", "password": "pwd_01"})
baza.insert({"login": "user_02", "password": "pwd_02"})

table_adresy = baza.table("adresy_osob")
table_adresy.insert({"name": "Pszczolka Maja", "address": "Warszawskie Ogrody"})

# wyszukiwania
search = Query()
wyniki = baza.search(search.login == "agata")
print(wyniki)

wyniki2 = baza.search(search.name == "Pszczolka Maja")
print(wyniki2)
# pusto, przez to, że szukamy w bazie, a nie w table_adresy

wyniki3 = table_adresy.search(search.name == "Pszczolka Maja")
print(wyniki3)

# print all from 'baza'
print("baza:", baza.all())
print("table_adresy:", table_adresy.all())
