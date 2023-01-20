function solution(number, limit, power) {
    let answer = 0;

    for (let i = 1; i <= number; i++) {
        let temp = 0;
        for (let j = 1; j <= i / 2; j++) {
            if (i % j == 0) {
                temp += 1;
            }
        }
        temp += 1;
        if (temp <= limit) {
            answer += temp;
        } else answer += power;
    }

    return answer;
}
