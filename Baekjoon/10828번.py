import sys

n = int(sys.stdin.readline())

# stack_operation = ['pop', 'size', 'empty', 'top']

sample_stack = []

for i in range(n):
    temp_list = list(map(str, sys.stdin.readline().rstrip().split()))
    # print(temp_list)
    if len(temp_list) == 2:
        sample_stack.append(temp_list[1])
    else:
        if temp_list[0] ==  'pop':      #stack_operation[0]
            if len(sample_stack) == 0 :
                print("-1")
            else:
                print(sample_stack[-1])
                sample_stack.pop()
        elif temp_list[0] == 'size' :   # stack_operation[1]
            print(len(sample_stack))
        elif temp_list[0] == 'empty' :  # stack_operation[2]
            if not sample_stack :
                print("1")
            else:
                print("0")
        elif temp_list[0] == 'top':        # stack_operation[3]
            if not sample_stack :
                print("-1")
            else:
                print(sample_stack[-1])