#!/usr/bin/python3
""" lists from a table using SQLAlchemy """

from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    """ coment """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).first()

    if result:
        print("{}: {}".format(1, str(result)))
    else:
        print("Nothing")
