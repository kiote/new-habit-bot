from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from settings import DATABASE_URL

# ORM base class
Base = declarative_base()


class Database(object):
    def __init__(self):
        self.session = None

    def bind(self, engine):
        if not self.session:
            self.session = sessionmaker(bind=engine)(autocommit=True)


"""
Test that we can create connection
"""
if __name__ == "__main__":
    db = Database()
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.bind = engine
    Base.metadata.create_all()
    db.bind(engine)
