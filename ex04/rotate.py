from load_image import ft_load
from PIL import Image
import numpy as np

def ft_zoom(image: np.ndarray) -> np.ndarray:
    x1, y1 = 450, 100
    x2, y2 = 850, 500
    zoom = image[y1:y2, x1:x2, 0]
    print("New shape after slicing:", np.shape(zoom))
    print(zoom)
    return zoom

if __name__ == "__main__":
	img = ft_load("animal.jpeg")
	img = ft_zoom(img)
	img = Image.fromarray(img)
	img.show()