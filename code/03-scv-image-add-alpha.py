import cv2

skyImg = cv2.imread('../fig/sky.jpg', -1)
rplogoImg = cv2.imread('../fig/raspberry-pi-logo.png', -1)

## Image info
print '===== Original Image Info ====='
print 'Sky Image : ', skyImg.shape
print 'RP Image  : ', rplogoImg.shape

## Image Resize
rp = cv2.resize(rplogoImg, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_AREA)
                                
print '===== Resized RP Logo Image Info ====='
print 'RP Image  : ', rp.shape

## Image Addtion with Alpha
x_offset = y_offset = 10
for c in range(0,3):
    skyImg[y_offset:y_offset+rp.shape[0], x_offset:x_offset+rp.shape[1], c] = \
    rp[:,:,c] * (rp[:,:,3]/255.0) + \
    skyImg[y_offset:y_offset+rp.shape[0], x_offset:x_offset+rp.shape[1], c] * (1.0 - rp[:,:,3]/255.0)
    
## Result
cv2.imshow('Sky and RP Logo with alpha transparency ', skyImg)
cv2.waitKey(0)

cv2.destroyAllWindows()
