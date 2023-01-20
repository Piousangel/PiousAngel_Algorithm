function solution(k, score) {
    let answer = [];
    let stack = [];
    let cnt = 0;

    for (let i = 0; i < score.length; i++) {
        if (cnt < k) {
            stack.push(score[i]);
            cnt++;
        } else {
            if (stack[0] < score[i]) {
                stack.shift();
                stack.push(score[i]);
            }
        }
        stack.sort((a, b) => a - b);
        answer.push(stack[0]);
    }

    return answer;
}
