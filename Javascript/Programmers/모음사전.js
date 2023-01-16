function solution(word) {
    var answer = 0;
    
    alpha = ['A','E','I','O','U'];
    arr = [];
    
    function dfs(st, alpha, idx) {
        
        if (idx == 6){
            return;
        }
        if (st != ''){
            arr.push(st);
        }
        for(let i = 0; i < alpha.length; i++){
            dfs(st + alpha[i], alpha, idx + 1);
        }
    }
    
    dfs('', alpha, 0);    
    answer = arr.indexOf(word) + 1;
    return answer;
}
