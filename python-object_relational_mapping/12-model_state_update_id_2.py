#!/usr/bin/python3
""" Inserts to a table using SQLAlchemy """
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    modified = session.query(State).filter(State.id == 2).first()
    modified.name = "New Mexico"
    session.commit()

    session.close()
