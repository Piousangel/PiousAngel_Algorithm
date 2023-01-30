const input = require("fs")
    .readFileSync("sample.txt")
    .toString()
    .trim()
    .split("\n");

const operatorList = ["+", "-", "*", "/"];
const operators = [];
let result = [];
let answer = [];
let target = Number(input[0]);
let numbers = input[1].split(" ").map(Number);
let Operators = input[2].split(" ").map(Number);

for (let i = 0; i < operatorList.length; i++) {
    let cnt = 0;

    while (cnt !== Operators[i]) {
        operators.push(operatorList[i]);
        cnt++;
    }
}

let ch = Array.from({ length: operators.length + 1 }, () => 0);
let temp = Array.from({ length: operators.length + N }, () => 0);

for (let i = 0; i < numbers.length; i++) {
    temp[i * 2] = numbers[i];
}

function dfs(idx) {
    if (idx === target - 1) {
        let stack = temp.slice().reverse();

        while (stack.length > 1) {
            let num1 = stack.pop();
            let operator = stack.pop();
            let num2 = stack.pop();

            switch (operator) {
                case "+":
                    stack.push(num1 + num2);
                    break;
                case "-":
                    stack.push(num1 - num2);
                    break;
                case "*":
                    stack.push(num1 * num2);
                    break;
                case "/":
                    stack.push(parseInt(num1 / num2));
                    break;
                default:
                    break;
            }
        }

        result.push(stack.pop());
    } else {
        for (let i = 0; i < operators.length; i++) {
            if (ch[i] === 0) {
                ch[i] = 1;
                temp[idx * 2 + 1] = operators[i];
                dfs(idx + 1);
                ch[i] = 0;
            }
        }
    }
}

dfs(0);

answer.push(Math.max(...result));
answer.push(Math.min(...result));
console.log(answer.join("\n"));
