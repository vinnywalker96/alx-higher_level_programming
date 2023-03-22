#!/usr/bin/python3
"""Define City that inherits from Base class"""
from model_state import Base, State
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    Class that defines each city
    """
    __tablename__ = "cities"

    id = Column(Integer, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey("States.id"), nullable=False)
