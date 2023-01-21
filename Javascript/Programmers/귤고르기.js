function solution(k, tangerine) {
    let answer = 0;

    map = new Map();

    for (let i = 0; i < tangerine.length; i++) {
        const num = tangerine[i];
        if (map.has(num)) {
            let temp = map.get(num);
            map.set(num, temp + 1);
        } else {
            map.set(num, 1);
        }
    }

    let sortedMap = new Map([...map].sort((a, b) => b[1] - a[1]));

    for (let item of sortedMap) {
        if (item[1] < k) {
            k -= item[1];
            answer++;
        } else {
            answer++;
            break;
        }
    }

    return answer;
}
