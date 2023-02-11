function solution(numbers) {
    let answer = "";
    const arr = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ];

    let temp = "";

    for (num of numbers) {
        if (arr.includes(temp)) {
            answer += arr.indexOf(temp);
            temp = num;
        } else {
            temp += num;
        }
    }
    answer += arr.indexOf(temp);
    return Number(answer);
}
