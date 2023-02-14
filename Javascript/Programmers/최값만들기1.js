function solution(numbers) {
    let arr = numbers.sort((a, b) => {
        return a - b;
    });
    let tempArr = arr.filter((v, idx) => idx > arr.length - 3);
    let answer = tempArr.reduce((a, b) => {
        return (a *= b);
    });
    return answer;
}
