function solution(box, n) {
    let answer = box
        .map((v) => parseInt(v / n))
        .reduce((a, b) => {
            return (a *= b);
        });
    return answer;
}
