function solution(keymap, targets) {
    let answer = [];
    const map = new Map();
    for(const str of keymap){
        for(const ch of str){
            if(!map.has(ch)){
                map.set(ch, str.indexOf(ch)+1)
            }
            else{
                map.set(ch, Math.min(map.get(ch), str.indexOf(ch) + 1));
            }
        }
    }
    
    for(const str of targets){
        let total = 0;
        for(const ch of str){
            if(!map.has(ch)){
                total += -1;
            }
            else
                total += map.get(ch)
        }
        answer.push(total);
    }
    
    return answer;
}