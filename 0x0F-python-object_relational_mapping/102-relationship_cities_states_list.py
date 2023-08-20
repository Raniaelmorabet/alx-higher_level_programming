#!/usr/bin/python3
"""
lists all City objects from the database 
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                        argv[2],
                                                                        argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(City).order_by(City.id).all()
    for city in row:
        print("{}: {} -> {}".format(city.id, city.state.name))
    session.close()
