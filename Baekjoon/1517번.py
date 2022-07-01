import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

n_list = [ i for i in range(1,n+1)] 

print(n_list)