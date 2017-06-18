---
layout: page
title: xwMOOC 고생대 프로젝트
subtitle: OpenCV 설치 및 헬로우 월드
---


## 1. 윈도우 설치 완성모습

[OpenCV](http://opencv.org/) 파이썬 설치가 성공적으로 이루어진 모습은 다음과 같다.

파이썬 쉘을 열고 `import cv2` 모듈을 가져와서 `cv2.__version__` 을 출력하면 OpenCV 버젼을 출력하면 준비가 완료된 것이다.

~~~ {.python}
>>> import cv2
>>> print cv2.__version__
~~~

~~~ {.output}
3.1.0
~~~

### 1.1. 윈도우 설치

윈도우 환경에서 OpenCV를 설치할 때 몇가지 설정을 주의해야 한다.

1. 파이썬 2.7 기준 파이썬을 설치한다. 
    * `C:\Python27` 디렉토리에 기본디폴트 설정으로 설치된다.
2. `OpenCV for Windows`를 [OpenCV 다운로드](http://opencv.org/downloads.html) 사이트에서 받는다.
    * 예를 들어 다운로드받은 디렉토리가 `C:\` 밑에 압축을 풀게되면 `C:\opencv\` 에 파일이 
3. `cv2.pyd` 파일을 파이썬 디렉토리에 복사한다.
    * 복사대상 `cv2.pyd` 파일 위치 : `C:\opencv\build\python\2.7\x86`
    * 복사될 위치 : `C:\Python27\Lib\site-packages`
4. 1--3번 적용후에 문제가 생길 경우: `C:\opencv` 디렉토리를 환경변수에 적용
    * `환경변수`에 `C:\opencv` 디렉토리를 위치를 운영체제에 알려준다.
    * 제어판 &rarr; 시스템 &rarr; 고급 시스템 설정 &rarr; 환경변수 &rarr; 시스템변수 &rarr; 편집 &rarr; `C:\opencv` 추가 &rarr; 확인

### 1.2. 맥(OS X) [^mac-opencv]

[^mac-opencv]: [Install OpenCV 3.0 and Python 2.7+ on OSX](http://www.pyimagesearch.com/2015/06/15/install-opencv-3-0-and-python-2-7-on-osx/)

맥(OSX)에서 openCV를 설치하는 방식은 다음과 같다. 먼저 맥 운영체제 버젼을 확인한다.

~~~ {.shell}
$ sw_vers
~~~ 

~~~ {.output}
ProductName:	Mac OS X
ProductVersion:	10.11.3
BuildVersion:	15D21
~~~

운영체제 버젼을 확인하고, 설치된 파이썬2 혹은 파이썬3를 확인 후에 openCV를 설치한다.

1. xcode를 설치한다.
1. [Homebrew](http://brew.sh)를 설치한다.


### 1.3. 공통 이미지 라이브러리 설치

[Python Imaging Library(PIL)](https://en.wikipedia.org/wiki/Python_Imaging_Library)는 이미지를 열고, 조작하고, 다양한 형태로 저장할 수 있게 돕는 이미지 라이브러리다. 2009년 마지막 출시된 후에 멈춰진 상태로, [Pillow](http://python-pillow.org/) 후속 프로젝트로 이어지고 있다.

~~~ {.python}
$ pip install Pillow
~~~

> ### 컴퓨터가 32비트 혹은 64비트 {.callout}
> 
> 32비트 혹은 64비트에 대한 설정, 32비트의 경우 `import Image`, 64비트의 경우 `from PIL import Image`을 사용한다.
> 
> ~~~ {.python}
> >>> import Image
> >>> from PIL import Image
> ~~~

## 2. 헬로우 월드

컴퓨터가 보는 세상을 컴퓨터로 작업하기 위한 모든 준비가 되었다면, 다음 단계로 이미지 정보를 가져오고, 
이를 처리하고, 저장하는 것이 정상적으로 작동되는지 확인한다. 일명, 컴퓨터 비젼 "헬로우 월드(Hello World)" 코드를 작성해 본다.

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

