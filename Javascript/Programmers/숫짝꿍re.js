function setMap(arr, map) {
    for (num of [...arr]) {
        if (!map.has(num)) {
            map.set(num, 1);
        } else {
            map.set(num, map.get(num) + 1);
        }
    }
}

function solution(X, Y) {
    let tempArr = [];
    const xMap = new Map();
    const yMap = new Map();

    setMap(X, xMap);
    setMap(Y, yMap);

    for (const [key, value] of xMap) {
        if (yMap.has(key)) {
            const cnt = Math.min(value, yMap.get(key));
            for (let i = 0; i < cnt; i++) {
                tempArr.push(key);
            }
        }
    }
    if (tempArr.length === 0) return "-1";

    const arr = tempArr.filter((v) => v !== "0");
    if (arr.length === 0) return "0";

    const sortedArr = tempArr.sort((a, b) => {
        return b - a;
    });

    return sortedArr.join("");
}