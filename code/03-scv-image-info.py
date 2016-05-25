import cv2
import urllib
import numpy as np

# Import Image from the ImageNet
raspberry = urllib.urlopen('http://farm1.static.flickr.com/49/194935899_8b7ae04746.jpg')

raspberryArr = np.asarray(bytearray(raspberry.read()), dtype=np.uint8)
raspberryImg = cv2.imdecode(raspberryArr, -1)

# Get Basic Info

print '===== Raspberry Image Info =====\n'
print 'Shape: ', raspberryImg.shape
print 'Size:  ', raspberryImg.size
print 'Type:  ', raspberryImg.dtype

# Further Info.

height, width = raspberryImg.shape[:2]

print height, width
