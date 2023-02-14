function solution(num_list, n) {
    let answer = [];
    let tempArr = [];
    let idx = 0;

    for (num of num_list) {
        if (idx === n) {
            answer.push(tempArr);
            idx = 1;
            tempArr = [num];
        } else {
            tempArr.push(num);
            idx += 1;
        }
    }
    answer.push(tempArr);
    return answer;
}
