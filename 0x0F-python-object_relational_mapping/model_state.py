#!/usr/bin/env python3
"""
contains the class definition of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Integer, String, create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
Base = declarative_base()

username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
engine = create_engine('mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
Session = sessionmaker(bind=engine)

class State(Base):
    """
    State and an instance Base
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state")

Base.metadata.create_all(engine)
