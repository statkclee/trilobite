import cv2
import matplotlib.pyplot as plt

# Import Image from the Local Disk

lenaJpg = cv2.imread('../fig/lena512.jpg')

# Get Basic Info

print '===== Lena Image Info =====\n'
print 'Shape: ', lenaJpg.shape
print 'Size:  ', lenaJpg.size
print 'Type:  ', lenaJpg.dtype

# Show

plt.axis("off")
#plt.imshow(lenaJpg) # BGR
plt.imshow(cv2.cvtColor(lenaJpg, cv2.COLOR_BGR2RGB)) # RGB
plt.show()
