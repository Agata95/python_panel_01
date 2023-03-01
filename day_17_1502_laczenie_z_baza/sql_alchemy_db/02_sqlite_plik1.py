from sqlalchemy import create_engine, text

# dla bazy sqlite, echo - pokazuje komunikaty na ekranie
sql_ = create_engine("sqlite+pysqlite:///sql_plik_01.db", echo=True)

with sql_.connect() as conn:
    conn.execute(text("select 'hello world'"))