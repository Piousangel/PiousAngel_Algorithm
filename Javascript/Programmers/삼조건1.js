function solution(sides) {
    let answer = 0;
    answer = sides.sort((a, b) => {
        return a - b;
    });
    return answer[2] < answer[1] + answer[0] ? 1 : 2;
}
