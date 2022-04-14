input_str = input()

stack = []
for char in input_str :
    
    while len(stack) > 2 :
        
        if stack[-3] + stack[-2] + stack[-1] + char == 'PPAP': #char 가 무조건 'P'니까....
            for i in range(3):
                stack.pop()          
        else:
            break
    
    stack.append(char)

print(stack)
if len(stack) == 1 and stack[-1] == 'P':
    print('PPAP')
else:
    print('NP')