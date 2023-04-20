#!/usr/bin/python3


def pascal_triangle(n):
    """Returns a list of integers of aPascal’s triangle
    Args:
         n (int)
    """
    res = []
    if n <= 0:
        return res
    else:
        for row_num in range(n):
            row = []
            for num_elem in range(row_num + 1):
                if num_elem == 0 or num_elem == row_num:
                    row.append(1)
                else:
                    prev = res[row_num - 1]
                    elem = prev[num_elem + 1] + prev[num_elem]
                    row.append(elem)
            res.append(row)
        return res
