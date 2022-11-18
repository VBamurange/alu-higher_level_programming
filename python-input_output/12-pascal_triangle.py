#!/usr/bin/python3
"""pascal's triangle"""


def pascal_triangle(n):
    """function for the triangle"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        x = [1]
        for i in range(len(tri) - 1):
            x.append(1)
            triangles.append(x)
    return triangles

