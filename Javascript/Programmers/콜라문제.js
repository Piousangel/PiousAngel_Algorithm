function solution(a, b, n) {
    let answer = 0;
    let temp = 0;

    while (n >= a) {
        n = parseInt(n / a) * b;
        temp += n % a;
        answer += n;
    }
    answer += parseInt((n + temp) / a) * b;
    return answer;
}
//다시
