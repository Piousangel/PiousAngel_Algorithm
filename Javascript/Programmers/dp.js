// 옷 3개, 5개를 담을 수 있는 상자
// 상자에는 반드시 옷이 모두 들어가야 함.
// 먼가 dp 같은데...

function dp(n) {
    const arr = new Array(n + 1).fill(10000000000);
    const items = [3, 5];

    arr[3] = 1;
    arr[5] = 1;

    for (let i = 0; i < items.length; i++) {
        for (let j = items[i]; j <= n; j++) {
            arr[j] = Math.min(arr[j], arr[j - items[i]] + 1);
        }
    }

    return arr[n];
}

function solution(n) {
    if (n % 3 !== 0 && n % 5 !== 0) {
        return -1;
    }

    return dp(n);
}
