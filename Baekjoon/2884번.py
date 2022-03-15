hour, min = map(int, input().split())

total = hour*60 + min - 45

if total < 0 :
    print(f'{23} {60+total}')
else:
    nowHour = total//60
    nowMin = total%60
    print(f'{nowHour} {nowMin}')