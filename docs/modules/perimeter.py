from math import sqrt

__all__ = ["circle_perimeter", "square_length", "square_perimeter"]
pi = 3.141592653589793


def circle_perimeter(diameter):
    return diameter * pi


def square_perimeter(length):
    return length * 4


def square_length(area):
    return sqrt(area)
