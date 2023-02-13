function solution(n) {
    let answer = [];
    let arr = new Array(n)
        .fill(0)
        .map((v, idx) => idx + 1)
        .filter((v) => n % v === 0);
    for (num of arr) {
        answer.push(Number(num));
    }

    return answer;
}
