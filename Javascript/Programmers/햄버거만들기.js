// 1 : 빵, 2 : 야채, 3 : 고기
// 순서는 빵 - 야채 - 고기 - 빵 ==> 1 2 3 1 순

function chkHambager(stack) {
    if (
        stack[stack.length - 1] +
            stack[stack.length - 2] +
            stack[stack.length - 3] +
            stack[stack.length - 4] ===
        "1321"
    ) {
        return true;
    }
    return false;
}

function solution(ingredient) {
    let answer = 0;
    let stack = [];

    for (num of ingredient) {
        if (stack.length < 4) {
            stack.push(String(num));
        }
        // 4보다 커지면 검사 시작
        else {
            stack.push(String(num));
            if (chkHambager(stack)) {
                for (let i = 0; i < 4; i++) {
                    stack.pop();
                }
                answer += 1;
            }
        }
    }
    if (chkHambager(stack)) answer += 1;
    return answer;
}
