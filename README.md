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

__라이브러리__  
- itertools(순열, 조합)
- heqpq(우선순위 큐)
- bisect(이진탐색)
- collections(deque, counter...)

__재귀함수 문제풀때 깊이를 설정해주면 좋다__  
~~~
import sys  
sys.setrecursionlimit(10**6)  
0의 개수만큼 늘려주면 된다고 합니다. 10^6 == 1,000,000
~~~
