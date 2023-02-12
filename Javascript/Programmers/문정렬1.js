function solution(my_string) {
    let answer = [];
    let temp = [];
    for (str of my_string) {
        if (0 <= Number(str) && Number(str) <= 9) {
            temp.push(Number(str));
        }
    }

    answer = temp.sort((a, b) => {
        return a - b;
    });

    return answer;
}
