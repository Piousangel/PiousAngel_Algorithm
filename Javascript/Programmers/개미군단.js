let answer = 1000;
const set = new Set();
function dfs(idx, target) {
    if (target === 0) {
        answer = Math.min(answer, idx);
    }

    if (idx > answer) {
        return;
    }

    if (!set.has(target - 5) && target - 5 >= 0) {
        set.add(target - 5);
        dfs(idx + 1, target - 5);
    }
    if (!set.has(target - 3) && target - 3 >= 0) {
        set.add(target - 3);
        dfs(idx + 1, target - 3);
    }
    if (!set.has(target - 1) && target - 1 >= 0) {
        set.add(target - 1);
        dfs(idx + 1, target - 1);
    }
}

function solution(hp) {
    dfs(0, hp);
    return answer;
}
