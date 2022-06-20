from collections import defaultdict

def solution(tickets):
    answer = []
    
    def init_graph():
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)
        return routes
    
    temp_list = []
    
    def dfs(dic, node, temp_list) :
  
        if len(temp_list) == len(tickets) + 1 :
            return temp_list

       
        for idx, country in enumerate(dic[node]):

            dic[node].pop(idx)
            tp = temp_list[:]
            tp.append(country)
            result = dfs(dic, country, tp)
            
            if result : 
                return result
        
            dic[node].insert(idx, country) 
            
    dic = init_graph()
    
    for r in dic:
        dic[r].sort()

    answer = dfs(dic, 'ICN', ['ICN'])
    
    return answer