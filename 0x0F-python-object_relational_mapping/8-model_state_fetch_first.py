#!/usr/bin/python3

"""
Script that prints the first State object from the database.
"""

from model_state import State, Base
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    main function
    """
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()
    if state is None:
        print("Nothing")
    else:
        print(state.id, state.name, sep=": ")
