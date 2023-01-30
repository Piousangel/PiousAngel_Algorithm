const input = require("fs")
    .readFileSync("sample.txt")
    .toString()
    .trim()
    .split("\n");

const n = input[0] + 1;
const k = input[1] + 1;

const Arr = [];

const q = Array.from({ length: n }, (v, i) => i + 1);
while (q.length > 0) {
    
    for (let i = 0; i < k - 1; i++){
        const number = q.shift();
        q.push(number);
    }
    const num = q.shift();
    Arr.push(number);
}