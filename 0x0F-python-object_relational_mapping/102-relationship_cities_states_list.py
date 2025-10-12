#!/usr/bin/env python3


from relationship_city import City
from relationship_state import State, Session

if __name__ == "__main__":
    session = Session()

    cities = session.query(City).join(State).order_by(City.id).all()

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
