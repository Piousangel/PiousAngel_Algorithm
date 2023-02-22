function factorial(num) {
    if (num > 1) return num * factorial(num - 1);
    return num;
}

function solution(n) {
    let answer = 0;

    let arr = new Array(10).fill(0).map((v, idx) => {
        return factorial(idx + 1);
    });

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] <= n) {
            answer = i + 1;
        }
    }

    return answer;
}
