#!/usr/bin/python3
"""Pascal's Triangle."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        x = triangles[-1]
        y = [1]
        for i in range(len(x) - 1):
            y.append(y[i] + x[i + 1])
        y.append(1)
        triangles.append(y)
    return triangles
