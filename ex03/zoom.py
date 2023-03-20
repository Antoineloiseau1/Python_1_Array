from load_image import ft_load
from PIL import Image
import numpy as np


def ft_zoom(image: np.ndarray) -> np.ndarray:
    """
    apply a zoom on image given as np.ndarray,
    print is new shape and pixels informations
    """
    x1, y1 = 450, 100
    x2, y2 = 850, 500
    zoom = image[y1:y2, x1:x2, :1]
    print("New shape after slicing:", np.shape(zoom))
    print(" or", np.shape(zoom))
    print(zoom)
    zoom = image[y1:y2, x1:x2, 0]
    return zoom


if __name__ == "__main__":
    pixels = ft_load("animal.jpeg")
    img = Image.fromarray(ft_zoom(pixels))
    img.show()
