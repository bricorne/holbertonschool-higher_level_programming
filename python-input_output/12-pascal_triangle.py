#!/usr/bin/python3
"""returns a list of lists of integers"""


def pascal_triangle(n):
    """def pascal_triangle"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            num = prev_row[j - 1] + prev_row[j]
            row.append(num)

        row.append(1)
        triangle.append(row)

    return triangle