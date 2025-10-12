#!/usr/bin/env python3


from model_state import Base, State, Session
if __name__ == "__main__":
    session = Session()

    state = session.query(State).filter(State.id == 2).first()

    state.name = "New Mexico"
    session.commit()
    session.close()
