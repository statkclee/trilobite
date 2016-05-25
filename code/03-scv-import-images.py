import cv2
import urllib
import numpy as np

raspberry = urllib.urlopen('http://farm1.static.flickr.com/49/194935899_8b7ae04746.jpg')

raspberryArr = np.asarray(bytearray(raspberry.read()), dtype=np.uint8)
raspberryImg = cv2.imdecode(raspberryArr,-1)

cv2.imshow('Raspberry', raspberryImg)

if cv2.waitKey() & 0xff == 27:
    quit()
