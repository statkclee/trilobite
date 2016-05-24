
## 1. 중학교 시절을 회고하며...

대수를 사용해서 미지의 수 $x$ 한개를 놓고 푸는 것을 넘어, 미지수를 두개 넣고 방정식을 푸는 것을 이원일차 연립방정식이라고 부른다.

* 미지수 $x$가 하나일 경우 수식이 하나 주어지면 미지수를 구할 수 있다.
    * 예를 들어, 미지수 $x$가 하나, 수식이 하나 $x-3=4$ 주어지면, $x=7$
* 미지수 $x$가 두개인 경우 수식이 최수 두개(두 수식도 일정 조건이 만족된다고 가정하면) 주어야 미지수 두개를 유일하게 구할 수 있다.
$$\begin{cases} 3x + 5y &= 1 \\ 
                -3x + 2y &= 6 \end{cases}$$
    * 가감법, 대입법 등의 이원일차연립방정식 해법을 사용해서 손으로 풀면 $y=1, x=-\frac{4}{3}$ 두 해를 구할 수 있다.

### 1.1. 파이썬 넘파이로 풀어보기

영혼이 없는 상기 이원일차 연립방정식을 파이썬이 알아먹기 좋은 형태, 행렬로 표현한다.

$$ \begin{bmatrix} 3 & 5 \\ 
                   -3 & 2 \end{bmatrix} \times 
   \left[ \begin{array}{c} x \\ 
                 y \end{array} \right] =                  
   \left[ \begin{array}{c} 1 \\ 
                 6 \end{array} \right] 
$$

행렬표기법으로 표현하면 $AX=B$ 가 되고, 이원일차 연립방정식의 해는 $X=A^{-1} B$가 된다.


```python
import numpy as np

A = np.matrix([[3,5],
               [-3,2]])
B = np.matrix([[1],
               [6]])

X = A**(-1)*B
print X
```

    [[-1.33333333]
     [ 1.        ]]
    

### 1.2. 넘파이 내부함수 활용


$X=A^{-1} B$ 수식을 바로 넣어 계산하는 대신에, 역행렬을 계산하는 넘파이 내부 함수를 사용하여 해를 바로 구할 수도 있다.


```python
sol = np.linalg.inv(A).dot(B)
print sol
```

    [[-1.33333333]
     [ 1.        ]]
    

## 2. 행렬 기본 연산

행렬 두개 $J$와 $H$를 정의하자. 

$$ J = \begin{bmatrix} 1 & 1 \\ 
                   0 & 1 \end{bmatrix}, 
   H = \begin{bmatrix} 2 & 0 \\ 
                   3 & 1 \end{bmatrix}$$ 

정의된 두 행렬에 대한 사칙연산을 수행한다.

### 2.1.행렬 덧셈

$J+H$ 를 손으로 계산하면 다음과 같다.

$$ \begin{bmatrix} 1 & 1 \\ 
                   0 & 1 \end{bmatrix} + 
   \begin{bmatrix} 2 & 0 \\ 
                   3 & 1 \end{bmatrix} =
   \begin{bmatrix} 3 & 1 \\ 
                   3 & 2 \end{bmatrix}
$$

넘파이를 사용해서 코드로 계산하면 다음과 같다.


```python
from numpy  import *

J = array( [[1,1],
            [0,1]] )
H = array( [[2,0],
            [3,1]] )
print J+H
```

    [[3 1]
     [3 2]]
    

### 2.2.행렬 뺄셈

$J-H$ 를 손으로 계산하면 다음과 같다.

$$ \begin{bmatrix} 1 & 1 \\ 
                   0 & 1 \end{bmatrix} - 
   \begin{bmatrix} 2 & 0 \\ 
                   3 & 1 \end{bmatrix} =
   \begin{bmatrix} -1 & 1 \\ 
                   -3 & 0 \end{bmatrix}
$$

넘파이를 사용해서 코드로 계산하면 다음과 같다.


```python
print J-H
```

    [[-1  1]
     [-3  0]]
    

### 2.3. 스칼라 행렬 곱셈

스칼라 $\lambda$를 2로 놓고, $\lambda \times J$ 를 손으로 계산하면 다음과 같다.

$$ 2 \times 
   \begin{bmatrix} 1 & 1 \\ 
                   0 & 1 \end{bmatrix} =
   \begin{bmatrix} 2 & 2 \\ 
                   0 & 2 \end{bmatrix}
$$

넘파이를 사용해서 코드로 계산하면 다음과 같다.


```python
print 2*J
```

    [[2 2]
     [0 2]]
    

### 2.4. 행렬 원소별 곱셈과 행렬곱셈

행렬 원소들마다 곱하는 곱셈이 있는 반면에, 내적으로 행렬을 계산하는 방식이 있다.

#### 2.4.1. 행렬 원소들마다 곱하는 곱셈

먼저, 원소들만 순차적으로 계산하는 것을 먼저 살펴보자. $J * H$ 를 손으로 계산하면 다음과 같다.

$$ \begin{bmatrix} 1 & 1 \\ 
                   0 & 1 \end{bmatrix} * 
   \begin{bmatrix} 2 & 0 \\ 
                   3 & 1 \end{bmatrix} =
   \begin{bmatrix} 2 & 0 \\ 
                   0 & 1 \end{bmatrix}
$$

넘파이를 사용해서 코드로 계산하면 다음과 같다. 내적에는 `dot()` 함수가 사용된다.

`*` 연산자를 사용하게 되면 $J$ 행렬 첫번째 원소와 $H$ 행렬 첫번째 원소를 곱하기 방식을 모든 행렬 원소들마다 반복한다. 따라서, $J_{11} \times H_{11} = 1 \times 2 = 2$, $\cdots$ $J_{22} \times H_{22} = 1 \times 1 = $이 된다.  


```python
print J*H
```

    [[2 0]
     [0 1]]
    

#### 2.4.2. 행렬 곱셈

$J \times H$ 를 손으로 계산하면 다음과 같다.

$$ \begin{bmatrix} 1 & 1 \\ 
                   0 & 1 \end{bmatrix} \times 
   \begin{bmatrix} 2 & 0 \\ 
                   3 & 1 \end{bmatrix} =
   \begin{bmatrix} 5 & 1 \\ 
                   3 & 1 \end{bmatrix}
$$

넘파이를 사용해서 코드로 계산하면 다음과 같다. 행렬곱셈 내적에는 `dot()` 함수가 사용된다.

`*` 연산자를 사용하게 되면 $J$ 행렬 첫번째 행과 $H$ 행렬 첫열 요소를 곱하기를 동일한 방식으로 반복하게 된다.
따라서, $J_{11} \times H_{11} + J_{12} \times H_{12} = 1 \times 2 + 1 \times 3 = 2 + 3 = 5$ 가 되고 이 값이 행렬곱셈으로 생성되는 결과행렬의 첫번째 행, 첫번째열 원소로 들어간다. 



```python
print dot(J, H)
```

    [[5 1]
     [3 1]]
    


```python

```
