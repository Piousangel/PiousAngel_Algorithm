// 택배상자를 트럭에 싣는 일
// 크기 같고 1~n 증가하는 순서대로 벨트에 놓여 전달됨
// re

function solution(order) {
    let answer = 0;
    let stack = [];
    let flag = true;

    const arr = new Array(order.length).fill(0).map((v, idx) => idx + 1);

    for (num of order) {
        while (true) {
            if (arr.length !== 0) {
                let temp = arr.shift();

                if (num === temp) {
                    answer += 1;
                    break;
                }

                if (stack.length === 0) {
                    stack.push(temp);
                }
            }

            if (stack.length !== 0) {
                if (stack[stack.length - 1] === num) {
                    stack.pop();
                    answer += 1;
                    break;
                } else {
                    if (arr.length !== 0) stack.push(arr.shift());
                }
            }
        }
    }

    return answer;
}
