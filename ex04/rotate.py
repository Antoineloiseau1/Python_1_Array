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
    print("The shape of the image is:", np.shape(zoom), end="")
    print(zoom)
    zoom = image[y1:y2, x1:x2, 0]
    return zoom


if __name__ == "__main__":
    img = ft_load("animal.jpeg")
    img = ft_zoom(img)
    img = np.transpose(img)
    print("New shape after transpose:", np.shape(img))
    print(img)
    plt.imshow(img, cmap='gray')
    plt.show()
