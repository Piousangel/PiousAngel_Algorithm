h, m = map(int, input().split())
w = int(input())

time = (h*60) + m + w
if(time == 0 or time == 1440) : 
    print(0, 0)
elif(time > 1440) :
    time -= 1440
    hour = time / 60
    min = time % 60
    print(hour, min)
else :
    hour = time / 60
    min = time % 60
    print(hour, min)