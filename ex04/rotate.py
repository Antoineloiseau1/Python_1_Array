from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """Load zoom and transpose on a image
"""
    img = ft_load("animal.jpeg")
    img = ft_zoom(img)
    try:
        img = np.transpose(img)
    except Exception as msg:
        print(msg)
        exit(-1)
    print("New shape after transpose:", np.shape(img))
    print(img)
    plt.imshow(img, cmap='gray')
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
        print("The shape of the image is:", np.shape(zoom))
        print(zoom)
        zoom = image[y1:y2, x1:x2, 0]
    except Exception as msg:
        print(msg)
        exit(-1)
    return zoom


if __name__ == "__main__":
    main()
