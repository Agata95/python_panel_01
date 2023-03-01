from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from faker import Faker



class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(10))
    fullname: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(10))
    address: Mapped[str] = mapped_column(String(10))
    email_address: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


fake_ = Faker("pl-PL")
engine = create_engine("sqlite+pysqlite:///adresy.db", echo=True)
with engine.connect() as conn:
    # tworzymy strukturę
    Base.metadata.create_all(engine)
    # dodajemy kilka rekordów
    