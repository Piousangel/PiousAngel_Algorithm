function solution(balls, share) {
    let answer = [];
    let arr = new Array(balls).fill(0).map((s, idx) => idx + 1);
    answer = permutation(arr, share);
    return answer;
}

function permutation(arr, selectNum) {
    const result = [];
    if (selectNum === 1) return arr.map((v) => [v]);

    arr.forEach((v, idx, arr) => {
        const fixed = v;
        const restArr = arr;
        const permutationArr = permutation(restArr, selectNum - 1);
        const combineFix = permutationArr.map((v) => [fixed, ...v]);
        result.push(...combineFix);
    });
    return result;
}
