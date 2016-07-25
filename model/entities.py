from functools import partial

from sqlalchemy import Column, ForeignKey,\
        String, DateTime
from sqlalchemy.ext.declarative import declarative_base


# ORM base class
Base = declarative_base()


# Aliases
PrimaryKey = partial(Column, primary_key=True)
Required = partial(Column, nullable=False)


class User(Base):
    __tablename__ = 'users'

    id = PrimaryKey(String)
    name = Column(String)


class Habit(Base):
    __tablename__ = 'habits'

    id = PrimaryKey(String)
    name = Column(String)


class DailyLog(Base):
    __tablename__ = 'daily_logs'

    id = PrimaryKey(String)
    date = Required(DateTime)
    habit_id = Required(ForeignKey(Habit.id))
    user_id = Required(ForeignKey(User.id))
