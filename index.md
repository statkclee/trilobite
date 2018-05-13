---
layout: page
title: xwMOOC 고생대 프로젝트
subtitle: 고생대 삼엽충의 전성기를 재현
---


> ### 기계와의 경쟁을 준비하며... {.challenge}
> "The future is here, it's just not evenly distributed yet."  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - William Gibson
> 
> "고대에는 '땅'이 가장 중요했고 땅이 소수에게 집중되자 인간은 귀족과 평민으로 구분됐으며, 
> 근대에는 '기계'가 중요해지면서 기계가 소수에게 집중되자 인간은 자본가와 노동자 계급으로 구분됐다". 
> 이제는 **데이터**가 또 한번 인류를 구분하는 기준이 될 것이다. 
> 향후 데이터가 소수에게 집중되면 단순 계급에 그치는 게 아니라 데이터를 가진 종과 그렇지 못한 종으로 분류될 것이이다. [^joongang-yuval]
> 
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 유발 하라리(Yuval Noah Harari) 

[^joongang-yuval]: ['사피엔스' 저자 유발 하라리 "인간을 해킹하는 시대가 온다", "머신러닝·AI·생물학 발전…뇌과학 이해도 한층 높여"](http://news.mk.co.kr/newsRead.php?year=2018&no=58432)


<iframe width="300" height="180" src="https://www.youtube.com/embed/7Xs3auqcX7k" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

물리적 세계를 다양한 카메라 기술을 사용해서 디지털 데이터로 변환을 한 후에 이를 최종상품 형태로 제공하기 전에
다양한 시각정보를 가공, 처리, 생성하는 과정을 거치게 된다. 
만약 각종 데이터를 효과적이고 효율적으로 처리하는 R과 파이썬 언어로 이를 통합적으로 이해하고 실용적인 사례를 만들어보자.

고생대 참엽충의 전성기 재현하는데 사용되는 R 팩키지와 파이썬 라이브러리와 작업흐름 파이프라인은 다음과 같다. [^python-cv-lib]

<img src="fig/python-cv-toolchain.png" alt="파이썬 컴퓨터 비젼 툴체인" width="70%">

[^python-cv-lib]: [My Top 9 Favorite Python Libraries for Building Image Search Engines](http://www.pyimagesearch.com/2014/01/12/my-top-9-favorite-python-libraries-for-building-image-search-engines/)

> ### R & 파이썬 컴퓨터 비전 도구 모음 {.getready}
> 
> * **자료구조와 데이터 다루는 도구**
>     * 파이썬: [Numpy](http://www.numpy.org/): 이미지는 결국 다차원 행렬로 행렬제어를 통해 이미지를 제어.
>     * R: [The tidyverse](http://tidyverse.org/): 깔끔한 데이터 우주.
> * **이미지 처리와 컴퓨터 비젼**    
>     * [Python Imaging Library(PIL)](https://en.wikipedia.org/wiki/Python_Imaging_Library): [Python Pillow](http://python-pillow.org/)는 [PIL](http://www.pythonware.com/products/pil/) 포크
>     * R: [EBImage](https://github.com/aoles/EBImage), [magick](https://github.com/ropensci/magick), [imager](https://github.com/dahtah/imager)
>     * [OpenCV](http://opencv.org/): 오픈 컴퓨터 비젼
>     * [SimpleCV](http://simplecv.org/): OpenCV를 쉽고 편하게.
>     * [Scikit-learn](http://scikit-learn.org/stable/): 파이썬 기계학습
>     * [mahotas](http://luispedro.org/software/mahotas): [생명정보 이미지](https:// en.wikipedia.org/wiki/Bioimage_informatics)
>     * [ilastik](http://www.ilastik.org/): interactive learning and segmentation toolkit
> * **시각화**
>     * 파이썬: [matplotlib](http://matplotlib.org/), bokeh
>     * R: ggplot2, lattice, base 시각화 시스템 
> * **기계학습**
>     * [Scipy](http://scipy.org/): 결국, 거리를 측정하여 두개 이상의 이미지 유사성 일치도를 파악하고 분류하는데 필요.
>     * [caret](https://github.com/topepo/caret)
>     * [$H_2 O$](https://github.com/h2oai/h2o-3)

## 학습 목차

1. **이미지 분석 및 처리를 위한 기초: 파이썬**
    1. [이미지 파일이 왜 큰가?](cv-intro.html)
    1. [이미지 분석을 위한 수학: 선형대수](basic-linear-algebra.html)
        - **Scikit-Image:** [이미지는 배열](skimage-numpy.html)
    1. [컴퓨터가 보는 이미지: 흑백, RBG](image-files.html)    
    1. [OpenCV 설치 및 헬로우 월드](opencv-install.html)
1. [이미지 작업 파이프라인](cv-pipeline.html)
    1. [이미지 파일 가져오기](cv-import.html)
    1. [이미지 파일 정보 살펴보기](cv-image-info.html)
    1. [이미지 합치기](cv-add-images.html)
    1. 이미지 처리 자동화
        1. [작업 이미지 긁어오기](cv-img-download.html)
        1. [이미지 한개 변환작업](cv-img-conversion.html)
1. **R 이미지 영상**
    1. [이미지 처리 101 - 건축학개론(`EBImage`)](cv-architecture-101.html)
    1. [이미지 처리 101 - 건축학개론(`magick`)](cv-architecture-101-magick.html)
    1. [R 이미지 처리 101](cv-r-101.html) 
    1. [이미지 &rarr; 레고(Lego)](cv-lego.html) 
    1. [이미지 &rarr; 스케치(pencil sketch)](cv-pencil-sketch.html) 
    1. [이미지 &rarr; 작은 입자(particles)](cv-particles.html) 
1. **프로젝트**
    1. [이미지 처리 작업흐름](skimage-workflow.html)
        1. [사진에 나온 미국동전 합계 계산](skimage-coins.html)
    1. [이미지에 나온 책이 몇개](cv-count-books.html)
    1. [얼굴인식-Cascade](cv-face-detection.html)
    1. [자동차 탐지](cv-car-detect.html)
    1. [물고기 인식](cv-flatfish.html)
    1. [사진속 나이 추정](http://statkclee.github.io/deep-learning/ms-oxford-age.html)
    1. [동영상 감정 분석](http://statkclee.github.io/deep-learning/ms-oxford-video.html)
1. **APIs**    
    1. [구글 클라우드 비젼(Google Cloud Vision API) 설치 및 헬로우 월드](gcv-hello-world.html)

### [xwMOOC 오픈 교재](https://statkclee.github.io/xwMOOC/)

- **컴퓨팅 사고력(Computational Thinking)**
    - [컴퓨터 과학 언플러그드](http://statkclee.github.io/unplugged)  
    - [리보그 - 프로그래밍과 문제해결](https://statkclee.github.io/code-perspectives/)  
         - [러플](http://statkclee.github.io/rur-ple/)  
    - [파이썬 거북이](http://swcarpentry.github.io/python-novice-turtles/index-kr.html)  
    - [정보과학을 위한 파이썬](https://statkclee.github.io/pythonlearn-kr/)  
    - [소프트웨어 카펜트리 5.3](http://statkclee.github.io/swcarpentry-version-5-3-new/)
    - [기호 수학(Symbolic Math)](https://statkclee.github.io/symbolic-math/)
    - [데이터 과학을 위한 R 알고리즘](https://statkclee.github.io/r-algorithm/)
    - [데이터 과학을 위한 저작도구](https://statkclee.github.io/ds-authoring/)
        - [The Official xwMOOC Blog](https://xwmooc.netlify.com/)
    - [비즈니스를 위한 오픈 소스 소프트웨어](http://statkclee.github.io/open-source-for-business/)
- **데이터 과학**
    - [R 데이터과학](https://statkclee.github.io/data-science/)
    - [시각화](https://statkclee.github.io/viz/)
    - [텍스트 - 자연어처리(NLP)](https://statkclee.github.io/text/)
    - [네트워크(network)](https://statkclee.github.io/network)
    - [데이터 과학– 기초 통계](https://statkclee.github.io/statistics/)    
        - [공개 기초 통계학 - OpenIntro Statistics](https://statkclee.github.io/openIntro-statistics-bookdown/)
    - [공간통계를 위한 데이터 과학](https://statkclee.github.io/spatial/)
    - [~~R 팩키지~~](http://r-pkgs.xwmooc.org/)
    - [~~통계적 사고~~](http://think-stat.xwmooc.org/)
    - [보안 R](https://statkclee.github.io/security/) - TBA
    - [금융(Finance)](https://statkclee.github.io/finance/) - TBA
- **빅데이터**
    - [빅데이터(Big Data)](http://statkclee.github.io/bigdata)
    - [데이터 제품](https://statkclee.github.io/data-product/)
    - [R 도커](http://statkclee.github.io/r-docker/)
- **기계학습, 딥러닝, 인공지능**
    - [기계학습](http://statkclee.github.io/ml)
    - [딥러닝](http://statkclee.github.io/deep-learning)
    - [R 병렬 프로그래밍](http://statkclee.github.io/parallel-r/)
    - [고생대 프로젝트](http://statkclee.github.io/trilobite)
    - [인공지능 연구회](https://statkclee.github.io/ai-lab/)
- [IoT 오픈 하드웨어(라즈베리 파이)](http://statkclee.github.io/raspberry-pi)
    - [$100 오픈 컴퓨터](https://statkclee.github.io/one-page/)   
    - [$100 오픈 슈퍼컴퓨터](https://statkclee.github.io/hpc/)
- [선거와 투표](http://statkclee.github.io/politics)
    - [저녁이 있는 삶과 새판짜기 - 제7공화국](https://statkclee.github.io/hq/)


[^David-Julian-2016]: [David Julian (2016), "Building Machine Learning Systems with Python", Packt Publishing](https://www.packtpub.com/big-data-and-business-intelligence/building-machine-learning-systems-python)