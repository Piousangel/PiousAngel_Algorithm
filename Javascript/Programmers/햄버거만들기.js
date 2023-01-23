function solution(ingredient) {
    
    let answer = 0;
    let stack = []
    
    for(ch of ingredient){
        console.log("stack", stack)
        while(stack.length > 2) {
            console.log("stack[-3] + stack[-2] + stack[-1] + ch");
            if (stack[-3] + stack[-2] + stack[-1] + ch === '1321') {
                answer += 1;
                for(let i = 0; i < 4; i++){
                    stack.pop();
                }
            }
            else
                break;
            
        }
        stack.push(ch); 
    }
    
    return answer;
}

//re