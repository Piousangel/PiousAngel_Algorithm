import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n_list = []
n = int(input())

for i in range(1, n+1) :
    n_list.append(i)

visited = [0] *(n+1)
visited2 = [0] * (n+1)
t = int(input())

for i in range(t) :
    a, b = map(int, input().split())
 
    for j in range(a, b+1) :
       
        if visited[j] == 0 :
            visited[j] = i+1
        visited2[j] = i+1
    
temp_list = [0] * (t+1)
temp_list2 = [0] * (t+1)
for i in range(1, len(visited)) :
    if visited[i] != 0 :
        temp_list[visited[i]] += 1
        temp_list2[visited2[i]] += 1

print(temp_list2.index(max(temp_list2)))
print(temp_list.index(max(temp_list)))