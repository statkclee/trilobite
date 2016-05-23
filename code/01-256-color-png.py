from PIL import Image
import numpy as np

# One Color
img256Png = Image.open('../fig/color-256-dot.png')
img256PngArr = np.asarray(img256Png)

print img256PngArr


