import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

while True :

    temp = input()
    if temp == '#' :
        break

    t_list = list(map(str, temp.split()))
    target = t_list[0]
    cnt = 0
    str1 = ""
    for i in range(len(t_list)):
        str1 += t_list[i].lower()
    if len(str1) != 0 :
        for k in str1 :
            if target == k :
                cnt += 1
    print(target, cnt-1)