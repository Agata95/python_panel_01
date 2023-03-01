from sqlalchemy import create_engine, text

# dla bazy sqlite, echo - pokazuje komunikaty na ekranie
sql_ = create_engine("sqlite+pysqlite:///sql_plik_02.db", echo=True)

with sql_.connect() as conn:
    results = conn.execute(text("select * from users"))
    rezultaty = results.all()
    # poniższe nie wykonuje się wielokrotnie
    for e in results:
        print("e", e)
    print(rezultaty)
    for elem in rezultaty:
        print(elem)