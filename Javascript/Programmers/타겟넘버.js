function solution(numbers, target) {
    let answer = 0;
    let arr = numbers;
    let total = 0;

    function dfs(arr, total, target, idx) {
        if (idx === arr.length) {
            if (total === target) {
                answer++;
            }
            return;
        }

        dfs(arr, total + arr[idx], target, idx + 1);
        dfs(arr, total - arr[idx], target, idx + 1);
    }

    dfs(arr, total, target, 0);
    return answer;
}
