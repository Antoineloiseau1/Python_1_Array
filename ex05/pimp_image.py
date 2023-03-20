import numpy as np
from PIL import Image
import PIL.ImageOps


def ft_invert(array) -> np.ndarray:
    """
Inverts the color of the image received"""
    tmp = np.copy(array)
    tmp = np.array(PIL.ImageOps.invert(Image.fromarray(tmp)))
    Image.fromarray(tmp).show()
    return (tmp)


def ft_red(array) -> np.ndarray:
    """
Displays and returns an image in red scale"""
    tmp = np.copy(array)
    tmp[:, :, 1:].fill(0)
    Image.fromarray(tmp).show()
    return (tmp)


def ft_green(array) -> np.ndarray:
    """
Displays and returns an image in green scale"""
    tmp = np.copy(array)
    tmp[:, :, 2].fill(0)
    tmp[:, :, 0].fill(0)
    Image.fromarray(tmp).show()
    return (tmp)


def ft_blue(array) -> np.ndarray:
    """
Displays and returns an image in blue scale"""
    tmp = np.copy(array)
    tmp[:, :, 0:2].fill(0)
    Image.fromarray(tmp).show()
    return (tmp)


def ft_grey(array) -> np.ndarray:
    """
Displays and returns image in grey scale"""
    tmp = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
    Image.fromarray(tmp).show()
    return (tmp)
