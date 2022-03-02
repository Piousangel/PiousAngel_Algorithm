# Practice Python 🐤

### 정글에 들어가기전 python공부를 하려고 합니다.
---
##### 기본 문법 및 자료구조 공부는 블로그에, 코딩테스트는 Github로 기록하겠습니다.

- [x] 프로그래머스LV1
- [x] 프로그래머스LV2
- [x] 백준 Sol

__람다표현식 자주 사용하면서 연습하기__  
- filter()
- map()
- reduce()

__input() 대신__ 
~~~
import sys  
sys.stdin.readline().rstrip()
~~~

__포맷 문자열 리터럴__
- {expression} 안에 변수 -> 값 출력, 수식 -> 결과값 출력

__라이브러리__  
- itertools(순열, 조합)
- heqpq(우선순위 큐)
- bisect(이진탐색)
- collections(deque, counter...)

__heapify_max__
- 기본적으로 heapq.heapify()를 사용하면 최소힙으로 구현
- 최대힙은 코드로 직접 구현해야하지만, heapq._heapify_max()를 사용하면 최대힙으로 만들 수 있음

__" * " 를 유용하게 사용하기__
- 리스트, 튜플, 셋, 딕셔너리 앞에 *를 붙여 왼쪽, 오른쪽 괄호를 제거할 수 있다.
- String앞에 *를 사용하면 문자 하나하나 분리됨
~~~
n_list = [1,2,3,4,5]
print(*n_list) // 1 2 3 4 5 출력
set{}, tuple(), dictionary{}도 마찬가지

str = 'abc'
print(*str) // a b c 출력
~~~

__zip() 내장함수 사용__
- zip()은 좀더 찾아볼게요

__재귀함수 문제풀때 깊이를 설정해주면 좋다__  
~~~
import sys  
sys.setrecursionlimit(10**6)  
0의 개수만큼 늘려주면 된다고 합니다. 10^6 == 1,000,000
~~~
