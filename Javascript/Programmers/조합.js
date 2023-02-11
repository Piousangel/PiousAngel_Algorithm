function solution(balls, share) {
    let answer = [];
    let arr = new Array(balls).fill(0).map((s, idx) => idx + 1);
    answer = combination(arr, share);
    return answer.length;
}

function combination(arr, selectNum) {
    const result = [];
    if (selectNum === 1) return arr.map((v) => [v]);
    arr.forEach((v, idx, arr) => {
        const fixed = v;
        const restArr = arr.slice(idx + 1);
        const combinationArr = combination(restArr, selectNum - 1);
        const combineFix = combinationArr.map((v) => [fixed, ...v]);
        result.push(...combineFix);
    });

    return result;
}
