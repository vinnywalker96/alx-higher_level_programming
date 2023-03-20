#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
from sqlalchemy.orm import delacrative_base
from sqlachemy import Column, Integer, String, metadata

metadata_obj = Metadata(metadata=metadata_obj)
Base = declarative_base()


class State(Base):
    """
    Class with id and name attributes of each state
    """
    __table__name = "states"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
