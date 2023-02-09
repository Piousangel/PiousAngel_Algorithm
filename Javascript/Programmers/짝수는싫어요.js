function solution(n) {
    const answer = new Array(n)
        .fill(0)
        .map((num, idx) => idx + 1)
        .filter((n) => n % 2);
    return answer;
}
