#!/usr/bin/env python3
"""
lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""

from model_state import Base, State, Session

if __name__ == "__main__":
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
