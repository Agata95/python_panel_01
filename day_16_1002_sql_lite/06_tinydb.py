# https://github.com/msiemens/tinydb
from tinydb import TinyDB, Query, where
db = TinyDB('db_test.json')
# na wszelki wypadek czyścimy
db.drop_tables()

table_email = db.table("tabela_email")
table_email.insert({"mail_from": "adam@jurkiewicz.tech"})

table_users = db.table("users")
table_users.insert({"login": "adasiek1", "password": "adasiek1"})

table_users.insert({"login": "adasiek", "password": "adasiek_pwd"})

# szukanie

users = Query()
users_q = table_users.search(users.login == "adasiek")
print(users_q)

users_2 = table_users.search(where('login') > "adasiek")
print(users_2)

users_2 = table_users.search(where('login') > "adas")
print(users_2)

users_2 = table_users.search(where('login') >= "adasiek")
print(users_2)
print("--------------------")
print(table_users.all())
print(table_email.all())