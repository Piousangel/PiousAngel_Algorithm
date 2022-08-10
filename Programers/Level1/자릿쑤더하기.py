def solution(n):

    answer = 0
    strN = str(n)
    n_list = list(map(int, strN.rstrip()))
    return sum(n_list)