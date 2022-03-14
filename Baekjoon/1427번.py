str1 = input()
n_list = []
for ch in str1:
    n_list.append(int(ch))
    
n_list.sort(reverse = True)

for i in range(len(n_list)):
    print(n_list[i], end='')