const input = require("fs")
    .readFileSync("sample.txt")
    .toString()
    .trim()
    .split("\n");

const [N, A, M, B] = input.map((v) => v.split(" ").map((x) => Number(x)));

A.sort((a, b) => a - b);

const bs = (list, target, left, right, mid) => {
    mid = Math.floor((left + right) / 2);

    if (right < left) {
        return list[mid] == target ? 1 : 0;
    }

    if (list[mid] > target) {
        right = mid - 1;
    } else {
        left = mid + 1;
    }

    return bs(list, target, left, right, mid);
};

const result = B.map((v) => bs(A, v, 0, A.length - 1, 0));

console.log(result.join("\n"));
