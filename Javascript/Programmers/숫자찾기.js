function solution(num, k) {
    const arr = [...String(num)];
    return arr.indexOf(String(k)) !== -1 ? arr.indexOf(String(k)) + 1 : -1;
}
