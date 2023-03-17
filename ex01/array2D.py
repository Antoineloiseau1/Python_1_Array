import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices the given family list from start to end
    """
    try:
        if (type(family) is not list):
            raise Exception("Family must be of type list")
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

# family = [[1.80, 78.4],
# 		    [2.15, 102.7],
# 		    [2.10, 98.5],
# 		    [1.88, 75.2]]
# print(slice_me(family, 0, 2))
# print(slice_me(family, 1, -2))

# My shape is : (4, 2)
# My new shape is : (2, 2)
# [[1.8, 78.4], [2.15, 102.7]]
# My shape is : (4, 2)
# My new shape is : (1, 2)
# [[2.15, 102.7]]
