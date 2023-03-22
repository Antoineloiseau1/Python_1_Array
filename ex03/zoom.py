from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """Load and zoom on an image, prints its original shape, \
then its shape after zoom and displays it
"""
    pixels = ft_load("animal.jpeg")
    pixels = ft_zoom(pixels)
    plt.imshow(pixels, cmap='gray')
    plt.show()


def ft_zoom(image: np.ndarray) -> np.ndarray:
    """
    apply a zoom on image given as np.ndarray,
    print is new shape and pixels informations
    """
    x1, y1 = 450, 100
    x2, y2 = 850, 500
    try:
        zoom = image[y1:y2, x1:x2, :1]
        if (0 in np.shape(zoom)):
            raise Exception("SliceError: Transformation singular")
        print("New shape after slicing:", np.shape(zoom))
        print(zoom)
        zoom = image[y1:y2, x1:x2, 0]
    except Exception as msg:
        print(msg)
        exit(-1)
    return zoom


if __name__ == "__main__":
    main()
