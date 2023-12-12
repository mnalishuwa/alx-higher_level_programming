#!/usr/bin/python3

"""
model_state module:
    State - models the state in database
            inherits from Base model/class
    Base -  is a base class constructed for declarative class definitions,
            the declarative class is a system used by SQLAlchemy ORM to define
            classes that are mapped to relational database systems.

            This is used to define the components of a user defined
            class along with the table metadata to which the class is mapped.

            The declarative_base() is an SQLAlchemy factory function that
            creates the class when called
"""


from sqlalchemy import Column,  create_engine, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base
import sys

from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
    State class template

    Attributes:

    Methods:

    """

    __tablename__ = "states"
    id = Column(Integer,
                Sequence("state_id_seq"),
                primary_key=True,
                nullable=False, unique=True)

    name = Column(String(128), nullable=False)
    state_cities = relationship("City", back_populates="state")

    def __init__(self, name):
        """
        Contructor method
        """
        self.name = name

# if __name__ == "__main__":

#     username = sys.argv[1]
#     password = sys.argv[2]
#     database_name = sys.argv[3]
#     port_number = 3306

#     dbengine = create_engine("mysql+mysqldb://" +
#         "{}:{}@localhost:{}/{}"
#         .format(username, password, port_number, database_name),
#         pool_pre_ping=True)

#     Base.metadata.create_all(dbengine)
