from PIL import Image
import numpy as np

# open images
imgSinglePng = Image.open('../fig/matplotlib-viewer.png')

# process images
imgSinglePngArr = np.asarray(imgSinglePng)
print imgSinglePngArr

# save image
saveImage = Image.fromarray(imgSinglePngArr)
saveImage.save('../fig/save-dot.png')
