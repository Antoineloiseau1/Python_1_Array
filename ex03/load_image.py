from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image file given by path and displays its pixels RGB values
    """
    try:
        image = Image.open(path)
    except Exception as msg:
        print(msg)
        exit(-1)
    pixels = np.array(image)
    print("The shape of image is:",  np.shape(pixels))
    image.close()
    return (pixels)
