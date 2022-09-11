#!/usr/bin/python3
"""
This script creates the State “California” with the City “San Francisco”
 from the database hbtn_0e_100_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    new_State = State(name="California")
    new_State.cities = [City(name="San Francisco")]
    re = session.add(new_State)
    session.commit()

    session.close()
