let answer = 0;

function dfs(dungeons, visited, k, cnt) {
    
    for(let i = 0; i < dungeons.length; i++){
        if (visited[i] != 0 && k >= dungeons[i][0]){
            visited[i] = 0;
            dfs(dungeons, visited, k - dungeons[i][1], cnt +1);
            visited[i] = -1;
        }
    }
    
    answer = Math.max(answer, cnt)
}

function solution(k, dungeons) {
    
    const visited =  Array(dungeons.length).fill(-1)
    dfs(dungeons, visited, k, 0)
    return answer
}