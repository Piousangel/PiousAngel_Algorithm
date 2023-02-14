function solution(array) {
    let answer = 0;
    const val = array[0];
    if (array.length === 1) {
        return val;
    }
    const map = new Map();

    for (num of array) {
        if (!map.has(num)) {
            map.set(num, 1);
        } else {
            const newValue = map.get(num) + 1;
            map.set(num, newValue);
        }
    }

    const sortedMap = new Map([...map].sort((a, b) => a[1] - b[1]).reverse());

    let idx = 0;
    let tempKey = 0;
    let tempValue = 0;

    if (map.size === 1) return val;

    for (const [key, value] of sortedMap) {
        if (idx === 0) {
            tempKey = key;
            tempValue = value;
            idx += 1;
            continue;
        }
        if (tempValue === value) {
            answer = -1;
            break;
        } else {
            answer = tempKey;
            break;
        }
    }

    return answer;
}
