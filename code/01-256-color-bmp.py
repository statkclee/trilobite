from PIL import Image
import numpy as np

# One Color
img256Bmp = Image.open('../fig/color-256-dot.bmp')
img256BmpArr = np.asarray(img256Bmp)

print img256BmpArr


