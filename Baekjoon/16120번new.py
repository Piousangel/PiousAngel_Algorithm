input_str = input()

stack = []
for char in input_str :

    stack.append(char)

    if len(stack) > 3 :

        if stack[-4]+stack[-3]+stack[-2]+stack[-1] == 'PPAP' :
            for i in range(3):
                stack.pop()

if len(stack) == 1 and stack[-1] == 'P':
    print('PPAP')
else:
    print('NP')
