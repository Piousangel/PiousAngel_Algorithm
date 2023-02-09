function solution(s) {
    let answer = "";
    const map = new Map();
    const arr = [...s].sort();
    for (ch of arr) {
        if (!map.has(ch)) {
            map.set(ch, 1);
        } else {
            map.set(ch, map.get(ch) + 1);
        }
    }
    map.forEach((value, key) => {
        if (value === 1) answer += key;
    });
    return answer;
}
