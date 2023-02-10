// 아주 깰끔하게 굿

let answer = 0;

function dfs(numbers, idx, sum, target) {
    if (idx === numbers.length) {
        if (sum === target) {
            answer += 1;
        }
        return;
    }

    dfs(numbers, idx + 1, sum + numbers[idx], target);
    dfs(numbers, idx + 1, sum - numbers[idx], target);
}

function solution(numbers, target) {
    dfs(numbers, 0, 0, target);
    return answer;
}
