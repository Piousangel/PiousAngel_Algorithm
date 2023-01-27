function solution(numbers) {
    var answer = 0;
    let total = 0;
    for(const num of numbers){
        total += parseFloat(num);
    }
    const row = 5;
    const col = 5;
    const  arr = Array.from(new Array(col), () => new Array(row).fill(0));
    console.log(arr)
    
    answer = total / numbers.length;
    return answer;
}
