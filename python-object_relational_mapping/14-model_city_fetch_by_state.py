#!/usr/bin/python3
""" lists from a table using SQLAlchemy """
from model_state import Base, State
from model_city import Base, City
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.name, City.id, City.name).join(
        City, City.state_id == State.id).all()
    for row in result:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
    session.close()
