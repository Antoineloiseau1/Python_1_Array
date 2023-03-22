import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices the given family list from start to end
    """
    try:
        if (type(family) is not list):
            raise Exception("family must be of type list")
        print("My shape is :", np.shape(family))
        sliced = slice(start, end)
        print("My new shape is : ", np.shape(family[sliced]))
        return list(family[sliced])
    except TypeError as msg:
        print("TypeError:", msg)
        exit(-1)
    except Exception as msg:
        print(msg)
        exit(-1)
