const fs = require("fs");
let inputList = fs.readFileSync("./thirdQuizInput.txt").toString();
inputList = inputList.split("\n");

// box하나당 최소 하나의 공이 들어가야합니다.
// 각각의 box들은 서로 다른 개수의 공을 가지고 있습니다.
// 예를 들어 박스가 3개있다면 1,2,3 => 최소 6개 이상의 공이 필요합니다.
// 4개면 1,2,3,4 => 박스 개수의 등차수열의 합보다 크거나 같으면 될 것 같은데

function mainFunction() {
    const count = Number(inputList[0]);

    for (let index = 1; index <= count; index++) {
        const numberList = inputList[i]
            .split(" ")
            .map((value) => Number(value));

        // the number of balls
        const N = numberList[0];
        // number of boxs
        const K = numberList[1];

        console.log(getAnswer(N, K));
    }
}

const getAnswer = (numberOfBalls, numberOfBoxes) => {
    const numberRequired = (numberOfBoxes * (numberOfBoxes + 1)) / 2;

    if (numberOfBalls >= numberRequired) {
        return "YES";
    } else {
        return "NO";
    }
};

mainFunction();
