#!/usr/bin/env python3


from relationship_city import City
from relationship_state import State, Session

if __name__ == "__main__":
    session = Session()

    states_cities = session.query(State).join(City).order_by(State.id, City.id)

    for state in states_cities:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
               print(f"  {city.id}: {city.name}")

    session.close()
