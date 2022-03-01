# arr = [[0 for c in range(len(land[0]))] for c in range(len(land))]

def solution(land):
    answer = 0
    # 밑에서 위로 , 전 열 제외
    for i in range(0, len(land)-1) :
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])

    answer = max(land[len(land)-1])
                  
    return answer





    # def solution(land):
    # for i in range(1, len(land)):
    #     for j in range(len(land[0])):
    #         land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]
    # return max(land[-1])