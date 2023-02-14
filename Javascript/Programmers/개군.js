let answer = 1000;

function dfs(idx, target) {
    if (target === 0) {
        answer = Math.min(answer, idx);
    }
    if (target < 0 || idx > answer) {
        return;
    }

    dfs(idx + 1, target - 5);
    dfs(idx + 1, target - 3);
    dfs(idx + 1, target - 1);
}

function solution(hp) {
    dfs(0, hp);
    return answer;
}
