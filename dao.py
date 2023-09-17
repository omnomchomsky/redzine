import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base


def create_engine():
    return sqlalchemy.create_engine("mariadb+mariadbconnector://root:h16oNRFFj6@127.0.0.1:53144/redzine_db")

def add_event(title, location, date, description, social):
    engine = create_engine()


Base = declarative_base()


class Event(Base):
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String(lenght=100))
    location = sqlalchemy.Column(sqlalchemy.String(length=100))
    date = sqlalchemy.Column(sqlalchemy.DateTime)
    description = sqlalchemy.Column(sqlalchemy.String(length=100))
    social = sqlalchemy.Column(sqlalchemy.String(length=100))
