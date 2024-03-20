#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_us
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]
                ), pool_pre_ping=True
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(
            State.name, City.id, City.name
            ).filter(State.id == City.state_id)

    for city in cities:
        print("{}: ({}) {}".formate(city[0], city[1], city[2]))
