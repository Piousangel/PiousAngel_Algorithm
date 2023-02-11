function solution(numlist, n) {
    let answer = [];
    const map = new Map();

    for (num of numlist) {
        map.set(num, Math.abs(n - num));
    }

    const sortedMap = new Map(
        [...map].sort((a, b) => {
            if (a[1] === b[1]) {
                return b[0] - a[0];
            } else {
                return a[1] - b[1];
            }
        })
    );

    for (let item of sortedMap) {
        answer.push(item[0]);
    }

    return answer;
}
