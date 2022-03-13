alph = ['c=','c-','dz=','d-','lj','nj','s=','z=']

str1 = input()

for s in alph:
    str1 = str1.replace(s, '@')
print(len(str1))