function solution(n, k) {
    var answer = 0;
    temp = n * 12000 + (k - parseInt(n / 10)) * 2000;
    return temp;
}
