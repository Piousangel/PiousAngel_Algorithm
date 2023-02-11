function solution(emergency) {
    let answer = [];
    const arr = [...emergency].sort((a, b) => {
        return b - a;
    });
    for (num of emergency) {
        answer.push(arr.indexOf(num) + 1);
    }
    return answer;
}
