function solution(chicken) {
    let answer = 0;

    while (chicken / 10 >= 1) {
        let less = parseInt(chicken / 10);
        chicken = less + (chicken % 10);
        answer += less;
    }

    return answer;
}
