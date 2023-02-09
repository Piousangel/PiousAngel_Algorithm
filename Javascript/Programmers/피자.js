function solution(slice, n) {
    let answer = 0;
    return n % slice === 0 ? n / slice : parseInt(n / slice) + 1;
}
