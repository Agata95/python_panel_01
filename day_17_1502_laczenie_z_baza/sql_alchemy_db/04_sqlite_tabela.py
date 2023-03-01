from sqlalchemy import create_engine, text, MetaData, Table, Column, String, Integer

sql_ = create_engine("sqlite+pysqlite:///sql_plik_02.db", echo=True)

# globalne dane o bazie, schemacie
meta = MetaData()
people = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('login', String),
    Column('password', String),
)

with sql_.connect() as conn:
    results = conn.execute(text("select * from users"))

    # inne wyszukiwanie
    print("-----------------------")

    selected_rows = people.select()
    results_2 = conn.execute(selected_rows)
    print(results_2.all())
