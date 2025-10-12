#!/usr/bin/env python3


from relationship_state import State, Session
from relationship_cities import City

if __name__ == "__main__":
    session = Session()

    California = State(name="California")
    San_Francisco = City(name="San Francisco", state=California)

    session.add_all([California, San_Francisco])
    session.commit()
    session.close()
