const input = require("fs")
    .readFileSync("sample.txt")
    .toString()
    .trim()
    .split("\n");

const [N, M] = input
    .shift()
    .split(" ")
    .map((v) => +v);

const tempHearSet = new Set();
const tempSeeSet = new Set();

for (let i = 0; i < input.length; i++) {
    if (i < N) tempHearSet.add(input[i]);
    else tempSeeSet.add(input[i]);
}

let answer = [];
tempSeeSet.forEach((v) => {
    if (tempHearSet.has(v)) answer.push(v);
});

console.log(answer.length + "\n" + answer.join("\n"));
