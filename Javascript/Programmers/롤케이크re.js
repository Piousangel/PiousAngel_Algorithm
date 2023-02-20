function solution(topping) {
    let answer = 0;
    
    const map = new Map();
    const set = new Set();

    for(const num of topping){
        map.set(num, (map.get(num) || 0) + 1);
    }
        
    for(const num of topping){
        
        map.set(num, map.get(num) - 1);
        if(map.get(num) === 0) map.delete(num);
    
        set.add(num);

        if(map.size === set.size){
            answer += 1;
        };
        
        if(set.size > map.size) break;
    }
    
    return answer;
}