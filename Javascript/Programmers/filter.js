function solution(n, numlist) {
    return numlist.filter((v, idx) => v % n === 0);
}
