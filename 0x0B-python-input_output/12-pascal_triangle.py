#!/usr/bin/python3
""" This module contains a function thet returns a pascal triangle """


def pascal_triangle(n):
    """ This function returns a list of lists of integers
    representing the Pascal’s triangle of n
    Args:
        n: number of lines
    Returns:
        an empty list if n <= 0
    """

    if n <= 0:
        return []

    p1 = [[1]]
    for i in range(2, n+1):
        tmp = [0] + p1[i-2] + [0]
        p1.append([sum(par) for par in zip(tmp, tmp[1:])])

    return p1
