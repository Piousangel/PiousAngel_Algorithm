const fs = require("fs");
let inputList = fs.readFileSync("./fourthQuizInput.txt").toString();
inputList = inputList.split(" ");

// 괄호 우선순위를 생각 -> stack 사용하면 좋을듯?


function mainFunction() {
    const count = Number(inputList[0]);
    let result = "";

    for (let index = 1; index <= count; index++) {
        const mathematicalExpression = inputList[index];
        result += getRPN(mathematicalExpression);
    }

    console.log(result);
}

const getRPN = (mathematicalExpression) => {
    const stack = [];
    const length = mathematicalExpression.length;
    let result = "";

    for (let index = 0; index < length; index++) {
        const character = mathematicalExpression[index];

        if (character === "(") {
            stack.push(character);
        } else if (character === ")") {
            while (stack[stack.length - 1] !== "(") {
                result += stack.pop();
            }
            stack.pop();
        } else if (isOperator(character)) {
            while (stack[stack.length - 1] !== "(") {
                result += stack.pop();
            }
            stack.push(character);
        } else {
            result += character;
        }
    }

    while (stack.length > 0) {
        result += stack.pop();
    }

    return result;
};

const isOperator = (value) => {
    const operatorList = ["+", "-", "*", "/", "^"];
    return operatorList.includes(value) ? true : false;
};

mainFunction();
