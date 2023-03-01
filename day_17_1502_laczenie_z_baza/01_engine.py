from sqlalchemy import create_engine, text

memory = True
disk = True

# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
engine = create_engine("sqlite+pysqlite:///sqlalchemy_database.db", echo=True)

# wysyłamy tekstowy SQL
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())
    print(conn.info)




