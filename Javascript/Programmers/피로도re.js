let answer = -1;
function solution(k, dungeons) {
    let visited = new Array(dungeons.length).fill(-1);
    dfs(dungeons, visited, k, 0);

    return answer;
}

function dfs(arr, visited, k, cnt) {
    for (let i = 0; i < arr.length; i++) {
        if (visited[i] !== 0 && k >= arr[i][0]) {
            visited[i] = 0;
            dfs(arr, visited, k - arr[i][1], cnt + 1);
            visited[i] = -1;
        }
    }

    answer = Math.max(answer, cnt);
}
