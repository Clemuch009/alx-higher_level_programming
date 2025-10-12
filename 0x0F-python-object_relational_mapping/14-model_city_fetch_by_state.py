#!/usr/bin/env python3


from model_city import City
from model_state import State, Session, Base
import sys
from sqlalchemy.orm import joinedload

if __name__ == "__main__":
    #name = sys.argv[4]
    session = Session()

    cities = session.query(City).join(State).order_by(City.id).all()

    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()
