#!/usr/bin/python3
""" Coment """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Class state """
    __tablename__ = 'States'
    id = Column(Integer, autoincrement="auto", unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return "{}(name='{}')".format(self.__class__.__name__, self.name)