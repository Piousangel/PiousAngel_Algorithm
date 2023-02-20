function solution(n) {
    let answer = 0;

    const arr = new Array(300)
        .fill(0)
        .map((v, idx) => idx + 1)
        .filter((v) => {
            return v % 3 !== 0 && !String(v).includes("3");
        });

    return arr[n - 1];
}
