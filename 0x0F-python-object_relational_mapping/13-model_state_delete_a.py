#!/usr/bin/env python3


from model_state import Base, State, Session

if __name__ == "__main__":
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        session.delete(state)
    session.commit()
    session.close()
