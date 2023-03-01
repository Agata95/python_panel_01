from sqlalchemy import create_engine, and_
from faker import Faker
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.sql import text


meta = MetaData()
people = Table(
    'people', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('adress', String),
)


fake_ = Faker("pl-PL")
engine = create_engine("sqlite+pysqlite:///people.db", echo=True)
meta.create_all(engine)

with engine.connect() as conn:
    for xx in range(5):
        inserted = people.insert().values(name=fake_.name(), adress=fake_.street_name())
        conn.execute(inserted)
    conn.commit()

    # teraz select
    selected = people.select()
    result = conn.execute(selected)
    for row in result:
       print(row)

    print()
    # teraz select + where
    selected = people.select().where(people.c.id < 10) # Here c attribute is an alias for column
    result = conn.execute(selected)
    for row in result:
       print(row)

    selected = people.select().where(and_(people.c.id < 10, people.c.name > "B")) # Here c attribute is an alias for column
    result = conn.execute(selected)
    for row in result:
       print(row)

    # text sql
    s = text("select people.name, people.adress from people where people.name between 'A' and 'L'")
    res = conn.execute(s).fetchall()
    print(res)

    # update
    stmt = people.update().where(people.c.id == 1).values(name='UPDATE #1')
    conn.execute(stmt)
    selected = people.select().where(people.c.id ==  1) # Here c attribute is an alias for column
    result = conn.execute(selected)
    print(result.fetchall())

    # delete
    stmt = people.delete().where(people.c.name == "Kornelia Latko")
    conn.execute(stmt)
    conn.commit()