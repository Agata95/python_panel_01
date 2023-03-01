from sqlalchemy import create_engine, text
from sqlalchemy import URL

# engine_psql = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase") - error pip install
engine_psql = create_engine("postgresql+pg8000://scott:tiger@localhost:5432/mydatabase")

url_object = URL.create(
    "postgresql+pg8000",
    username="dbuser",
    password="kx@jj5/g",  # plain (unescaped) text
    host="pghost10",
    database="appdb",
)
engine_url = create_engine(url_object)
"""
URL.drivername: database backend and driver name, such as postgresql+psycopg2
URL.username: username string
URL.password: password string
URL.host: string hostname
URL.port: integer port number
URL.database: string database name
URL.query: an immutable mapping representing the query string. contains strings for keys and either strings or tuples of strings for values.
"""
