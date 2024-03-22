#!/usr/bin/python3

"""
City Module - defines the city model, City model inherits from Base
"""


from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, Sequence, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
# Can use mapped column and Mapped class in sqlalchemy 2.0.x


class City(Base):
    """
    City model template

    Attributes:

    Methods:
    """
    __tablename__ = "cities"
    id = Column(Integer,
                Sequence("city_id_seq"),
                primary_key=True,
                nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="state_cities")

    def __init__(self, name):
        self.name = name
