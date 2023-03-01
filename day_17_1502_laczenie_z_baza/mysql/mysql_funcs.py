import sqlalchemy
from sqlalchemy import create_engine, URL, CursorResult, text

# more dialects on: https://docs.sqlalchemy.org/en/20/dialects/mysql.html#dialect-mysql

url_object = URL.create(
    "mysql+mysqlconnector",
    username="root",
    password="Bitnami",  # plain (unescaped) text
    host="192.168.22.44",
    port=3306,
    database="EH",
)

engine_url = create_engine(url_object, echo=True) # echo pokazuje informacje - ważne

def sample_db_insert(connection):
    print(connection)
    users_table = sqlalchemy.Table('EH_users', sqlalchemy.MetaData(), autoload_with=engine_url)
    query = sqlalchemy.insert(users_table).values(username="adasiek", password="adasiek_pwd", login_info="login info")
    connection.execute(query)
    connection.commit()


def sample_query(connection):
    print(connection)
    incidents_table = sqlalchemy.Table('EH_users', sqlalchemy.MetaData(), autoload_with=engine_url)
    query_all = sqlalchemy.select(incidents_table)
    cursor_result_all: CursorResult = connection.execute(query_all)
    print(cursor_result_all.all())

if __name__ == "__main__":
    connection = engine_url.connect()
    sample_db_insert(connection)
    sample_query(connection)
    connection.close()


"""
Efekt:

2023-02-12 15:48:53,177 INFO sqlalchemy.engine.Engine SELECT DATABASE()
2023-02-12 15:48:53,177 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-02-12 15:48:53,178 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
2023-02-12 15:48:53,179 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-02-12 15:48:53,179 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
2023-02-12 15:48:53,179 INFO sqlalchemy.engine.Engine [raw sql] {}
<sqlalchemy.engine.base.Connection object at 0x7f5814000790>
2023-02-12 15:48:53,206 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2023-02-12 15:48:53,206 INFO sqlalchemy.engine.Engine SHOW CREATE TABLE `EH_users`
2023-02-12 15:48:53,206 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-02-12 15:48:53,209 INFO sqlalchemy.engine.Engine ROLLBACK
2023-02-12 15:48:53,211 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2023-02-12 15:48:53,211 INFO sqlalchemy.engine.Engine INSERT INTO `EH_users` (username, password, login_info) VALUES (%(username)s, %(password)s, %(login_info)s)
2023-02-12 15:48:53,211 INFO sqlalchemy.engine.Engine [generated in 0.00066s] {'username': 'adasiek', 'password': 'adasiek_pwd', 'login_info': 'login info'}
2023-02-12 15:48:53,212 INFO sqlalchemy.engine.Engine COMMIT

Process finished with exit code 0

"""
