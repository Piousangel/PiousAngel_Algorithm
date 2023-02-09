function solution(rsp) {
    let answer = "";
    const arr = ["2", "0", "5"];
    for (ch of rsp) {
        answer += arr[(arr.indexOf(ch) + 1) % 3];
    }
    return answer;
}
