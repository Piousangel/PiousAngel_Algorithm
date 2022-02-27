def solution(n):

    str1 = str(n)
    str_list = list(str1)
    str_list.sort(reverse = True)
    return int("".join(str_list))