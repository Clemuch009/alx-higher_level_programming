#!/usr/bin/env python3


from model_state import Base, State, Session
if __name__ == "__main__":
    session = Session()
    
    Louisiana = State(name = "Louisiana")
    session.add(Louisiana)
    session.commit()

    print(Louisiana.id)
    
    session.close()
