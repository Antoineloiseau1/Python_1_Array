from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    try:
        image = Image.open(path)
    except Exception as msg:
        print(msg)
        exit(-1)
    pixels = np.array(image)
    image.close()
    print("The shape of image is:",  np.shape(pixels))
    print(pixels)
    return (pixels)
