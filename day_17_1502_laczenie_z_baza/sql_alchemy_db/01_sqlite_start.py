from sqlalchemy import create_engine, text

# dla bazy sqlite, echo - pokazuje komunikaty na ekranie
sql_ = create_engine("sqlite+pysqlite:///:memory:", echo=True)

with sql_.connect() as conn:
    conn.execute(text("select 'hello world'"))