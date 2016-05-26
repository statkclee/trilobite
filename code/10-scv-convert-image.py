import cv2
import os
import matplotlib.pyplot as plt
import glob

## Select Image
os.chdir("tea")
jpg_files = glob.glob("*.jpg")

infile = jpg_files[7]

## Image Converstion
orig_img = cv2.imread(infile)
gray_img = cv2.cvtColor(orig_img, cv2.COLOR_RGB2GRAY)

## Matplotlib Viz.
plt.subplot(1,2,1)
plt.imshow(orig_img)
plt.xticks([]), plt.yticks([])  # Hide X and Y axis tick values

plt.subplot(1,2,2)
plt.imshow(gray_img)
plt.xticks([]), plt.yticks([])  # Hide X and Y axis tick values

plt.show()

