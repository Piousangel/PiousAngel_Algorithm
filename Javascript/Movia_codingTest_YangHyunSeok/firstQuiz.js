const fs = require("fs");
let inputList = fs.readFileSync("./firstQuizInput.txt").toString();
inputList = inputList.split("\n");


function mainFunction() {
    const count = Number(inputList[0]);

    for (let index = 1; index <= count; index++) {
        const numberList = inputList[i]
            .split(" ")
            .map((value) => Number(value));
        const firstNumber = numberList[0];
        const secondNumber = numberList[1];
        console.log(
            getGCD(firstNumber, secondNumber),
            getLCM(firstNumber, secondNumber)
        );
    }
}

// 최대 공약수
const getGCD = (firstNumber, secondNumber) => {
    if (firstNumber % secondNumber === 0) {
        return secondNumber;
    } else {
        return getGCD(secondNumber, firstNumber % secondNumber);
    }
};

// 최소 공배수
const getLCM = (firstNumber, secondNumber) => {
    return (firstNumber * secondNumber) / getGCD(firstNumber, secondNumber);
};

mainFunction();
