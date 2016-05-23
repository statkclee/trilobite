from PIL import Image
import numpy as np

# One Color
imgSinglePng = Image.open('../fig/bw-single-dot.png')
imgSinglePngArr = np.asarray(imgSinglePng)

print imgSinglePngArr


