---
layout: page
title: xwMOOC 고생대 프로젝트
subtitle: 컴퓨터 비젼 헬로우 월드
---

컴퓨터가 보는 세상을 컴퓨터로 작업하기 위한 모든 준비가 되었다면, 다음 단계로 이미지 정보를 가져오고, 이를 처리하고, 저장하는 것이 정상적으로 작동되는지 확인한다. 일명, 컴퓨터 비젼 "헬로우 월드(Hello World)" 코드를 작성해 본다.

1. 파이썬 PIL 라이브러리를 사용해서 컴퓨터가 이미지를 불러와서 인식하게 한다.
1. 불러온 이미지를 넘파이 객체로 변환하여 화면에 출력하여 이미지 내용을 확인한다.
1. 이미지 그대로 어떤 변경작업을 수행하지 않았기 때문에 이름을 변경하여 다른 이름으로 저정한다.

~~~ {.python}
from PIL import Image
import numpy as np

# 1. 이미지 열기
imgSinglePng = Image.open('../fig/matplotlib-viewer.png')

# 2. 이미지 처리
imgSinglePngArr = np.asarray(imgSinglePng)
print imgSinglePngArr

# 3. 처리결과 저장
saveImage = Image.fromarray(imgSinglePngArr)
saveImage.save('../fig/save-img.png')
~~~

