function solution(numbers) {
    let answer = 0;
    let sorted_list = numbers.sort((a, b) => {
        return a - b;
    });

    answer = Math.max(
        numbers[0] * numbers[1],
        numbers[numbers.length - 2] * numbers[numbers.length - 1]
    );
    return answer;
}
