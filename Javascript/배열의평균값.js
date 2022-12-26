function solution(numbers) {
    var answer = 0;
    let total = 0;
    for(const num of numbers){
        total += parseFloat(num);
    }
    answer = total / numbers.length;
    return answer;
}