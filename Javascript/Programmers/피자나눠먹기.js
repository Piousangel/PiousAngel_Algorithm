function solution(n) {
    let answer = 0;
    answer = n % 7 === 0 ? n / 7 : parseInt(n/7) + 1;
    return answer;
}