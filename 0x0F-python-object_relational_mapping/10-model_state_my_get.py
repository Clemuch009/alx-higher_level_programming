#!/usr/bin/env python3


from model_state import Base, State, Session
import sys

if __name__ == "__main__":
    name = sys.argv[4]
    session = Session()

    state = session.query(State).filter(State.name == name).first()

    if state:
        print(state.id)
    else:
        print("Not found")
