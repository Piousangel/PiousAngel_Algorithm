from bisect import bisect_left, bisect_right

def count_by_range(b, left_value, right_value):
    right_idx = bisect_right(b, right_value)
    left_idx = bisect_left(b, left_value)
    print('right : ', right_idx, 'left : ', left_idx)
    return right_idx - left_idx



a = [1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a,4,4))
print("====================")
print(count_by_range(a,-1,3))