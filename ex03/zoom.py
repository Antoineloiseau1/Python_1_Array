from load_image import ft_load
from PIL import Image
import numpy as np


if __name__ == "__main__":
	pixels = ft_load("animal.jpeg")
	size = 400
	h = 100
	w = 200
	d_h = (len(pixels) - size) // 2
	d_w = (len(pixels[0]) - size) // 2
	arr = pixels[h - d_h:d_h - h, w:d_w, :1]
	print(np.shape(arr))
	img = Image.fromarray(arr)
	img = img.convert("L")
	img.show()



