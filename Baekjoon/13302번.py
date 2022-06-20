import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

# 하루에 만원
# 3일 연속 2만5천원 + 쿠폰 1장
# 5일 3만7천원 + 쿠폰 2장
# 쿠폰 3장은 하루이용권으로 교환가능
# 방학 N일중 M일은 리조트에 갈수 없다
# 그외에 시간은 모두 리조트에서 보내고자 함
# 가장 저렴한 방법으로 

N, M = map(int, input().split())

n_list = list(map(int, input().split()))

def dfs(oneCnt, threeCnt, fiveCnt, coupon, totalDay, n_list) :

    global answer 

    if totalDay == 0 :
        coupon = threeCnt + (fiveCnt*2)

        if coupon >= 5 :
            mock = coupon//5
            coupon = coupon % 5
            fiveCnt -= mock

        if coupon >= 3 :
            mock = coupon//3
            coupon = coupon % 3
            threeCnt -= mock

        if coupon >= 1 :
            mock = coupon//1
            oneCnt -= mock

        temp = (oneCnt * 10000) + (threeCnt * 25000) + (fiveCnt * 37000)
        answer = min(answer, temp)
        return


    if totalDay - 1 >= 0 :
        dfs(oneCnt + 1, threeCnt, fiveCnt, coupon, totalDay - 1, n_list)
    if totalDay - 3 >= 0 :
        dfs(oneCnt, threeCnt + 1, fiveCnt, coupon, totalDay - 3, n_list)
    if totalDay - 5 >= 0 :
        dfs(oneCnt, threeCnt, fiveCnt + 1, coupon, totalDay - 5, n_list)

answer = 10000000001
dfs(0, 0, 0, 0, N, n_list)
print(answer)
