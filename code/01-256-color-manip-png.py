from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 256 Color
img256Png = Image.open('../fig/color-256-dot.png')
img256PngArr = np.asarray(img256Png)

plt.imshow(img256PngArr)
plt.show()
           


