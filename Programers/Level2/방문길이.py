def solution(dirs):

    # 튜플사용법
    
    command = {'U' : (0,1), 'D' : (0,-1), 'L' : (-1,0), 'R' : (1,0)}
    visited = set()
    cur_x, cur_y = (0,0)
    
    for i in dirs:
        next_x, next_y = cur_x + command[i][0], cur_y + command[i][1]
        if( -5 <= next_x <= 5 and -5 <= next_y <= 5) :
            visited.add((cur_x, cur_y, next_x, next_y))
            visited.add((next_x, next_y, cur_x, cur_y))
            cur_x, cur_y = next_x, next_y
    
    return len(visited)//2