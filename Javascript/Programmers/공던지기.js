function solution(numbers, k) {
    let answer = 0;
    let idx = 0;
    while(k > 1){
        idx = (idx + 2) % numbers.length;
        k -= 1;
    }
    return numbers[idx];
}