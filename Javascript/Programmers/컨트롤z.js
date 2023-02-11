function solution(s) {
    let answer = 0;
    let arr = s.split(" ");
    let stack = [];
    for (s of arr) {
        if (s === "Z") {
            stack.pop();
        } else {
            stack.push(Number(s));
        }
    }
    for (n of stack) {
        answer += n;
    }
    return answer;
}
