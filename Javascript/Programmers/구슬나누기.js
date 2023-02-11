function dfs(ball_list, visited, idx, target) {
    if (idx === target) {
        answer += 1;
        return;
    }

    for (let i = 0; i < ball_list.length; i++) {
        if (visited[i] === 0) {
            visited[i] = 1;
            dfs(ball_list, visited, idx + 1, target);
            visited[i] = 0;
        }
    }
}
let answer = 0;
function solution(balls, share) {
    const ball_list = new Array(balls).fill(0).map((s, idx) => idx + 1);
    let visited = new Array(balls).fill(0);

    dfs(ball_list, visited, 0, share);
    return answer;
}
