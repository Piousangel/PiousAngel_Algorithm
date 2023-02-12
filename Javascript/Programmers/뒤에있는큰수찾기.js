// 빡세당! 4점 주네요 굿굿 ㅎㅎ
function solution(numbers) {
    let answer = new Array(numbers.length).fill(-1);
    let stack = [];
    
    for(let i = 0; i < numbers.length; i++){
        while(stack.length > 0 && numbers[stack[stack.length-1]] < numbers[i]){
            answer[stack.pop()] = numbers[i];         
        }
        stack.push(i);
    }
    
    for(s of stack){
        answer[stack.pop()] = -1;
    }
        
    return answer;
}