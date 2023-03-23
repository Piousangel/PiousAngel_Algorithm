function solution(n, k) {
    const answer = [];
    const arr = new Array(n).fill(0).map((v, idx) => idx + 1);
    let cnt = arr.reduce((a, b) => a * b, 1);

    while (answer.length < n) {
        cnt = cnt / arr.length;
        answer.push(...arr.splice(Math.floor((k - 1) / cnt), 1));
        k = k % cnt;
    }

    return answer;
}
