#!/usr/bin/python3
"""Defines class student"""


class Student:
    """Representing a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student
        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of student
        Args:
            json (dict): key is public name , value is attr
        """
        for key, value in json.items():
            setattr(self, key, value)
