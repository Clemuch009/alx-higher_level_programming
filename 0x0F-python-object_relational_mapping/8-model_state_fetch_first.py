#!/usr/bin/env python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""

from model_state import Base, State, Session

if __name__ == "__main__":
    session = Session()

    state = session.query(State).first()

    if state:
        print(f"{state.id}: {state.name}")

    else:
        print("Nothing")

    session.close()
