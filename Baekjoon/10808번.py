alph = "abcdefghijklmnopqrstuvwxyz"
box = list(alph)
cnt = [0]*len(box)
str1 = input()

for i in range(len(box)):
    for ch in str1:
        if box[i] == ch:
            cnt[i] += 1

for x in cnt:
    print(x, end=" ")