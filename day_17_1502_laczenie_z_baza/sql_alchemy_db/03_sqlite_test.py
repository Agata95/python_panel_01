from sqlalchemy import create_engine, text, URL

# połączenie Bitnami (virtualBox) z mysql-workbench
# baza nazywa się EH.EH_users
mysql_connect = URL.create(
    "mysql+mysqlconnector",   # moduł: mysql-connector-python
    username="root",
    password="Bitnami",  # plain (unescaped) text
    host="192.168.22.44",
    port=3306,
    database="EH",
)

sql_ = create_engine(mysql_connect, echo=True)

with sql_.connect() as conn:
    results = conn.execute(text("select * from EH_users"))

    print(results.all())