#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the databasee hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.schema import Table
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)

    session.commit()
    session.close()
