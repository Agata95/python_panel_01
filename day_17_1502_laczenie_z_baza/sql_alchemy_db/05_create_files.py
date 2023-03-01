from sqlalchemy import create_engine, text, MetaData, Table, Column, String, Integer
from faker import Faker
from random import randint

fake_ = Faker("pl-PL")

bazy = (
    "baza_01.db",
    "baza_02.db",
    "baza_03.db",
    "baza_04.db",
)

for baza in bazy:
    sql_ = create_engine(f"sqlite+pysqlite:///{baza}", echo=True)

    meta = MetaData()
    people = Table(
        'users', meta,
        Column('id', Integer, primary_key=True),
        Column('login', String),
        Column('password', String),
        Column('address', String),
        Column('card_number', String),
        Column('payment', Integer),
    )
    # create database
    meta.create_all(sql_)

    # czyszczenie tabeli, aby była pusta:
    deleted = people.delete().where(people.c.id > 0)

    with sql_.connect() as conn:
        conn.execute(deleted)

        # tworzymy przykładowe dane:
        for _ in range(randint(10, 20)):
            inserted = people.insert().values(login=fake_.name(), password="XXX", address=fake_.street_name(), card_number=fake_.credit_card_number(), payment=randint(300, 3000))

            conn.execute(inserted)

        conn.commit()
