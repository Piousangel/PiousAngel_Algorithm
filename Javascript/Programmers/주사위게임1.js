function solution(a, b) {
    let answer = 0;
    let count = 0;

    if (a % 2 !== 0) count += 1;
    if (b % 2 !== 0) count += 1;

    switch (count) {
        case 0:
            answer = Math.abs(a - b);
            break;
        case 1:
            answer = 2 * (a + b);
            break;
        case 2:
            answer = a ** 2 + b ** 2;
            break;
    }
    return answer;
}
