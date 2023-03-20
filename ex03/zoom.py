from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(image: np.ndarray) -> np.ndarray:
    """
    apply a zoom on image given as np.ndarray,
    print is new shape and pixels informations
    """
    x1, y1 = 450, 100
    x2, y2 = 850, 500
    zoom = image[y1:y2, x1:x2, :1]
    print("New shape after slicing:", np.shape(zoom))
    print(zoom)
    zoom = image[y1:y2, x1:x2, 0]
    return zoom


if __name__ == "__main__":
    pixels = ft_load("animal.jpeg")
    pixels = ft_zoom(pixels)
    plt.imshow(pixels, cmap='gray')
    plt.show()
