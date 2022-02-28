a, b = map(int, input().split())

time = (a * 60) + b - 45
if(time < 0) :
    print(23, 60+time)
else :
    hour = time / 60
    min = time % 60
    print(hour, min)