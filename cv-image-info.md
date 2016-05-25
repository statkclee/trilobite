---
layout: page
title: xwMOOC 고생대 프로젝트
subtitle: 이미지 파일 정보 살펴보기
---

## 1. 이미지 정보

인터넷에서 가져온 이미지 정보를 살펴본다. 팩키지를 불러오고 나서, 인터넷에서 이미지 파일을 불러온다.
그리고, 이미지 형태, 크기, 자료형에 대해 출력한다.

~~~ {.python}
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
~~~

<img src="fig/raspberry.jpg" alt="이미지넷 라즈베리파이" width="50%">

상기 이미지에 대한 정보는 모양(Shape)를 보면 행이 `355`, 열이 `500`, 색상은 RGB `3`으로 표현된다. 
만약 흑백인 경우는 행과 열정보만 표현된다. 크기(size)는 $355 \times 500 \times 3 = 532,500$으로 계산된다.
자료형은 `uint8`으로 디버깅에서 중요하게 사용되는 정보다.

~~~ {.output}
===== Raspberry Image Info =====

Shape:  (355, 500, 3)
Size:   532500
Type:   uint8
~~~

