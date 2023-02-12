// runtime?

function solution(x, y, n) {
    let answer = 10000000;
    let cnt = 0;
    
    function dfs(sum, target, n, cnt) {
        
        if(sum === target){
            answer = Math.min(answer, cnt);
            return;
        }
        if(sum > target){
            return;
        }
        
        if(cnt > answer){
            return
        }
    
        dfs(sum * 3, target, n, cnt + 1);
        dfs(sum * 2, target, n, cnt + 1);
        dfs(sum + n, target, n, cnt + 1);
       
    }
    
    dfs(x, y, n, cnt);
    if (answer === 10000000) answer = -1;
    return answer;
}