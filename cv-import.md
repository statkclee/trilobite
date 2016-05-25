---
layout: page
title: xwMOOC 고생대 프로젝트
subtitle: 이미지 파일 가져오기
---

## 1. 이미지 파일 저장소

영어를 위해 단어를 모아놓은 저장소가 [워드넷(WordNet)](http://wordnet.princeton.edu/)이라면,
이미지를 워드넷과 동일한 목적으로 만들어 놓은 저장소가 [이미지넷(ImageNet)](http://image-net.org/)이다.

이곳에서 목적에 맞는 이미지를 마치 외부 디스크처럼 연결하여 로컬 컴퓨터에 저장하지 않고도 가져와서 작업할 수 있다.

## 2. 이미지 데이터를 가져오는 다양한 방법

### 2.1. 외부장비를 직접활용

### 2.2. 인터넷에서 가져오는 방법

인터넷에서 이미지를 가져오는 방법은 다음과 같다.

1. 먼저 이미지가 위치한 정확한 URL을 파악: [이미지넷(ImageNet)](http://image-net.org/)에서 검색어로 `raspberry`를 넣어 라즈베리 이미지 URL을 확보
1. `urllib` 통한 인터넷 연결: 라즈베리 이미지가 외부 저장소를 작업컴퓨터와 `urllib` 통해 연결
1. 이미지 객체를 넘파이 자료구조로 변환: `urllib`으로 넘어온 문자열 데이터를 넘파이 행렬 자료구조로 변환
1. 넘파이 객체를 openCV 객체로 변환: 넘파이 행렬 데이터를 openCV 작업데이터로 변환
1. 자유로이 활용

~~~ {.python}
import cv2
import urllib
import numpy as np

raspberry = urllib.urlopen('http://farm1.static.flickr.com/49/194935899_8b7ae04746.jpg')

raspberryArr = np.asarray(bytearray(raspberry.read()), dtype=np.uint8)
raspberryImg = cv2.imdecode(raspberryArr, -1)

cv2.imshow('Raspberry', raspberryImg)

if cv2.waitKey() & 0xff == 27:
    quit()
~~~

### 2.3. 로컬 컴퓨터(이동용 USB)에 저장된 이미지를 가져오는 방법


