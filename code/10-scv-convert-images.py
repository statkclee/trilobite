import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import glob

#filelist = os.listdir("tea")

os.chdir("tea")
jpg_files = glob.glob("*.jpg")

infile = jpg_files[3]

img = cv2.imread(infile)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(str(infile)+'.png', gray_img)
cv2.imshow("gray", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
##for infile in jpg_files:
##    print(infile)
##    img = cv2.imread(infile)
##    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##    cv2.imwrite(infile, gray_img)
##    cv2.imshow("gray", gray_img)
##    cv2.waitKey(0)
##    cv2.destroyAllWindows()
    


        
##    output = os.path.splitext(infile)[0] + ".png"
##    print(output)
##
##    if infile != outfile:
##        try:
##            Image.open(infile).save(outfile)
##        except IOError:
##            print("cannot convert", infile)
