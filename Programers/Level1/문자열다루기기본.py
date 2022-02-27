# def solution(s):
#     answer = True
    
#     s = s.lower()
    
#     ch = ['a','b','c','d','e','f','g','h','i','j','k','l',
#            'm','n','o','p','q','r','s','t','u','v','w','x','y','z'];
    
#     str_list = list(s)
    
#     if(len(str_list) != 4 | len(str_list) != 6) :
#         return False
    
#     for i in range(len(str_list)) :
        
#         for j in range(len(ch)) :
            
#             if(str_list[i] == ch[j]) :
#                 return False
    
#     return answer


def solution(s):
    
    if(len(s) == 4 or len(s) == 6 ) and s.isdigit() :
        return True
    else :
        return False