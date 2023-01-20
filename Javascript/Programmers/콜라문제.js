function solution(a, b, n) {
    let answer = 0;
    let temp = 0;

    while (n >= a) {
        let temp = parseInt(n / a) * b;
        answer += temp;
        n = temp + (n % a);
    }

    return answer;
}
