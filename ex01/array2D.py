import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices the given family list from start to end
    """
    try:
        if (type(family) is not list):
            raise Exception("family must be of type list")
        print("My shape is :", np.shape(family))
        sliced = family[start:end]
        print("My new shape is : ", np.shape(sliced))
        return list([list(elem) for elem in sliced])
    except TypeError as msg:
        print("TypeError:", msg)
        exit(-1)
    except Exception as msg:
        print(msg)
        exit(-1)
