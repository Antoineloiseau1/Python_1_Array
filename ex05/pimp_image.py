import numpy as np
from PIL import Image, ImageFilter, ImageColor
import PIL.ImageOps
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """
Inverts the color of the image received"""
    return (np.array(PIL.ImageOps.invert(Image.fromarray(array))))



def ft_red(array) -> np.ndarray:
    array = array[:, :, 0]
    return (array)



# def ft_green(array) -> np.ndarray:


# def ft_blue(array) -> np.ndarray:


def ft_grey(array) -> np.ndarray:
    """
Return image in grey scale"""
    return np.array(Image.fromarray(array).convert("L"))
