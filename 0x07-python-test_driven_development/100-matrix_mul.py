#!/usr/bin/python3
"""Define a function that multiplies matrix"""

def matrix_mul(m_a, m_b):
    """Returns 2 multiple indices

    Args:
        m_a (int/ float): first argument
        m_b (int/float): second argument

    Raises:
        TypeError: if m_a or m_b is not a float or int
        TypeError: if m_a or m_b is a list of list
        ValueError: if m_a or m_b is empty
    """
    for i in m_a:
        if not isinstance(i, int) or
            not isinstance(i, float):
            raise TypeError("m_a should contain only integers or floats")
    for j in m_b:
        if not isinstance(j, int) or
            not isinstance(j, float):
            raise TypeError("m_b should contain only integers or floats")
    if m_a == [] or len(m_a) <= 0 or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]] or len(m_b) <= 0:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for col in
