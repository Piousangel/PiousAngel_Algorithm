function calFactory(num) {
    if (num === 0 || num === 1) {
        return 1;
    }
    let tempFactory = new Array(num)
        .fill(0)
        .map((v, idx) => idx + 1)
        .reduce((a, b) => {
            return a * b;
        });

    return tempFactory;
}

function solution(balls, share) {
    let answer = 0;
    answer =
        calFactory(balls) / (calFactory(balls - share) * calFactory(share));
    return answer;
}
