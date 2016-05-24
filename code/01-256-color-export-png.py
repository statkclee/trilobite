from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 256 Color
img256Png = Image.open('../fig/color-256-dot.png')
img256PngArr = np.asarray(img256Png)

saveImage = Image.fromarray(img256PngArr.astype(np.uint8))
saveImage.save('dot.png')
