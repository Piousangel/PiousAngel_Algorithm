hour, min = map(int, input().split())
plusmin = int(input())

total = hour*60 + min + plusmin
nowHour = (total//60)%24
nowMin = total%60
print(f'{nowHour} {nowMin}')