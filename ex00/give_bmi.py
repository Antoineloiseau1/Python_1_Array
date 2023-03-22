import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """
    Calculates bmi from a list of heights and weights
    """
    h = np.array(height)
    w = np.array(weight)
    try:
        if (0 in height):
            raise ZeroDivisionError("Cannot divide by zero")
        lst = list(w / (h**2))
        return lst
    except TypeError as msg:
        print("TypeError:", msg)
        exit(-1)
    except ValueError as msg:
        print("ValueError:", msg)
        exit(-1)
    except ZeroDivisionError as msg:
        print("ZeroDivisionError:", msg)
        exit(-1)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks wether or not the bmi limit is reached returning a list of bool
    """
    try:
        lst = list(i > limit for i in bmi)
        return lst
    except TypeError as msg:
        print("TypeError:", msg)
        exit(-1)
