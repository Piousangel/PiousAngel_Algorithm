#이분 그래프
# 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때 이분그래프라고 합니다.

import sys

sys.stdin = open('sample.txt')

input = sys.stdin.readline

n = int(input())

# 첫줄 정점, 간선 수

N, V = map(int, input().split())
 