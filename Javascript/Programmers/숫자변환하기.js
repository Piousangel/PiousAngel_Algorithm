function solution(x, y, n) {
    let answer = 1000000;
    let cnt = 0;

    function dfs(sum, target, n, cnt) {
        if (sum === target) {
            answer = Math.min(answer, cnt);
            return;
        }
        if (sum > target) {
            if (answer === 1000000) answer = -1;
            return;
        }

        dfs(sum + n, target, n, cnt + 1);
        dfs(sum * 2, target, n, cnt + 1);
        dfs(sum * 3, target, n, cnt + 1);
    }

    dfs(x, y, n, cnt);
    return answer;
}
